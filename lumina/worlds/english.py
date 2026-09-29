import streamlit as st

from lumina.ai_service import GeminiService
from lumina.curriculum.catalog import ENGLISH_T1
from lumina.curriculum.grounding import build_grounded_pdf, curriculum_prompt
from lumina.curriculum.english_unit1 import UNIT1_LESSONS
from lumina.curriculum.english_unit2 import UNIT2_LESSONS
from lumina.curriculum.english_unit3 import UNIT3_LESSONS
from lumina.learning.progress import derive_mastery, mastery_label
from lumina.learning.progress_view import render_learning_brain_summary
from lumina.session_state import (
    complete_review,
    get_learning_attempts,
    get_mistakes,
    get_reviews,
    queue_review,
    record_learning_attempt,
    record_mistake,
    resolve_mistake,
)


def render_english_world(ai: GeminiService) -> None:
    st.markdown('<div class="section-title">🇬🇧 English Adventure</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="mission"><b>Two tracks, one goal: stronger English.</b><br>'
        '<span class="muted">School English follows Nour\'s curriculum. Real English grows her actual language level beyond the school grade.</span></div>',
        unsafe_allow_html=True,
    )

    school_tab, real_tab = st.tabs(["📘 School English", "🚀 Real English"])

    with school_tab:
        _render_school_track(ai)

    with real_tab:
        _render_real_english(ai)


def _render_school_track(ai: GeminiService) -> None:
    source = ENGLISH_T1
    st.markdown(
        '<div class="track-card"><b>School English · Curriculum Grounded</b><br>'
        '<span class="muted">The school track uses the trusted curriculum source and refuses to invent missing curriculum content.</span></div>',
        unsafe_allow_html=True,
    )

    st.caption(f"Trusted source: {source.display_name}")
    unit_title = st.selectbox(
        "Choose unit / review",
        [unit.title for unit in source.units],
        key="school_english_unit",
    )

    st.markdown("**Source map**")
    for unit in source.units:
        prefix = "→" if unit.title == unit_title else "•"
        st.write(f"{prefix} {unit.title}")

    if unit_title == "Personal Identity":
        _render_verified_unit("Unit 1 · Personal Identity", UNIT1_LESSONS, "english_u1_lesson")
    elif unit_title == "Communication with Family and Friends":
        _render_verified_unit(
            "Unit 2 · Communication with Family and Friends",
            UNIT2_LESSONS,
            "english_u2_lesson",
        )
    elif unit_title == "Artificial Intelligence":
        _render_verified_unit(
            "Unit 3 · Artificial Intelligence",
            UNIT3_LESSONS,
            "english_u3_lesson",
        )

    st.markdown("---")
    st.caption("Advanced source session")
    uploaded = st.file_uploader(
        "Load the trusted school English book for this session",
        type=["pdf"],
        key="school_english_source_pdf",
        help=(
            "Optional advanced source session until permanent document storage is connected. "
            f"Expected source: {source.filename}"
        ),
    )

    if uploaded:
        if uploaded.name != source.filename:
            st.warning(
                "The filename is different from the inventoried trusted source. "
                "LUMINA will treat it as temporary material and will not silently promote it to the trusted curriculum library."
            )

        grounded = build_grounded_pdf(source, uploaded.read())
        question = st.text_input(
            "Ask anything from the loaded book",
            key="school_english_question",
            placeholder="Explain the main idea, vocabulary, grammar, or give me a short practice...",
        )

        if st.button("Teach me from the book", key="school_english_teach") and question and _need_ai(ai):
            prompt = curriculum_prompt(source, question, unit_title=unit_title)
            with st.spinner("Reading the trusted school source..."):
                st.markdown(ai.generate([grounded.part, prompt]))


def _render_real_english(ai: GeminiService) -> None:
    st.markdown(
        '<div class="track-card"><b>Real English</b><br>'
        '<span class="muted">Practice real communication, get focused feedback, and gradually reduce Arabic help as Nour improves.</span></div>',
        unsafe_allow_html=True,
    )

    mode = st.radio(
        "Choose a mission",
        ["Writing Snapshot", "Real-life Conversation", "Vocabulary in Context"],
        horizontal=False,
        key="real_english_mode",
    )

    if mode == "Writing Snapshot":
        _writing_snapshot(ai)
    elif mode == "Real-life Conversation":
        _conversation_mission(ai)
    else:
        _vocabulary_mission(ai)


def _need_ai(ai: GeminiService) -> bool:
    if not ai.available:
        st.warning("Gemini API Key is required for this mission.")
        return False
    return True


def _writing_snapshot(ai: GeminiService) -> None:
    st.caption("This is a learning snapshot, not a formal CEFR certificate.")
    writing = st.text_area(
        "Write 4–6 sentences about yourself, your day, or something you like.",
        key="english_world_writing",
        placeholder="My name is Nour. I like...",
    )
    if st.button("Check my English", key="english_world_check") and writing and _need_ai(ai):
        prompt = f"""You are Nour's English coach. She is an Egyptian third-prep language-school student, but this track is designed to improve her English beyond her school grade.

Her writing:
{writing}

Give a short, encouraging diagnostic snapshot:
1. Natural corrected version preserving her meaning.
2. Two strengths only if genuinely visible.
3. The single most important improvement point.
4. One useful expression at a slightly higher level, with a simple example.
5. One tiny follow-up writing challenge.
6. Give a cautious approximate CEFR-style writing band only if there is enough evidence; otherwise say there is not enough evidence yet.

Use English first. Use brief Arabic only when it helps understanding. Do not overwhelm her."""
        st.markdown(ai.generate(prompt))


