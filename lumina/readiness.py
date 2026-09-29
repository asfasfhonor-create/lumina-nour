from __future__ import annotations

from dataclasses import dataclass

from lumina.curriculum.mapped_curriculum import all_mapped_lessons
from lumina.persistence.session_store import persistence_status


@dataclass(frozen=True)
class ReadinessItem:
    key: str
    label: str
    ready: bool
    detail: str


def build_release_readiness(*, ai_available: bool, app_pin_configured: bool, parent_pin_configured: bool) -> tuple[ReadinessItem, ...]:
    storage = persistence_status()
    mapped_count = len(all_mapped_lessons())

    return (
        ReadinessItem(
            key="curriculum",
            label="Mapped curriculum",
            ready=mapped_count > 0,
            detail=f"{mapped_count} mapped learning blocks",
        ),
        ReadinessItem(
            key="ai",
            label="Gemini tutor",
            ready=ai_available,
            detail="Configured" if ai_available else "GEMINI_API_KEY not configured",
        ),
        ReadinessItem(
            key="storage",
            label="Durable learning storage",
            ready=bool(storage["durable"]),
            detail=storage["label"],
        ),
        ReadinessItem(
            key="parent_pin",
            label="Parent Dashboard protection",
            ready=parent_pin_configured,
            detail="Configured" if parent_pin_configured else "PARENT_PIN not configured",
        ),
        ReadinessItem(
            key="app_pin",
            label="Whole-app PIN",
            ready=app_pin_configured,
            detail="Configured" if app_pin_configured else "Optional / not configured",
        ),
    )
