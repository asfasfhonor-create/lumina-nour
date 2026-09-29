import streamlit as st

from lumina.persistence.session_store import get_learning_store


def render_review_center() -> None:
    store = get_learning_store()
    mistakes = store.get_mistakes(unresolved_only=True)
    reviews = store.get_reviews("due")

    st.markdown('<div class="section-title">📝 Mistake Notebook & Review</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="mission"><b>الغلط هنا معلومة مفيدة، مش عقوبة.</b><br>'
        '<span class="muted">بنرجع للحاجات اللي محتاجة مراجعة ونقفلها لما يظهر فهم جديد.</span></div>',
        unsafe_allow_html=True,
    )

    c1, c2 = st.columns(2)
    with c1:
        st.metric("Mistakes to revisit", len(mistakes))
    with c2:
        st.metric("Reviews due", len(reviews))

    if not mistakes and not reviews:
        st.success("مفيش مراجعات مستحقة حاليًا. كمّلي تعلمك 🌱")
        return

    if mistakes:
        st.markdown("### Mistake Notebook")
        for mistake in mistakes:
            with st.expander(mistake.get("lesson_title", mistake.get("lesson_id", "Lesson"))):
                st.write(f"**Question:** {mistake.get('question', '—')}")
                st.write(f"**Your answer:** {mistake.get('answer', '—')}")
                st.info(f"Hint: {mistake.get('hint', 'راجعي الفكرة مرة أخرى.')}")
                if mistake.get("source_pages"):
                    st.caption(f"Source: {mistake['source_pages']}")

    if reviews:
        st.markdown("### Review Queue")
        seen = set()
        for review in reviews:
            key = (review.get("lesson_id"), review.get("check_id"))
            if key in seen:
                continue
            seen.add(key)
            st.write(f"• {review.get('lesson_title', review.get('lesson_id'))}")
        st.caption("افتحي الدرس نفسه وجربي السؤال مرة أخرى؛ الإجابة الصحيحة الجديدة تغلق المراجعة تلقائيًا.")
