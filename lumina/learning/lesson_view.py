import streamlit as st

from lumina.learning.progress import derive_mastery, mastery_label
from lumina.learning.progress_view import render_learning_brain_summary
from lumina.persistence.session_store import get_learning_store
from lumina.learning.rewards import apply_success_reward
from lumina.learning.scaffolding import (
    eligible_checks,
    learning_stage,
    mission_theme,
    support_depth,
)
from lumina.curriculum.permanent_source_learning import render_permanent_source_booster


def render_verified_unit(
    title: str,
    lessons,
    select_key: str,
    *,
    module_id: str,
    ai=None,
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
    render_verified_lesson(lesson, module_id=module_id, ai=ai)


def _pick_check(checks, attempts, mistakes):
    unresolved_ids = {
        str(item.get("check_id"))
        for item in mistakes
        if not item.get("resolved", False) and item.get("check_id")
    }
    for check in checks:
        if check.id in unresolved_ids:
            return check

    correct_ids = {
        str(item.get("check_id"))
        for item in attempts
        if item.get("correct") is True and item.get("check_id")
    }
    for check in checks:
        if check.id not in correct_ids:
            return check
    return checks[-1] if checks else None


def _render_concept_support(lesson, depth: int) -> None:
    if not lesson.evidence_summary:
        return

    if depth == 0:
        st.info("💡 تلميح صغير: خدي بالك من الكلمات الأساسية في السؤال، وبعدين اختاري.")
        return

    if depth == 1:
        st.markdown("**نفك الفكرة سوا قبل ما تجربي تاني:**")
        st.write(f"• {lesson.evidence_summary[0]}")
        if len(lesson.evidence_summary) > 1:
            st.write(f"• {lesson.evidence_summary[1]}")
        return

    st.markdown("**نرجع للفكرة من غير حفظ الإجابة:**")
    for point in lesson.evidence_summary[:3]:
        st.write(f"• {point}")
    st.caption("اقري الفكرة، وبعدها اختاري بإيدك. مفيش خصم على المحاولة.")


def render_verified_lesson(lesson, *, module_id: str, ai=None) -> None:
    store = get_learning_store()
    attempts = store.get_attempts(lesson.id)
    mistakes = store.get_mistakes(lesson.id)
    stage = learning_stage(attempts, mistakes)
    icon, mission_name = mission_theme(module_id)

    st.markdown(f"### {lesson.title}")
    st.caption(f"من المصدر: {lesson.source_pages}")

    st.markdown(
        f'<div class="mission"><b>{icon} {mission_name} · {stage.label}</b><br>'
        f'<span class="muted">{stage.mission_label} — {stage.reassurance}</span></div>',
        unsafe_allow_html=True,
    )

    st.markdown("#### الفكرة ببساطة")
    for point in lesson.evidence_summary[:2]:
        st.write(f"• {point}")

    with st.expander("عايزة تعرفي أكتر عن الدرس؟", expanded=False):
        st.markdown("**هنتعلم إيه؟**")
        for objective in lesson.objectives:
            st.write(f"• {objective}")
        if lesson.key_terms:
            st.markdown("**الكلمات والمصطلحات المهمة**")
            st.write(" · ".join(lesson.key_terms))
        if len(lesson.evidence_summary) > 2:
            st.markdown("**أفكار إضافية من المصدر**")
            for point in lesson.evidence_summary[2:]:
                st.write(f"• {point}")

    if ai is not None:
        render_permanent_source_booster(
            ai,
            subject_id=module_id,
            lesson_title=lesson.title,
            stage_label=stage.label,
        )

    checks = eligible_checks(lesson, stage)
    check = _pick_check(checks, attempts, mistakes)
    if check is None:
        st.info("الدرس متاح للشرح حاليًا، ولسه مفيش تحدّي مناسب مضاف له.")
        return

    st.markdown("#### 🎮 تحدّي صغير")
    st.caption("سؤال واحد بس دلوقتي. لما الفكرة تثبت، LUMINA تزود التحدّي تدريجيًا.")

    depth = support_depth(attempts, check.id)
    if depth:
        _render_concept_support(lesson, depth)

    answer = st.radio(
        check.prompt,
        list(check.options),
        index=None,
        key=f"lesson_check_{module_id}_{lesson.id}_{check.id}",
    )

    if st.button(
        "أجرب إجابتي",
        key=f"lesson_check_button_{module_id}_{lesson.id}_{check.id}",
        use_container_width=True,
    ):
        if answer is None:
            st.warning("اختاري إجابة الأول — مفيش أي خصم لو كانت غلط.")
        else:
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
                    "activity_type": f"creative_mission_level_{getattr(check, 'difficulty', 1)}",
                }
            )

            if correct:
                store.resolve_mistake(lesson.id, check.id)
                store.complete_review(lesson.id, check.id)
                earned_xp = apply_success_reward(
                    module_id=module_id,
                    lesson_id=lesson.id,
                    evidence_id=check.id,
                    activity_type="creative_mission",
                )
                st.success("ممتاز 👏 فهمتي الفكرة، مش مجرد حفظتي الإجابة.")
                if earned_xp:
                    st.caption(f"+{earned_xp} XP لأنك أثبتّي فهم جديد.")
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
                st.warning("عادي جدًا — دي علامة إننا محتاجين نفك الفكرة أكتر، مش نحفظ الإجابة.")
                st.info(f"تلميح: {check.hint}")
                _render_concept_support(lesson, min(depth + 1, 2))

    attempts = store.get_attempts(lesson.id)
    mistakes = store.get_mistakes(lesson.id)
    mastery = derive_mastery(attempts, mistakes)
    st.caption(
        f"رحلة الفهم: {mastery_label(mastery.state)} · "
        f"{mastery.correct_attempts}/{mastery.attempts} محاولات صحيحة · "
        f"{mastery.distinct_evidence} دليل فهم مختلف"
    )

    due_reviews = [
        review
        for review in store.get_reviews("due")
        if review.get("lesson_id") == lesson.id
    ]
    if due_reviews:
        st.caption("🌱 في نقطة هنرجعلها بعدين بطريقة مختلفة علشان تثبت من غير ضغط.")
