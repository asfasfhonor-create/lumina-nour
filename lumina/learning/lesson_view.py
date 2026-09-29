import streamlit as st

from lumina.learning.progress import derive_mastery, mastery_label
from lumina.learning.progress_view import render_learning_brain_summary
from lumina.persistence.session_store import get_learning_store
from lumina.learning.rewards import apply_success_reward


def render_verified_unit(
    title: str,
    lessons,
    select_key: str,
    *,
    module_id: str,
) -> None:
    st.markdown(f"### {title}")
    st.caption("Verified from a trusted curriculum source.")
    render_learning_brain_summary([lesson.id for lesson in lessons])

    lesson = st.selectbox(
        "Choose lesson",
        lessons,
        format_func=lambda item: item.title,
        key=select_key,
    )
    render_verified_lesson(lesson, module_id=module_id)


def render_verified_lesson(lesson, *, module_id: str) -> None:
    store = get_learning_store()
    st.markdown(f"### {lesson.title}")
    st.caption(f"Verified curriculum extract · {lesson.source_pages}")

    with st.expander("What you will learn", expanded=True):
        for objective in lesson.objectives:
            st.write(f"• {objective}")

    st.markdown("**Key words / language**")
    st.write(" · ".join(lesson.key_terms))

    st.markdown("**Core ideas from the lesson**")
    for point in lesson.evidence_summary:
        st.write(f"• {point}")

    st.markdown("#### Quick understanding checks")
    for check in lesson.checks:
        answer = st.radio(
            check.prompt,
            list(check.options),
            index=None,
            key=f"lesson_check_{module_id}_{lesson.id}_{check.id}",
        )

        if st.button(
            "Check my thinking",
            key=f"lesson_check_button_{module_id}_{lesson.id}_{check.id}",
        ) and answer:
            selected_index = list(check.options).index(answer)
            correct = selected_index == check.correct_index
            store.record_attempt(
                {
                    "module_id": module_id,
                    "unit_id": lesson.unit_id,
                    "lesson_id": lesson.id,
                    "check_id": check.id,
                    "evidence_id": check.id,
                    "answer": answer,
                    "correct": correct,
                    "source_pages": lesson.source_pages,
                }
            )

            if correct:
                store.resolve_mistake(lesson.id, check.id)
                store.complete_review(lesson.id, check.id)
                earned_xp = apply_success_reward(
                    module_id=module_id,
                    lesson_id=lesson.id,
                    evidence_id=check.id,
                    activity_type="lesson",
                )
                st.success("Good thinking — this matches the lesson.")
                if earned_xp:
                    st.caption(f"+{earned_xp} XP for new demonstrated learning evidence.")
            else:
                store.record_mistake(
                    {
                        "module_id": module_id,
                        "unit_id": lesson.unit_id,
                        "lesson_id": lesson.id,
                        "lesson_title": lesson.title,
                        "check_id": check.id,
                        "question": check.prompt,
                        "answer": answer,
                        "mistake_type": "concept_understanding",
                        "hint": check.hint,
                        "source_pages": lesson.source_pages,
                        "resolved": False,
                    }
                )
                store.queue_review(
                    {
                        "module_id": module_id,
                        "lesson_id": lesson.id,
                        "lesson_title": lesson.title,
                        "check_id": check.id,
                        "status": "due",
                        "reason": "incorrect_understanding_check",
                        "source_pages": lesson.source_pages,
                    }
                )
                st.warning("Not yet. Use the hint, then try again.")
                st.info(f"Hint: {check.hint}")

    attempts = store.get_attempts(lesson.id)
    mistakes = store.get_mistakes(lesson.id)
    mastery = derive_mastery(attempts, mistakes)
    st.caption(
        f"Mastery: {mastery_label(mastery.state)} · "
        f"{mastery.correct_attempts}/{mastery.attempts} successful attempt(s) · "
        f"{mastery.distinct_evidence} distinct evidence item(s) · "
        f"{mastery.unresolved_mistakes} unresolved mistake(s)"
    )

    due_reviews = [
        review
        for review in store.get_reviews("due")
        if review.get("lesson_id") == lesson.id
    ]
    if due_reviews:
        st.warning("Review due: this lesson has something worth revisiting before moving on.")
