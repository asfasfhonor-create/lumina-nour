from __future__ import annotations

from typing import Any

from google import genai
from google.genai import types


DEFAULT_MODEL = "gemini-2.5-flash"


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
            raise RuntimeError("Gemini API key is not configured.")

        config = None
        if system_instruction:
            config = types.GenerateContentConfig(
                system_instruction=system_instruction,
            )

        response = self._client.models.generate_content(
            model=self.model,
            contents=contents,
            config=config,
        )
        return response.text or ""
