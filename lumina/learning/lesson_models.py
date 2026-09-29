from dataclasses import dataclass, field
from typing import Tuple


@dataclass(frozen=True)
class LessonCheck:
    id: str
    prompt: str
    expected_points: Tuple[str, ...]
    hint: str


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
