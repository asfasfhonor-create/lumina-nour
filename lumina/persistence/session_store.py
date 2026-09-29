from __future__ import annotations

from datetime import datetime, timezone

import streamlit as st

from lumina.persistence.base import LearningStore


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


_STORE = SessionLearningStore()


def get_learning_store() -> LearningStore:
    return _STORE
