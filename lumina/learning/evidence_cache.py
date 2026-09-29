from __future__ import annotations

from collections import defaultdict


def group_by_lesson(items: list[dict]) -> dict[str, list[dict]]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for item in items:
        lesson_id = item.get("lesson_id")
        if lesson_id:
            grouped[str(lesson_id)].append(item)
    return dict(grouped)


def snapshot_learning_evidence(store):
    """Fetch attempt/mistake evidence in bulk to avoid N+1 database queries."""
    attempts = store.get_attempts()
    mistakes = store.get_mistakes()
    return {
        "attempts": attempts,
        "mistakes": mistakes,
        "attempts_by_lesson": group_by_lesson(attempts),
        "mistakes_by_lesson": group_by_lesson(mistakes),
    }
