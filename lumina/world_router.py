import streamlit as st

from lumina.ai_service import GeminiService
from lumina.worlds.english import render_english_world
from lumina.worlds.science import render_science_world
from lumina.worlds.math import render_math_world
from lumina.worlds.ict import render_ict_world
from lumina.worlds.arabic import render_arabic_world
from lumina.worlds.social import render_social_world
from lumina.worlds.religion import render_religion_world
from lumina.worlds.ai_lab import render_ai_world
from lumina.review_center import render_review_center
from lumina.exam_mode import render_exam_mode
from lumina.daily_mission import render_daily_mission_world
from lumina.weekly_plan import render_weekly_plan
from lumina.curriculum_search import render_curriculum_search
from lumina.lesson_focus import render_lesson_focus
from lumina.parent_dashboard import render_parent_dashboard


WORLD_RENDERERS = {
    "english": render_english_world,
    "science": render_science_world,
    "math": render_math_world,
    "ict": render_ict_world,
    "arabic": render_arabic_world,
    "social": render_social_world,
    "religion": render_religion_world,
    "ai": render_ai_world,
}


def render_active_world(ai: GeminiService, parent_pin: str | None = None, *, app_pin_configured: bool = False) -> bool:
    """Render the selected structured world. Return True when a world is active."""
    module_id = st.session_state.get("active_world")
    if not module_id:
        return False

    if st.button("← العودة إلى عالم نور", key="back_to_nour_world"):
        st.session_state.active_world = None
        st.rerun()

    if module_id == "parent":
        render_parent_dashboard(parent_pin, ai_available=ai.available, app_pin_configured=app_pin_configured)
        return True

    if module_id == "review":
        render_review_center()
        return True

    if module_id == "exam":
        render_exam_mode()
        return True

    if module_id == "mission":
        render_daily_mission_world()
        return True

    if module_id == "weekly":
        render_weekly_plan()
        return True

    if module_id == "curriculum_search":
        render_curriculum_search(ai)
        return True

    if module_id == "lesson_focus":
        render_lesson_focus()
        return True

    renderer = WORLD_RENDERERS.get(module_id)
    if renderer is None:
        st.warning("العالم ده لسه تحت البناء.")
        return True

    renderer(ai)
    return True
