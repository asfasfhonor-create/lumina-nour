from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class CurriculumSource:
    id: str
    subject_id: str
    title: str
    filename: str
    term: str
    pages: int
    extraction_mode: str
    trust: str = "trusted_project_source"
    notes: str = ""


CURRICULUM_SOURCES: Tuple[CurriculumSource, ...] = (
    CurriculumSource("arabic_t1","arabic","Arabic — Term 1","Arabic_language_prep3_t1.pdf","Term 1",161,"page_image",notes="Integrated Arabic skills; page-image-aware retrieval required."),
    CurriculumSource("english_t1","english","English — Term 1","English_language_prep3_t1.pdf","Term 1",114,"page_image",notes="School English source; keep separate from Real English enrichment."),
    CurriculumSource("religion_t1","religion","Islamic Religion — Term 1","Islamic_religion_prep3_t1.pdf","Term 1",82,"parsed_text",notes="Knowledge, skills and values strands."),
    CurriculumSource("social_t1","social","Social Studies — Term 1","Social_studies_prep3_t1.pdf","Term 1",113,"page_image",notes="Maps and visual evidence are educational content."),
    CurriculumSource("math_t1","math","Mathematics in English — Student Book","الرياضيات باللغة الانجليزية-كتاب الطالب-334a9f66.pdf","Term 1",178,"mixed_page_image_preferred",notes="Preserve formulas, notation, diagrams and worked examples."),
    CurriculumSource("science_t1","science","Science in English — Student Book","العلوم باللغة الانجليزية-كتاب الطالب-0d9bc9e8.pdf","Term 1",148,"page_image",notes="2025–2026 cover; preserve diagrams, formulas and observations."),
    CurriculumSource("ict_t2","ict","Computer / ICT — Second Semester","computer_3prep_scond_term_english.pdf","Second Semester",66,"parsed_text",trust="supplied_source_unverified_current_year",notes="Uses VB.NET. Do not silently replace school ICT with Python."),
)


def get_source(source_id: str) -> CurriculumSource | None:
    return next((source for source in CURRICULUM_SOURCES if source.id == source_id), None)


def sources_for_subject(subject_id: str) -> Tuple[CurriculumSource, ...]:
    return tuple(source for source in CURRICULUM_SOURCES if source.subject_id == subject_id)


def source_inventory_summary() -> dict:
    return {
        "source_count": len(CURRICULUM_SOURCES),
        "subjects": sorted({source.subject_id for source in CURRICULUM_SOURCES}),
        "page_image_aware_required": any("page_image" in source.extraction_mode for source in CURRICULUM_SOURCES),
        "unverified_current_year": [source.id for source in CURRICULUM_SOURCES if source.trust != "trusted_project_source"],
    }
