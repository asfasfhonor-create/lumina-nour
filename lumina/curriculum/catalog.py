from typing import Dict, Tuple

from lumina.curriculum.models import (
    CurriculumSource,
    CurriculumUnit,
    SOURCE_ROLE_OFFICIAL,
    SOURCE_ROLE_SUPPLIED,
)


ENGLISH_T1 = CurriculumSource(
    id="english_prep3_t1",
    subject_id="english",
    title="English Language — Third Preparatory",
    filename="English_language_prep3_t1.pdf",
    term="Term 1",
    language="English",
    source_role=SOURCE_ROLE_OFFICIAL,
    publisher="Ministry of Education",
    extraction_mode="page_image",
    units=(
        CurriculumUnit("u1", "Personal Identity"),
        CurriculumUnit("u2", "Communication with Family and Friends"),
        CurriculumUnit("u3", "Artificial Intelligence"),
        CurriculumUnit("review1", "Review 1"),
        CurriculumUnit("u4", "Screen Time"),
        CurriculumUnit("u5", "Design Thinking"),
        CurriculumUnit("u6", "Why Do We Like Stories?"),
        CurriculumUnit("review2", "Review 2"),
    ),
)

SCIENCE_T1 = CurriculumSource(
    id="science_prep3_t1",
    subject_id="science",
    title="Science and Life — Third Preparatory",
    filename="العلوم باللغة الانجليزية-كتاب الطالب-0d9bc9e8.pdf",
    term="Term 1",
    language="English",
    source_role=SOURCE_ROLE_OFFICIAL,
    publisher="Ministry of Education",
    extraction_mode="page_image",
    units=(
        CurriculumUnit("u1", "Force and Motion", ("Motion in One Direction", "Graphic Representation of Motion", "Scalars and Vectors")),
        CurriculumUnit("u2", "Light Energy (Mirrors and Lenses)", ("Mirrors", "Lenses")),
        CurriculumUnit("u3", "The Universe and the Solar System", ("The Universe and the Solar System",)),
        CurriculumUnit("u4", "Reproduction and Species Continuity", ("Cell Division", "Sexual and Asexual Reproduction")),
    ),
)

SCIENCE_T2 = CurriculumSource(
    id="science_prep3_t2",
    subject_id="science",
    title="Science and Life — Third Preparatory",
    filename="العلوم باللغة الانجليزية-كتاب الطالب-0d9bc9e8.pdf",
    term="Term 2",
    language="English",
    source_role=SOURCE_ROLE_OFFICIAL,
    publisher="Ministry of Education",
    extraction_mode="page_image",
    units=(
        CurriculumUnit("t2_u1", "Chemical Reactions", ("Chemical Reactions", "Rate of the Chemical Reaction")),
        CurriculumUnit(
            "t2_u2",
            "Electric Energy and Radioactivity",
            ("Physical Properties of the Electric Current", "The Electric Current and Cells", "Radioactivity and Nuclear Energy"),
        ),
        CurriculumUnit("t2_u3", "Genetics", ("The Main Principles of Heredity",)),
    ),
)

MATH_T1 = CurriculumSource(
    id="math_prep3_t1",
    subject_id="math",
    title="Mathematics — Third Preparatory",
    filename="الرياضيات باللغة الانجليزية-كتاب الطالب-334a9f66.pdf",
    term="Term 1",
    language="English",
    source_role=SOURCE_ROLE_OFFICIAL,
    publisher="Ministry of Education",
    extraction_mode="mixed",
    units=(
        CurriculumUnit("u1", "Relations and Functions", ("Cartesian Product", "Relations", "Functions (Mapping)", "Polynomial Functions")),
        CurriculumUnit("u2", "Ratio, Proportion, Direct Variation and Inverse Variation"),
        CurriculumUnit("u3", "Statistics", ("Collecting Data", "Dispersion")),
        CurriculumUnit("u4", "Trigonometry"),
        CurriculumUnit("u5", "Coordinate Geometry"),
    ),
)

