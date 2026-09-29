import streamlit as st

from lumina.context_help import render_context_help

from lumina.ai_service import GeminiService
from lumina.curriculum.catalog import RELIGION_T1
from lumina.curriculum.religion_unit1 import RELIGION_U1_LESSONS
from lumina.curriculum.religion_unit2 import RELIGION_U2_LESSONS
from lumina.curriculum.religion_unit3 import RELIGION_U3_LESSONS
from lumina.learning.lesson_view import render_verified_unit
from lumina.curriculum.source_session import render_temporary_source_session


def render_religion_world(ai: GeminiService) -> None:
    st.markdown('<div class="section-title">🕌 رحلة الدين</div>', unsafe_allow_html=True)
    render_context_help("religion", label="💬 قوليلي العالم ده بيعمل إيه")
    st.markdown(
        '<div class="mission"><b>فهم + قيمة + تطبيق.</b><br>'
        '<span class="muted">نحافظ على نص ومقاصد كتاب التربية الدينية، ونربط الفهم بالسلوك اليومي.</span></div>',
        unsafe_allow_html=True,
    )

    source = RELIGION_T1
    st.caption(f"المصدر الموثوق: {source.display_name}")
    unit_title = st.selectbox(
        "اختاري الوحدة",
        [unit.title for unit in source.units],
        key="school_religion_unit",
    )

    if unit_title == "قيم الإسلام في بناء الفرد والمجتمع":
        render_verified_unit("الوحدة الأولى · قيم الإسلام في بناء الفرد والمجتمع", RELIGION_U1_LESSONS, "religion_u1_lesson", module_id="religion", ai=ai)
    elif unit_title == "الإسلام دين وحياة":
        render_verified_unit("الوحدة الثانية · الإسلام دين وحياة", RELIGION_U2_LESSONS, "religion_u2_lesson", module_id="religion", ai=ai)
    elif unit_title == "تحمل المسئولية في الإسلام":
        render_verified_unit("الوحدة الثالثة · تحمل المسئولية في الإسلام", RELIGION_U3_LESSONS, "religion_u3_lesson", module_id="religion", ai=ai)
    render_temporary_source_session(
        ai,
        source,
        section_title=unit_title,
        key_prefix="religion_source_session",
    )

