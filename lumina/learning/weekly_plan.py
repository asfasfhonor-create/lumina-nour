from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from lumina.curriculum.mapped_curriculum import MAPPED_CURRICULUM, SUBJECT_LABELS
from lumina.learning.progress import NOT_STARTED, derive_mastery


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
    for module_id, units in MAPPED_CURRICULUM.items():
        for lessons in units.values():
            for lesson in lessons:
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
                reason="Review due",
            )
        )
        seen_lessons.add(lesson.id)
        if len(items) >= limit:
            return tuple(items)

    subject_queues: dict[str, list] = {}
    for module_id, units in MAPPED_CURRICULUM.items():
        queue = []
        for lessons in units.values():
            for lesson in lessons:
                if lesson.id in seen_lessons:
                    continue
                state = derive_mastery(
                    store.get_attempts(lesson.id),
                    store.get_mistakes(lesson.id),
                ).state
                if state == NOT_STARTED:
                    queue.append(lesson)
        subject_queues[module_id] = queue

    subject_ids = list(MAPPED_CURRICULUM)
    rotation = date.today().isocalendar().week % len(subject_ids)
    subject_ids = subject_ids[rotation:] + subject_ids[:rotation]

    while len(items) < limit and any(subject_queues.values()):
        for module_id in subject_ids:
            queue = subject_queues.get(module_id, [])
            if not queue:
                continue
            lesson = queue.pop(0)
            items.append(
                WeeklyPlanItem(
                    module_id=module_id,
                    subject_label=SUBJECT_LABELS.get(module_id, module_id),
                    lesson_id=lesson.id,
                    lesson_title=lesson.title,
                    source_pages=lesson.source_pages,
                    reason="New mapped learning",
                )
            )
            if len(items) >= limit:
                break

    return tuple(items)
