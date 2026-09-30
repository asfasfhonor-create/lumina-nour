import streamlit as st

from lumina.ai_service import GeminiService
from lumina.curriculum.retrieval import context_for_hit, grounded_prompt
from lumina.curriculum.search import lesson_by_id, search_curriculum


def render_curriculum_search(ai: GeminiService) -> None:
    st.markdown('<div class="section-title">🔎 البحث في المنهج</div>', unsafe_allow_html=True)
    st.caption("ابحثي داخل المحتوى الموثق من كتبك — من غير إضافة درس أو معلومة مش موجودة في المصدر.")

    query = st.text_input(
        "اكتبي كلمة أو فكرة",
        placeholder="مثال: Ohm's law / اسم المفعول / الثورة العرابية",
        key="curriculum_search_query",
    )

    if not query:
        return

    hits = search_curriculum(query)
    if not hits:
        st.info("ملقتش نتيجة موثقة داخل الخريطة الحالية.")
        return

    selected_id = st.selectbox(
        "اختاري النتيجة",
        [hit.lesson_id for hit in hits],
        format_func=lambda lesson_id: next(
            f"{hit.title} · {hit.source_pages}"
            for hit in hits
            if hit.lesson_id == lesson_id
        ),
        key="curriculum_search_result",
    )

    lesson = lesson_by_id(selected_id)
    if lesson is None:
        return

    st.markdown(f"### {lesson.title}")
    for point in lesson.evidence_summary:
        st.write(f"• {point}")
    st.caption(f"المصدر: {lesson.source_pages}")

    if st.button(
        "افتحي الدرس كامل",
        key=f"curriculum_open_{lesson.id}",
        use_container_width=True,
    ):
        st.session_state.focus_lesson_id = lesson.id
        st.session_state.active_world = "lesson_focus"
        st.rerun()

    question = st.text_input(
        "عندك سؤال عن الجزء ده؟",
        key=f"curriculum_question_{lesson.id}",
    )
    if st.button("اشرح من الجزء الموثق", key=f"curriculum_ask_{lesson.id}") and question:
        if not ai.available:
            st.warning("الشرح الذكي مش مفعّل حاليًا. تقدري تفتحي الدرس وتكمّلي المراجعة عادي.")
            return

        selected_hit = next((hit for hit in hits if hit.lesson_id == lesson.id), None)
        context = context_for_hit(selected_hit) if selected_hit is not None else None
        if context is None:
            st.warning("المصدر المرتبط بالدرس غير مكتمل في سجل المنهج، لذلك لن نخمن الإجابة.")
            return

        response = ai.generate(grounded_prompt(context, question))
        st.markdown(response)
        st.caption(f"الشرح مبني على المصدر: {context.provenance_label}")
        if not context.trusted:
            st.caption("تنبيه: هذا المصدر مرفوع للمشروع لكن تغطيته للسنة الحالية لم تُتحقق بعد.")
