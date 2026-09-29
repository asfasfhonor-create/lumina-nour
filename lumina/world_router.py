import streamlit as st

from lumina.ai_service import GeminiService
from lumina.worlds.english import render_english_world
from lumina.worlds.science import render_science_world
from lumina.worlds.math import render_math_world
from lumina.parent_dashboard import render_parent_dashboard


WORLD_RENDERERS = {
    "english": render_english_world,
    "science": render_science_world,
    "math": render_math_world,
}


def render_active_world(ai: GeminiService, parent_pin: str | None = None) -> bool:
    """Render the selected structured world. Return True when a world is active."""
    module_id = st.session_state.get("active_world")
    if not module_id:
        return False

    if st.button("← العودة إلى عالم نور", key="back_to_nour_world"):
        st.session_state.active_world = None
        st.rerun()

    if module_id == "parent":
        render_parent_dashboard(parent_pin)
        return True

    renderer = WORLD_RENDERERS.get(module_id)
    if renderer is None:
        st.warning("العالم ده لسه تحت البناء.")
        return True

    renderer(ai)
    return True
