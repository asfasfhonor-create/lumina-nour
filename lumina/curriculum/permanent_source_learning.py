from __future__ import annotations

import streamlit as st
from google.genai import types

from lumina.ai_service import AIServiceError, GeminiService
from lumina.curriculum.trusted_source_storage import (
    NeonTrustedSourceStorage,
    StorageConfig,
    TrustedSourceStorageError,
)
from lumina.learning.source_strategy import choose_explanation_source
from lumina.persistence.base import PersistenceError
from lumina.persistence.trusted_source_catalog import NeonTrustedSourceCatalog


def _support_prompt(*, lesson_title: str, mode: str, stage_label: str, source_name: str) -> str:
    mode_rule = {
        "simple": (
            "Explain the lesson point in a simpler way using at most 4 short steps. "
            "Use one tiny example only if it is supported by the PDF."
        ),
        "creative": (
            "Turn the lesson point into a short playful mission or story hook. "
            "You may invent the story wrapper, but every curriculum fact must come from the PDF. "
            "End with one very easy thinking prompt, not an exam-style trap."
        ),
    }[mode]

    return f"""You are LUMINA, Nour's gentle curriculum tutor.

The attached PDF is a SUPPLEMENTARY source, not the authority that defines the curriculum.
The official Ministry source remains the primary curriculum reference.

Current lesson: {lesson_title}
Current learning stage: {stage_label}
Supplementary source: {source_name}

Rules:
1. Use curriculum facts only if they are actually supported by the attached PDF.
2. If this source does not clearly cover the current lesson, say exactly:
   "المصدر المساعد لا يغطي النقطة دي بوضوح."
   Then stop.
3. Do not make the level harder than the current stage.
4. Teach for understanding, not memorization.
5. Keep English curriculum terms in English when the source uses English.
6. Arabic support is welcome when it helps understanding.
7. Do not dump answers from an answer guide.
8. Keep the response short and encouraging, with no pressure language.
9. {mode_rule}
"""


def render_permanent_source_booster(
    ai: GeminiService,
    *,
    subject_id: str,
    lesson_title: str,
    stage_label: str,
) -> None:
    """Use a saved supplementary main book as optional extra teaching support."""
    if not ai.available:
        return

    database_url = str(st.secrets.get("NEON_DATABASE_URL", "") or "").strip()
    learner_key = str(st.secrets.get("NOUR_LEARNER_KEY", "") or "").strip()
    storage_config = StorageConfig.from_mapping(st.secrets)
    if not database_url or not learner_key or storage_config is None:
        return

    try:
        catalog = NeonTrustedSourceCatalog(database_url, learner_key)
        sources = [
            item for item in catalog.list_active()
            if item.get("subject") == subject_id
        ]
    except PersistenceError:
        return

    source = choose_explanation_source(sources)
    if source is None:
        return

    metadata = source.get("metadata") or {}
    publisher = metadata.get("publisher") or "المصدر المساعد"
    edition = metadata.get("edition_label")
    source_label = f"{source.get('display_name', source.get('filename', 'مصدر مساعد'))}"
    if edition:
        source_label += f" · {edition}"

    with st.expander(f"✨ شرح إضافي من {publisher}", expanded=False):
        st.caption(
            "ده دعم إضافي للفهم من المصدر المساعد. "
            "كتاب الوزارة يفضل المرجع الأساسي للمنهج."
        )

        c1, c2 = st.columns(2)
        simple = c1.button(
            "فهمهالي أبسط",
            key=f"source_booster_simple_{subject_id}_{source['source_id']}_{lesson_title}",
            use_container_width=True,
        )
        creative = c2.button(
            "حوّلها لمهمة ممتعة",
            key=f"source_booster_creative_{subject_id}_{source['source_id']}_{lesson_title}",
            use_container_width=True,
        )

        mode = "simple" if simple else "creative" if creative else None
        response_key = (
            f"source_booster_response_{subject_id}_{source['source_id']}_{lesson_title}"
        )

        if mode:
            try:
                storage = NeonTrustedSourceStorage(storage_config)
                pdf_bytes = storage.get_bytes(source["storage_key"])
                pdf_part = types.Part.from_bytes(
                    data=pdf_bytes,
                    mime_type=source["mime_type"],
                )
                prompt = _support_prompt(
                    lesson_title=lesson_title,
                    mode=mode,
                    stage_label=stage_label,
                    source_name=source_label,
                )
                with st.spinner("بجهز شرح خفيف من المصدر المساعد..."):
                    st.session_state[response_key] = ai.generate([pdf_part, prompt])
            except (TrustedSourceStorageError, AIServiceError):
                st.warning("الشرح الإضافي من المصدر المساعد مش متاح دلوقتي.")

        response = st.session_state.get(response_key)
        if response:
            st.markdown(response)
            st.caption(f"المصدر المساعد المستخدم: {source_label}")
