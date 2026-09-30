from __future__ import annotations

import streamlit as st

from lumina.persistence.base import PersistenceError
from lumina.persistence.session_store import get_learning_store, persistence_status


PROFILE_KEYS = (
    "xp",
    "streak",
    "badges",
    "learning_days",
    "rewarded_evidence",
    "english_profile",
    "ai_profile",
    "daily_mission_lesson_id",
    "daily_mission_date",
    "first_run_complete",
    "onboarding_version",
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



def verify_persistence_after_hydration() -> None:
    """Verify durable storage at most once per session after profile hydration."""
    if st.session_state.get("persistence_verified", False):
        return
    if st.session_state.get("persistence_verification_attempted", False):
        return

    status = persistence_status()
    if not status.get("durable"):
        return

    st.session_state.persistence_verification_attempted = True
    store = get_learning_store()
    try:
        st.session_state.persistence_verified = bool(store.health_check())
        if not st.session_state.persistence_verified:
            st.session_state.persistence_warning = (
                "اتصال الحفظ السحابي موجود، لكن مخطط قاعدة البيانات غير مكتمل."
            )
    except PersistenceError as exc:
        st.session_state.persistence_disabled_for_session = True
        st.session_state.persistence_verified = False
        st.session_state.persistence_warning = str(exc)
