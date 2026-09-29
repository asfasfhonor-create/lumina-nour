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
    required: bool = True


def build_release_readiness(
    *,
    ai_available: bool,
    app_pin_configured: bool,
    parent_pin_configured: bool,
    storage_status: dict | None = None,
    storage_verified: bool = False,
) -> tuple[ReadinessItem, ...]:
    storage = storage_status if storage_status is not None else persistence_status()
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
            ready=bool(storage["durable"] and storage_verified),
            detail=(
                f"{storage['label']} · verified"
                if storage["durable"] and storage_verified
                else (
                    f"{storage['label']} · configured, not verified"
                    if storage["durable"]
                    else storage["label"]
                )
            ),
        ),
        ReadinessItem(
            key="parent_pin",
            label="Parent Dashboard protection",
            ready=parent_pin_configured,
            detail="Configured" if parent_pin_configured else "Optional / not configured",
            required=False,
        ),
        ReadinessItem(
            key="app_pin",
            label="Whole-app PIN",
            ready=app_pin_configured,
            detail="Configured" if app_pin_configured else "Optional / not configured",
            required=False,
        ),
    )



def release_blockers(items: tuple[ReadinessItem, ...]) -> tuple[ReadinessItem, ...]:
    """Return only required readiness items that still block a production release."""
    return tuple(item for item in items if item.required and not item.ready)


def is_release_ready(items: tuple[ReadinessItem, ...]) -> bool:
    return not release_blockers(items)
