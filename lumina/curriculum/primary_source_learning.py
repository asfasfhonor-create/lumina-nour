from __future__ import annotations

import os
import tempfile
from pathlib import Path

import streamlit as st
from google.genai import types

from lumina.ai_service import AIServiceError, GeminiService
from lumina.curriculum.lesson_source_context import context_for_lesson, grounding_instruction
from lumina.curriculum.trusted_source_storage import (
    NeonTrustedSourceStorage,
    StorageConfig,
    TrustedSourceStorageError,
)
from lumina.persistence.base import PersistenceError
from lumina.persistence.trusted_source_catalog import NeonTrustedSourceCatalog


INLINE_PDF_LIMIT_BYTES = 45 * 1024 * 1024


def _runtime_source(lesson):
    context = context_for_lesson(lesson)
    if context is None:
        return None, None, None
    database_url = str(st.secrets.get("NEON_DATABASE_URL", "") or "").strip()
    learner_key = str(st.secrets.get("NOUR_LEARNER_KEY", "") or "").strip()
    storage_config = StorageConfig.from_mapping(st.secrets)
    if not database_url or not learner_key or storage_config is None:
        return context, None, None
    try:
        catalog = NeonTrustedSourceCatalog(database_url, learner_key)
        record = catalog.find_active_by_canonical_source(context.source_id)
        if record is None:
            record = catalog.find_active_by_filename(context.filename)
    except PersistenceError:
        return context, None, None
    return context, record, storage_config


def _load_pdf(ai: GeminiService, storage: NeonTrustedSourceStorage, record: dict):
    size = int(record.get("size_bytes") or storage.object_size(record["storage_key"]))
    if size <= INLINE_PDF_LIMIT_BYTES:
        return types.Part.from_bytes(
            data=storage.get_bytes(record["storage_key"]),
            mime_type=record["mime_type"],
        )

    cache_key = f"official_gemini_file_{record['source_id']}"
    cached_name = st.session_state.get(cache_key)
    if cached_name:
        try:
            return ai.get_uploaded_file(str(cached_name))
        except AIServiceError:
            st.session_state.pop(cache_key, None)

    suffix = Path(str(record.get("filename") or "source.pdf")).suffix or ".pdf"
    handle = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
    temp_path = handle.name
    handle.close()
    try:
        storage.download_to_path(record["storage_key"], temp_path)
        uploaded = ai.upload_file_path(temp_path)
        name = str(getattr(uploaded, "name", "") or "")
        if name:
            st.session_state[cache_key] = name
        return uploaded
    finally:
        try:
            os.remove(temp_path)
        except OSError:
            pass


def answer_from_primary_source(ai: GeminiService, lesson, question: str) -> tuple[str | None, str]:
    context, record, storage_config = _runtime_source(lesson)
    if context is None:
        return None, "المصدر الأساسي للدرس غير مسجل."
    if record is None or storage_config is None:
        return None, "ملف الكتاب الأساسي نفسه غير محفوظ بعد داخل مخزن المصادر الدائمة."

    try:
        storage = NeonTrustedSourceStorage(storage_config)
        pdf_part = _load_pdf(ai, storage, record)
        prompt = f"""You are LUMINA, Nour's curriculum tutor.
{grounding_instruction(lesson)}
The attached PDF is the registered primary curriculum file.
Focus only on the registered lesson page range. Respect whether the registry identifies printed book pages or PDF page indices. Do not silently use other pages or general model knowledge.\nFor visual pages, inspect the actual page evidence including diagrams, maps, formulas, tables and layout when relevant.
If the requested fact is not supported in that page range, say clearly that the source range does not support it.
Preserve the book's terminology and level. Explain for understanding, then ask one short checking question.

Nour's question:
{question}
"""
        return ai.generate([pdf_part, prompt]), ""
    except (TrustedSourceStorageError, AIServiceError):
        return None, "تعذر قراءة الكتاب الأساسي الآن."
