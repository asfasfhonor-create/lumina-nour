import streamlit as st


def initialize_session_state() -> None:
    """Initialize prototype state in one place until persistent storage replaces it."""
    defaults = {
        "xp": 120,
        "streak": 3,
        "daily_done": False,
        "tasks_list": [],
        "chat_history": [],
        "active_world": None,
        "learning_attempts": [],
        "lesson_hints": {},
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
