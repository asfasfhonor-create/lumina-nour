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
    resolution: str


def audit_primary_runtime_sources(database_url: str, learner_key: str, storage=None) -> tuple[RuntimeSourceStatus, ...]:
    """Check whether every registered curriculum book also exists in durable runtime storage."""
    catalog = NeonTrustedSourceCatalog(database_url, learner_key)
    statuses = []
    for source in CURRICULUM_SOURCES:
        resolution = "missing"
        try:
            record = catalog.find_active_by_canonical_source(source.id)
            if record is not None:
                resolution = "canonical"
            else:
                record = catalog.find_active_by_filename(source.filename)
                if record is not None:
                    resolution = "filename_fallback"
        except PersistenceError:
            record = None
        ready = record is not None
        if ready and storage is not None:
            try:
                ready = storage.object_size(record.get("storage_key", "")) > 0
            except Exception:
                ready = False
            if not ready:
                resolution = "missing_object"
        if ready:
            reason = "ready"
        elif resolution == "missing_object":
            reason = "storage_object_missing_or_unreadable"
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
                resolution=resolution,
            )
        )
    return tuple(statuses)
