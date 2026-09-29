import streamlit as st

from lumina.ai_service import GeminiService
from lumina.curriculum.catalog import ARABIC_T1
from lumina.curriculum.arabic_unit1 import ARABIC_U1_LESSONS
from lumina.curriculum.arabic_unit2 import ARABIC_U2_LESSONS
from lumina.curriculum.arabic_unit3 import ARABIC_U3_LESSONS
from lumina.learning.lesson_view import render_verified_unit


def render_arabic_world(ai: GeminiService) -> None:
    st.markdown('<div class="section-title">📖 Arabic World</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="mission"><b>نفهم اللغة ونستخدمها، مش نحفظها بس.</b><br>'
        '<span class="muted">الشرح يحافظ على ترتيب ومصطلحات كتاب نور، مع تدريب على الفهم والتعبير.</span></div>',
        unsafe_allow_html=True,
    )

    source = ARABIC_T1
    st.caption(f"المصدر الموثوق: {source.display_name}")
    unit_title = st.selectbox(
        "اختاري الوحدة",
        [unit.title for unit in source.units],
        key="school_arabic_unit",
    )

    if unit_title == "قيم تحمي شبابنا":
        render_verified_unit("الوحدة الأولى · قيم تحمي شبابنا", ARABIC_U1_LESSONS, "arabic_u1_lesson", module_id="arabic")
    elif unit_title == "نحو تفكير سليم":
        render_verified_unit("الوحدة الثانية · نحو تفكير سليم", ARABIC_U2_LESSONS, "arabic_u2_lesson", module_id="arabic")
    elif unit_title == "أنا والمستقبل":
        render_verified_unit("الوحدة الثالثة · أنا والمستقبل", ARABIC_U3_LESSONS, "arabic_u3_lesson", module_id="arabic")
    else:
        st.info("الجزء التمهيدي موجود في المصدر وسيظل متاحًا كمادة موثقة منفصلة عن الوحدات الثلاث.")
