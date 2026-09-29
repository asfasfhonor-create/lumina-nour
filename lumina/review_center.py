import streamlit as st

from lumina.context_help import render_context_help

from lumina.curriculum.mapped_curriculum import SUBJECT_LABELS
from lumina.curriculum.search import lesson_by_id
from lumina.learning.rewards import apply_success_reward
from lumina.persistence.session_store import get_learning_store


def _find_check(lesson, check_id: str):
    return next((check for check in lesson.checks if check.id == check_id), None)


def render_review_center() -> None:
    store = get_learning_store()
    mistakes = store.get_mistakes(unresolved_only=True)
    reviews = store.get_reviews("due")

    st.markdown('<div class="section-title">📝 Mistake Notebook & Review</div>', unsafe_allow_html=True)
    render_context_help("review_center")
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
            subject = SUBJECT_LABELS.get(mistake.get("module_id"), mistake.get("module_id", ""))
            title = mistake.get("lesson_title", mistake.get("lesson_id", "Lesson"))
            with st.expander(f"{subject} · {title}"):
                st.write(f"**Question:** {mistake.get('question', '—')}")
                st.write(f"**Your previous answer:** {mistake.get('answer', '—')}")
                st.info(f"Hint: {mistake.get('hint', 'راجعي الفكرة مرة أخرى.')}")
                if mistake.get("source_pages"):
                    st.caption(f"Source: {mistake['source_pages']}")

    if reviews:
        st.markdown("### Review Queue")
        st.caption("راجعي السؤال هنا مباشرة بدل ما تدوري على الدرس من جديد.")

        seen = set()
        for review in reviews:
            key = (review.get("lesson_id"), review.get("check_id"))
            if key in seen:
                continue
            seen.add(key)

            lesson = lesson_by_id(review.get("lesson_id"))
            if lesson is None:
                st.warning(f"تعذر العثور على الدرس: {review.get('lesson_title', review.get('lesson_id'))}")
                continue

            check = _find_check(lesson, review.get("check_id"))
            if check is None:
                st.warning(f"تعذر العثور على سؤال المراجعة داخل: {lesson.title}")
                continue

            module_id = review.get("module_id") or "review"
            subject = SUBJECT_LABELS.get(module_id, module_id)

            with st.container(border=True):
                st.markdown(f"**{subject} · {lesson.title}**")
                st.caption(f"Source: {lesson.source_pages}")
                answer = st.radio(
                    check.prompt,
                    list(check.options),
                    index=None,
                    key=f"review_retry_{lesson.id}_{check.id}",
                )

                if st.button(
                    "راجعت وجربت تاني",
                    key=f"review_retry_button_{lesson.id}_{check.id}",
                ):
                    if answer is None:
                        st.warning("اختاري إجابة الأول.")
                        continue

                    selected_index = list(check.options).index(answer)
                    correct = selected_index == check.correct_index

                    store.record_attempt(
                        {
                            "module_id": module_id,
                            "unit_id": lesson.unit_id,
                            "lesson_id": lesson.id,
                            "check_id": check.id,
                            "evidence_id": f"review:{check.id}",
                            "answer": answer,
                            "correct": correct,
                            "source_pages": lesson.source_pages,
                            "activity_type": "review",
                        }
                    )

                    if correct:
                        store.resolve_mistake(lesson.id, check.id)
                        store.complete_review(lesson.id, check.id)
                        earned_xp = apply_success_reward(
                            module_id=module_id,
                            lesson_id=lesson.id,
                            evidence_id=f"review:{check.id}",
                            activity_type="review",
                        )
                        st.success("تمام — المراجعة اتقفلت لأنك أظهرتِ فهم جديد.")
                        if earned_xp:
                            st.caption(f"+{earned_xp} XP for successful review evidence.")
                        st.rerun()
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
                                "mistake_type": "review_retry",
                                "hint": check.hint,
                                "source_pages": lesson.source_pages,
                                "resolved": False,
                            }
                        )
                        st.warning("لسه محتاجة محاولة كمان. استخدمي الـHint وجربي مرة أخرى.")
                        st.info(f"Hint: {check.hint}")
