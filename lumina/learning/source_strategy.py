from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SourceUsePolicy:
    resource_use: str
    learner_visible: bool
    explanation: bool
    practice: bool
    assessment: bool
    correction_reference: bool
    label: str


POLICIES = {
    "main_book": SourceUsePolicy(
        resource_use="main_book",
        learner_visible=True,
        explanation=True,
        practice=True,
        assessment=False,
        correction_reference=False,
        label="شرح وتدريب",
    ),
    "assessment_revision": SourceUsePolicy(
        resource_use="assessment_revision",
        learner_visible=True,
        explanation=False,
        practice=True,
        assessment=True,
        correction_reference=False,
        label="اختبارات ومراجعة",
    ),
    "revision_exam": SourceUsePolicy(
        resource_use="revision_exam",
        learner_visible=True,
        explanation=False,
        practice=True,
        assessment=True,
        correction_reference=False,
        label="مراجعة وامتحانات",
    ),
    "answer_guide": SourceUsePolicy(
        resource_use="answer_guide",
        learner_visible=False,
        explanation=False,
        practice=False,
        assessment=False,
        correction_reference=True,
        label="مرجع تصحيح خلف الكواليس",
    ),
    "support": SourceUsePolicy(
        resource_use="support",
        learner_visible=True,
        explanation=True,
        practice=False,
        assessment=False,
        correction_reference=False,
        label="مصدر مساعد",
    ),
}


def source_policy(metadata: dict | None) -> SourceUsePolicy:
    metadata = metadata or {}
    return POLICIES.get(str(metadata.get("resource_use", "support")), POLICIES["support"])


def choose_explanation_source(sources: list[dict]) -> dict | None:
    candidates = []
    for source in sources:
        policy = source_policy(source.get("metadata"))
        if source.get("active") and policy.learner_visible and policy.explanation:
            candidates.append(source)
    return candidates[0] if candidates else None


def correction_references(sources: list[dict]) -> list[dict]:
    return [
        source
        for source in sources
        if source.get("active") and source_policy(source.get("metadata")).correction_reference
    ]


def choose_practice_source(sources: list[dict]) -> dict | None:
    preferred = ("assessment_revision", "revision_exam", "main_book")
    for resource_use in preferred:
        for source in sources:
            policy = source_policy(source.get("metadata"))
            if (
                source.get("active")
                and policy.learner_visible
                and policy.practice
                and policy.resource_use == resource_use
            ):
                return source
    return None
