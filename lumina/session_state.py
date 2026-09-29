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
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def current_level() -> int:
    return max(1, st.session_state.xp // 100 + 1)
