from collections import OrderedDict

from lumina.curriculum.arabic_unit1 import ARABIC_U1_LESSONS
from lumina.curriculum.arabic_unit2 import ARABIC_U2_LESSONS
from lumina.curriculum.arabic_unit3 import ARABIC_U3_LESSONS
from lumina.curriculum.english_curriculum import ENGLISH_UNIT_LESSONS
from lumina.curriculum.english_reviews import REVIEW1, REVIEW2
from lumina.curriculum.ict_chapter1 import ICT_CHAPTER1_LESSONS
from lumina.curriculum.ict_chapter2 import ICT_CHAPTER2_LESSONS
from lumina.curriculum.ict_chapter3 import ICT_CHAPTER3_LESSONS
from lumina.curriculum.ict_chapter4 import ICT_CHAPTER4_LESSONS
from lumina.curriculum.math_unit1 import MATH_UNIT1_LESSONS
from lumina.curriculum.math_unit2 import MATH_UNIT2_LESSONS
from lumina.curriculum.math_unit3 import MATH_UNIT3_LESSONS
from lumina.curriculum.math_unit4 import MATH_UNIT4_LESSONS
from lumina.curriculum.math_unit5 import MATH_UNIT5_LESSONS
from lumina.curriculum.math_t2_unit1 import MATH_T2_UNIT1_LESSONS
from lumina.curriculum.math_t2_unit2 import MATH_T2_UNIT2_LESSONS
from lumina.curriculum.math_t2_unit3 import MATH_T2_UNIT3_LESSONS
from lumina.curriculum.math_t2_unit4 import MATH_T2_UNIT4_LESSONS
from lumina.curriculum.math_t2_unit5 import MATH_T2_UNIT5_LESSONS
from lumina.curriculum.religion_unit1 import RELIGION_U1_LESSONS
from lumina.curriculum.religion_unit2 import RELIGION_U2_LESSONS
from lumina.curriculum.religion_unit3 import RELIGION_U3_LESSONS
from lumina.curriculum.science_unit1 import SCIENCE_UNIT1_LESSONS
from lumina.curriculum.science_unit2 import SCIENCE_UNIT2_LESSONS
from lumina.curriculum.science_unit3 import SCIENCE_UNIT3_LESSONS
from lumina.curriculum.science_unit4 import SCIENCE_UNIT4_LESSONS
from lumina.curriculum.science_t2_unit1 import SCIENCE_T2_UNIT1_LESSONS
from lumina.curriculum.science_t2_unit2 import SCIENCE_T2_UNIT2_LESSONS
from lumina.curriculum.science_t2_unit3 import SCIENCE_T2_UNIT3_LESSONS
from lumina.curriculum.social_unit1 import SOCIAL_U1_LESSONS
from lumina.curriculum.social_unit2 import SOCIAL_U2_LESSONS
from lumina.curriculum.social_unit3 import SOCIAL_U3_LESSONS
from lumina.curriculum.social_unit4 import SOCIAL_U4_LESSONS


