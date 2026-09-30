from __future__ import annotations

import json
from datetime import datetime, timezone

import streamlit as st

from lumina.persistence.base import LearningStore


PROFILE_KEYS = (
    "xp",
    "streak",
    "english_profile",
    "ai_profile",
    "rewarded_evidence",
    "learning_days",
    "badges",
    "daily_mission_lesson_id",
    "daily_mission_date",
    "first_run_complete",
)


def export_learning_backup(store: LearningStore) -> str:
    payload = {
        "schema_version": 2,
        "exported_at": datetime.now(timezone.utc).isoformat(),
        "profile": store.get_profile_state(),
        "attempts": store.get_attempts(),
        "mistakes": store.get_mistakes(),
        "reviews": store.get_reviews(),
    }
    return json.dumps(payload, ensure_ascii=False, indent=2, default=str)


def _attempt_signature(item: dict) -> tuple:
    return (
        item.get("lesson_id"),
        item.get("check_id"),
        item.get("evidence_id"),
        item.get("answer"),
        item.get("correct"),
        str(item.get("created_at") or ""),
    )


def restore_learning_backup(raw: str, store: LearningStore) -> tuple[bool, str]:
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError:
        return False, "ملف النسخة الاحتياطية غير صالح."

    if payload.get("schema_version") != 2:
        return False, "صيغة النسخة الاحتياطية قديمة أو غير مدعومة."

    profile = payload.get("profile") or {}
    attempts = payload.get("attempts") or []
    mistakes = payload.get("mistakes") or []
    reviews = payload.get("reviews") or []

    if not all(isinstance(items, list) for items in (attempts, mistakes, reviews)):
        return False, "محتويات النسخة الاحتياطية غير صالحة."

    existing_signatures = {
        _attempt_signature(item)
        for item in store.get_attempts()
    }
    restored_attempts = 0
    for attempt in attempts:
        signature = _attempt_signature(attempt)
        if signature in existing_signatures:
            continue
        attempt = dict(attempt)
        attempt.pop("id", None)
        store.record_attempt(attempt)
        existing_signatures.add(signature)
        restored_attempts += 1

    for mistake in mistakes:
        item = dict(mistake)
        item.pop("id", None)
        store.record_mistake(item)
        if item.get("resolved"):
            store.resolve_mistake(item["lesson_id"], item["check_id"])

    for review in reviews:
        item = dict(review)
        item.pop("id", None)
        store.queue_review(item)
        if item.get("status") == "completed":
            store.complete_review(item["lesson_id"], item["check_id"])

    store.save_profile_state(profile)
    for key in PROFILE_KEYS:
        if key in profile:
            st.session_state[key] = profile[key]

    return (
        True,
        f"تم استرجاع النسخة الاحتياطية. تمت إضافة {restored_attempts} محاولة غير مكررة.",
    )
