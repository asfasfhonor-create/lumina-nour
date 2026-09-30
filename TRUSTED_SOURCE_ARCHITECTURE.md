# LUMINA — Permanent Trusted Source Architecture

Status: provider selected; runtime credentials/upload wiring pending

## Goal

Allow Mohamed/Nour to upload a curriculum or learning file once, explicitly mark it as a trusted permanent source, and keep it available after the Streamlit session closes.

## Safety rule

A normal upload is **temporary by default**. It becomes authoritative only after an explicit permanent-source action and successful durable storage.

## Architecture

1. UI upload creates an untrusted `SourceUpload`.
2. Validation checks supported type, non-empty bytes, safe filename, size and SHA-256.
3. Durable binary storage writes the PDF/image to a provider designed for files/objects.
4. Only after step 3 succeeds, LUMINA creates a `TrustedSourceRecord`.
5. Neon PostgreSQL stores metadata/provenance only, not whole PDF blobs.
6. Duplicate detection uses `(learner_key, sha256)`.
7. Sources can later be archived/disabled without deleting historical learning evidence.
8. Retrieval must preserve source id, subject, term/unit metadata and page/range provenance.

## Why binaries are not stored in Neon

Keeping large PDFs outside the relational learning database reduces database bloat, backup size, query overhead and provider lock-in. The binary provider can therefore change later without rewriting mastery/progress tables.

## Provider decision

Neon Object Storage is the selected durable binary provider for LUMINA. The dedicated LUMINA Neon project reports object storage as enabled, and a private bucket named `lumina-trusted-sources` has been created on the production `main` branch. PostgreSQL continues to store metadata/provenance only. The application contract keeps `storage_provider + storage_key` so migration remains possible later without rewriting curriculum records.

Runtime upload/download wiring still requires a branch-scoped storage credential to be stored securely in Streamlit Secrets. No storage credential may be committed to GitHub or written into source metadata.

## Acceptance gates

- Temporary upload never appears in the permanent source catalog automatically.
- Unsupported/empty uploads are rejected.
- Same learner + same SHA-256 cannot be registered twice.
- Binary storage must succeed before metadata registration.
- Archive/disable must not erase learning history.
- No credentials or signed private URLs are stored in source metadata.
