import streamlit as st

from lumina.learning.lesson_view import render_verified_lesson
from lumina.learning.missions import choose_mission, get_lesson_by_id
from lumina.persistence.session_store import get_learning_store


def render_daily_mission_world() -> None:
    store = get_learning_store()
    target_id = st.session_state.get("daily_mission_lesson_id")
    lesson = get_lesson_by_id(target_id) if target_id else None

    if lesson is None:
        mission = choose_mission(store)
        if mission is None:
            st.info("لا توجد مهمة متاحة حاليًا.")
            return
        st.session_state.daily_mission_lesson_id = mission.lesson_id
        lesson = get_lesson_by_id(mission.lesson_id)
        module_id = mission.module_id
    else:
        mission = choose_mission(store)
        module_id = next(
            (
                attempt_module
                for attempt_module in (
                    review.get("module_id") for review in store.get_reviews()
                    if review.get("lesson_id") == lesson.id
                )
                if attempt_module
            ),
            None,
        )
        if module_id is None:
            from lumina.curriculum.mapped_curriculum import MAPPED_CURRICULUM
            module_id = next(
                sid for sid, units in MAPPED_CURRICULUM.items()
                if any(lesson in lessons for lessons in units.values())
            )

    st.markdown('<div class="section-title">🎯 مهمة اليوم</div>', unsafe_allow_html=True)
    st.caption("مهمة قصيرة من Learning Brain — المراجعة المستحقة لها الأولوية.")
    render_verified_lesson(lesson, module_id=module_id)
