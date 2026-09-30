"""Adaptive language policy for Nour's learner-facing UI.

English-first is the default. Arabic is a scaffold, not a second permanent
translation layer. Parent/admin surfaces remain Arabic-first.
"""

import streamlit as st

from lumina.learning.english_profile import support_level


ENGLISH_FIRST_LABELS = {
    "curriculum_search": "Curriculum Search · البحث في المنهج",
    "weekly_plan": "My Plan · خطتي",
    "exam_mode": "Quick Practice · تدريب سريع",
    "review_center": "My Reviews · مراجعاتي",
    "daily_mission": "Daily Mission · مهمة اليوم",
    "start_daily_mission": "Start today's mission · ابدئي مهمة اليوم",
    "learning_worlds": "Choose Your World · اختاري عالمك",
    "parent_area": "للأسرة",
}

WORLD_LABELS = {
    "english": ("English Adventure", "Start English Adventure · ابدئي مغامرة الإنجليزي"),
    "science": ("Science Lab", "Enter Science Lab · ادخلي معمل العلوم"),
    "math": ("Math Quest", "Start Math Quest · ابدئي تحدّي الرياضيات"),
    "ict": ("ICT Lab", "Enter ICT Lab · ادخلي معمل الكمبيوتر"),
    "arabic": ("Arabic World · عالم العربي", "Open Arabic World · ادخلي عالم العربي"),
    "social": ("Social Detective · مغامرة الدراسات", "Start Social Detective · ابدئي مغامرة الدراسات"),
    "religion": ("Religion Journey · رحلة الدين", "Start Religion Journey · ابدئي رحلة الدين"),
    "ai": ("AI Lab", "Enter AI Lab · ادخلي عالم الذكاء الاصطناعي"),
}


def learner_support_level() -> str:
    """Derive UI scaffolding from Nour's demonstrated Real English baseline."""
    level = support_level(st.session_state.get("english_profile") or {})
    if level == "light":
        return "light"
    return "supported"


def learner_label(english: str, arabic: str = "") -> str:
    """Render an English-first learner label with optional Arabic scaffold."""
    level = learner_support_level()
    if level == "english_only" or not arabic:
        return english
    if level == "light":
        return english
    return f"{english} · {arabic}"
