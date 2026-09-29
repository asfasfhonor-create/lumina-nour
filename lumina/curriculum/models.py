from dataclasses import dataclass, field
from typing import Tuple


@dataclass(frozen=True)
class CurriculumUnit:
    id: str
    title: str
    topics: Tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class CurriculumSource:
    id: str
    subject_id: str
    title: str
    filename: str
    term: str
    language: str
    source_kind: str = "project_source"
    extraction_mode: str = "mixed"
    trusted: bool = True
    units: Tuple[CurriculumUnit, ...] = field(default_factory=tuple)

    @property
    def display_name(self) -> str:
        return f"{self.title} · {self.term}"
