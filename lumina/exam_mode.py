from __future__ import annotations

import streamlit as st

from lumina.curriculum.mapped_curriculum import MAPPED_CURRICULUM, SUBJECT_LABELS
from lumina.persistence.session_store import get_learning_store
from lumina.learning.rewards import apply_success_reward
from lumina.learning.progress import LEARNING, MASTERED, NEEDS_REVIEW, NOT_STARTED, derive_mastery
from lumina.learning.evidence_cache import group_by_lesson


def _pick_checks(lessons, store, limit: int = 5):
    """Build a source-grounded adaptive exam set without inventing questions.

    Priority is weak/in-progress learning first, then unseen material, then
    mastered material for spaced reinforcement. We prefer one check per lesson
    before taking a second check from the same lesson.
    """
    attempts_by_lesson = group_by_lesson(store.get_attempts())
    mistakes_by_lesson = group_by_lesson(store.get_mistakes())

    priority = {
        NEEDS_REVIEW: 0,
        LEARNING: 1,
        NOT_STARTED: 2,
        MASTERED: 3,
    }

    ranked = []
    for curriculum_index, lesson in enumerate(lessons):
        state = derive_mastery(
            attempts_by_lesson.get(lesson.id, []),
            mistakes_by_lesson.get(lesson.id, []),
        ).state
        ranked.append((priority.get(state, 9), curriculum_index, lesson))

    ranked.sort(key=lambda item: (item[0], item[1]))

    picked = []
    for _, _, lesson in ranked:
        if lesson.checks:
            picked.append((lesson, lesson.checks[0]))
            if len(picked) >= limit:
                return picked

    for _, _, lesson in ranked:
        for check in lesson.checks[1:]:
            picked.append((lesson, check))
            if len(picked) >= limit:
                return picked

    return picked


def render_exam_mode() -> None:
    st.markdown('<div class="section-title">🧪 Exam Mode</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="mission"><b>اختبار من المحتوى الموثق فقط.</b><br>'
        '<span class="muted">الأسئلة هنا تأتي من خرائط الدروس المأخوذة من المصادر، '
        'والنتيجة تدخل Learning Brain بدل ما تكون درجة منفصلة.</span></div>',
        unsafe_allow_html=True,
    )

    subject_id = st.selectbox(
        "المادة",
        list(MAPPED_CURRICULUM.keys()),
        format_func=lambda sid: SUBJECT_LABELS.get(sid, sid),
        key="exam_subject",
    )
    units = MAPPED_CURRICULUM[subject_id]
    unit_title = st.selectbox(
        "الوحدة / الفصل",
        list(units.keys()),
        key="exam_unit",
    )
    lessons = units[unit_title]
    store = get_learning_store()
    checks = _pick_checks(lessons, store, limit=5)

    if not checks:
        st.info("لا توجد أسئلة موثقة لهذا الجزء حتى الآن.")
        return

    st.caption(
        f"{len(checks)} سؤال · من {unit_title} · "
        "Adaptive set: نقاط الضعف والتعلم الجاري أولًا"
    )

    answers: dict[str, int] = {}
    for idx, (lesson, check) in enumerate(checks, start=1):
        choice = st.radio(
            f"{idx}. {check.prompt}",
            list(check.options),
            index=None,
            key=f"exam_{subject_id}_{unit_title}_{lesson.id}_{check.id}",
        )
        if choice is not None:
            answers[f"{lesson.id}:{check.id}"] = list(check.options).index(choice)

    if st.button("سلّمي الاختبار", key=f"exam_submit_{subject_id}_{unit_title}"):
        if len(answers) != len(checks):
            st.warning("جاوبي على كل الأسئلة الأول.")
            return

        score = 0
        results = []

        for lesson, check in checks:
            selected = answers[f"{lesson.id}:{check.id}"]
            correct = selected == check.correct_index
            score += int(correct)
            answer_text = check.options[selected]

            store.record_attempt(
                {
                    "module_id": subject_id,
                    "unit_id": lesson.unit_id,
                    "lesson_id": lesson.id,
                    "check_id": check.id,
                    "evidence_id": f"exam:{check.id}",
                    "answer": answer_text,
                    "correct": correct,
                    "source_pages": lesson.source_pages,
                    "activity_type": "exam",
                }
            )

            if correct:
                store.resolve_mistake(lesson.id, check.id)
                store.complete_review(lesson.id, check.id)
                apply_success_reward(
                    module_id=subject_id,
                    lesson_id=lesson.id,
                    evidence_id=f"exam:{check.id}",
                    activity_type="exam",
                )
            else:
                store.record_mistake(
                    {
                        "module_id": subject_id,
                        "unit_id": lesson.unit_id,
                        "lesson_id": lesson.id,
                        "lesson_title": lesson.title,
                        "check_id": check.id,
                        "question": check.prompt,
                        "answer": answer_text,
                        "mistake_type": "exam_understanding",
                        "hint": check.hint,
                        "source_pages": lesson.source_pages,
                        "resolved": False,
                    }
                )
                store.queue_review(
                    {
                        "module_id": subject_id,
                        "lesson_id": lesson.id,
                        "lesson_title": lesson.title,
                        "check_id": check.id,
                        "status": "due",
                        "reason": "exam_mistake",
                        "source_pages": lesson.source_pages,
                    }
                )
            results.append((lesson, check, correct))

        st.success(f"النتيجة: {score}/{len(checks)}")

        if score == len(checks):
            st.info("ممتاز. النتيجة أضافت Learning Evidence، لكنها لا تمنح Mastery تلقائيًا من اختبار واحد.")
        else:
            st.warning("الأخطاء اتسجلت تلقائيًا في Mistake Notebook وReview Queue.")

        with st.expander("مراجعة النتيجة", expanded=True):
            for idx, (lesson, check, correct) in enumerate(results, start=1):
                icon = "✅" if correct else "❌"
                st.write(f"{icon} {idx}. {lesson.title}")
                if not correct:
                    st.caption(f"Hint للمراجعة: {check.hint} · Source: {lesson.source_pages}")
