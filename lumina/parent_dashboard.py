import streamlit as st

from lumina.curriculum.english_curriculum import ENGLISH_UNIT_LESSONS, all_english_lessons
from lumina.learning.progress import derive_mastery, mastery_label
from lumina.persistence.session_store import get_learning_store


def render_parent_dashboard(parent_pin: str | None) -> None:
    st.markdown('<div class="section-title">👨‍👧 Parent Dashboard</div>', unsafe_allow_html=True)

    if not parent_pin:
        st.info(
            "Parent Dashboard is protected by design. Configure PARENT_PIN in Streamlit secrets "
            "before enabling this area."
        )
        return

    if not st.session_state.get("parent_unlocked", False):
        entered = st.text_input("Parent PIN", type="password", key="parent_pin_input")
        if st.button("Open Parent Dashboard", key="parent_unlock"):
            if entered == parent_pin:
                st.session_state.parent_unlocked = True
                st.rerun()
            else:
                st.error("PIN غير صحيح.")
        return

    if st.button("Lock Parent Dashboard", key="parent_lock"):
        st.session_state.parent_unlocked = False
        st.rerun()

    store = get_learning_store()
    attempts = store.get_attempts()
    mistakes = store.get_mistakes(unresolved_only=True)
    reviews = store.get_reviews("due")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Learning attempts", len(attempts))
    with c2:
        st.metric("Mistakes to review", len(mistakes))
    with c3:
        st.metric("Reviews due", len(reviews))

    st.markdown("### English curriculum progress")
    unit_rows = []
    for unit_title, lessons in ENGLISH_UNIT_LESSONS.items():
        states = []
        for lesson in lessons:
            lesson_attempts = [a for a in attempts if a.get("lesson_id") == lesson.id]
            lesson_mistakes = store.get_mistakes(lesson.id)
            states.append(derive_mastery(lesson_attempts, lesson_mistakes).state)

        started = sum(1 for state in states if state != "not_started")
        needs_review = sum(1 for state in states if state == "needs_review")
        mastered = sum(1 for state in states if state == "mastered")
        unit_rows.append((unit_title, started, needs_review, mastered, len(lessons)))

    for unit_title, started, needs_review, mastered, total in unit_rows:
        st.write(
            f"**{unit_title}** — started {started}/{total} · "
            f"needs review {needs_review} · mastered {mastered}"
        )

    if mistakes:
        st.markdown("### Current weak points")
        for mistake in mistakes:
            st.write(
                f"• {mistake.get('lesson_title', mistake.get('lesson_id'))} — "
                f"{mistake.get('mistake_type', 'learning mistake')}"
            )

    total_lessons = len(all_english_lessons())
    started_lessons = 0
    states = []
    for lesson in all_english_lessons():
        snapshot = derive_mastery(store.get_attempts(lesson.id), store.get_mistakes(lesson.id))
        states.append(snapshot.state)
        if snapshot.state != "not_started":
            started_lessons += 1

    st.caption(
        f"English mapped lessons: {total_lessons} · started: {started_lessons} · "
        f"overall view uses evidence, not button clicks."
    )
