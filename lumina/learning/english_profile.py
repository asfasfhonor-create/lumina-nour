from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class EnglishBaselineResult:
    correct: int
    total: int
    broad_band: str
    note: str


BASELINE_ITEMS = (
    {
        "id": "vocab_context",
        "skill": "Vocabulary",
        "prompt": "Choose the best word: I was very ___ before the exam, but I felt better after I started.",
        "options": ("stressed", "ancient", "silent"),
        "correct_index": 0,
    },
    {
        "id": "grammar_present_perfect",
        "skill": "Grammar",
        "prompt": "Choose the best sentence.",
        "options": (
            "I have finished my homework already.",
            "I has finished my homework already.",
            "I finished already my homework tomorrow.",
        ),
        "correct_index": 0,
    },
    {
        "id": "grammar_condition",
        "skill": "Grammar",
        "prompt": "Choose the best sentence for an unreal past situation.",
        "options": (
            "If I had studied more, I would have done better.",
            "If I study more, I would have did better.",
            "If I will study more, I did better.",
        ),
        "correct_index": 0,
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
            "Maya became more confident after practice.",
            "Maya stopped caring about debate.",
            "Maya never practiced speaking.",
        ),
        "correct_index": 0,
    },
    {
        "id": "real_life_expression",
        "skill": "Speaking/Use",
        "prompt": "Which reply sounds most natural when someone says, 'Thanks for helping me'?",
        "options": ("You're welcome!", "I am welcome.", "No thanks me."),
        "correct_index": 0,
    },
    {
        "id": "connector",
        "skill": "Writing/Grammar",
        "prompt": "Choose the best connector: I was tired, ___ I finished my project.",
        "options": ("but", "because of", "unless"),
        "correct_index": 0,
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

    return EnglishBaselineResult(
        correct=correct,
        total=total,
        broad_band=band,
        note=note,
    )
