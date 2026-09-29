from __future__ import annotations

from dataclasses import dataclass


GENTLE_START = "gentle_start"
BUILDING = "building"
READY_CHALLENGE = "ready_challenge"


@dataclass(frozen=True)
class LearningStage:
    id: str
    label: str
    max_difficulty: int
    mission_label: str
    reassurance: str


STAGES = {
    GENTLE_START: LearningStage(
        id=GENTLE_START,
        label="بداية هادية",
        max_difficulty=1,
        mission_label="نفهم الفكرة الأول",
        reassurance="مفيش استعجال. هدفنا نفهم الفكرة خطوة خطوة.",
    ),
    BUILDING: LearningStage(
        id=BUILDING,
        label="بنثبت الفهم",
        max_difficulty=2,
        mission_label="نجربها بطريقة مختلفة",
        reassurance="إحنا بنبني على اللي فهمتيه، مش بنحفظ إجابة.",
    ),
    READY_CHALLENGE: LearningStage(
        id=READY_CHALLENGE,
        label="جاهزة لتحدّي صغير",
        max_difficulty=3,
        mission_label="تحدّي خفيف",
        reassurance="التحدي قصير، ولو لخبّطك هنرجع خطوة بدون أي خصم.",
    ),
}


MISSION_THEMES = {
    "science": ("🔬", "مهمة المختبر"),
    "math": ("🧩", "لغز الرياضيات"),
    "english": ("💬", "مهمة الكلام والفهم"),
    "arabic": ("📝", "مهمة اللغة"),
    "social": ("🗺️", "مهمة الاستكشاف"),
    "religion": ("🌿", "مهمة الفهم والتطبيق"),
    "ict": ("💻", "مهمة التقنية"),
}


def learning_stage(attempts: list[dict], mistakes: list[dict]) -> LearningStage:
    """Choose a low-pressure level from real evidence, never from age assumptions."""
    unresolved = [item for item in mistakes if not item.get("resolved", False)]
    correct = [item for item in attempts if item.get("correct") is True]
    distinct_correct = {
        str(item.get("evidence_id") or item.get("check_id") or "")
        for item in correct
        if item.get("evidence_id") or item.get("check_id")
    }

    if not attempts or unresolved:
        return STAGES[GENTLE_START]
    if len(distinct_correct) >= 2 and len(correct) >= 3:
        return STAGES[READY_CHALLENGE]
    return STAGES[BUILDING]


def eligible_checks(lesson, stage: LearningStage):
    """Return only questions that are not above Nour's current demonstrated level."""
    checks = tuple(
        check
        for check in lesson.checks
        if int(getattr(check, "difficulty", 1)) <= stage.max_difficulty
    )
    return checks or tuple(lesson.checks[:1])


def mission_theme(module_id: str) -> tuple[str, str]:
    return MISSION_THEMES.get(module_id, ("✨", "مهمة صغيرة"))


def support_depth(attempts: list[dict], check_id: str) -> int:
    """0 = normal hint, 1 = explain the idea again, 2 = full guided recovery."""
    wrong = [
        item
        for item in attempts
        if item.get("check_id") == check_id and item.get("correct") is False
    ]
    return min(len(wrong), 2)
