from lumina.learning.lesson_models import LessonCheck, LessonData


SCIENCE_T2_U1_L1 = LessonData(
    id="science_t2_u1_l1",
    source_id="science_prep3_t2",
    unit_id="t2_u1",
    title="Chemical Reactions",
    source_pages="Second Term book pages 74–83",
    objectives=(
        "Classify common chemical reactions.",
        "Understand thermal decomposition, substitution, neutralization, oxidation, and reduction.",
        "Use the chemical activity series to predict simple substitution reactions.",
    ),
    key_terms=(
        "thermal decomposition",
        "simple substitution",
        "double substitution",
        "neutralization",
        "oxidation",
        "reduction",
        "chemical activity series",
    ),
    evidence_summary=(
        "Thermal decomposition breaks a compound into simpler substances by heating; the book illustrates several metal compounds that decompose on heating.",
        "In simple substitution, a more active element replaces a less active one; the chemical activity series is used to predict whether substitution can occur.",
        "Double substitution includes reactions such as acid-base neutralization and salt precipitation.",
        "Oxidation and reduction occur together: oxidation involves loss of electrons or gain of oxygen, while reduction involves gain of electrons or loss of oxygen in the book's examples.",
    ),
    checks=(
        LessonCheck(
            id="decomposition",
            prompt="What best describes a thermal decomposition reaction?",
            expected_points=("a compound breaks into simpler substances by heat",),
            hint="Look at the reaction pattern shown with the Δ symbol.",
            options=(
                "A compound breaks into simpler substances when heated.",
                "Two elements always combine into one compound without heat.",
                "A metal only dissolves in water.",
            ),
            correct_index=0,
        ),
        LessonCheck(
            id="substitution",
            prompt="When can one metal substitute another metal in a compound?",
            expected_points=("when it is more active in the chemical activity series",),
            hint="Compare their positions in the chemical activity series.",
            options=(
                "When the substituting metal is more active.",
                "When it is less active.",
                "Activity does not matter.",
            ),
            correct_index=0,
        ),
    ),
)


SCIENCE_T2_U1_L2 = LessonData(
    id="science_t2_u1_l2",
    source_id="science_prep3_t2",
    unit_id="t2_u1",
    title="Rate of the Chemical Reaction",
    source_pages="Second Term book pages 84–93",
    objectives=(
        "Define rate of a chemical reaction.",
        "Interpret change in reactant or product concentration over time.",
        "Explain factors affecting reaction rate.",
        "Recognize the role of catalysts and enzymes.",
    ),
    key_terms=("reaction rate", "concentration", "surface area", "temperature", "catalyst", "enzyme", "nature of reactants"),
    evidence_summary=(
        "The reaction rate describes how quickly reactants are consumed or products are formed over time.",
        "The book relates reaction rate to concentration changes and uses graphs to represent these changes.",
        "Factors increasing reaction rate include suitable reactant nature, greater surface area, greater concentration, higher temperature, and catalysts.",
        "Catalysts change reaction rate without being consumed; enzymes are biological catalysts.",
    ),
    checks=(
        LessonCheck(
            id="surface_area",
            prompt="Why does increasing the surface area of a solid reactant usually increase reaction rate?",
            expected_points=("more particles are exposed for collisions",),
            hint="Compare powder with a single large piece.",
            options=(
                "More reactant particles are exposed for collisions.",
                "It always lowers the temperature.",
                "It removes all reactant particles.",
            ),
            correct_index=0,
        ),
        LessonCheck(
            id="catalyst",
            prompt="What is a catalyst?",
            expected_points=("a substance that changes reaction rate without being consumed",),
            hint="The catalyst remains after the reaction.",
            options=(
                "A substance that changes reaction rate without being consumed.",
                "A product that must disappear completely.",
                "A substance that always stops every reaction.",
            ),
            correct_index=0,
        ),
    ),
)


SCIENCE_T2_UNIT1_LESSONS = (
    SCIENCE_T2_U1_L1,
    SCIENCE_T2_U1_L2,
)
