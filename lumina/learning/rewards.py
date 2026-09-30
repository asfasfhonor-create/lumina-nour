from __future__ import annotations

from datetime import date, timedelta

import streamlit as st

from lumina.persistence.profile_state import persist_profile_state


XP_PER_NEW_SUCCESS = 10


def _recalculate_streak() -> int:
    days = sorted({date.fromisoformat(day) for day in st.session_state.get("learning_days", [])})
    if not days:
        return 0

    latest = days[-1]
    today = date.today()
    if latest not in {today, today - timedelta(days=1)}:
        return 0

    streak = 1
    cursor = latest
    known = set(days)
    while cursor - timedelta(days=1) in known:
        cursor -= timedelta(days=1)
        streak += 1
    return streak


def apply_success_reward(
    *,
    module_id: str,
    lesson_id: str,
    evidence_id: str,
    activity_type: str = "lesson",
) -> int:
    """Reward new demonstrated evidence once, never repeated button clicks."""
    reward_key = f"{module_id}:{lesson_id}:{evidence_id}"
    rewarded = st.session_state.setdefault("rewarded_evidence", [])
    if reward_key in rewarded:
        return 0

    rewarded.append(reward_key)
    today = date.today().isoformat()
    learning_days = st.session_state.setdefault("learning_days", [])
    if today not in learning_days:
        learning_days.append(today)

    st.session_state.xp = int(st.session_state.get("xp", 0)) + XP_PER_NEW_SUCCESS
    st.session_state.streak = _recalculate_streak()
    _update_badges()
    persist_profile_state()
    return XP_PER_NEW_SUCCESS


def _update_badges() -> None:
    badges = st.session_state.setdefault("badges", [])
    evidence_count = len(st.session_state.get("rewarded_evidence", []))

    candidates = []
    if evidence_count >= 1:
        candidates.append("First Evidence")
    if evidence_count >= 10:
        candidates.append("Learning Explorer")
    if evidence_count >= 25:
        candidates.append("Persistent Thinker")

    for badge in candidates:
        if badge not in badges:
            badges.append(badge)
