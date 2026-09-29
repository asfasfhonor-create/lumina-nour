import streamlit as st

from lumina.ai_service import GeminiService
from lumina.worlds.english import render_english_world


WORLD_RENDERERS = {
    "english": render_english_world,
}


def render_active_world(ai: GeminiService) -> bool:
    """Render the selected structured world. Return True when a world is active."""
    module_id = st.session_state.get("active_world")
    if not module_id:
        return False

    if st.button("← العودة إلى عالم نور", key="back_to_nour_world"):
        st.session_state.active_world = None
        st.rerun()

    renderer = WORLD_RENDERERS.get(module_id)
    if renderer is None:
        st.warning("العالم ده لسه تحت البناء.")
        return True

    renderer(ai)
    return True
