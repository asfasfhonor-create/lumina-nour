import streamlit as st

from lumina.ai_service import GeminiService
from lumina.curriculum.catalog import ICT_T2
from lumina.curriculum.ict_chapter1 import ICT_CHAPTER1_LESSONS
from lumina.learning.lesson_view import render_verified_unit


def render_ict_world(ai: GeminiService) -> None:
    st.markdown('<div class="section-title">💻 ICT Lab</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="mission"><b>School ICT stays school ICT.</b><br>'
        '<span class="muted">This world preserves the supplied Visual Basic .NET curriculum. Python remains a separate enrichment track.</span></div>',
        unsafe_allow_html=True,
    )

    source = ICT_T2
    st.caption(f"Trusted source: {source.display_name}")
    chapter_title = st.selectbox(
        "Choose chapter",
        [unit.title for unit in source.units],
        key="school_ict_chapter",
    )

    if chapter_title == "Data":
        render_verified_unit(
            "Chapter I · Data",
            ICT_CHAPTER1_LESSONS,
            "ict_c1_lesson",
            module_id="ict",
        )
    else:
        st.info("This chapter is inventoried and will be converted into verified lesson data next.")
