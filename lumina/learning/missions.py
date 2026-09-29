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
    """Pick review first; otherwise rotate through not-started mapped lessons."""
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
                reason="Review due from a previous mistake",
            )

    evidence = snapshot_learning_evidence(store)
    attempts_by_lesson = evidence["attempts_by_lesson"]
    mistakes_by_lesson = evidence["mistakes_by_lesson"]

    by_state: dict[str, list[tuple[str, object]]] = {
        NEEDS_REVIEW: [],
        LEARNING: [],
        NOT_STARTED: [],
        MASTERED: [],
    }

    for module_id, units in MAPPED_CURRICULUM.items():
        for lessons in units.values():
            for lesson in lessons:
                state = derive_mastery(
                    attempts_by_lesson.get(lesson.id, []),
                    mistakes_by_lesson.get(lesson.id, []),
                ).state
                by_state.setdefault(state, []).append((module_id, lesson))

    priority = (
        (NEEDS_REVIEW, "Needs another look before moving on"),
        (LEARNING, "Continue an in-progress lesson"),
        (NOT_STARTED, "Next mapped lesson to explore"),
        (MASTERED, "Keep mastery fresh"),
    )

    chosen = None
    reason = ""
    ordinal = date.today().toordinal()
    for state, state_reason in priority:
        candidates = by_state.get(state, [])
        if candidates:
            chosen = candidates[ordinal % len(candidates)]
            reason = state_reason
            break

    if chosen is None:
        return None

    module_id, lesson = chosen

    return MissionRecommendation(
        module_id=module_id,
        subject_label=SUBJECT_LABELS.get(module_id, module_id),
        lesson_id=lesson.id,
        lesson_title=lesson.title,
        source_pages=lesson.source_pages,
        reason=reason,
    )


def get_lesson_by_id(lesson_id: str):
    item = _lesson_index().get(lesson_id)
    return item[1] if item else None


def get_module_for_lesson_id(lesson_id: str) -> str | None:
    item = _lesson_index().get(lesson_id)
    return item[0] if item else None
