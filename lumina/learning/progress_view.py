import streamlit as st

from lumina.learning.progress import (
    LEARNING,
    MASTERED,
    NEEDS_REVIEW,
    NOT_STARTED,
    derive_mastery,
    mastery_label,
)
from lumina.persistence.session_store import get_learning_store


def render_learning_brain_summary(lesson_ids: list[str] | None = None) -> None:
    """Render a compact evidence summary from the current persistence adapter."""
    store = get_learning_store()
    attempts = store.get_attempts()
    mistakes = store.get_mistakes(unresolved_only=True)
    due_reviews = store.get_reviews("due")

    st.markdown('<div class="section-title">🧠 Learning Brain</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Attempts", len(attempts))
    with c2:
        st.metric("Mistakes to review", len(mistakes))
    with c3:
        st.metric("Reviews due", len(due_reviews))

    if lesson_ids:
        states = []
        for lesson_id in lesson_ids:
            lesson_attempts = [a for a in attempts if a.get("lesson_id") == lesson_id]
            lesson_mistakes = [m for m in store.get_mistakes(lesson_id) if not m.get("resolved", False)]
            states.append(derive_mastery(lesson_attempts, lesson_mistakes).state)

        counts = {
            NOT_STARTED: states.count(NOT_STARTED),
            LEARNING: states.count(LEARNING),
            NEEDS_REVIEW: states.count(NEEDS_REVIEW),
            MASTERED: states.count(MASTERED),
        }
        st.caption(
            " · ".join(
                f"{mastery_label(state)}: {count}"
                for state, count in counts.items()
                if count
            )
        )

    if due_reviews:
        with st.expander("What needs review?", expanded=False):
            for review in due_reviews:
                st.write(f"• {review.get('lesson_title', review.get('lesson_id'))}")
