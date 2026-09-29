from __future__ import annotations

import streamlit as st
from google.genai import types

from lumina.ai_service import AIServiceError, GeminiService
from lumina.curriculum.trusted_source_storage import (
    NeonTrustedSourceStorage,
    StorageConfig,
    TrustedSourceStorageError,
)
from lumina.learning.source_strategy import (
    choose_explanation_source,
    choose_practice_source,
)
from lumina.persistence.base import PersistenceError
from lumina.persistence.trusted_source_catalog import NeonTrustedSourceCatalog


def _source_label(source: dict) -> str:
    metadata = source.get("metadata") or {}
    edition = metadata.get("edition_label")
    label = str(source.get("display_name") or source.get("filename") or "مصدر مساعد")
    return f"{label} · {edition}" if edition else label


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


def _practice_prompt(*, lesson_title: str, stage_label: str, source_name: str) -> str:
    return f"""Create ONE gentle multiple-choice practice item for Nour from the attached supplementary PDF.

Current lesson: {lesson_title}
Current learning stage: {stage_label}
Supplementary source: {source_name}

Return JSON only with exactly these fields:
{{
  "supported": true,
  "prompt": "short learner-friendly question",
  "options": ["option 1", "option 2", "option 3"],
  "correct_index": 0,
  "hint": "one short hint that helps understanding without giving the answer away",
  "explanation": "one short explanation of the idea after the learner answers"
}}

Rules:
1. The curriculum fact and correct answer MUST be supported by the attached PDF.
2. If the PDF does not clearly cover the lesson, return:
   {{"supported": false, "prompt": "", "options": [], "correct_index": 0, "hint": "", "explanation": ""}}
3. Keep the question at or below the current learning stage.
4. Prefer concept understanding or a tiny application, not memorized wording.
5. Exactly 3 options. Only one correct option.
6. No trick wording, double negatives, or unnecessarily difficult vocabulary.
7. Keep English curriculum terms in English when the source uses English.
8. Do not use answer-guide content as learner-facing material.
"""


def _load_pdf_part(storage: NeonTrustedSourceStorage, source: dict):
    pdf_bytes = storage.get_bytes(source["storage_key"])
    return types.Part.from_bytes(
        data=pdf_bytes,
        mime_type=source["mime_type"],
    )


def _valid_practice(payload: dict) -> bool:
    if payload.get("supported") is not True:
        return False
    options = payload.get("options")
    if not isinstance(options, list) or len(options) != 3:
        return False
    if not all(isinstance(item, str) and item.strip() for item in options):
        return False
    try:
        correct = int(payload.get("correct_index"))
    except (TypeError, ValueError):
        return False
    return (
        0 <= correct < 3
        and bool(str(payload.get("prompt", "")).strip())
        and bool(str(payload.get("hint", "")).strip())
        and bool(str(payload.get("explanation", "")).strip())
    )


def render_permanent_source_booster(
    ai: GeminiService,
    *,
    subject_id: str,
    lesson_title: str,
    stage_label: str,
) -> None:
    """Turn saved supplementary books into optional explanation and gentle practice."""
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

    explanation_source = choose_explanation_source(sources)
    practice_source = choose_practice_source(sources)
    if explanation_source is None and practice_source is None:
        return

    with st.expander("✨ استفيدي من الكتب المساعدة", expanded=False):
        st.caption(
            "الكتب المساعدة بتقوّي الشرح والتدريب، لكن كتاب الوزارة يفضل المرجع الأساسي للمنهج."
        )

        if explanation_source is not None:
            metadata = explanation_source.get("metadata") or {}
            publisher = metadata.get("publisher") or "المصدر المساعد"
            source_label = _source_label(explanation_source)
            c1, c2 = st.columns(2)
            simple = c1.button(
                "فهمهالي أبسط",
                key=f"source_booster_simple_{subject_id}_{explanation_source['source_id']}_{lesson_title}",
                use_container_width=True,
            )
            creative = c2.button(
                "حوّلها لمهمة ممتعة",
                key=f"source_booster_creative_{subject_id}_{explanation_source['source_id']}_{lesson_title}",
                use_container_width=True,
            )

            mode = "simple" if simple else "creative" if creative else None
            response_key = (
                f"source_booster_response_{subject_id}_{explanation_source['source_id']}_{lesson_title}"
            )

            if mode:
                try:
                    storage = NeonTrustedSourceStorage(storage_config)
                    pdf_part = _load_pdf_part(storage, explanation_source)
                    prompt = _support_prompt(
                        lesson_title=lesson_title,
                        mode=mode,
                        stage_label=stage_label,
                        source_name=source_label,
                    )
                    with st.spinner(f"بجهز دعم خفيف من {publisher}..."):
                        st.session_state[response_key] = ai.generate([pdf_part, prompt])
                except (TrustedSourceStorageError, AIServiceError):
                    st.warning("الشرح الإضافي من المصدر المساعد مش متاح دلوقتي.")

            response = st.session_state.get(response_key)
            if response:
                st.markdown(response)
                st.caption(f"المصدر المساعد المستخدم: {source_label}")

        if practice_source is not None:
            practice_label = _source_label(practice_source)
            question_key = (
                f"source_practice_question_{subject_id}_{practice_source['source_id']}_{lesson_title}"
            )
            answer_key = (
                f"source_practice_answer_{subject_id}_{practice_source['source_id']}_{lesson_title}"
            )

            st.markdown("**🎲 تحدّي إضافي خفيف من المصدر المساعد**")
            if st.button(
                "هاتلي تحدّي مناسب",
                key=f"source_practice_generate_{subject_id}_{practice_source['source_id']}_{lesson_title}",
                use_container_width=True,
            ):
                try:
                    storage = NeonTrustedSourceStorage(storage_config)
                    pdf_part = _load_pdf_part(storage, practice_source)
                    payload = ai.generate_json([
                        pdf_part,
                        _practice_prompt(
                            lesson_title=lesson_title,
                            stage_label=stage_label,
                            source_name=practice_label,
                        ),
                    ])
                    if _valid_practice(payload):
                        st.session_state[question_key] = payload
                        st.session_state.pop(answer_key, None)
                    else:
                        st.info("المصدر المساعد مش مدي سؤال واضح مناسب للدرس ده، فمش هنخمن.")
                except (TrustedSourceStorageError, AIServiceError):
                    st.warning("تعذر تجهيز التحدّي الإضافي دلوقتي.")

            question = st.session_state.get(question_key)
            if question:
                answer = st.radio(
                    str(question["prompt"]),
                    list(question["options"]),
                    index=None,
                    key=answer_key,
                )
                if st.button(
                    "أجرب التحدّي",
                    key=f"source_practice_check_{subject_id}_{practice_source['source_id']}_{lesson_title}",
                    use_container_width=True,
                ):
                    if answer is None:
                        st.warning("اختاري إجابة الأول — مفيش أي خصم.")
                    else:
                        selected = list(question["options"]).index(answer)
                        if selected == int(question["correct_index"]):
                            st.success("صح 👏 فهم جميل للفكرة.")
                        else:
                            st.warning("ولا يهمك — جربي تستخدمي التلميح وبعدها فكري فيها تاني.")
                            st.info(f"تلميح: {question['hint']}")
                        st.info(f"الفكرة: {question['explanation']}")
                st.caption(f"مصدر التحدّي: {practice_label}")
