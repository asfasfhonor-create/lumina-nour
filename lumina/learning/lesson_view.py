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
    st.caption("محتوى موثّق من مصدر المنهج.")
    render_learning_brain_summary([lesson.id for lesson in lessons])

    lesson = st.selectbox(
        "اختاري الدرس",
        lessons,
        format_func=lambda item: item.title,
        key=select_key,
    )
    render_verified_lesson(lesson, module_id=module_id)


def render_verified_lesson(lesson, *, module_id: str) -> None:
    store = get_learning_store()
    st.markdown(f"### {lesson.title}")
    st.caption(f"من المصدر: {lesson.source_pages}")

    with st.expander("هنتعلم إيه؟", expanded=True):
        for objective in lesson.objectives:
            st.write(f"• {objective}")

    st.markdown("**الكلمات والمصطلحات المهمة**")
    st.write(" · ".join(lesson.key_terms))

    st.markdown("**أهم أفكار الدرس**")
    for point in lesson.evidence_summary:
        st.write(f"• {point}")

    st.markdown("#### أسئلة سريعة للتأكد من الفهم")
    for check in lesson.checks:
        answer = st.radio(
            check.prompt,
            list(check.options),
            index=None,
            key=f"lesson_check_{module_id}_{lesson.id}_{check.id}",
        )

        if st.button(
            "تحققي من إجابتي",
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
                st.success("إجابة صحيحة 👏 الفكرة واضحة عندك.")
                if earned_xp:
                    st.caption(f"+{earned_xp} XP لأنك أثبتّي فهم جديد.")
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
                st.warning("لسه محتاجة محاولة تانية. استخدمي التلميح وجربي من جديد.")
                st.info(f"تلميح: {check.hint}")

    attempts = store.get_attempts(lesson.id)
    mistakes = store.get_mistakes(lesson.id)
    mastery = derive_mastery(attempts, mistakes)
    st.caption(
        f"حالة التعلّم: {mastery_label(mastery.state)} · "
        f"{mastery.correct_attempts}/{mastery.attempts} محاولات صحيحة · "
        f"{mastery.distinct_evidence} أدلة فهم مختلفة · "
        f"{mastery.unresolved_mistakes} أخطاء محتاجة مراجعة"
    )

    due_reviews = [
        review
        for review in store.get_reviews("due")
        if review.get("lesson_id") == lesson.id
    ]
    if due_reviews:
        st.warning("في نقطة في الدرس محتاجة مراجعة قبل ما نعتبرها ثابتة.")