MATH_T2 = CurriculumSource(
    id="math_prep3_t2",
    subject_id="math",
    title="Mathematics — Third Preparatory",
    filename="الرياضيات باللغة الانجليزية-كتاب الطالب-334a9f66.pdf",
    term="Term 2",
    language="English",
    source_role=SOURCE_ROLE_OFFICIAL,
    publisher="Ministry of Education",
    extraction_mode="mixed",
    units=(
        CurriculumUnit(
            "t2_u1",
            "Equations",
            (
                "Solving two equations of first degrees in two variables Graphically and Algebraically",
                "Solving an equation of second degree in one unknown Graphically and Algebraically",
                "Solving two equations in two variables, one of them is of the first degree and the other is of the second degree",
            ),
        ),
        CurriculumUnit(
            "t2_u2",
            "Algebraic Rational Functions and the operations on them",
            (
                "Set of zeroes of a polynomial function",
                "Algebraic rational function",
                "Equality of two Algebraic fractions",
                "Operations on Algebraic fractions",
            ),
        ),
        CurriculumUnit("t2_u3", "Probability", ("Operations on events", "Complementary event and the difference between two events")),
        CurriculumUnit(
            "t2_u4",
            "The Circle",
            (
                "Basic Definitions and Concepts",
                "Positions of a point, a Straight Line and a Circle with Respect to a Circle",
                "Identifying the Circle",
                "The Relation Between the Chords of a Circle and its Center",
            ),
        ),
        CurriculumUnit(
            "t2_u5",
            "Angles and Arcs in the circle",
            (
                "Central Angle and Measuring Arcs",
                "The relation between the Inscribed and central angles subtended by the same arc",
                "Inscribed Angles Subtended by the Same Arc",
                "Cyclic Quadrilaterals",
                "Properties of Cyclic Quadrilaterals",
                "The relation between the tangents of a circle",
                "Angle of Tangency",
            ),
        ),
    ),
)

ARABIC_T1 = CurriculumSource(
    id="arabic_prep3_t1",
    subject_id="arabic",
    title="Arabic Language — Third Preparatory",
    filename="Arabic_language_prep3_t1.pdf",
    term="Term 1",
    language="Arabic",
    source_role=SOURCE_ROLE_OFFICIAL,
    publisher="وزارة التربية والتعليم",
    extraction_mode="page_image",
    units=(
        CurriculumUnit("intro", "فراعنة عظماء"),
        CurriculumUnit("u1", "قيم تحمي شبابنا"),
        CurriculumUnit("u2", "نحو تفكير سليم"),
        CurriculumUnit("u3", "أنا والمستقبل"),
    ),
)

SOCIAL_T1 = CurriculumSource(
    id="social_prep3_t1",
    subject_id="social",
    title="Social Studies — Third Preparatory",
    filename="Social_studies_prep3_t1.pdf",
    term="Term 1",
    language="Arabic",
    source_role=SOURCE_ROLE_OFFICIAL,
    publisher="وزارة التربية والتعليم",
    extraction_mode="page_image",
    units=(
        CurriculumUnit("u1", "الملامح الطبيعية والحضارية لقارات العالم الجديد"),
        CurriculumUnit("u2", "مصر في عصر محمد علي وخلفائه"),
        CurriculumUnit("u3", "النظم البيئية في قارات العالم الجديد"),
        CurriculumUnit("u4", "الحركة الوطنية في مواجهة الاحتلال البريطاني"),
    ),
)

RELIGION_T1 = CurriculumSource(
    id="religion_prep3_t1",
    subject_id="religion",
    title="Islamic Religion — Third Preparatory",
    filename="Islamic_religion_prep3_t1.pdf",
    term="Term 1",
    language="Arabic",
    source_role=SOURCE_ROLE_OFFICIAL,
    publisher="وزارة التربية والتعليم",
    extraction_mode="text",
    units=(
        CurriculumUnit("u1", "قيم الإسلام في بناء الفرد والمجتمع"),
        CurriculumUnit("u2", "الإسلام دين وحياة"),
        CurriculumUnit("u3", "تحمل المسئولية في الإسلام"),
    ),
)

ICT_T2 = CurriculumSource(
    id="ict_prep3_t2",
    subject_id="ict",
    title="Computer and Information Technology — Third Preparatory",
    filename="computer_3prep_scond_term_english.pdf",
    term="Second Semester",
    language="English",
    source_role=SOURCE_ROLE_SUPPLIED,
    publisher=None,
    extraction_mode="text",
    units=(
        CurriculumUnit("c1", "Data", ("Data Types", "Constants & Variables", "Assignment statement", "Operator Precedence", "Errors")),
        CurriculumUnit("c2", "Branching", ("If Then", "If Then Else", "Select Case")),
        CurriculumUnit("c3", "Looping & Procedures", ("For Next", "Do While", "Procedure", "Function")),
        CurriculumUnit("c4", "Cyber bullying"),
    ),
)

SOURCES: Tuple[CurriculumSource, ...] = (
    ENGLISH_T1,
    SCIENCE_T1,
    SCIENCE_T2,
    MATH_T1,
    MATH_T2,
    ARABIC_T1,
    SOCIAL_T1,
    RELIGION_T1,
    ICT_T2,
)

_BY_SUBJECT: Dict[str, Tuple[CurriculumSource, ...]] = {}
for source in SOURCES:
    _BY_SUBJECT.setdefault(source.subject_id, tuple())
    _BY_SUBJECT[source.subject_id] = _BY_SUBJECT[source.subject_id] + (source,)


def get_sources(subject_id: str | None = None) -> Tuple[CurriculumSource, ...]:
    if subject_id is None:
        return SOURCES
    return _BY_SUBJECT.get(subject_id, tuple())


def get_source(source_id: str) -> CurriculumSource | None:
    return next((source for source in SOURCES if source.id == source_id), None)
