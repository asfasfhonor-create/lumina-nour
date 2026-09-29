from datetime import date

import streamlit as st

from lumina.learning.lesson_view import render_verified_lesson
from lumina.learning.missions import choose_mission, get_lesson_by_id, get_module_for_lesson_id
from lumina.persistence.session_store import get_learning_store
from lumina.persistence.profile_state import persist_profile_state


def render_daily_mission_world() -> None:
    store = get_learning_store()
    today = date.today().isoformat()
    if st.session_state.get("daily_mission_date") != today:
        st.session_state.daily_mission_date = today
        st.session_state.daily_mission_lesson_id = None

    target_id = st.session_state.get("daily_mission_lesson_id")
    lesson = get_lesson_by_id(target_id) if target_id else None

    if lesson is None:
        mission = choose_mission(store)
        if mission is None:
            st.info("لا توجد مهمة متاحة حاليًا.")
            return
        st.session_state.daily_mission_lesson_id = mission.lesson_id
        st.session_state.daily_mission_date = today
        persist_profile_state()
        lesson = get_lesson_by_id(mission.lesson_id)
        module_id = mission.module_id
        reason = mission.reason
    else:
        module_id = get_module_for_lesson_id(lesson.id)
        reason = "كمّلي مهمة اليوم من المكان اللي وقفتي عنده"

    if lesson is None or module_id is None:
        st.warning("تعذر تحديد مهمة اليوم. ارجعي للصفحة الرئيسية وجربي مرة أخرى.")
        return

    st.markdown('<div class="section-title">🎯 مهمة اليوم</div>', unsafe_allow_html=True)
    st.caption(f"{reason} · المصدر: {lesson.source_pages}")
    render_verified_lesson(lesson, module_id=module_id)
