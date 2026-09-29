import streamlit as st

from lumina.ai_service import GeminiService
from lumina.curriculum.catalog import RELIGION_T1
from lumina.curriculum.religion_unit1 import RELIGION_UNIT1_LESSONS
from lumina.learning.lesson_view import render_verified_unit


def render_religion_world(ai: GeminiService) -> None:
    st.markdown('<div class="section-title">🕌 Religion Journey</div>', unsafe_allow_html=True)
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
        render_verified_unit(
            "الوحدة الأولى · قيم الإسلام في بناء الفرد والمجتمع",
            RELIGION_UNIT1_LESSONS,
            "religion_u1_lesson",
            module_id="religion",
        )
    else:
        st.info("هذه الوحدة موجودة في خريطة المنهج وسيتم تحويل دروسها إلى محتوى موثق بالتتابع.")
