import streamlit as st

from lumina.ai_service import GeminiService
from lumina.curriculum.catalog import SOCIAL_T1
from lumina.curriculum.social_unit1 import SOCIAL_UNIT1_LESSONS
from lumina.learning.lesson_view import render_verified_unit


def render_social_world(ai: GeminiService) -> None:
    st.markdown('<div class="section-title">🌍 Social Detective</div>', unsafe_allow_html=True)
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
        render_verified_unit(
            "الوحدة الأولى · الملامح الطبيعية والحضارية لقارات العالم الجديد",
            SOCIAL_UNIT1_LESSONS,
            "social_u1_lesson",
            module_id="social",
        )
    else:
        st.info("هذه الوحدة موجودة في خريطة المنهج وسيتم تحويل دروسها إلى محتوى موثق بالتتابع.")
