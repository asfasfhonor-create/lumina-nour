from __future__ import annotations

import streamlit as st

from lumina.context_help import render_context_help

from lumina.curriculum.mapped_curriculum import MAPPED_CURRICULUM, SUBJECT_LABELS
from lumina.persistence.session_store import get_learning_store
from lumina.learning.rewards import apply_success_reward
from lumina.learning.progress import LEARNING, MASTERED, NEEDS_REVIEW, NOT_STARTED, derive_mastery
from lumina.learning.evidence_cache import group_by_lesson


def _pick_checks(lessons, store, limit: int = 5, max_difficulty: int = 1):
    """Build a source-grounded practice set in curriculum order.

    Review/mistake priority belongs in Review Center. Inside an explicitly chosen
    unit, questions stay in source order so the learner never sees lesson 3 before
    lesson 1 merely because of adaptive ranking.
    """
    picked = []

    for lesson in lessons:
        eligible = [
            check for check in lesson.checks
            if int(getattr(check, "difficulty", 1)) <= max_difficulty
        ]
        if eligible:
            picked.append((lesson, eligible[0]))
            if len(picked) >= limit:
                return picked

    for lesson in lessons:
        eligible = [
            check for check in lesson.checks
            if int(getattr(check, "difficulty", 1)) <= max_difficulty
        ]
        for check in eligible[1:]:
            picked.append((lesson, check))
            if len(picked) >= limit:
                return picked

    return picked

def render_exam_mode() -> None:
    st.markdown('<div class="section-title">🧪 تدريب سريع</div>', unsafe_allow_html=True)
    render_context_help("exam_mode")
    st.markdown(
        '<div class="mission"><b>تدريب من المحتوى الموثق فقط.</b><br>'
        '<span class="muted">ابدئي بهدوء، وزوّدي المستوى فقط لما تكوني جاهزة. '
        'الغلط هنا بيساعد LUMINA يعرف يشرح إيه بطريقة أبسط.</span></div>',
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
    practice_mode = st.radio(
        "اختاري شكل التدريب",
        [
            "مراجعة هادية · 3 أسئلة",
            "تدريب متدرج · 5 أسئلة",
            "تحدّي اختياري · 5 أسئلة",
        ],
        index=0,
        key="exam_practice_mode",
        help="ابدئي بالمراجعة الهادية. مفيش داعي للتحدّي إلا لما تحسي إنك جاهزة.",
    )
    mode_config = {
        "مراجعة هادية · 3 أسئلة": (3, 1),
        "تدريب متدرج · 5 أسئلة": (5, 2),
        "تحدّي اختياري · 5 أسئلة": (5, 3),
    }
    limit, max_difficulty = mode_config[practice_mode]

    store = get_learning_store()
    checks = _pick_checks(
        lessons,
        store,
        limit=limit,
        max_difficulty=max_difficulty,
    )

    if not checks:
        st.info("لا توجد أسئلة موثقة لهذا الجزء حتى الآن.")
        return

    st.caption(
        f"{len(checks)} سؤال · من {unit_title} · "
        "الأسئلة ماشية حسب ترتيب الدروس في المنهج"
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

    if st.button("شوفي نتيجتي", key=f"exam_submit_{subject_id}_{unit_title}"):
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
                    "cognitive_kind": getattr(check, "activity_kind", "concept"),
                    "mastery_eligible": bool(getattr(check, "mastery_eligible", True)),
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
            st.info("ممتاز. النتيجة اتسجلت ضمن تقدّمك، لكن الإتقان الكامل يحتاج أكتر من دليل واحد.")
        else:
            st.warning("الأسئلة اللي محتاجة مراجعة اتضافت تلقائيًا لقسم مراجعاتي.")

        with st.expander("مراجعة النتيجة", expanded=True):
            for idx, (lesson, check, correct) in enumerate(results, start=1):
                icon = "✅" if correct else "❌"
                st.write(f"{icon} {idx}. {lesson.title}")
                if not correct:
                    st.caption(f"تلميح للمراجعة: {check.hint} · المصدر: {lesson.source_pages}")