MAPPED_CURRICULUM = OrderedDict(
    (
        (
            "english",
            OrderedDict(
                list(
                    (f"Term 1 · {title}", lessons)
                    for title, lessons in ENGLISH_UNIT_LESSONS.items()
                )
                + [
                    ("Term 1 · Review 1", (REVIEW1,)),
                    ("Term 1 · Review 2", (REVIEW2,)),
                ]
            ),
        ),
        (
            "science",
            OrderedDict(
                (
                    ("Term 1 · Force and Motion", SCIENCE_UNIT1_LESSONS),
                    ("Term 1 · Light Energy", SCIENCE_UNIT2_LESSONS),
                    ("Term 1 · Universe and Solar System", SCIENCE_UNIT3_LESSONS),
                    ("Term 1 · Reproduction and Species Continuity", SCIENCE_UNIT4_LESSONS),
                    ("Term 2 · Chemical Reactions", SCIENCE_T2_UNIT1_LESSONS),
                    ("Term 2 · Electric Energy and Radioactivity", SCIENCE_T2_UNIT2_LESSONS),
                    ("Term 2 · Genetics", SCIENCE_T2_UNIT3_LESSONS),
                )
            ),
        ),
        (
            "math",
            OrderedDict(
                (
                    ("Term 1 · Relations and Functions", MATH_UNIT1_LESSONS),
                    ("Term 1 · Ratio and Variation", MATH_UNIT2_LESSONS),
                    ("Term 1 · Statistics", MATH_UNIT3_LESSONS),
                    ("Term 1 · Trigonometry", MATH_UNIT4_LESSONS),
                    ("Term 1 · Coordinate Geometry", MATH_UNIT5_LESSONS),
                    ("Term 2 · Equations", MATH_T2_UNIT1_LESSONS),
                    ("Term 2 · Algebraic Rational Functions", MATH_T2_UNIT2_LESSONS),
                    ("Term 2 · Probability", MATH_T2_UNIT3_LESSONS),
                    ("Term 2 · The Circle", MATH_T2_UNIT4_LESSONS),
                    ("Term 2 · Angles and Arcs", MATH_T2_UNIT5_LESSONS),
                )
            ),
        ),
        (
            "arabic",
            OrderedDict(
                (
                    ("Term 1 · قيم تحمي شبابنا", ARABIC_U1_LESSONS),
                    ("Term 1 · نحو تفكير سليم", ARABIC_U2_LESSONS),
                    ("Term 1 · أنا والمستقبل", ARABIC_U3_LESSONS),
                )
            ),
        ),
        (
            "social",
            OrderedDict(
                (
                    ("Term 1 · الملامح الطبيعية والحضارية لقارات العالم الجديد", SOCIAL_U1_LESSONS),
                    ("Term 1 · مصر في عصر محمد علي وخلفائه", SOCIAL_U2_LESSONS),
                    ("Term 1 · النظم البيئية في قارات العالم الجديد", SOCIAL_U3_LESSONS),
                    ("Term 1 · الحركة الوطنية في مواجهة الاحتلال البريطاني", SOCIAL_U4_LESSONS),
                )
            ),
        ),
        (
            "religion",
            OrderedDict(
                (
                    ("Term 1 · قيم الإسلام في بناء الفرد والمجتمع", RELIGION_U1_LESSONS),
                    ("Term 1 · الإسلام دين وحياة", RELIGION_U2_LESSONS),
                    ("Term 1 · تحمل المسئولية في الإسلام", RELIGION_U3_LESSONS),
                )
            ),
        ),
        (
            "ict",
            OrderedDict(
                (
                    ("Second Semester · Data", ICT_CHAPTER1_LESSONS),
                    ("Second Semester · Branching", ICT_CHAPTER2_LESSONS),
                    ("Second Semester · Looping & Procedures", ICT_CHAPTER3_LESSONS),
                    ("Second Semester · Cyber bullying", ICT_CHAPTER4_LESSONS),
                )
            ),
        ),
    )
)


SUBJECT_LABELS = {
    "english": "English",
    "science": "Science",
    "math": "Math",
    "arabic": "Arabic",
    "social": "Social Studies",
    "religion": "Religion",
    "ict": "ICT",
}


def all_mapped_lessons(subject_id: str | None = None):
    if subject_id is not None:
        units = MAPPED_CURRICULUM.get(subject_id, {})
        return tuple(lesson for lessons in units.values() for lesson in lessons)
    return tuple(
        lesson
        for units in MAPPED_CURRICULUM.values()
        for lessons in units.values()
        for lesson in lessons
    )


def curriculum_counts() -> dict[str, int]:
    return {
        subject_id: len(all_mapped_lessons(subject_id))
        for subject_id in MAPPED_CURRICULUM
    }
