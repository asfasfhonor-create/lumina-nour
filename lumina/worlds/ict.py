import streamlit as st

from lumina.context_help import render_context_help

from lumina.ai_service import GeminiService
from lumina.curriculum.catalog import ICT_T2
from lumina.curriculum.ict_chapter1 import ICT_CHAPTER1_LESSONS
from lumina.curriculum.ict_chapter2 import ICT_CHAPTER2_LESSONS
from lumina.curriculum.ict_chapter3 import ICT_CHAPTER3_LESSONS
from lumina.curriculum.ict_chapter4 import ICT_CHAPTER4_LESSONS
from lumina.learning.lesson_view import render_verified_unit
from lumina.curriculum.source_session import render_temporary_source_session


def render_ict_world(ai: GeminiService) -> None:
    st.markdown('<div class="section-title">💻 ICT Lab</div>', unsafe_allow_html=True)
    render_context_help("ict", label="💬 قوليلي العالم ده بيعمل إيه")
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
        render_verified_unit("Chapter I · Data", ICT_CHAPTER1_LESSONS, "ict_c1_lesson", module_id="ict")
    elif chapter_title == "Branching":
        render_verified_unit("Chapter II · Branching", ICT_CHAPTER2_LESSONS, "ict_c2_lesson", module_id="ict")
    elif chapter_title == "Looping & Procedures":
        render_verified_unit("Chapter III · Looping & Procedures", ICT_CHAPTER3_LESSONS, "ict_c3_lesson", module_id="ict")
    elif chapter_title == "Cyber bullying":
        render_verified_unit("Chapter IV · Cyber bullying", ICT_CHAPTER4_LESSONS, "ict_c4_lesson", module_id="ict")
    render_temporary_source_session(
        ai,
        source,
        section_title=chapter_title,
        key_prefix="ict_source_session",
    )

