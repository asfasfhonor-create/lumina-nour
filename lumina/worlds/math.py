import streamlit as st

from lumina.context_help import render_context_help

from lumina.ai_service import GeminiService
from lumina.curriculum.catalog import MATH_T1, MATH_T2
from lumina.curriculum.math_unit1 import MATH_UNIT1_LESSONS
from lumina.curriculum.math_unit2 import MATH_UNIT2_LESSONS
from lumina.curriculum.math_unit3 import MATH_UNIT3_LESSONS
from lumina.curriculum.math_unit4 import MATH_UNIT4_LESSONS
from lumina.curriculum.math_unit5 import MATH_UNIT5_LESSONS
from lumina.curriculum.math_t2_unit1 import MATH_T2_UNIT1_LESSONS
from lumina.curriculum.math_t2_unit2 import MATH_T2_UNIT2_LESSONS
from lumina.curriculum.math_t2_unit3 import MATH_T2_UNIT3_LESSONS
from lumina.curriculum.math_t2_unit4 import MATH_T2_UNIT4_LESSONS
from lumina.curriculum.math_t2_unit5 import MATH_T2_UNIT5_LESSONS
from lumina.learning.lesson_view import render_verified_unit
from lumina.curriculum.source_session import render_temporary_source_session


def render_math_world(ai: GeminiService) -> None:
    st.markdown('<div class="section-title">➗ Math Quest</div>', unsafe_allow_html=True)
    render_context_help("math", label="💬 قوليلي العالم ده بيعمل إيه")
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
    elif source.id == "math_prep3_t1" and unit_title == "Statistics":
        render_verified_unit(
            "Unit 3 · Statistics",
            MATH_UNIT3_LESSONS,
            "math_u3_lesson",
            module_id="math",
        )
    elif source.id == "math_prep3_t1" and unit_title == "Trigonometry":
        render_verified_unit(
            "Unit 4 · Trigonometry",
            MATH_UNIT4_LESSONS,
            "math_u4_lesson",
            module_id="math",
        )
    elif source.id == "math_prep3_t1" and unit_title == "Coordinate Geometry":
        render_verified_unit(
            "Unit 5 · Coordinate Geometry",
            MATH_UNIT5_LESSONS,
            "math_u5_lesson",
            module_id="math",
        )
    elif source.id == "math_prep3_t2" and unit_title == "Equations":
        render_verified_unit(
            "Term 2 · Unit 1 · Equations",
            MATH_T2_UNIT1_LESSONS,
            "math_t2_u1_lesson",
            module_id="math",
        )
    elif source.id == "math_prep3_t2" and unit_title == "Algebraic Rational Functions and the operations on them":
        render_verified_unit(
            "Term 2 · Unit 2 · Algebraic Rational Functions",
            MATH_T2_UNIT2_LESSONS,
            "math_t2_u2_lesson",
            module_id="math",
        )
    elif source.id == "math_prep3_t2" and unit_title == "Probability":
        render_verified_unit(
            "Term 2 · Unit 3 · Probability",
            MATH_T2_UNIT3_LESSONS,
            "math_t2_u3_lesson",
            module_id="math",
        )
    elif source.id == "math_prep3_t2" and unit_title == "The Circle":
        render_verified_unit(
            "Term 2 · Unit 4 · The Circle",
            MATH_T2_UNIT4_LESSONS,
            "math_t2_u4_lesson",
            module_id="math",
        )
    elif source.id == "math_prep3_t2" and unit_title == "Angles and Arcs in the circle":
        render_verified_unit(
            "Term 2 · Unit 5 · Angles and Arcs in the Circle",
            MATH_T2_UNIT5_LESSONS,
            "math_t2_u5_lesson",
            module_id="math",
        )
    else:
        st.info(
            "This unit is inventoried from the trusted source. "
            "Its verified lesson data will be connected progressively without inventing content."
        )

    render_temporary_source_session(
        ai,
        source,
        section_title=unit_title,
        key_prefix="math_source_session",
    )
