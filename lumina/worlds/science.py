import streamlit as st

from lumina.ai_service import GeminiService
from lumina.curriculum.catalog import SCIENCE_T1, SCIENCE_T2
from lumina.curriculum.science_unit1 import SCIENCE_UNIT1_LESSONS
from lumina.curriculum.science_unit2 import SCIENCE_UNIT2_LESSONS
from lumina.curriculum.science_unit3 import SCIENCE_UNIT3_LESSONS
from lumina.curriculum.science_unit4 import SCIENCE_UNIT4_LESSONS
from lumina.curriculum.science_t2_unit1 import SCIENCE_T2_UNIT1_LESSONS
from lumina.curriculum.science_t2_unit2 import SCIENCE_T2_UNIT2_LESSONS
from lumina.curriculum.science_t2_unit3 import SCIENCE_T2_UNIT3_LESSONS
from lumina.learning.lesson_view import render_verified_unit
from lumina.curriculum.source_session import render_temporary_source_session


def render_science_world(ai: GeminiService) -> None:
    st.markdown('<div class="section-title">🔬 Science Lab</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="mission"><b>Observe → Understand → Predict → Apply</b><br>'
        '<span class="muted">Science is built from Nour\'s supplied curriculum source, with reasoning before memorization.</span></div>',
        unsafe_allow_html=True,
    )

    source = st.selectbox(
        "Choose term",
        [SCIENCE_T1, SCIENCE_T2],
        format_func=lambda item: item.term,
        key="school_science_term",
    )
    st.caption(f"Trusted source: {source.display_name} · {source.term}")
    unit_title = st.selectbox(
        "Choose unit",
        [unit.title for unit in source.units],
        key=f"school_science_unit_{source.id}",
    )

    if source.id == "science_prep3_t1" and unit_title == "Force and Motion":
        render_verified_unit(
            "Unit 1 · Force and Motion",
            SCIENCE_UNIT1_LESSONS,
            "science_u1_lesson",
            module_id="science",
        )
    elif source.id == "science_prep3_t1" and unit_title == "Light Energy (Mirrors and Lenses)":
        render_verified_unit(
            "Unit 2 · Light Energy (Mirrors and Lenses)",
            SCIENCE_UNIT2_LESSONS,
            "science_u2_lesson",
            module_id="science",
        )
    elif source.id == "science_prep3_t1" and unit_title == "The Universe and the Solar System":
        render_verified_unit(
            "Unit 3 · The Universe and the Solar System",
            SCIENCE_UNIT3_LESSONS,
            "science_u3_lesson",
            module_id="science",
        )
    elif source.id == "science_prep3_t1" and unit_title == "Reproduction and Species Continuity":
        render_verified_unit(
            "Unit 4 · Reproduction and Species Continuity",
            SCIENCE_UNIT4_LESSONS,
            "science_u4_lesson",
            module_id="science",
        )
    elif source.id == "science_prep3_t2" and unit_title == "Chemical Reactions":
        render_verified_unit(
            "Term 2 · Unit 1 · Chemical Reactions",
            SCIENCE_T2_UNIT1_LESSONS,
            "science_t2_u1_lesson",
            module_id="science",
        )
    elif source.id == "science_prep3_t2" and unit_title == "Electric Energy and Radioactivity":
        render_verified_unit(
            "Term 2 · Unit 2 · Electric Energy and Radioactivity",
            SCIENCE_T2_UNIT2_LESSONS,
            "science_t2_u2_lesson",
            module_id="science",
        )
    elif source.id == "science_prep3_t2" and unit_title == "Genetics":
        render_verified_unit(
            "Term 2 · Unit 3 · Genetics",
            SCIENCE_T2_UNIT3_LESSONS,
            "science_t2_u3_lesson",
            module_id="science",
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
        key_prefix="science_source_session",
    )
