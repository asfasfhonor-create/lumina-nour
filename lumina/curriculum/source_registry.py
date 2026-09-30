from __future__ import annotations

from typing import Tuple

from lumina.curriculum.models import (
    CurriculumSource,
    SOURCE_ROLE_OFFICIAL,
    SOURCE_ROLE_SUPPLIED,
)


CURRICULUM_SOURCES: Tuple[CurriculumSource, ...] = (
    CurriculumSource(
        id="arabic_t1", subject_id="arabic", title="Arabic", filename="Arabic_language_prep3_t1.pdf",
        term="Term 1", language="ar", source_role=SOURCE_ROLE_SUPPLIED, extraction_mode="page_image",
    ),
    CurriculumSource(
        id="english_t1", subject_id="english", title="English", filename="English_language_prep3_t1.pdf",
        term="Term 1", language="en", source_role=SOURCE_ROLE_SUPPLIED, extraction_mode="page_image",
    ),
    CurriculumSource(
        id="religion_t1", subject_id="religion", title="Islamic Religion", filename="Islamic_religion_prep3_t1.pdf",
        term="Term 1", language="ar", source_role=SOURCE_ROLE_SUPPLIED, extraction_mode="parsed_text",
    ),
    CurriculumSource(
        id="social_t1", subject_id="social", title="Social Studies", filename="Social_studies_prep3_t1.pdf",
        term="Term 1", language="ar", source_role=SOURCE_ROLE_SUPPLIED, extraction_mode="page_image",
    ),
    CurriculumSource(
        id="math_t1", subject_id="math", title="Mathematics in English — Student Book",
        filename="الرياضيات باللغة الانجليزية-كتاب الطالب-334a9f66.pdf", term="Term 1", language="en",
        source_role=SOURCE_ROLE_OFFICIAL, publisher="Ministry curriculum development",
        edition_label="Cover: 2025–2026; internal legacy strings preserved as source metadata",
        extraction_mode="mixed_page_image_preferred",
    ),
    CurriculumSource(
        id="science_t1", subject_id="science", title="Science in English — Student Book",
        filename="العلوم باللغة الانجليزية-كتاب الطالب-0d9bc9e8.pdf", term="Term 1", language="en",
        source_role=SOURCE_ROLE_OFFICIAL, publisher="Ministry curriculum development",
        edition_label="2025–2026", extraction_mode="page_image",
    ),
    CurriculumSource(
        id="ict_t2", subject_id="ict", title="Computer / ICT", filename="computer_3prep_scond_term_english.pdf",
        term="Second Semester", language="en", source_role=SOURCE_ROLE_SUPPLIED,
        extraction_mode="parsed_text", trusted=False,
        edition_label="Supplied source; current-year coverage not yet externally verified",
    ),
)


def get_source(source_id: str) -> CurriculumSource | None:
    return next((source for source in CURRICULUM_SOURCES if source.id == source_id), None)


def sources_for_subject(subject_id: str) -> Tuple[CurriculumSource, ...]:
    return tuple(source for source in CURRICULUM_SOURCES if source.subject_id == subject_id)


def source_inventory_summary() -> dict:
    return {
        "source_count": len(CURRICULUM_SOURCES),
        "subjects": tuple(sorted({source.subject_id for source in CURRICULUM_SOURCES})),
        "page_image_aware_required": any("page_image" in source.extraction_mode for source in CURRICULUM_SOURCES),
        "needs_verification": tuple(source.id for source in CURRICULUM_SOURCES if not source.trusted),
    }
