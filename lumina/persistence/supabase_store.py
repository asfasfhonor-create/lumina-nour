from __future__ import annotations

import json
from datetime import datetime, timezone
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from lumina.persistence.base import LearningStore


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


class SupabaseLearningStore(LearningStore):
    """Optional server-side REST adapter for a dedicated LUMINA Supabase project."""

    def __init__(self, url: str, api_key: str, learner_key: str) -> None:
        self.url = url.rstrip("/")
        self.api_key = api_key
        self.learner_key = learner_key

    def _request(self, table: str, *, method: str = "GET", params=None, payload=None, prefer=None):
        query = f"?{urlencode(params)}" if params else ""
        body = None if payload is None else json.dumps(payload).encode("utf-8")
        headers = {
            "apikey": self.api_key,
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json",
        }
        if body is not None:
            headers["Content-Type"] = "application/json"
        if prefer:
            headers["Prefer"] = prefer
        req = Request(
            f"{self.url}/rest/v1/{table}{query}",
            data=body,
            headers=headers,
            method=method,
        )
        with urlopen(req, timeout=12) as response:
            raw = response.read()
            return json.loads(raw.decode("utf-8")) if raw else None

    def record_attempt(self, attempt: dict) -> None:
        payload = dict(attempt, learner_key=self.learner_key)
        payload.setdefault("created_at", _utc_now())
        self._request("lumina_learning_attempts", method="POST", payload=payload, prefer="return=minimal")

    def get_attempts(self, lesson_id: str | None = None) -> list[dict]:
        params = {"select": "*", "learner_key": f"eq.{self.learner_key}", "order": "created_at.asc"}
        if lesson_id is not None:
            params["lesson_id"] = f"eq.{lesson_id}"
        return self._request("lumina_learning_attempts", params=params) or []

    def record_mistake(self, mistake: dict) -> None:
        payload = dict(mistake, learner_key=self.learner_key, updated_at=_utc_now())
        payload.setdefault("created_at", _utc_now())
        self._request(
            "lumina_mistakes",
            method="POST",
            params={"on_conflict": "learner_key,lesson_id,check_id"},
            payload=payload,
            prefer="resolution=merge-duplicates,return=minimal",
        )

    def resolve_mistake(self, lesson_id: str, check_id: str) -> None:
        self._request(
            "lumina_mistakes",
            method="PATCH",
            params={
                "learner_key": f"eq.{self.learner_key}",
                "lesson_id": f"eq.{lesson_id}",
                "check_id": f"eq.{check_id}",
            },
            payload={"resolved": True, "resolved_at": _utc_now(), "updated_at": _utc_now()},
            prefer="return=minimal",
        )

    def get_mistakes(self, lesson_id: str | None = None, unresolved_only: bool = False) -> list[dict]:
        params = {"select": "*", "learner_key": f"eq.{self.learner_key}", "order": "updated_at.asc"}
        if lesson_id is not None:
            params["lesson_id"] = f"eq.{lesson_id}"
        if unresolved_only:
            params["resolved"] = "eq.false"
        return self._request("lumina_mistakes", params=params) or []

    def queue_review(self, review: dict) -> None:
        payload = dict(review, learner_key=self.learner_key, updated_at=_utc_now())
        payload.setdefault("created_at", _utc_now())
        self._request(
            "lumina_reviews",
            method="POST",
            params={"on_conflict": "learner_key,lesson_id,check_id"},
            payload=payload,
            prefer="resolution=merge-duplicates,return=minimal",
        )

    def complete_review(self, lesson_id: str, check_id: str) -> None:
        self._request(
            "lumina_reviews",
            method="PATCH",
            params={
                "learner_key": f"eq.{self.learner_key}",
                "lesson_id": f"eq.{lesson_id}",
                "check_id": f"eq.{check_id}",
            },
            payload={"status": "completed", "completed_at": _utc_now(), "updated_at": _utc_now()},
            prefer="return=minimal",
        )

    def get_reviews(self, status: str | None = None) -> list[dict]:
        params = {"select": "*", "learner_key": f"eq.{self.learner_key}", "order": "updated_at.asc"}
        if status is not None:
            params["status"] = f"eq.{status}"
        return self._request("lumina_reviews", params=params) or []
