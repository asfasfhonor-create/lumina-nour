from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from lumina.curriculum.mapped_curriculum import (
    MAPPED_CURRICULUM,
    SUBJECT_LABELS,
    all_mapped_lessons,
)
from lumina.learning.progress import MASTERED, NEEDS_REVIEW, derive_mastery
from lumina.learning.evidence_cache import snapshot_learning_evidence


AUTO_STUDY_SUBJECTS = ("english", "science", "math", "arabic", "social", "religion")


def _term1_lessons(module_id: str):
    units = MAPPED_CURRICULUM.get(module_id, {})
    return tuple(
        lesson
        for unit_name, lessons in units.items()
        if unit_name.startswith("Term 1")
        for lesson in lessons
    )


def _has_success(attempts: list[dict]) -> bool:
    return any(item.get("correct") is True for item in attempts)


@dataclass(frozen=True)
class MissionRecommendation:
    module_id: str
    subject_label: str
    lesson_id: str
    lesson_title: str
    source_pages: str
    reason: str


def _lesson_index() -> dict[str, tuple[str, object]]:
    index = {}
    for module_id, units in MAPPED_CURRICULUM.items():
        for lessons in units.values():
            for lesson in lessons:
                index[lesson.id] = (module_id, lesson)
    return index


def choose_mission(store) -> MissionRecommendation | None:
    """Review genuine problems first, then move forward through Term 1 in source order.

    A first correct answer means the learner is ready to move on, not permanently
    mastered. Mastery can still grow later through review and varied evidence.
    Automatic recommendations deliberately exclude second-semester-only ICT and
    Term 2 material; those remain available when Nour opens them intentionally.
    """
    index = _lesson_index()

    for review in store.get_reviews("due"):
        lesson_id = review.get("lesson_id")
        if lesson_id in index:
            module_id, lesson = index[lesson_id]
            return MissionRecommendation(
                module_id=module_id,
                subject_label=SUBJECT_LABELS.get(module_id, module_id),
                lesson_id=lesson.id,
                lesson_title=lesson.title,
                source_pages=lesson.source_pages,
                reason="مراجعة خفيفة لنقطة اتلخبطت قبل كده",
            )

    evidence = snapshot_learning_evidence(store)
    attempts_by_lesson = evidence["attempts_by_lesson"]
    mistakes_by_lesson = evidence["mistakes_by_lesson"]

    for module_id in AUTO_STUDY_SUBJECTS:
        for lesson in _term1_lessons(module_id):
            state = derive_mastery(
                attempts_by_lesson.get(lesson.id, []),
                mistakes_by_lesson.get(lesson.id, []),
            ).state
            if state == NEEDS_REVIEW:
                return MissionRecommendation(
                    module_id=module_id,
                    subject_label=SUBJECT_LABELS.get(module_id, module_id),
                    lesson_id=lesson.id,
                    lesson_title=lesson.title,
                    source_pages=lesson.source_pages,
                    reason="نراجع نقطة سابقة قبل ما نكمل الجديد",
                )

    subject_ids = list(AUTO_STUDY_SUBJECTS)
    rotation = date.today().toordinal() % len(subject_ids)
    subject_ids = subject_ids[rotation:] + subject_ids[:rotation]

    for module_id in subject_ids:
        for lesson in _term1_lessons(module_id):
            attempts = attempts_by_lesson.get(lesson.id, [])
            mistakes = mistakes_by_lesson.get(lesson.id, [])
            unresolved = [item for item in mistakes if not item.get("resolved", False)]
            if unresolved:
                continue
            if not _has_success(attempts):
                reason = (
                    "نكمل محاولة بدأناها بهدوء"
                    if attempts
                    else "نبدأ الدرس التالي حسب ترتيب المنهج"
                )
                return MissionRecommendation(
                    module_id=module_id,
                    subject_label=SUBJECT_LABELS.get(module_id, module_id),
                    lesson_id=lesson.id,
                    lesson_title=lesson.title,
                    source_pages=lesson.source_pages,
                    reason=reason,
                )

    for module_id in subject_ids:
        lessons = _term1_lessons(module_id)
        if lessons:
            lesson = lessons[0]
            return MissionRecommendation(
                module_id=module_id,
                subject_label=SUBJECT_LABELS.get(module_id, module_id),
                lesson_id=lesson.id,
                lesson_title=lesson.title,
                source_pages=lesson.source_pages,
                reason="تحدّي خفيف للمراجعة بعد ما غطّينا الجديد",
            )

    return None


def get_lesson_by_id(lesson_id: str):
    item = _lesson_index().get(lesson_id)
    return item[1] if item else None


def get_module_for_lesson_id(lesson_id: str) -> str | None:
    item = _lesson_index().get(lesson_id)
    return item[0] if item else None
