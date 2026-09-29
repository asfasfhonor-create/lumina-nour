from dataclasses import dataclass

from google.genai import types

from lumina.curriculum.models import CurriculumSource


@dataclass(frozen=True)
class GroundedPdf:
    source: CurriculumSource
    part: types.Part


def build_grounded_pdf(source: CurriculumSource, pdf_bytes: bytes) -> GroundedPdf:
    """Create a provider-ready PDF part while preserving source metadata separately."""
    return GroundedPdf(
        source=source,
        part=types.Part.from_bytes(data=pdf_bytes, mime_type="application/pdf"),
    )


def curriculum_prompt(source: CurriculumSource, question: str, unit_title: str | None = None) -> str:
    scope = f"Unit/section selected by Nour: {unit_title}." if unit_title else "No unit filter selected."
    return f"""You are LUMINA's curriculum-grounded tutor for Nour.

Trusted source:
- Subject: {source.subject_id}
- Source: {source.display_name}
- File: {source.filename}
- {scope}

Rules:
1. Answer only from the attached trusted source for curriculum facts.
2. Preserve the source's terminology and framing.
3. If the source does not support something, say that clearly instead of guessing.
4. Teach; do not just dump the final answer.
5. Start with a concise explanation, then ask Nour one short check question or give a small practice prompt.
6. Use Arabic support when useful, but keep English curriculum terminology unchanged when the source uses English.
7. Do not claim a page number unless you can reliably identify it from the supplied document context.

Nour's question:
{question}
"""
