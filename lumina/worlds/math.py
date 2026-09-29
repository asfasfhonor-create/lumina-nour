import streamlit as st

from lumina.ai_service import GeminiService
from lumina.curriculum.catalog import MATH_T1
from lumina.curriculum.math_unit1 import MATH_UNIT1_LESSONS
from lumina.learning.lesson_view import render_verified_unit


def render_math_world(ai: GeminiService) -> None:
    st.markdown('<div class="section-title">➗ Math Quest</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="mission"><b>Understand the pattern before using the rule.</b><br>'
        '<span class="muted">Math Quest follows Nour\'s supplied curriculum and keeps notation and reasoning visible.</span></div>',
        unsafe_allow_html=True,
    )

    source = MATH_T1
    st.caption(f"Trusted source: {source.display_name}")
    unit_title = st.selectbox(
        "Choose unit",
        [unit.title for unit in source.units],
        key="school_math_unit",
    )

    if unit_title == "Relations and Functions":
        render_verified_unit(
            "Unit 1 · Relations and Functions",
            MATH_UNIT1_LESSONS,
            "math_u1_lesson",
            module_id="math",
        )
    else:
        st.info("This unit is inventoried and will be converted into verified lesson data next.")
