"""Language policy for Nour's learner-facing UI.

Navigation is English-first by design. Arabic is used inside Arabic-medium
subject content and in parent/admin surfaces, not as a permanent translation
layer beside learner navigation.
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

PARENT_AREA_LABEL = "Parent Area"

WORLD_LABELS = {
    "english": (("English Adventure", ""), ("Start English Adventure", "")),
    "science": (("Science Lab", ""), ("Enter Science Lab", "")),
    "math": (("Math Quest", ""), ("Start Math Quest", "")),
    "ict": (("ICT Lab", ""), ("Enter ICT Lab", "")),
    "arabic": (("Arabic World", ""), ("Enter Arabic World", "")),
    "social": (("Social Studies", ""), ("Start Social Studies", "")),
    "religion": (("Religion Journey", ""), ("Start Religion Journey", "")),
    "ai": (("AI Lab", ""), ("Enter AI Lab", "")),
}


def learner_support_level() -> str:
    """Derive content scaffolding from Nour's demonstrated Real English baseline."""
    return support_level(st.session_state.get("english_profile") or {})


def learner_label(english: str, arabic: str = "") -> str:
    """Keep learner navigation English-first.

    Arabic support belongs in learning content/context when it genuinely helps;
    it should not turn the main navigation into an Arabic or duplicated UI.
    """
    return english


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
