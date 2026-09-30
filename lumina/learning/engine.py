from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class CheckEvaluation:
    status: str
    matched_points: tuple[str, ...]
    missing_points: tuple[str, ...]


def evaluate_keywords(answer: str, expected_points: Iterable[str]) -> CheckEvaluation:
    """Small deterministic first-pass evaluator.

    This is intentionally conservative and is not the final mastery engine.
    It prevents rewards from being based only on a button click while keeping
    the evidence model independent from any one AI provider.
    """
    normalized = answer.lower().strip()
    expected = tuple(expected_points)
    matched = tuple(point for point in expected if all(token in normalized for token in point.lower().split()))
    missing = tuple(point for point in expected if point not in matched)

    if not normalized:
        status = "empty"
    elif len(matched) == len(expected):
        status = "strong"
    elif matched:
        status = "partial"
    else:
        status = "needs_review"

    return CheckEvaluation(status=status, matched_points=matched, missing_points=missing)
