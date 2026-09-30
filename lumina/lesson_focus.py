import streamlit as st

from lumina.learning.lesson_view import render_verified_lesson
from lumina.learning.missions import get_lesson_by_id, get_module_for_lesson_id


def render_lesson_focus() -> None:
    lesson_id = st.session_state.get("focus_lesson_id")
    lesson = get_lesson_by_id(lesson_id) if lesson_id else None
    module_id = get_module_for_lesson_id(lesson_id) if lesson_id else None

    if lesson is None or module_id is None:
        st.warning("تعذر فتح الدرس المحدد.")
        return

    st.markdown('<div class="section-title">🎯 الدرس المختار</div>', unsafe_allow_html=True)
    render_verified_lesson(lesson, module_id=module_id)
