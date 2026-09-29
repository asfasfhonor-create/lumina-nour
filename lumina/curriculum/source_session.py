import streamlit as st

from lumina.ai_service import GeminiService
from lumina.curriculum.grounding import build_grounded_pdf, curriculum_prompt


def render_temporary_source_session(
    ai: GeminiService,
    source,
    *,
    section_title: str | None = None,
    key_prefix: str,
) -> None:
    """Optional page-aware source session using Gemini's native PDF input.

    This is deliberately temporary: uploaded bytes are used only for the
    current Streamlit session and are never promoted to the trusted library.
    """
    st.markdown("---")
    st.caption("📎 اسألي من كتاب أو مذكرة في الجلسة الحالية")
    uploaded = st.file_uploader(
        "حمّلي نسخة الكتاب الموثوق لهذه الجلسة",
        type=["pdf"],
        key=f"{key_prefix}_trusted_source_pdf",
        help=(
            "الملف يُستخدم داخل الجلسة الحالية فقط. "
            f"المصدر المتوقع: {source.filename}"
        ),
    )
    if not uploaded:
        return

    if uploaded.name != source.filename:
        st.warning(
            "اسم الملف مختلف عن المصدر الموثق المسجل. "
            "سيُعامل كملف مؤقت ولن يُضاف تلقائيًا للمكتبة الموثوقة."
        )

    question = st.text_input(
        "اسألي من الكتاب نفسه",
        key=f"{key_prefix}_trusted_source_question",
        placeholder="اشرحي الفكرة، المصطلح، المثال أو التدريب من المصدر...",
    )
    if not question:
        return

    if st.button(
        "اشرحي من الكتاب",
        key=f"{key_prefix}_trusted_source_ask",
        use_container_width=True,
    ):
        if not ai.available:
            st.warning("ميزة الشرح الذكي من الملف مش مفعّلة حاليًا.")
            return

        grounded = build_grounded_pdf(source, uploaded.getvalue())
        prompt = curriculum_prompt(source, question, unit_title=section_title)
        with st.spinner("بقرأ المصدر..."):
            st.markdown(ai.generate([grounded.part, prompt]))
        st.caption(
            f"المصدر المستخدم الآن: {source.display_name} · "
            "لا يتم حفظ الملف أو اعتباره مصدرًا دائمًا تلقائيًا."
        )
