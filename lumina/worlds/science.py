import streamlit as st

from lumina.ai_service import GeminiService
from lumina.curriculum.catalog import SCIENCE_T1
from lumina.curriculum.science_unit1 import SCIENCE_UNIT1_LESSONS
from lumina.learning.lesson_view import render_verified_unit


def render_science_world(ai: GeminiService) -> None:
    st.markdown('<div class="section-title">🔬 Science Lab</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="mission"><b>Observe → Understand → Predict → Apply</b><br>'
        '<span class="muted">Science is built from Nour\'s supplied curriculum source, with reasoning before memorization.</span></div>',
        unsafe_allow_html=True,
    )

    source = SCIENCE_T1
    st.caption(f"Trusted source: {source.display_name}")
    unit_title = st.selectbox(
        "Choose unit",
        [unit.title for unit in source.units],
        key="school_science_unit",
    )

    if unit_title == "Force and Motion":
        render_verified_unit(
            "Unit 1 · Force and Motion",
            SCIENCE_UNIT1_LESSONS,
            "science_u1_lesson",
            module_id="science",
        )
    else:
        st.info("This unit is inventoried and will be converted into verified lesson data next.")
