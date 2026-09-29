"""Permanent trusted-source contracts for LUMINA.

This module deliberately separates temporary study uploads from explicitly
promoted permanent trusted sources. The selected durable binary provider is Neon Object Storage; metadata remains provider-aware.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from hashlib import sha256
from pathlib import PurePath
from typing import Mapping

SUPPORTED_MIME_TYPES = {
    "application/pdf",
    "image/jpeg",
    "image/png",
    "image/webp",
}

TEMPORARY = "temporary"
TRUSTED = "trusted"
ARCHIVED = "archived"
NEON_OBJECT_STORAGE = "neon_object_storage"
TRUSTED_SOURCE_BUCKET = "lumina-trusted-sources"


def content_sha256(data: bytes) -> str:
    """Return a stable lowercase SHA-256 digest for uploaded bytes."""
    if not data:
        raise ValueError("Source content cannot be empty.")
    return sha256(data).hexdigest()


def safe_filename(filename: str) -> str:
    """Keep only the final path component and reject empty file names."""
    cleaned = PurePath((filename or "").replace("\\", "/")).name.strip()
    if not cleaned or cleaned in {".", ".."}:
        raise ValueError("A valid filename is required.")
    return cleaned


@dataclass(frozen=True)
class SourceUpload:
    """Untrusted upload received from the UI before explicit promotion."""

    filename: str
    mime_type: str
    data: bytes

    def __post_init__(self) -> None:
        object.__setattr__(self, "filename", safe_filename(self.filename))
        if self.mime_type not in SUPPORTED_MIME_TYPES:
            raise ValueError(f"Unsupported source type: {self.mime_type}")
        if not self.data:
            raise ValueError("Source content cannot be empty.")

    @property
    def digest(self) -> str:
        return content_sha256(self.data)

    @property
    def size_bytes(self) -> int:
        return len(self.data)


@dataclass(frozen=True)
class TrustedSourceRecord:
    """Metadata persisted after deliberate trusted-source promotion."""

    source_id: str
    learner_key: str
    filename: str
    display_name: str
    subject: str
    term_label: str
    mime_type: str
    sha256: str
    size_bytes: int
    storage_provider: str
    storage_key: str
    trust_status: str = TRUSTED
    active: bool = True
    unit_label: str | None = None
    notes: str | None = None
    metadata: Mapping[str, str] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if self.trust_status not in {TRUSTED, ARCHIVED}:
            raise ValueError("Permanent sources must be trusted or archived.")
        if not self.learner_key.strip():
            raise ValueError("learner_key is required.")
        if not self.subject.strip():
            raise ValueError("subject is required.")
        if not self.storage_provider.strip() or not self.storage_key.strip():
            raise ValueError("Durable storage provider/key are required.")
        if self.mime_type not in SUPPORTED_MIME_TYPES:
            raise ValueError(f"Unsupported source type: {self.mime_type}")
        if len(self.sha256) != 64:
            raise ValueError("sha256 must be a 64-character hex digest.")
        int(self.sha256, 16)
        if self.size_bytes <= 0:
            raise ValueError("size_bytes must be positive.")


def build_trusted_record(
    upload: SourceUpload,
    *,
    learner_key: str,
    display_name: str,
    subject: str,
    term_label: str,
    storage_provider: str,
    storage_key: str,
    unit_label: str | None = None,
    notes: str | None = None,
    metadata: Mapping[str, str] | None = None,
) -> TrustedSourceRecord:
    """Create metadata only after durable binary storage has succeeded."""
    digest = upload.digest
    return TrustedSourceRecord(
        source_id=f"src_{digest[:24]}",
        learner_key=learner_key,
        filename=upload.filename,
        display_name=display_name.strip() or upload.filename,
        subject=subject.strip(),
        term_label=term_label.strip(),
        unit_label=unit_label.strip() if unit_label else None,
        mime_type=upload.mime_type,
        sha256=digest,
        size_bytes=upload.size_bytes,
        storage_provider=storage_provider.strip(),
        storage_key=storage_key.strip(),
        notes=notes.strip() if notes else None,
        metadata=dict(metadata or {}),
    )
