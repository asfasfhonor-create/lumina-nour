from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from lumina.curriculum.mapped_curriculum import MAPPED_CURRICULUM, SUBJECT_LABELS
from lumina.learning.progress import NEEDS_REVIEW, derive_mastery
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
class WeeklyPlanItem:
    module_id: str
    subject_label: str
    lesson_id: str
    lesson_title: str
    source_pages: str
    reason: str


def build_weekly_plan(store, limit: int = 5) -> tuple[WeeklyPlanItem, ...]:
    items: list[WeeklyPlanItem] = []
    seen_lessons: set[str] = set()

    lesson_lookup = {}
    for module_id in AUTO_STUDY_SUBJECTS:
        for lesson in _term1_lessons(module_id):
            lesson_lookup[lesson.id] = (module_id, lesson)

    for review in store.get_reviews("due"):
        lesson_id = review.get("lesson_id")
        item = lesson_lookup.get(lesson_id)
        if not item or lesson_id in seen_lessons:
            continue
        module_id, lesson = item
        items.append(
            WeeklyPlanItem(
                module_id=module_id,
                subject_label=SUBJECT_LABELS.get(module_id, module_id),
                lesson_id=lesson.id,
                lesson_title=lesson.title,
                source_pages=lesson.source_pages,
                reason="مراجعة مستحقة",
            )
        )
        seen_lessons.add(lesson.id)
        if len(items) >= limit:
            return tuple(items)

    evidence = snapshot_learning_evidence(store)
    attempts_by_lesson = evidence["attempts_by_lesson"]
    mistakes_by_lesson = evidence["mistakes_by_lesson"]

    subject_ids = list(AUTO_STUDY_SUBJECTS)
    rotation = date.today().isocalendar().week % len(subject_ids)
    subject_ids = subject_ids[rotation:] + subject_ids[:rotation]

    # First, keep unresolved weak points visible without flooding the week.
    for module_id in subject_ids:
        for lesson in _term1_lessons(module_id):
            if lesson.id in seen_lessons:
                continue
            state = derive_mastery(
                attempts_by_lesson.get(lesson.id, []),
                mistakes_by_lesson.get(lesson.id, []),
            ).state
            if state == NEEDS_REVIEW:
                items.append(
                    WeeklyPlanItem(
                        module_id=module_id,
                        subject_label=SUBJECT_LABELS.get(module_id, module_id),
                        lesson_id=lesson.id,
                        lesson_title=lesson.title,
                        source_pages=lesson.source_pages,
                        reason="نقطة محتاجة تثبيت",
                    )
                )
                seen_lessons.add(lesson.id)
                break
        if len(items) >= limit:
            return tuple(items)

    # Then add only the earliest lesson not yet passed in each subject.
    while len(items) < limit:
        added = False
        for module_id in subject_ids:
            candidate = None
            for lesson in _term1_lessons(module_id):
                if lesson.id in seen_lessons:
                    continue
                attempts = attempts_by_lesson.get(lesson.id, [])
                mistakes = mistakes_by_lesson.get(lesson.id, [])
                unresolved = [item for item in mistakes if not item.get("resolved", False)]
                if unresolved:
                    continue
                if not _has_success(attempts):
                    candidate = lesson
                    break
            if candidate is None:
                continue
            items.append(
                WeeklyPlanItem(
                    module_id=module_id,
                    subject_label=SUBJECT_LABELS.get(module_id, module_id),
                    lesson_id=candidate.id,
                    lesson_title=candidate.title,
                    source_pages=candidate.source_pages,
                    reason="الدرس التالي حسب ترتيب المنهج",
                )
            )
            seen_lessons.add(candidate.id)
            added = True
            if len(items) >= limit:
                break
        if not added:
            break

    return tuple(items)
