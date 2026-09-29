from dataclasses import dataclass, field
from typing import Tuple


@dataclass(frozen=True)
class LessonCheck:
    id: str
    prompt: str
    expected_points: Tuple[str, ...]
    hint: str
    options: Tuple[str, ...] = field(default_factory=tuple)
    correct_index: int | None = None
    difficulty: int = 1
    activity_kind: str = "concept"

    def __post_init__(self) -> None:
        if self.difficulty not in (1, 2, 3):
            raise ValueError("LessonCheck difficulty must be 1, 2, or 3.")
        if self.correct_index is not None and not (0 <= self.correct_index < len(self.options)):
            raise ValueError("LessonCheck correct_index is outside the available options.")


@dataclass(frozen=True)
class LessonData:
    id: str
    source_id: str
    unit_id: str
    title: str
    source_pages: str
    objectives: Tuple[str, ...]
    key_terms: Tuple[str, ...]
    evidence_summary: Tuple[str, ...]
    checks: Tuple[LessonCheck, ...] = field(default_factory=tuple)
