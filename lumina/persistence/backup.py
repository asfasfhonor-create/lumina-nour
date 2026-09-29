from __future__ import annotations

import json
from datetime import datetime, timezone

import streamlit as st


BACKUP_KEYS = (
    "xp",
    "streak",
    "daily_done",
    "tasks_list",
    "learning_attempts",
    "mistake_notebook",
    "review_queue",
    "english_profile",
    "rewarded_evidence",
    "learning_days",
    "badges",
)


def export_learning_backup() -> str:
    payload = {
        "schema_version": 1,
        "exported_at": datetime.now(timezone.utc).isoformat(),
        "data": {
            key: st.session_state.get(key)
            for key in BACKUP_KEYS
        },
    }
    return json.dumps(payload, ensure_ascii=False, indent=2)


def restore_learning_backup(raw: str) -> tuple[bool, str]:
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError:
        return False, "ملف النسخة الاحتياطية غير صالح."

    if payload.get("schema_version") != 1 or not isinstance(payload.get("data"), dict):
        return False, "صيغة النسخة الاحتياطية غير مدعومة."

    data = payload["data"]
    for key in BACKUP_KEYS:
        if key in data:
            st.session_state[key] = data[key]

    return True, "تم استرجاع بيانات التعلم من النسخة الاحتياطية."
