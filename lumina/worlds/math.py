import streamlit as st

from lumina.ai_service import GeminiService
from lumina.curriculum.catalog import MATH_T1, MATH_T2
from lumina.curriculum.math_unit1 import MATH_UNIT1_LESSONS
from lumina.curriculum.math_unit2 import MATH_UNIT2_LESSONS
from lumina.learning.lesson_view import render_verified_unit


def render_math_world(ai: GeminiService) -> None:
    st.markdown('<div class="section-title">➗ Math Quest</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="mission"><b>Understand the pattern before using the rule.</b><br>'
        '<span class="muted">Math Quest follows Nour\'s supplied curriculum and keeps notation and reasoning visible.</span></div>',
        unsafe_allow_html=True,
    )

    source = st.selectbox(
        "Choose term",
        [MATH_T1, MATH_T2],
        format_func=lambda item: item.term,
        key="school_math_term",
    )
    st.caption(f"Trusted source: {source.display_name} · {source.term}")
    unit_title = st.selectbox(
        "Choose unit",
        [unit.title for unit in source.units],
        key=f"school_math_unit_{source.id}",
    )

    if source.id == "math_prep3_t1" and unit_title == "Relations and Functions":
        render_verified_unit(
            "Unit 1 · Relations and Functions",
            MATH_UNIT1_LESSONS,
            "math_u1_lesson",
            module_id="math",
        )
    elif source.id == "math_prep3_t1" and unit_title == "Ratio, Proportion, Direct Variation and Inverse Variation":
        render_verified_unit(
            "Unit 2 · Ratio, Proportion, Direct Variation and Inverse Variation",
            MATH_UNIT2_LESSONS,
            "math_u2_lesson",
            module_id="math",
        )
    else:
        st.info(
            "This unit is inventoried from the trusted source. "
            "Its verified lesson data will be connected progressively without inventing content."
        )
