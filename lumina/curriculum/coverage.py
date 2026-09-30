from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SourceCoverage:
    subject_id: str
    supplied_terms: tuple[str, ...]
    notes: str


SOURCE_COVERAGE = {
    "english": SourceCoverage(
        "english",
        ("Term 1",),
        "Only the supplied Term 1 English source is curriculum-authoritative.",
    ),
    "science": SourceCoverage(
        "science",
        ("Term 1", "Term 2"),
        "Both terms were verified inside the same supplied Science PDF.",
    ),
    "math": SourceCoverage(
        "math",
        ("Term 1", "Term 2"),
        "Both terms were verified inside the same supplied Mathematics PDF.",
    ),
    "arabic": SourceCoverage(
        "arabic",
        ("Term 1",),
        "Only the supplied Term 1 Arabic source is curriculum-authoritative.",
    ),
    "social": SourceCoverage(
        "social",
        ("Term 1",),
        "Only the supplied Term 1 Social Studies source is curriculum-authoritative.",
    ),
    "religion": SourceCoverage(
        "religion",
        ("Term 1",),
        "Only the supplied Term 1 Religion source is curriculum-authoritative.",
    ),
    "ict": SourceCoverage(
        "ict",
        ("Second Semester",),
        "The supplied ICT source identifies itself as Second Semester; current-year external verification remains separate.",
    ),
}


def get_source_coverage(subject_id: str) -> SourceCoverage | None:
    return SOURCE_COVERAGE.get(subject_id)
