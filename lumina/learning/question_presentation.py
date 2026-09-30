from __future__ import annotations

import hashlib


def presented_options(check) -> tuple[str, ...]:
    """Return a stable, balanced option order derived from the check id.

    Curriculum authors can keep source-faithful option tuples. Presentation order
    is diversified here so learners cannot exploit a repeated correct-position
    pattern. The order is deterministic for the same check, so review stays
    predictable rather than changing on every rerun.
    """
    options = list(check.options)
    if len(options) < 2:
        return tuple(options)

    digest = hashlib.sha256(str(check.id).encode("utf-8")).digest()
    # Fisher-Yates with deterministic bytes; no runtime randomness/session drift.
    for i in range(len(options) - 1, 0, -1):
        j = digest[i % len(digest)] % (i + 1)
        options[i], options[j] = options[j], options[i]
    return tuple(options)


def correct_answer_text(check) -> str:
    if check.correct_index is None:
        raise ValueError(f"Check {check.id} has no correct_index")
    return check.options[check.correct_index]


def is_correct_answer(check, answer: str) -> bool:
    return answer == correct_answer_text(check)
