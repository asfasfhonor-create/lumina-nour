from lumina.learning.lesson_models import LessonCheck, LessonData


SCIENCE_U2_L1 = LessonData(
    id="science_u2_l1",
    source_id="science_prep3_t1",
    unit_id="u2",
    title="Mirrors",
    source_pages="Book pages 24–31",
    objectives=(
        "Explain reflection of light and the two laws of reflection.",
        "Identify the properties of images formed by a plane mirror.",
        "Distinguish concave and convex spherical mirrors.",
        "Understand focal length, image formation, and common uses of spherical mirrors.",
    ),
    key_terms=(
        "reflection of light",
        "angle of incidence",
        "angle of reflection",
        "plane mirror",
        "concave mirror",
        "convex mirror",
        "focus",
        "focal length",
        "radius of curvature",
    ),
    evidence_summary=(
        "A plane mirror forms an image that is upright, equal in size to the object, laterally inverted, virtual, and as far behind the mirror as the object is in front.",
        "The laws of reflection state that the angle of incidence equals the angle of reflection, and the incident ray, reflected ray, and normal lie in the same plane.",
        "Spherical mirrors are concave (converging) or convex (diverging), with concepts including pole, centre of curvature, radius, principal axis, and focus.",
        "For a concave mirror, focal length equals half the radius of curvature.",
        "Image properties in a concave mirror change with object position, while a convex mirror forms a virtual, upright, diminished image.",
    ),
    checks=(
        LessonCheck(
            id="reflection_law",
            prompt="Which statement is one of the laws of reflection?",
            expected_points=("angle of incidence equals angle of reflection",),
            hint="Compare the two angles measured from the normal.",
            options=(
                "The angle of incidence equals the angle of reflection.",
                "The angle of incidence is always twice the angle of reflection.",
                "The reflected ray always travels along the mirror surface.",
            ),
            correct_index=0,
        ),
        LessonCheck(
            id="plane_mirror",
            prompt="Which property belongs to an image formed by a plane mirror?",
            expected_points=("virtual upright equal size laterally inverted",),
            hint="Think about the image you see in an ordinary mirror.",
            options=(
                "Real, inverted, and always smaller.",
                "Virtual, upright, equal in size, and laterally inverted.",
                "Real, upright, and projected on a screen.",
            ),
            correct_index=1,
        ),
    ),
)


SCIENCE_U2_L2 = LessonData(
    id="science_u2_l2",
    source_id="science_prep3_t1",
    unit_id="u2",
    title="Lenses",
    source_pages="Book pages 32–39",
    objectives=(
        "Distinguish convex and concave lenses.",
        "Understand the optical centre, principal axis, focus, and focal length of a lens.",
        "Predict basic image properties for convex and concave lenses.",
        "Explain how lenses are used to correct short-sightedness and long-sightedness.",
    ),
    key_terms=(
        "lens",
        "convex lens",
        "concave lens",
        "optical centre",
        "principal axis",
        "focus",
        "focal length",
        "short-sightedness",
        "long-sightedness",
    ),
    evidence_summary=(
        "A convex lens is thicker at the centre and converges light rays, while a concave lens is thinner at the centre and diverges light rays.",
        "The lesson defines optical centre, centres/radii of curvature, principal axis, focus, and focal length.",
        "For a convex lens, image properties depend on object position; a concave lens forms a virtual, upright, diminished image.",
        "Short-sightedness is corrected with a concave lens, while long-sightedness is corrected with a convex lens.",
    ),
    checks=(
        LessonCheck(
            id="lens_type",
            prompt="Which statement correctly distinguishes a convex lens from a concave lens?",
            expected_points=("convex converges and concave diverges",),
            hint="Think about what parallel rays do after passing through each lens.",
            options=(
                "A convex lens converges light rays, while a concave lens diverges them.",
                "Both types always converge light rays.",
                "A concave lens converges and a convex lens diverges.",
            ),
            correct_index=0,
        ),
        LessonCheck(
            id="vision_correction",
            prompt="Which pairing matches the lesson's correction of vision defects?",
            expected_points=("short sight concave, long sight convex",),
            hint="The correction lens changes where the image forms relative to the retina.",
            options=(
                "Short-sightedness → convex; long-sightedness → concave",
                "Short-sightedness → concave; long-sightedness → convex",
                "Both are corrected only with plane mirrors",
            ),
            correct_index=1,
        ),
    ),
)


SCIENCE_UNIT2_LESSONS = (
    SCIENCE_U2_L1,
    SCIENCE_U2_L2,
)
