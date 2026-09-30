from __future__ import annotations

from datetime import datetime, timezone

import streamlit as st

from lumina.persistence.base import LearningStore
from lumina.persistence.neon_store import NeonLearningStore


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


class SessionLearningStore(LearningStore):
    """Prototype adapter.

    The UI talks to this interface instead of owning session-state details.
    A durable backend can replace this adapter without rewriting learning worlds.
    """

    def record_attempt(self, attempt: dict) -> None:
        payload = dict(attempt)
        payload.setdefault("created_at", _now_iso())
        st.session_state.learning_attempts.append(payload)

    def get_attempts(self, lesson_id: str | None = None) -> list[dict]:
        attempts = st.session_state.learning_attempts
        if lesson_id is None:
            return attempts
        return [a for a in attempts if a.get("lesson_id") == lesson_id]

    def record_mistake(self, mistake: dict) -> None:
        payload = dict(mistake)
        payload.setdefault("created_at", _now_iso())
        payload["updated_at"] = _now_iso()
        for existing in st.session_state.mistake_notebook:
            if (
                existing.get("lesson_id") == mistake.get("lesson_id")
                and existing.get("check_id") == mistake.get("check_id")
                and not existing.get("resolved", False)
            ):
                existing.update(payload)
                return
        st.session_state.mistake_notebook.append(payload)

    def resolve_mistake(self, lesson_id: str, check_id: str) -> None:
        for mistake in st.session_state.mistake_notebook:
            if mistake.get("lesson_id") == lesson_id and mistake.get("check_id") == check_id:
                mistake["resolved"] = True
                mistake["resolved_at"] = _now_iso()
                mistake["updated_at"] = _now_iso()

    def get_mistakes(
        self,
        lesson_id: str | None = None,
        unresolved_only: bool = False,
    ) -> list[dict]:
        mistakes = st.session_state.mistake_notebook
        if lesson_id is not None:
            mistakes = [m for m in mistakes if m.get("lesson_id") == lesson_id]
        if unresolved_only:
            mistakes = [m for m in mistakes if not m.get("resolved", False)]
        return mistakes

    def queue_review(self, review: dict) -> None:
        payload = dict(review)
        payload.setdefault("created_at", _now_iso())
        payload["updated_at"] = _now_iso()
        for existing in st.session_state.review_queue:
            if (
                existing.get("lesson_id") == review.get("lesson_id")
                and existing.get("check_id") == review.get("check_id")
                and existing.get("status") == "due"
            ):
                existing.update(payload)
                return
        st.session_state.review_queue.append(payload)

    def complete_review(self, lesson_id: str, check_id: str) -> None:
        for review in st.session_state.review_queue:
            if review.get("lesson_id") == lesson_id and review.get("check_id") == check_id:
                review["status"] = "completed"
                review["completed_at"] = _now_iso()
                review["updated_at"] = _now_iso()

    def get_reviews(self, status: str | None = None) -> list[dict]:
        reviews = st.session_state.review_queue
        if status is None:
            return reviews
        return [review for review in reviews if review.get("status") == status]

    def get_profile_state(self) -> dict:
        keys = (
            "xp",
            "streak",
            "badges",
            "learning_days",
            "rewarded_evidence",
            "english_profile",
            "ai_profile",
            "daily_mission_lesson_id",
            "daily_mission_date",
        )
        return {key: st.session_state.get(key) for key in keys}

    def save_profile_state(self, state: dict) -> None:
        for key, value in state.items():
            st.session_state[key] = value

    def health_check(self) -> bool:
        return True


_SESSION_STORE = SessionLearningStore()
_REMOTE_STORE: LearningStore | None = None


class ResilientLearningStore:
    """Use Neon normally, but preserve a failed write in the current session."""

    def __init__(self, remote: LearningStore, fallback: SessionLearningStore) -> None:
        self.remote = remote
        self.fallback = fallback

    def _write(self, method: str, *args) -> None:
        try:
            getattr(self.remote, method)(*args)
        except Exception as exc:
            from lumina.persistence.base import PersistenceError
            if not isinstance(exc, PersistenceError):
                raise
            getattr(self.fallback, method)(*args)
            st.session_state.persistence_disabled_for_session = True
            st.session_state.persistence_verified = False
            st.session_state.persistence_warning = (
                "الحفظ السحابي متوقف مؤقتًا. احتفظنا بآخر تقدم داخل هذه الجلسة؛ "
                "لا تغلقي الصفحة، ويمكن تنزيل نسخة أمان من لوحة وليّ الأمر."
            )

    def record_attempt(self, attempt: dict) -> None:
        self._write("record_attempt", attempt)

    def record_mistake(self, mistake: dict) -> None:
        self._write("record_mistake", mistake)

    def resolve_mistake(self, lesson_id: str, check_id: str) -> None:
        self._write("resolve_mistake", lesson_id, check_id)

    def queue_review(self, review: dict) -> None:
        self._write("queue_review", review)

    def complete_review(self, lesson_id: str, check_id: str) -> None:
        self._write("complete_review", lesson_id, check_id)

    def save_profile_state(self, state: dict) -> None:
        self._write("save_profile_state", state)

    def get_attempts(self, lesson_id: str | None = None) -> list[dict]:
        return self.remote.get_attempts(lesson_id)

    def get_mistakes(self, lesson_id: str | None = None, unresolved_only: bool = False) -> list[dict]:
        return self.remote.get_mistakes(lesson_id, unresolved_only)

    def get_reviews(self, status: str | None = None) -> list[dict]:
        return self.remote.get_reviews(status)

    def get_profile_state(self) -> dict:
        return self.remote.get_profile_state()

    def health_check(self) -> bool:
        return self.remote.health_check()


def get_learning_store() -> LearningStore:
    global _REMOTE_STORE

    if st.session_state.get("persistence_disabled_for_session", False):
        return _SESSION_STORE

    learner_key = st.secrets.get("NOUR_LEARNER_KEY", None)
    neon_database_url = st.secrets.get("NEON_DATABASE_URL", None)

    if neon_database_url and learner_key:
        if _REMOTE_STORE is None or not isinstance(_REMOTE_STORE, NeonLearningStore):
            _REMOTE_STORE = NeonLearningStore(
                database_url=str(neon_database_url),
                learner_key=str(learner_key),
            )
        return ResilientLearningStore(_REMOTE_STORE, _SESSION_STORE)

    return _SESSION_STORE


def persistence_status() -> dict:
    """Return a non-secret persistence status for UI/diagnostics."""
    if st.session_state.get("persistence_disabled_for_session", False):
        return {
            "mode": "session_fallback",
            "durable": False,
            "label": "Session fallback",
        }

    learner_key = st.secrets.get("NOUR_LEARNER_KEY", None)
    neon_database_url = st.secrets.get("NEON_DATABASE_URL", None)
    if neon_database_url and learner_key:
        return {
            "mode": "neon",
            "durable": True,
            "label": "Neon PostgreSQL",
        }

    return {
        "mode": "session",
        "durable": False,
        "label": "Session only",
    }
