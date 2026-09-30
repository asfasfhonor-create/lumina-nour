from __future__ import annotations

from dataclasses import dataclass
import re

from lumina.curriculum.source_registry import get_source


_PAGE_RE = re.compile(r"(\d+)\s*(?:[–—-]\s*(\d+))?")


@dataclass(frozen=True)
class LessonSourceContext:
    source_id: str
    source_title: str
    filename: str
    term: str
    page_start: int | None
    page_end: int | None
    extraction_mode: str
    trusted: bool

    @property
    def page_label(self) -> str:
        if self.page_start is None:
            return ""
        if self.page_end is None or self.page_end == self.page_start:
            return f"page {self.page_start}"
        return f"pages {self.page_start}–{self.page_end}"

    @property
    def needs_page_image(self) -> bool:
        return "page_image" in self.extraction_mode


def parse_page_range(source_pages: str) -> tuple[int | None, int | None]:
    match = _PAGE_RE.search(source_pages or "")
    if not match:
        return None, None
    start = int(match.group(1))
    end = int(match.group(2)) if match.group(2) else start
    if end < start:
        start, end = end, start
    return start, end


def context_for_lesson(lesson) -> LessonSourceContext | None:
    source = get_source(lesson.source_id)
    if source is None:
        return None
    start, end = parse_page_range(lesson.source_pages)
    return LessonSourceContext(
        source_id=source.id,
        source_title=source.title,
        filename=source.filename,
        term=source.term,
        page_start=start,
        page_end=end,
        extraction_mode=source.extraction_mode,
        trusted=source.trusted,
    )


def grounding_instruction(lesson) -> str:
    context = context_for_lesson(lesson)
    if context is None:
        return (
            "No registered curriculum source is linked to this lesson. "
            "Do not claim source-grounded facts until the source link is fixed."
        )

    page_scope = context.page_label or "the lesson's registered page range"
    visual_rule = (
        "Treat page images, diagrams, maps, formulas, tables and layout as evidence; "
        "do not rely on extracted text alone. "
        if context.needs_page_image
        else ""
    )
    trust_rule = (
        "This supplied source is not yet verified as current-year coverage; say so when relevant. "
        if not context.trusted
        else ""
    )
    return (
        f"Primary curriculum source: {context.source_title} ({context.term}), "
        f"file {context.filename}, {page_scope}. "
        f"{visual_rule}{trust_rule}"
        "Use only evidence supported by that source scope. If the evidence available to the runtime "
        "is insufficient, say that clearly instead of filling the gap from general model knowledge."
    )
