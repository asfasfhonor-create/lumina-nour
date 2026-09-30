from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class EnglishBaselineResult:
    correct: int
    total: int
    broad_band: str
    note: str
    skill_scores: dict[str, dict[str, int]]


BASELINE_ITEMS = (
    {
        "id": "vocab_context",
        "skill": "Vocabulary",
        "prompt": "Choose the best word: I was very ___ before the exam, but I felt better after I started.",
        "options": ("ancient", "stressed", "silent"),
        "correct_index": 1,
    },
    {
        "id": "grammar_present_perfect",
        "skill": "Grammar",
        "prompt": "Choose the best sentence.",
        "options": (
            "I has finished my homework already.",
            "I have finished my homework already.",
            "I finished already my homework tomorrow.",
        ),
        "correct_index": 1,
    },
    {
        "id": "grammar_condition",
        "skill": "Grammar",
        "prompt": "Choose the best sentence for an unreal past situation.",
        "options": (
            "If I study more, I would have did better.",
            "If I will study more, I did better.",
            "If I had studied more, I would have done better.",
        ),
        "correct_index": 2,
    },
    {
        "id": "reading_inference",
        "skill": "Reading",
        "prompt": (
            "Maya wanted to join the school debate team, but she was nervous about speaking in front of people. "
            "She practiced with a friend every afternoon. On Friday, she raised her hand and volunteered first. "
            "What can we infer?"
        ),
        "options": (
            "Maya stopped caring about debate.",
            "Maya became more confident after practice.",
            "Maya never practiced speaking.",
        ),
        "correct_index": 1,
    },
    {
        "id": "real_life_expression",
        "skill": "Speaking/Use",
        "prompt": "Which reply sounds most natural when someone says, 'Thanks for helping me'?",
        "options": ("I am welcome.", "No thanks me.", "You're welcome!"),
        "correct_index": 2,
    },
    {
        "id": "connector",
        "skill": "Writing/Grammar",
        "prompt": "Choose the best connector: I was tired, ___ I finished my project.",
        "options": ("unless", "but", "because of"),
        "correct_index": 1,
    },
)


def score_baseline(answers: dict[str, int]) -> EnglishBaselineResult:
    total = len(BASELINE_ITEMS)
    correct = sum(
        1
        for item in BASELINE_ITEMS
        if answers.get(item["id"]) == item["correct_index"]
    )

    if correct <= 2:
        band = "Foundation"
        note = "Start with highly supported real-life English and build core vocabulary/grammar confidence."
    elif correct <= 4:
        band = "Developing"
        note = "Use practical English with moderate support while strengthening accuracy and reading."
    else:
        band = "Independent-start"
        note = "Begin with less Arabic support and more open-ended reading, writing, and conversation."

    skill_scores: dict[str, dict[str, int]] = {}
    for item in BASELINE_ITEMS:
        skill = item["skill"]
        bucket = skill_scores.setdefault(skill, {"correct": 0, "total": 0})
        bucket["total"] += 1
        if answers.get(item["id"]) == item["correct_index"]:
            bucket["correct"] += 1

    return EnglishBaselineResult(
        correct=correct,
        total=total,
        broad_band=band,
        note=note,
        skill_scores=skill_scores,
    )


def support_level(profile: dict | None) -> str:
    """Translate the current broad band into a gentle language-support policy."""
    band = str((profile or {}).get("broad_band", ""))
    if band == "Independent-start":
        return "light"
    if band == "Developing":
        return "medium"
    return "high"


def support_instruction(profile: dict | None) -> str:
    level = support_level(profile)
    if level == "light":
        return (
            "Use mostly natural English. Give Arabic only for a genuinely blocking idea. "
            "Invite a slightly longer learner response."
        )
    if level == "medium":
        return (
            "Use clear natural English with short sentences. Give one brief Arabic hint when useful. "
            "Ask for a short but complete learner response."
        )
    return (
        "Use very clear short English and brief Arabic support for meaning. "
        "Ask for one small learner response at a time and avoid overload."
    )



def recommended_focus(profile: dict | None) -> tuple[str, str]:
    """Suggest a gentle next Real English activity from the weakest observed baseline skill."""
    profile = profile or {}
    scores = profile.get("skill_scores") or {}
    if not scores:
        return (
            "تحديد نقطة البداية",
            "نبدأ بصورة بسيطة عن المهارات علشان التدريب يبقى مناسب.",
        )

    ranked = []
    for skill, values in scores.items():
        total = int(values.get("total", 0))
        correct = int(values.get("correct", 0))
        ratio = (correct / total) if total else 0.0
        ranked.append((ratio, skill))
    ranked.sort(key=lambda item: (item[0], item[1]))
    weakest = ranked[0][1]

    mapping = {
        "Reading": (
            "قراءة وفهم",
            "نقوّي فهم المعنى والاستنتاج من سياق قصير.",
        ),
        "Vocabulary": (
            "كلمات في سياق",
            "نزود كلمات مفيدة من مواقف حقيقية بدل قوائم الحفظ.",
        ),
        "Grammar": (
            "كتابة قصيرة",
            "نثبت القواعد جوه جمل من تعبير نور نفسها.",
        ),
        "Writing/Grammar": (
            "كتابة قصيرة",
            "نقوّي الربط والتعبير بجمل قصيرة ثم نوسعها تدريجيًا.",
        ),
        "Speaking/Use": (
            "محادثة واقعية",
            "نتمرن على ردود طبيعية في مواقف قصيرة من الحياة.",
        ),
    }
    return mapping.get(
        weakest,
        (
            "محادثة واقعية",
            "نكمل استخدام اللغة في موقف عملي قصير.",
        ),
    )
