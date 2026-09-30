from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from lumina.curriculum.mapped_curriculum import (
    MAPPED_CURRICULUM,
    SUBJECT_LABELS,
    all_mapped_lessons,
)
from lumina.learning.progress import LEARNING, MASTERED, NEEDS_REVIEW, NOT_STARTED, derive_mastery
from lumina.learning.evidence_cache import snapshot_learning_evidence


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
    """Choose review first; otherwise advance through curriculum in source order.

    New learning must never jump ahead merely because of the calendar date.
    Reviews may intentionally return to an earlier lesson that needs reinforcement.
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

    # If a lesson has an unresolved mistake, review it before introducing new content.
    for module_id, units in MAPPED_CURRICULUM.items():
        for lessons in units.values():
            for lesson in lessons:
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

    # Rotate subjects, but inside each subject always take the earliest unfinished lesson.
    subject_ids = list(MAPPED_CURRICULUM)
    rotation = date.today().toordinal() % len(subject_ids)
    subject_ids = subject_ids[rotation:] + subject_ids[:rotation]

    for module_id in subject_ids:
        for lessons in MAPPED_CURRICULUM[module_id].values():
            for lesson in lessons:
                state = derive_mastery(
                    attempts_by_lesson.get(lesson.id, []),
                    mistakes_by_lesson.get(lesson.id, []),
                ).state
                if state in (LEARNING, NOT_STARTED):
                    reason = (
                        "نكمل الدرس اللي بدأناه حسب ترتيب المنهج"
                        if state == LEARNING
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

    # Everything is mastered: spaced reinforcement can return to the first mapped lesson.
    for module_id in subject_ids:
        lessons = all_mapped_lessons(module_id)
        if lessons:
            lesson = lessons[0]
            return MissionRecommendation(
                module_id=module_id,
                subject_label=SUBJECT_LABELS.get(module_id, module_id),
                lesson_id=lesson.id,
                lesson_title=lesson.title,
                source_pages=lesson.source_pages,
                reason="تحدّي خفيف يحافظ على الفهم",
            )

    return None

def get_lesson_by_id(lesson_id: str):
    item = _lesson_index().get(lesson_id)
    return item[1] if item else None


def get_module_for_lesson_id(lesson_id: str) -> str | None:
    item = _lesson_index().get(lesson_id)
    return item[0] if item else None
