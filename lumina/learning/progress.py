from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


NOT_STARTED = "not_started"
LEARNING = "learning"
NEEDS_REVIEW = "needs_review"
MASTERED = "mastered"


@dataclass(frozen=True)
class MasterySnapshot:
    state: str
    attempts: int
    correct_attempts: int
    distinct_evidence: int
    unresolved_mistakes: int


def derive_mastery(
    attempts: Iterable[dict],
    mistakes: Iterable[dict] = (),
) -> MasterySnapshot:
    """Derive a conservative mastery state from learning evidence.

    This is an initial provider-independent rule, intentionally conservative:
    repeated success on the same underlying check is not enough for Mastered,
    even if it happened in lesson, review, or exam contexts. Any unresolved
    mistake keeps the lesson in Needs review until that mistake is resolved.
    The thresholds remain replaceable/configurable as the Master requires.
    """
    attempts_list = list(attempts)
    mistakes_list = [m for m in mistakes if not m.get("resolved", False)]

    if not attempts_list:
        return MasterySnapshot(
            state=NOT_STARTED,
            attempts=0,
            correct_attempts=0,
            distinct_evidence=0,
            unresolved_mistakes=len(mistakes_list),
        )

    correct = [a for a in attempts_list if a.get("correct") is True]
    mastery_correct = [
        a for a in correct
        if a.get("mastery_eligible", True) is not False
    ]
    distinct = {
        a.get("check_id") or a.get("evidence_id")
        for a in mastery_correct
        if a.get("check_id") or a.get("evidence_id")
    }
    last_correct = attempts_list[-1].get("correct") is True

    if mistakes_list:
        state = NEEDS_REVIEW
    elif len(mastery_correct) >= 3 and len(distinct) >= 2:
        state = MASTERED
    elif last_correct:
        state = LEARNING
    else:
        state = NEEDS_REVIEW

    return MasterySnapshot(
        state=state,
        attempts=len(attempts_list),
        correct_attempts=len(correct),
        distinct_evidence=len(distinct),
        unresolved_mistakes=len(mistakes_list),
    )


def mastery_label(state: str) -> str:
    return {
        NOT_STARTED: "Not started",
        LEARNING: "Learning",
        NEEDS_REVIEW: "Needs review",
        MASTERED: "Mastered",
    }.get(state, state)
