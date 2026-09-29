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
    prerequisites: Tuple[str, ...] = field(default_factory=tuple)
    stages: Tuple[str, ...] = field(default_factory=tuple)
    activity_types: Tuple[str, ...] = field(default_factory=tuple)
    source_requirements: Tuple[str, ...] = field(default_factory=tuple)
    parent_metrics: Tuple[str, ...] = field(default_factory=tuple)


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


_MODULES = {module.id: module for module in CORE_MODULES}


def register_module(module: LearningModule, *, replace: bool = False) -> None:
    """Register a future learning module without changing navigation/business logic."""
    if module.id in _MODULES and not replace:
        raise ValueError(f"Module already registered: {module.id}")
    _MODULES[module.id] = module


def get_modules(enabled_only: bool = True) -> Tuple[LearningModule, ...]:
    modules = tuple(_MODULES.values())
    if enabled_only:
        return tuple(module for module in modules if module.enabled)
    return modules


def get_school_subjects() -> Tuple[LearningModule, ...]:
    return tuple(module for module in get_modules() if module.category in {"school_subject", "language"})


def get_module(module_id: str) -> LearningModule | None:
    return _MODULES.get(module_id)
