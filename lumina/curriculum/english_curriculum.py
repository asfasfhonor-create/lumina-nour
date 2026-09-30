from collections import OrderedDict

from lumina.curriculum.english_unit1 import UNIT1_LESSONS
from lumina.curriculum.english_unit2 import UNIT2_LESSONS
from lumina.curriculum.english_unit3 import UNIT3_LESSONS
from lumina.curriculum.english_unit4 import UNIT4_LESSONS
from lumina.curriculum.english_unit5 import UNIT5_LESSONS
from lumina.curriculum.english_unit6 import UNIT6_LESSONS


ENGLISH_UNIT_LESSONS = OrderedDict(
    (
        ("Personal Identity", UNIT1_LESSONS),
        ("Communication with Family and Friends", UNIT2_LESSONS),
        ("Artificial Intelligence", UNIT3_LESSONS),
        ("Screen Time", UNIT4_LESSONS),
        ("Design Thinking", UNIT5_LESSONS),
        ("Why Do We Like Stories?", UNIT6_LESSONS),
    )
)


def get_english_lessons(unit_title: str):
    return ENGLISH_UNIT_LESSONS.get(unit_title, tuple())


def all_english_lessons():
    return tuple(
        lesson
        for lessons in ENGLISH_UNIT_LESSONS.values()
        for lesson in lessons
    )
