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
        description="School English plus real English for everyday life.",
        category="language",
        icon="🇬🇧",
        mastery_dimensions=("vocabulary", "grammar", "reading", "writing", "listening", "speaking", "pronunciation"),
    ),
    LearningModule(
        id="science",
        title="Science Lab",
        description="Discover ideas through experiments, models, and why/how thinking.",
        category="school_subject",
        icon="🔬",
        mastery_dimensions=("concept", "application", "interpretation", "scientific_reasoning"),
    ),
    LearningModule(
        id="math",
        title="Math Quest",
        description="Solve, reason, and build your thinking step by step.",
        category="school_subject",
        icon="➗",
        mastery_dimensions=("concept", "problem_solving", "reasoning", "notation"),
    ),
    LearningModule(
        id="arabic",
        title="Arabic World",
        description="Reading, grammar, expression, and language skills.",
        category="school_subject",
        icon="📖",
        mastery_dimensions=("listening", "reading", "grammar", "spelling", "speaking", "writing"),
    ),
    LearningModule(
        id="social",
        title="Social Studies",
        description="History and geography through stories, maps, evidence, and investigation.",
        category="school_subject",
        icon="🌍",
        mastery_dimensions=("knowledge", "chronology", "cause_effect", "comparison", "inference", "maps"),
    ),
    LearningModule(
        id="religion",
        title="Religion Journey",
        description="Understand, connect, and apply ideas from the curriculum.",
        category="school_subject",
        icon="🕌",
        mastery_dimensions=("knowledge", "understanding", "application", "values"),
    ),
    LearningModule(
        id="ict",
        title="ICT Lab",
        description="Technology and digital skills through hands-on practice.",
        category="school_subject",
        icon="💻",
        mastery_dimensions=("concept", "syntax", "debugging", "digital_citizenship"),
    ),
    LearningModule(
        id="ai",
        title="AI Lab",
        description="Ask, experiment, verify, and build something new.",
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
