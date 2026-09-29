import streamlit as st

from lumina.ai_service import GeminiService
from lumina.curriculum.search import lesson_by_id, search_curriculum


def render_curriculum_search(ai: GeminiService) -> None:
    st.markdown('<div class="section-title">🔎 Curriculum Search</div>', unsafe_allow_html=True)
    st.caption("ابحثي داخل المحتوى المرسوم والموثق من كتبك — من غير اختراع Term أو درس غير موجود.")

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
    st.caption(f"Source: {lesson.source_pages} · {lesson.source_id}")

    question = st.text_input(
        "عندك سؤال عن الجزء ده؟",
        key=f"curriculum_question_{lesson.id}",
    )
    if st.button("اشرح من الجزء الموثق", key=f"curriculum_ask_{lesson.id}") and question:
        if not ai.available:
            st.warning("الشرح الذكي يحتاج Gemini API Key.")
            return

        source_text = "\n".join(f"- {point}" for point in lesson.evidence_summary)
        response = ai.generate(
            f"""You are Nour's curriculum tutor.
Answer ONLY from the verified lesson evidence below.
If the evidence is insufficient, say clearly that the mapped evidence is not enough.
Do not invent facts, page details, examples, or exam rules.
Preserve the lesson terminology and explain simply.

Lesson: {lesson.title}
Source pages: {lesson.source_pages}
Verified evidence:
{source_text}

Nour's question:
{question}

Use the tutor pattern: explain briefly, give one small example only if supported by the evidence, then ask one checking question."""
        )
        st.markdown(response)
        st.caption(f"Grounded to: {lesson.source_pages}")
