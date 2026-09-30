from dataclasses import dataclass, field
from typing import Tuple


@dataclass(frozen=True)
class CurriculumUnit:
    id: str
    title: str
    topics: Tuple[str, ...] = field(default_factory=tuple)


SOURCE_ROLE_OFFICIAL = "official"
SOURCE_ROLE_SUPPLIED = "supplied"
SOURCE_ROLE_SUPPLEMENTARY = "supplementary"

SOURCE_PRIORITY = {
    SOURCE_ROLE_OFFICIAL: 100,
    SOURCE_ROLE_SUPPLIED: 70,
    SOURCE_ROLE_SUPPLEMENTARY: 50,
}


@dataclass(frozen=True)
class CurriculumSource:
    id: str
    subject_id: str
    title: str
    filename: str
    term: str
    language: str
    source_kind: str = "project_source"
    source_role: str = SOURCE_ROLE_SUPPLIED
    publisher: str | None = None
    edition_label: str | None = None
    extraction_mode: str = "mixed"
    trusted: bool = True
    units: Tuple[CurriculumUnit, ...] = field(default_factory=tuple)

    def __post_init__(self) -> None:
        if self.source_role not in SOURCE_PRIORITY:
            raise ValueError(f"Unsupported source role: {self.source_role}")

    @property
    def priority(self) -> int:
        return SOURCE_PRIORITY[self.source_role]

    @property
    def display_name(self) -> str:
        return f"{self.title} · {self.term}"
