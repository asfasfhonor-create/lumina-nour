from __future__ import annotations

from dataclasses import dataclass
import re

from lumina.curriculum.mapped_curriculum import all_mapped_lessons


@dataclass(frozen=True)
class CurriculumHit:
    lesson_id: str
    title: str
    source_id: str
    unit_id: str
    source_pages: str
    score: int


def _tokens(text: str) -> set[str]:
    return {
        token
        for token in re.findall(r"[A-Za-z0-9\u0600-\u06FF]+", text.lower())
        if len(token) >= 2
    }


def search_curriculum(query: str, limit: int = 8) -> tuple[CurriculumHit, ...]:
    query_tokens = _tokens(query)
    if not query_tokens:
        return ()

    hits = []
    for lesson in all_mapped_lessons():
        haystack = " ".join(
            (
                lesson.title,
                " ".join(lesson.objectives),
                " ".join(lesson.key_terms),
                " ".join(lesson.evidence_summary),
            )
        )
        lesson_tokens = _tokens(haystack)
        overlap = len(query_tokens & lesson_tokens)
        title_overlap = len(query_tokens & _tokens(lesson.title))
        score = overlap + (title_overlap * 3)
        if score:
            hits.append(
                CurriculumHit(
                    lesson_id=lesson.id,
                    title=lesson.title,
                    source_id=lesson.source_id,
                    unit_id=lesson.unit_id,
                    source_pages=lesson.source_pages,
                    score=score,
                )
            )

    hits.sort(key=lambda item: (-item.score, item.title))
    return tuple(hits[:limit])


def lesson_by_id(lesson_id: str):
    return next((lesson for lesson in all_mapped_lessons() if lesson.id == lesson_id), None)
