import streamlit as st

from lumina.context_help import render_context_help

from lumina.ai_service import GeminiService
from lumina.curriculum.catalog import SOCIAL_T1
from lumina.curriculum.social_unit1 import SOCIAL_U1_LESSONS
from lumina.curriculum.social_unit2 import SOCIAL_U2_LESSONS
from lumina.curriculum.social_unit3 import SOCIAL_U3_LESSONS
from lumina.curriculum.social_unit4 import SOCIAL_U4_LESSONS
from lumina.learning.lesson_view import render_verified_unit
from lumina.curriculum.source_session import render_temporary_source_session


def render_social_world(ai: GeminiService) -> None:
    st.markdown('<div class="section-title">🌍 Social Studies</div>', unsafe_allow_html=True)
    render_context_help("social", label="💬 What can I do here?")
    st.markdown(
        '<div class="mission"><b>خريطة + دليل + استنتاج.</b><br>'
        '<span class="muted">الدراسات هنا تحقيق: نقرأ الخريطة ونربط السبب بالنتيجة بدل الحفظ المنفصل.</span></div>',
        unsafe_allow_html=True,
    )

    source = SOCIAL_T1
    st.caption(f"المصدر الموثوق: {source.display_name}")
    unit_title = st.selectbox(
        "اختاري الوحدة",
        [unit.title for unit in source.units],
        key="school_social_unit",
    )

    if unit_title == "الملامح الطبيعية والحضارية لقارات العالم الجديد":
        render_verified_unit("الوحدة الأولى · الملامح الطبيعية والحضارية لقارات العالم الجديد", SOCIAL_U1_LESSONS, "social_u1_lesson", module_id="social", ai=ai)
    elif unit_title == "مصر في عصر محمد علي وخلفائه":
        render_verified_unit("الوحدة الثانية · مصر في عصر محمد علي وخلفائه", SOCIAL_U2_LESSONS, "social_u2_lesson", module_id="social", ai=ai)
    elif unit_title == "النظم البيئية في قارات العالم الجديد":
        render_verified_unit("الوحدة الثالثة · النظم البيئية في قارات العالم الجديد", SOCIAL_U3_LESSONS, "social_u3_lesson", module_id="social", ai=ai)
    elif unit_title == "الحركة الوطنية في مواجهة الاحتلال البريطاني":
        render_verified_unit("الوحدة الرابعة · الحركة الوطنية في مواجهة الاحتلال البريطاني", SOCIAL_U4_LESSONS, "social_u4_lesson", module_id="social", ai=ai)
    render_temporary_source_session(
        ai,
        source,
        section_title=unit_title,
        key_prefix="social_source_session",
    )

