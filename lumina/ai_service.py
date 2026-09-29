from __future__ import annotations

from typing import Any
import json

from google import genai
from google.genai import types


DEFAULT_MODEL = "gemini-2.5-flash"


class AIServiceError(RuntimeError):
    """User-safe wrapper for provider failures."""


class GeminiService:
    """Centralized Gemini access for LUMINA.

    UI code owns the learning prompt/context. This service owns provider access,
    model selection, and a single place for future retry/cost/error policies.
    """

    def __init__(self, api_key: str | None, model: str = DEFAULT_MODEL) -> None:
        self.api_key = api_key
        self.model = model
        self._client = genai.Client(api_key=api_key) if api_key else None

    @property
    def available(self) -> bool:
        return self._client is not None

    def generate(
        self,
        contents: Any,
        *,
        system_instruction: str | None = None,
    ) -> str:
        if not self._client:
            raise AIServiceError("الأداة الذكية غير مفعلة لأن Gemini API Key غير موجود.")

        config = None
        if system_instruction:
            config = types.GenerateContentConfig(
                system_instruction=system_instruction,
            )

        try:
            response = self._client.models.generate_content(
                model=self.model,
                contents=contents,
                config=config,
            )
        except Exception as exc:
            raise AIServiceError(
                "تعذر تشغيل الأداة الذكية الآن. جرّبي مرة أخرى بعد قليل."
            ) from exc

        return response.text or ""

    def generate_json(
        self,
        contents: Any,
        *,
        system_instruction: str | None = None,
    ) -> dict:
        if not self._client:
            raise AIServiceError("الأداة الذكية غير مفعلة لأن Gemini API Key غير موجود.")

        config = types.GenerateContentConfig(
            system_instruction=system_instruction,
            response_mime_type="application/json",
        )
        try:
            response = self._client.models.generate_content(
                model=self.model,
                contents=contents,
                config=config,
            )
            payload = json.loads(response.text or "{}")
        except Exception as exc:
            raise AIServiceError(
                "تعذر تجهيز النشاط الذكي الآن. جرّبي مرة أخرى بعد قليل."
            ) from exc

        if not isinstance(payload, dict):
            raise AIServiceError("الاستجابة الذكية غير صالحة للنشاط.")
        return payload
