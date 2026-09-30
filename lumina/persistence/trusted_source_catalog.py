from __future__ import annotations

from datetime import datetime, timezone

import psycopg
from psycopg.rows import dict_row
from psycopg.types.json import Jsonb

from lumina.curriculum.trusted_sources import TrustedSourceRecord, source_role_priority, SOURCE_ROLE_SUPPLIED
from lumina.persistence.base import PersistenceError


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)


class NeonTrustedSourceCatalog:
    """Metadata catalog for permanent trusted learning sources."""

    def __init__(self, database_url: str, learner_key: str) -> None:
        self.database_url = database_url
        self.learner_key = learner_key

    def register(self, record: TrustedSourceRecord) -> bool:
        if record.learner_key != self.learner_key:
            raise PersistenceError("تعذر اعتماد المصدر بسبب عدم تطابق ملف المتعلم.")

        try:
            with psycopg.connect(self.database_url, row_factory=dict_row) as conn:
                row = conn.execute(
                    """
                    insert into lumina_trusted_sources (
                        source_id, learner_key, filename, display_name, subject,
                        term_label, unit_label, mime_type, sha256, size_bytes,
                        storage_provider, storage_key, trust_status, active,
                        notes, metadata, created_at, updated_at
                    )
                    values (
                        %(source_id)s, %(learner_key)s, %(filename)s, %(display_name)s, %(subject)s,
                        %(term_label)s, %(unit_label)s, %(mime_type)s, %(sha256)s, %(size_bytes)s,
                        %(storage_provider)s, %(storage_key)s, %(trust_status)s, %(active)s,
                        %(notes)s, %(metadata)s, %(created_at)s, %(updated_at)s
                    )
                    on conflict (learner_key, sha256) do nothing
                    returning source_id
                    """,
                    {
                        "source_id": record.source_id,
                        "learner_key": record.learner_key,
                        "filename": record.filename,
                        "display_name": record.display_name,
                        "subject": record.subject,
                        "term_label": record.term_label,
                        "unit_label": record.unit_label,
                        "mime_type": record.mime_type,
                        "sha256": record.sha256,
                        "size_bytes": record.size_bytes,
                        "storage_provider": record.storage_provider,
                        "storage_key": record.storage_key,
                        "trust_status": record.trust_status,
                        "active": record.active,
                        "notes": record.notes,
                        "metadata": Jsonb(dict(record.metadata)),
                        "created_at": _utc_now(),
                        "updated_at": _utc_now(),
                    },
                ).fetchone()
            return bool(row)
        except psycopg.Error as exc:
            raise PersistenceError(
                "تم حفظ الملف، لكن تعذر تسجيل بيانات المصدر الدائم."
            ) from exc

    def list_active(self) -> list[dict]:
        try:
            with psycopg.connect(self.database_url, row_factory=dict_row) as conn:
                rows = list(
                    conn.execute(
                        """
                        select *
                        from lumina_trusted_sources
                        where learner_key = %s and active = true
                        """,
                        (self.learner_key,),
                    ).fetchall()
                )

            def _priority(row: dict) -> int:
                metadata = row.get("metadata") or {}
                raw = metadata.get("priority")
                try:
                    return int(raw)
                except (TypeError, ValueError):
                    return source_role_priority(
                        str(metadata.get("source_role", SOURCE_ROLE_SUPPLIED))
                    )

            return sorted(
                rows,
                key=lambda row: (
                    row.get("subject", ""),
                    row.get("term_label", ""),
                    -_priority(row),
                    row.get("display_name", ""),
                ),
            )
        except psycopg.Error as exc:
            raise PersistenceError("تعذر قراءة قائمة المصادر الدائمة.") from exc


    def find_active_by_canonical_source(self, canonical_source_id: str) -> dict | None:
        target = (canonical_source_id or "").strip()
        if not target:
            return None
        try:
            with psycopg.connect(self.database_url, row_factory=dict_row) as conn:
                row = conn.execute(
                    """
                    select *
                    from lumina_trusted_sources
                    where learner_key = %s
                      and active = true
                      and metadata ->> 'canonical_source_id' = %s
                    order by updated_at desc
                    limit 1
                    """,
                    (self.learner_key, target),
                ).fetchone()
            return dict(row) if row else None
        except psycopg.Error as exc:
            raise PersistenceError("تعذر العثور على مصدر المنهج الأساسي.")

    def find_active_by_filename(self, filename: str) -> dict | None:
        target = (filename or "").strip()
        if not target:
            return None
        try:
            with psycopg.connect(self.database_url, row_factory=dict_row) as conn:
                row = conn.execute(
                    """
                    select *
                    from lumina_trusted_sources
                    where learner_key = %s and active = true and filename = %s
                    order by updated_at desc
                    limit 1
                    """,
                    (self.learner_key, target),
                ).fetchone()
            return dict(row) if row else None
        except psycopg.Error as exc:
            raise PersistenceError("تعذر العثور على مصدر المنهج المحفوظ.") from exc

    def archive(self, source_id: str) -> None:
        try:
            with psycopg.connect(self.database_url) as conn:
                conn.execute(
                    """
                    update lumina_trusted_sources
                    set trust_status = 'archived', active = false, updated_at = %s
                    where learner_key = %s and source_id = %s
                    """,
                    (_utc_now(), self.learner_key, source_id),
                )
        except psycopg.Error as exc:
            raise PersistenceError("تعذر أرشفة المصدر الآن.") from exc
