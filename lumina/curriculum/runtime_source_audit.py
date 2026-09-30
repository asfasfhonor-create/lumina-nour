from __future__ import annotations

from dataclasses import dataclass

from lumina.curriculum.source_registry import CURRICULUM_SOURCES
from lumina.persistence.base import PersistenceError
from lumina.persistence.trusted_source_catalog import NeonTrustedSourceCatalog


@dataclass(frozen=True)
class RuntimeSourceStatus:
    source_id: str
    filename: str
    subject_id: str
    ready: bool
    trusted: bool
    reason: str


def audit_primary_runtime_sources(database_url: str, learner_key: str) -> tuple[RuntimeSourceStatus, ...]:
    """Check whether every registered curriculum book also exists in durable runtime storage."""
    catalog = NeonTrustedSourceCatalog(database_url, learner_key)
    statuses = []
    for source in CURRICULUM_SOURCES:
        try:
            record = catalog.find_active_by_filename(source.filename)
        except PersistenceError:
            record = None
        ready = record is not None
        if ready:
            reason = "ready"
        elif not source.trusted:
            reason = "source_needs_current_year_verification"
        else:
            reason = "primary_file_not_in_runtime_storage"
        statuses.append(
            RuntimeSourceStatus(
                source_id=source.id,
                filename=source.filename,
                subject_id=source.subject_id,
                ready=ready,
                trusted=source.trusted,
                reason=reason,
            )
        )
    return tuple(statuses)
