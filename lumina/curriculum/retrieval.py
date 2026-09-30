from __future__ import annotations

from dataclasses import dataclass

from lumina.curriculum.search import CurriculumHit, lesson_by_id, search_curriculum
from lumina.curriculum.source_registry import get_source
from lumina.curriculum.lesson_source_context import parse_page_range


@dataclass(frozen=True)
class RetrievalContext:
    lesson_id: str
    lesson_title: str
    source_id: str
    source_filename: str
    source_pages: str
    extraction_mode: str
    evidence: tuple[str, ...]
    trusted: bool
    page_start: int | None = None
    page_end: int | None = None

    @property
    def provenance_label(self) -> str:
        return f"{self.source_filename} · {self.source_pages}"


def context_for_hit(hit: CurriculumHit) -> RetrievalContext | None:
    lesson = lesson_by_id(hit.lesson_id)
    if lesson is None:
        return None

    source = get_source(hit.source_id)
    if source is None:
        return None

    page_start, page_end = parse_page_range(lesson.source_pages)

    return RetrievalContext(
        lesson_id=lesson.id,
        lesson_title=lesson.title,
        source_id=source.id,
        source_filename=source.filename,
        source_pages=lesson.source_pages,
        extraction_mode=source.extraction_mode,
        evidence=tuple(lesson.evidence_summary),
        trusted=source.trusted,
        page_start=page_start,
        page_end=page_end,
    )


def retrieve_context(query: str, limit: int = 5) -> tuple[RetrievalContext, ...]:
    contexts = []
    for hit in search_curriculum(query, limit=limit):
        context = context_for_hit(hit)
        if context is not None:
            contexts.append(context)
    return tuple(contexts)


def page_scope_prompt(context: RetrievalContext) -> str:
    if context.page_start is None:
        return "Use the registered lesson range only."
    if context.page_end is None or context.page_end == context.page_start:
        return f"Use book page {context.page_start} only."
    return f"Use book pages {context.page_start} through {context.page_end} only."


def grounded_prompt(context: RetrievalContext, question: str) -> str:
    evidence = "\n".join(f"- {point}" for point in context.evidence)
    trust_note = (
        "This source is marked as supplied but not yet verified as current-year coverage. "
        if not context.trusted else ""
    )
    return f"""You are Nour's curriculum tutor.
Answer only from the verified mapped evidence below.
{trust_note}If the mapped evidence is insufficient, say so clearly.
Do not invent missing facts, page details, examples, formulas, diagrams, exam rules, or curriculum coverage.
Preserve the source terminology. Keep school curriculum separate from enrichment.
For page-image-aware sources, do not pretend the text summary replaces diagrams, maps, formulas, tables, or page layout.

Lesson: {context.lesson_title}
Source: {context.source_filename}
Pages/range: {context.source_pages}\nPage scope rule: {page_scope_prompt(context)}\nExtraction mode: {context.extraction_mode}
Verified mapped evidence:
{evidence}

Nour's question:
{question}

Explain briefly, use a small example only when supported by the evidence, then ask one checking question."""
