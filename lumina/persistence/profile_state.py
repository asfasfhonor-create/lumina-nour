from __future__ import annotations

import streamlit as st

from lumina.persistence.base import PersistenceError
from lumina.persistence.session_store import get_learning_store


PROFILE_KEYS = (
    "xp",
    "streak",
    "badges",
    "learning_days",
    "rewarded_evidence",
    "english_profile",
)


def hydrate_profile_state() -> None:
    if st.session_state.get("profile_hydrated", False):
        return

    store = get_learning_store()
    try:
        state = store.get_profile_state() or {}
    except PersistenceError as exc:
        st.session_state.persistence_disabled_for_session = True
        st.session_state.persistence_warning = str(exc)
        state = {}
    for key in PROFILE_KEYS:
        if key in state and state[key] is not None:
            st.session_state[key] = state[key]

    st.session_state.profile_hydrated = True


def persist_profile_state() -> None:
    store = get_learning_store()
    state = {key: st.session_state.get(key) for key in PROFILE_KEYS}
    try:
        store.save_profile_state(state)
    except PersistenceError as exc:
        st.session_state.persistence_disabled_for_session = True
        st.session_state.persistence_warning = str(exc)