def _conversation_mission(ai: GeminiService) -> None:
    situation = st.selectbox(
        "Situation",
        [
            "Ordering food",
            "Introducing yourself to a new friend",
            "Asking for help in a shop",
            "Talking about a movie or story",
        ],
        key="english_world_situation",
    )
    answer = st.text_area(
        "Your reply in English",
        key="english_world_conversation",
        placeholder="Write what you would say...",
    )

    if st.button("Continue the conversation", key="english_world_conversation_go") and _need_ai(ai):
        prompt = f"""Act as a friendly English conversation partner for Nour.
Situation: {situation}
Nour's reply: {answer if answer else "[no reply yet]"}

Rules:
- Keep the conversation realistic and age-appropriate.
- If she has not replied, start with one short line and ask her to answer.
- If she replied, respond naturally, correct only one important issue, then ask the next short question.
- Do not turn this into a grammar lecture.
- Keep most of the response in English; use one brief Arabic hint only if needed."""
        st.markdown(ai.generate(prompt))


def _vocabulary_mission(ai: GeminiService) -> None:
    topic = st.selectbox(
        "Topic",
        ["Daily life", "Friends", "Technology", "Stories", "Travel", "School"],
        key="english_world_vocab_topic",
    )
    if st.button("Give me a vocabulary mission", key="english_world_vocab_go") and _need_ai(ai):
        prompt = f"""Create a tiny vocabulary mission for Nour about: {topic}.
She is improving real English beyond her school grade.

Include exactly:
- 3 useful words/expressions in context, not isolated translation lists.
- one very short example for each;
- one mini challenge that makes her use at least two of them;
- brief Arabic support only for difficult meaning.
Keep it concise and practical."""
        st.markdown(ai.generate(prompt))


def _render_verified_unit(title: str, lessons, select_key: str) -> None:
    st.markdown(f"### {title}")
    st.caption("Verified from the supplied English curriculum source.")
    render_learning_brain_summary([lesson.id for lesson in lessons])

    lesson = st.selectbox(
        "Choose lesson",
        lessons,
        format_func=lambda item: item.title,
        key=select_key,
    )
    _render_verified_lesson(lesson)


def _render_verified_lesson(lesson) -> None:
    st.markdown(f"### {lesson.title}")
    st.caption(f"Verified curriculum extract · {lesson.source_pages}")

    with st.expander("What you will learn", expanded=True):
        for objective in lesson.objectives:
            st.write(f"• {objective}")

    st.markdown("**Key words / language**")
    st.write(" · ".join(lesson.key_terms))

    st.markdown("**Core ideas from the lesson**")
    for point in lesson.evidence_summary:
        st.write(f"• {point}")

    check = lesson.checks[0]
    st.markdown("#### Quick understanding check")
    answer = st.radio(
        check.prompt,
        list(check.options),
        index=None,
        key=f"lesson_check_{lesson.id}_{check.id}",
    )

    if st.button("Check my thinking", key=f"lesson_check_button_{lesson.id}_{check.id}") and answer:
        selected_index = list(check.options).index(answer)
        correct = selected_index == check.correct_index
        attempt = {
            "module_id": "english",
            "unit_id": lesson.unit_id,
            "lesson_id": lesson.id,
            "check_id": check.id,
            "evidence_id": check.id,
            "answer": answer,
            "correct": correct,
            "source_pages": lesson.source_pages,
        }
        record_learning_attempt(attempt)

        if correct:
            resolve_mistake(lesson.id, check.id)
            complete_review(lesson.id, check.id)
            st.success("Good thinking — this matches the lesson.")
            st.info(
                "This is learning evidence, not automatic mastery. "
                "LUMINA requires varied evidence before a lesson can become Mastered."
            )
        else:
            record_mistake(
                {
                    "module_id": "english",
                    "unit_id": lesson.unit_id,
                    "lesson_id": lesson.id,
                    "lesson_title": lesson.title,
                    "check_id": check.id,
                    "question": check.prompt,
                    "answer": answer,
                    "mistake_type": "concept_understanding",
                    "hint": check.hint,
                    "source_pages": lesson.source_pages,
                    "resolved": False,
                }
            )
            queue_review(
                {
                    "module_id": "english",
                    "lesson_id": lesson.id,
                    "lesson_title": lesson.title,
                    "check_id": check.id,
                    "status": "due",
                    "reason": "incorrect_understanding_check",
                    "source_pages": lesson.source_pages,
                }
            )
            st.warning("Not yet. Use the hint, then try again.")
            st.info(f"Hint: {check.hint}")

    attempts = get_learning_attempts(lesson.id)
    mistakes = get_mistakes(lesson.id)
    mastery = derive_mastery(attempts, mistakes)
    st.caption(
        f"Mastery: {mastery_label(mastery.state)} · "
        f"{mastery.correct_attempts}/{mastery.attempts} successful attempt(s) · "
        f"{mastery.unresolved_mistakes} unresolved mistake(s)"
    )

    due_reviews = [
        review
        for review in get_reviews("due")
        if review.get("lesson_id") == lesson.id
    ]
    if due_reviews:
        st.warning("Review due: this lesson has something worth revisiting before moving on.")
