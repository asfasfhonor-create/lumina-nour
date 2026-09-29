import streamlit as st


def initialize_session_state() -> None:
    """Initialize prototype state in one place until persistent storage replaces it."""
    defaults = {
        "xp": 0,
        "streak": 0,
        "daily_done": False,
        "tasks_list": [],
        "chat_history": [],
        "active_world": None,
        "learning_attempts": [],
        "lesson_hints": {},
        "mistake_notebook": [],
        "review_queue": [],
        "parent_unlocked": False,
        "app_unlocked": False,
        "english_profile": {},
        "rewarded_evidence": [],
        "learning_days": [],
        "badges": [],
        "daily_mission_lesson_id": None,
        "daily_mission_date": None,
        "focus_lesson_id": None,
        "profile_hydrated": False,
        "persistence_disabled_for_session": False,
        "persistence_warning": None,
        "persistence_verified": False,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def current_level() -> int:
    return max(1, st.session_state.xp // 100 + 1)


def record_learning_attempt(attempt: dict) -> None:
    st.session_state.learning_attempts.append(attempt)


def get_learning_attempts(lesson_id: str | None = None) -> list[dict]:
    attempts = st.session_state.learning_attempts
    if lesson_id is None:
        return attempts
    return [attempt for attempt in attempts if attempt.get("lesson_id") == lesson_id]


def record_mistake(mistake: dict) -> None:
    """Add or refresh one unresolved mistake for the same lesson/check."""
    for existing in st.session_state.mistake_notebook:
        if (
            existing.get("lesson_id") == mistake.get("lesson_id")
            and existing.get("check_id") == mistake.get("check_id")
            and not existing.get("resolved", False)
        ):
            existing.update(mistake)
            return
    st.session_state.mistake_notebook.append(mistake)


def resolve_mistake(lesson_id: str, check_id: str) -> None:
    for mistake in st.session_state.mistake_notebook:
        if mistake.get("lesson_id") == lesson_id and mistake.get("check_id") == check_id:
            mistake["resolved"] = True


def get_mistakes(lesson_id: str | None = None, unresolved_only: bool = False) -> list[dict]:
    mistakes = st.session_state.mistake_notebook
    if lesson_id is not None:
        mistakes = [m for m in mistakes if m.get("lesson_id") == lesson_id]
    if unresolved_only:
        mistakes = [m for m in mistakes if not m.get("resolved", False)]
    return mistakes


def queue_review(review: dict) -> None:
    for existing in st.session_state.review_queue:
        if (
            existing.get("lesson_id") == review.get("lesson_id")
            and existing.get("check_id") == review.get("check_id")
            and existing.get("status") == "due"
        ):
            existing.update(review)
            return
    st.session_state.review_queue.append(review)


def complete_review(lesson_id: str, check_id: str) -> None:
    for review in st.session_state.review_queue:
        if review.get("lesson_id") == lesson_id and review.get("check_id") == check_id:
            review["status"] = "completed"


def get_reviews(status: str | None = None) -> list[dict]:
    reviews = st.session_state.review_queue
    if status is None:
        return reviews
    return [review for review in reviews if review.get("status") == status]
