from __future__ import annotations

from contextlib import contextmanager
from datetime import datetime, timezone

import psycopg
from psycopg.rows import dict_row
from psycopg.types.json import Jsonb

from lumina.persistence.base import LearningStore, PersistenceError


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)


class NeonLearningStore(LearningStore):
    """Durable PostgreSQL adapter for the dedicated LUMINA NOUR Neon database.

    Use Neon's pooled connection string with SSL enabled and keep it only in
    Streamlit secrets as NEON_DATABASE_URL.
    """

    def __init__(self, database_url: str, learner_key: str) -> None:
        self.database_url = database_url
        self.learner_key = learner_key

    @contextmanager
    def _connect(self):
        try:
            with psycopg.connect(self.database_url, row_factory=dict_row) as conn:
                yield conn
        except psycopg.Error as exc:
            raise PersistenceError(
                "تعذر الوصول إلى قاعدة بيانات تقدم نور الآن. لم يتم تسجيل هذه العملية."
            ) from exc

    def record_attempt(self, attempt: dict) -> None:
        payload = dict(attempt)
        with self._connect() as conn:
            conn.execute(
                """
                insert into lumina_learning_attempts (
                    learner_key, module_id, unit_id, lesson_id, check_id,
                    evidence_id, answer, correct, source_pages, activity_type, created_at
                )
                values (
                    %(learner_key)s, %(module_id)s, %(unit_id)s, %(lesson_id)s, %(check_id)s,
                    %(evidence_id)s, %(answer)s, %(correct)s, %(source_pages)s, %(activity_type)s, %(created_at)s
                )
                """,
                {
                    "learner_key": self.learner_key,
                    "module_id": payload.get("module_id"),
                    "unit_id": payload.get("unit_id"),
                    "lesson_id": payload["lesson_id"],
                    "check_id": payload.get("check_id"),
                    "evidence_id": payload.get("evidence_id"),
                    "answer": payload.get("answer"),
                    "correct": payload.get("correct"),
                    "source_pages": payload.get("source_pages"),
                    "activity_type": payload.get("activity_type"),
                    "created_at": payload.get("created_at") or _utc_now(),
                },
            )

    def get_attempts(self, lesson_id: str | None = None) -> list[dict]:
        sql = """
            select *
            from lumina_learning_attempts
            where learner_key = %s
        """
        params: list[object] = [self.learner_key]
        if lesson_id is not None:
            sql += " and lesson_id = %s"
            params.append(lesson_id)
        sql += " order by created_at asc"

        with self._connect() as conn:
            return list(conn.execute(sql, params).fetchall())

    def record_mistake(self, mistake: dict) -> None:
        payload = dict(mistake)
        now = _utc_now()
        with self._connect() as conn:
            conn.execute(
                """
                insert into lumina_mistakes (
                    learner_key, module_id, unit_id, lesson_id, lesson_title,
                    check_id, question, answer, mistake_type, hint, source_pages,
                    resolved, created_at, updated_at, resolved_at
                )
                values (
                    %(learner_key)s, %(module_id)s, %(unit_id)s, %(lesson_id)s, %(lesson_title)s,
                    %(check_id)s, %(question)s, %(answer)s, %(mistake_type)s, %(hint)s, %(source_pages)s,
                    %(resolved)s, %(created_at)s, %(updated_at)s, %(resolved_at)s
                )
                on conflict (learner_key, lesson_id, check_id)
                do update set
                    module_id = excluded.module_id,
                    unit_id = excluded.unit_id,
                    lesson_title = excluded.lesson_title,
                    question = excluded.question,
                    answer = excluded.answer,
                    mistake_type = excluded.mistake_type,
                    hint = excluded.hint,
                    source_pages = excluded.source_pages,
                    resolved = excluded.resolved,
                    updated_at = excluded.updated_at,
                    resolved_at = excluded.resolved_at
                """,
                {
                    "learner_key": self.learner_key,
                    "module_id": payload.get("module_id"),
                    "unit_id": payload.get("unit_id"),
                    "lesson_id": payload["lesson_id"],
                    "lesson_title": payload.get("lesson_title"),
                    "check_id": payload["check_id"],
                    "question": payload.get("question"),
                    "answer": payload.get("answer"),
                    "mistake_type": payload.get("mistake_type"),
                    "hint": payload.get("hint"),
                    "source_pages": payload.get("source_pages"),
                    "resolved": payload.get("resolved", False),
                    "created_at": payload.get("created_at") or now,
                    "updated_at": now,
                    "resolved_at": payload.get("resolved_at"),
                },
            )

    def resolve_mistake(self, lesson_id: str, check_id: str) -> None:
        now = _utc_now()
        with self._connect() as conn:
            conn.execute(
                """
                update lumina_mistakes
                set resolved = true, resolved_at = %s, updated_at = %s
                where learner_key = %s and lesson_id = %s and check_id = %s
                """,
                (now, now, self.learner_key, lesson_id, check_id),
            )

    def get_mistakes(
        self,
        lesson_id: str | None = None,
        unresolved_only: bool = False,
    ) -> list[dict]:
        sql = "select * from lumina_mistakes where learner_key = %s"
        params: list[object] = [self.learner_key]

        if lesson_id is not None:
            sql += " and lesson_id = %s"
            params.append(lesson_id)
        if unresolved_only:
            sql += " and resolved = false"

        sql += " order by updated_at asc"
        with self._connect() as conn:
            return list(conn.execute(sql, params).fetchall())

    def queue_review(self, review: dict) -> None:
        payload = dict(review)
        now = _utc_now()
        with self._connect() as conn:
            conn.execute(
                """
                insert into lumina_reviews (
                    learner_key, module_id, lesson_id, lesson_title, check_id,
                    status, reason, source_pages, created_at, updated_at, completed_at
                )
                values (
                    %(learner_key)s, %(module_id)s, %(lesson_id)s, %(lesson_title)s, %(check_id)s,
                    %(status)s, %(reason)s, %(source_pages)s, %(created_at)s, %(updated_at)s, %(completed_at)s
                )
                on conflict (learner_key, lesson_id, check_id)
                do update set
                    module_id = excluded.module_id,
                    lesson_title = excluded.lesson_title,
                    status = excluded.status,
                    reason = excluded.reason,
                    source_pages = excluded.source_pages,
                    updated_at = excluded.updated_at,
                    completed_at = excluded.completed_at
                """,
                {
                    "learner_key": self.learner_key,
                    "module_id": payload.get("module_id"),
                    "lesson_id": payload["lesson_id"],
                    "lesson_title": payload.get("lesson_title"),
                    "check_id": payload["check_id"],
                    "status": payload.get("status", "due"),
                    "reason": payload.get("reason"),
                    "source_pages": payload.get("source_pages"),
                    "created_at": payload.get("created_at") or now,
                    "updated_at": now,
                    "completed_at": payload.get("completed_at"),
                },
            )

    def complete_review(self, lesson_id: str, check_id: str) -> None:
        now = _utc_now()
        with self._connect() as conn:
            conn.execute(
                """
                update lumina_reviews
                set status = 'completed', completed_at = %s, updated_at = %s
                where learner_key = %s and lesson_id = %s and check_id = %s
                """,
                (now, now, self.learner_key, lesson_id, check_id),
            )

    def get_reviews(self, status: str | None = None) -> list[dict]:
        sql = "select * from lumina_reviews where learner_key = %s"
        params: list[object] = [self.learner_key]
        if status is not None:
            sql += " and status = %s"
            params.append(status)
        sql += " order by updated_at asc"

        with self._connect() as conn:
            return list(conn.execute(sql, params).fetchall())

    def get_profile_state(self) -> dict:
        with self._connect() as conn:
            row = conn.execute(
                """
                select state
                from lumina_profile_state
                where learner_key = %s
                limit 1
                """,
                (self.learner_key,),
            ).fetchone()
        return dict(row["state"]) if row and row.get("state") else {}

    def save_profile_state(self, state: dict) -> None:
        with self._connect() as conn:
            conn.execute(
                """
                insert into lumina_profile_state (learner_key, state, updated_at)
                values (%s, %s, %s)
                on conflict (learner_key)
                do update set state = excluded.state, updated_at = excluded.updated_at
                """,
                (self.learner_key, Jsonb(state), _utc_now()),
            )


    def health_check(self) -> bool:
        """Verify connectivity and the complete LUMINA persistence schema."""
        with self._connect() as conn:
            row = conn.execute(
                """
                select
                    to_regclass('public.lumina_learning_attempts') is not null as attempts_ok,
                    to_regclass('public.lumina_mistakes') is not null as mistakes_ok,
                    to_regclass('public.lumina_reviews') is not null as reviews_ok,
                    to_regclass('public.lumina_profile_state') is not null as profile_ok
                """
            ).fetchone()
        return bool(
            row
            and row.get("attempts_ok")
            and row.get("mistakes_ok")
            and row.get("reviews_ok")
            and row.get("profile_ok")
        )
