from dataclasses import dataclass, field
from typing import Tuple


@dataclass(frozen=True)
class LearningModule:
    id: str
    title: str
    description: str
    category: str
    icon: str
    track: str = "school"
    enabled: bool = True
    coming_soon: bool = True
    mastery_dimensions: Tuple[str, ...] = field(default_factory=tuple)


CORE_MODULES: Tuple[LearningModule, ...] = (
    LearningModule(
        id="english",
        title="English Adventure",
        description="School English + real language growth.",
        category="language",
        icon="🇬🇧",
        mastery_dimensions=("vocabulary", "grammar", "reading", "writing", "listening", "speaking", "pronunciation"),
    ),
    LearningModule(
        id="science",
        title="Science Lab",
        description="اكتشفي الفكرة بالتجربة والتشبيه.",
        category="school_subject",
        icon="🔬",
        mastery_dimensions=("concept", "application", "interpretation", "scientific_reasoning"),
    ),
    LearningModule(
        id="math",
        title="Math Quest",
        description="حلّي وفكّري خطوة بخطوة.",
        category="school_subject",
        icon="➗",
        mastery_dimensions=("concept", "problem_solving", "reasoning", "notation"),
    ),
    LearningModule(
        id="arabic",
        title="Arabic World",
        description="لغة وقراءة وتعبير بطريقة ممتعة.",
        category="school_subject",
        icon="📖",
        mastery_dimensions=("listening", "reading", "grammar", "spelling", "speaking", "writing"),
    ),
    LearningModule(
        id="social",
        title="Social Detective",
        description="تاريخ وجغرافيا كقصة وتحقيق.",
        category="school_subject",
        icon="🌍",
        mastery_dimensions=("knowledge", "chronology", "cause_effect", "comparison", "inference", "maps"),
    ),
    LearningModule(
        id="religion",
        title="Religion Journey",
        description="فهم وربط وتطبيق من المنهج.",
        category="school_subject",
        icon="🕌",
        mastery_dimensions=("knowledge", "understanding", "application", "values"),
    ),
    LearningModule(
        id="ict",
        title="ICT Lab",
        description="تكنولوجيا ومهارات رقمية بالتجربة.",
        category="school_subject",
        icon="💻",
        mastery_dimensions=("concept", "syntax", "debugging", "digital_citizenship"),
    ),
    LearningModule(
        id="ai",
        title="AI Lab",
        description="اسألي، جرّبي، راجعي، وابني حاجة جديدة.",
        category="ai",
        icon="🤖",
        track="enrichment",
        mastery_dimensions=("prompting", "verification", "critical_use", "creation", "responsible_use"),
    ),
)


def get_modules(enabled_only: bool = True) -> Tuple[LearningModule, ...]:
    if enabled_only:
        return tuple(module for module in CORE_MODULES if module.enabled)
    return CORE_MODULES


def get_school_subjects() -> Tuple[LearningModule, ...]:
    return tuple(module for module in get_modules() if module.category in {"school_subject", "language"})


def get_module(module_id: str) -> LearningModule | None:
    return next((module for module in CORE_MODULES if module.id == module_id), None)
