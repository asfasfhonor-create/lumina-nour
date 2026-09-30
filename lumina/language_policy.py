"""Adaptive language policy for Nour's learner-facing UI.

English-first is the default. Arabic is a scaffold, not a second permanent
translation layer. Parent/admin surfaces remain Arabic-first.
"""

import streamlit as st

from lumina.learning.english_profile import support_level


LEARNER_LABELS = {
    "curriculum_search": ("Curriculum Search", "البحث في المنهج"),
    "weekly_plan": ("My Plan", "خطتي"),
    "exam_mode": ("Quick Practice", "تدريب سريع"),
    "review_center": ("My Reviews", "مراجعاتي"),
    "daily_mission": ("Daily Mission", "مهمة اليوم"),
    "start_daily_mission": ("Start today's mission", "ابدئي مهمة اليوم"),
    "learning_worlds": ("Choose Your World", "اختاري عالمك"),
}

# Parent/admin surfaces deliberately stay Arabic-first.
PARENT_AREA_LABEL = "للأسرة"

WORLD_LABELS = {
    "english": (("English Adventure", ""), ("Start English Adventure", "ابدئي مغامرة الإنجليزي")),
    "science": (("Science Lab", ""), ("Enter Science Lab", "ادخلي معمل العلوم")),
    "math": (("Math Quest", ""), ("Start Math Quest", "ابدئي تحدّي الرياضيات")),
    "ict": (("ICT Lab", ""), ("Enter ICT Lab", "ادخلي معمل الكمبيوتر")),
    # Subject-language rule overrides English-profile adaptation here.
    "arabic": (("عالم العربي", ""), ("ادخلي عالم العربي", "")),
    "social": (("مغامرة الدراسات", ""), ("ابدئي مغامرة الدراسات", "")),
    "religion": (("رحلة الدين", ""), ("ابدئي رحلة الدين", "")),
    "ai": (("AI Lab", ""), ("Enter AI Lab", "ادخلي عالم الذكاء الاصطناعي")),
}


def learner_support_level() -> str:
    """Derive UI scaffolding from Nour's demonstrated Real English baseline."""
    return support_level(st.session_state.get("english_profile") or {})


def learner_label(english: str, arabic: str = "") -> str:
    """Render English-first UI; Arabic scaffold fades only at independent level."""
    level = learner_support_level()
    if level == "light" or not arabic:
        return english
    return f"{english} · {arabic}"


def ui_label(key: str) -> str:
    english, arabic = LEARNER_LABELS[key]
    return learner_label(english, arabic)


def world_title(module_id: str, fallback: str) -> str:
    spec = WORLD_LABELS.get(module_id)
    if not spec:
        return fallback
    english, arabic = spec[0]
    return learner_label(english, arabic)


def world_action(module_id: str) -> str:
    english, arabic = WORLD_LABELS[module_id][1]
    return learner_label(english, arabic)
