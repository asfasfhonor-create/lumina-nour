import streamlit as st

from lumina.context_help import render_context_help

from lumina.curriculum.mapped_curriculum import SUBJECT_LABELS
from lumina.curriculum.search import lesson_by_id
from lumina.learning.rewards import apply_success_reward
from lumina.learning.question_presentation import presented_options, is_correct_answer
from lumina.learning.scaffolding import support_depth
from lumina.persistence.session_store import get_learning_store


def _find_check(lesson, check_id: str):
    return next((check for check in lesson.checks if check.id == check_id), None)


def render_review_center() -> None:
    store = get_learning_store()
    mistakes = store.get_mistakes(unresolved_only=True)
    reviews = store.get_reviews("due")

    st.markdown('<div class="section-title">📝 مراجعاتي</div>', unsafe_allow_html=True)
    render_context_help("review_center")
    st.markdown(
        '<div class="mission"><b>الغلط هنا معلومة مفيدة، مش عقوبة.</b><br>'
        '<span class="muted">بنرجع للحاجات اللي محتاجة مراجعة ونقفلها لما يظهر فهم جديد.</span></div>',
        unsafe_allow_html=True,
    )

    c1, c2 = st.columns(2)
    with c1:
        st.metric("أخطاء نراجعها", len(mistakes))
    with c2:
        st.metric("مراجعات مستحقة", len(reviews))

    if not mistakes and not reviews:
        st.success("مفيش مراجعات مستحقة حاليًا. كمّلي تعلمك 🌱")
        return

    if mistakes:
        st.markdown("### دفتر الأخطاء")
        for mistake in mistakes:
            subject = SUBJECT_LABELS.get(mistake.get("module_id"), mistake.get("module_id", ""))
            title = mistake.get("lesson_title", mistake.get("lesson_id", "Lesson"))
            with st.expander(f"{subject} · {title}"):
                st.write(f"**السؤال:** {mistake.get('question', '—')}")
                st.write(f"**إجابتك السابقة:** {mistake.get('answer', '—')}")
                st.info(f"تلميح: {mistake.get('hint', 'راجعي الفكرة مرة أخرى.')}")
                st.caption("الغلط هنا مش بيتحسب ضدك؛ بنستخدمه علشان نعرف نشرح الفكرة بطريقة أبسط.")
                if mistake.get("source_pages"):
                    st.caption(f"المصدر: {mistake['source_pages']}")

    if reviews:
        st.markdown("### أسئلة جاهزة للمراجعة")
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
                st.caption(f"المصدر: {lesson.source_pages}")
                previous_attempts = store.get_attempts(lesson.id)
                depth = support_depth(previous_attempts, check.id)
                if depth >= 1 and lesson.evidence_summary:
                    st.info("نفك الفكرة الأول: " + lesson.evidence_summary[0])
                if depth >= 2 and len(lesson.evidence_summary) > 1:
                    st.write("• " + lesson.evidence_summary[1])

                answer = st.radio(
                    check.prompt,
                    list(presented_options(check)),
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

                    correct = is_correct_answer(check, answer)

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
                            "activity_type": (
                                "review_recall"
                                if getattr(check, "mastery_eligible", True) is False
                                else "review"
                            ),
                            "cognitive_kind": getattr(check, "activity_kind", "concept"),
                            "mastery_eligible": bool(getattr(check, "mastery_eligible", True)),
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
                        if getattr(check, "mastery_eligible", True) is False:
                            st.success("تمام — معلومة التذكّر اتصححت واتقفلت. الإتقان الكامل لسه محتاج فهم أو تطبيق.")
                        else:
                            st.success("تمام — المراجعة اتقفلت لأنك أظهرتِ فهم جديد.")
                        if earned_xp:
                            st.caption(f"+{earned_xp} XP لإجابة مراجعة صحيحة.")
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
                        st.warning("ولا يهمك — نرجع خطوة صغيرة ونفهمها، وبعدها نجرب تاني.")
                        st.info(f"تلميح: {check.hint}")
                        if lesson.evidence_summary:
                            st.write("الفكرة الأساسية من المصدر: " + lesson.evidence_summary[0])
