from __future__ import annotations

import json
from datetime import datetime, timezone

import psycopg
from psycopg.rows import dict_row

from lumina.persistence.base import LearningStore


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)


class PostgresLearningStore(LearningStore):
    """Durable PostgreSQL store for LUMINA.

    Intended for Neon through a server-side DATABASE_URL with SSL required.
    """

    def __init__(self, database_url: str, learner_key: str) -> None:
        self.database_url = database_url
        self.learner_key = learner_key

    def _connect(self):
        return psycopg.connect(
            self.database_url,
            row_factory=dict_row,
            connect_timeout=12,
        )

    def record_attempt(self, attempt: dict) -> None:
        payload = dict(attempt)
        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    insert into lumina_learning_attempts (
                        learner_key, module_id, unit_id, lesson_id, check_id,
                        evidence_id, answer, correct, source_pages, activity_type, created_at
                    ) values (
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
            select module_id, unit_id, lesson_id, check_id, evidence_id, answer,
                   correct, source_pages, activity_type, created_at
            from lumina_learning_attempts
            where learner_key = %s
        """
        params: list[object] = [self.learner_key]
        if lesson_id is not None:
            sql += " and lesson_id = %s"
            params.append(lesson_id)
        sql += " order by created_at asc"

        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, params)
                return list(cur.fetchall())

    def record_mistake(self, mistake: dict) -> None:
        payload = dict(mistake)
        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    insert into lumina_mistakes (
                        learner_key, module_id, unit_id, lesson_id, lesson_title,
                        check_id, question, answer, mistake_type, hint, source_pages,
                        resolved, created_at, updated_at
                    ) values (
                        %(learner_key)s, %(module_id)s, %(unit_id)s, %(lesson_id)s, %(lesson_title)s,
                        %(check_id)s, %(question)s, %(answer)s, %(mistake_type)s, %(hint)s, %(source_pages)s,
                        %(resolved)s, %(created_at)s, %(updated_at)s
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
                        resolved = false,
                        resolved_at = null,
                        updated_at = excluded.updated_at
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
                        "resolved": bool(payload.get("resolved", False)),
                        "created_at": payload.get("created_at") or _utc_now(),
                        "updated_at": _utc_now(),
                    },
                )

    def resolve_mistake(self, lesson_id: str, check_id: str) -> None:
        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    update lumina_mistakes
                    set resolved = true, resolved_at = %s, updated_at = %s
                    where learner_key = %s and lesson_id = %s and check_id = %s
                    """,
                    (_utc_now(), _utc_now(), self.learner_key, lesson_id, check_id),
                )

    def get_mistakes(
        self,
        lesson_id: str | None = None,
        unresolved_only: bool = False,
    ) -> list[dict]:
        sql = """
            select module_id, unit_id, lesson_id, lesson_title, check_id, question,
                   answer, mistake_type, hint, source_pages, resolved,
                   created_at, updated_at, resolved_at
            from lumina_mistakes
            where learner_key = %s
        """
        params: list[object] = [self.learner_key]
        if lesson_id is not None:
            sql += " and lesson_id = %s"
            params.append(lesson_id)
        if unresolved_only:
            sql += " and resolved = false"
        sql += " order by updated_at asc"

        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, params)
                return list(cur.fetchall())

    def queue_review(self, review: dict) -> None:
        payload = dict(review)
        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    insert into lumina_reviews (
                        learner_key, module_id, lesson_id, lesson_title, check_id,
                        status, reason, source_pages, created_at, updated_at
                    ) values (
                        %(learner_key)s, %(module_id)s, %(lesson_id)s, %(lesson_title)s, %(check_id)s,
                        %(status)s, %(reason)s, %(source_pages)s, %(created_at)s, %(updated_at)s
                    )
                    on conflict (learner_key, lesson_id, check_id)
                    do update set
                        module_id = excluded.module_id,
                        lesson_title = excluded.lesson_title,
                        status = excluded.status,
                        reason = excluded.reason,
                        source_pages = excluded.source_pages,
                        completed_at = null,
                        updated_at = excluded.updated_at
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
                        "created_at": payload.get("created_at") or _utc_now(),
                        "updated_at": _utc_now(),
                    },
                )

    def complete_review(self, lesson_id: str, check_id: str) -> None:
        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    update lumina_reviews
                    set status = 'completed', completed_at = %s, updated_at = %s
                    where learner_key = %s and lesson_id = %s and check_id = %s
                    """,
                    (_utc_now(), _utc_now(), self.learner_key, lesson_id, check_id),
                )

    def get_reviews(self, status: str | None = None) -> list[dict]:
        sql = """
            select module_id, lesson_id, lesson_title, check_id, status, reason,
                   source_pages, created_at, updated_at, completed_at
            from lumina_reviews
            where learner_key = %s
        """
        params: list[object] = [self.learner_key]
        if status is not None:
            sql += " and status = %s"
            params.append(status)
        sql += " order by updated_at asc"

        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, params)
                return list(cur.fetchall())

    def get_profile_state(self) -> dict:
        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "select state from lumina_profile_state where learner_key = %s",
                    (self.learner_key,),
                )
                row = cur.fetchone()
                return dict(row["state"]) if row and row.get("state") else {}

    def save_profile_state(self, state: dict) -> None:
        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    insert into lumina_profile_state (learner_key, state, updated_at)
                    values (%s, %s::jsonb, %s)
                    on conflict (learner_key)
                    do update set state = excluded.state, updated_at = excluded.updated_at
                    """,
                    (self.learner_key, json.dumps(state, ensure_ascii=False), _utc_now()),
                )
