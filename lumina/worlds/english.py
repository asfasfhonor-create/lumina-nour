import streamlit as st

from lumina.ai_service import GeminiService
from lumina.curriculum.catalog import ENGLISH_T1
from lumina.curriculum.grounding import build_grounded_pdf, curriculum_prompt
from lumina.curriculum.english_curriculum import get_english_lessons
from lumina.curriculum.english_reviews import get_review
from lumina.learning.lesson_view import render_verified_unit
from lumina.learning.english_profile import BASELINE_ITEMS, score_baseline


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

    lessons = get_english_lessons(unit_title)
    if lessons:
        unit_number = {
            "Personal Identity": 1,
            "Communication with Family and Friends": 2,
            "Artificial Intelligence": 3,
            "Screen Time": 4,
            "Design Thinking": 5,
            "Why Do We Like Stories?": 6,
        }[unit_title]
        render_verified_unit(
            f"Unit {unit_number} · {unit_title}",
            lessons,
            f"english_u{unit_number}_lesson",
            module_id="english",
        )
    elif unit_title in {"Review 1", "Review 2"}:
        review = get_review(unit_title)
        if review:
            render_verified_unit(
                unit_title,
                (review,),
                f"english_{review.unit_id}_lesson",
                module_id="english",
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
        ["Level Snapshot", "Writing Snapshot", "Real-life Conversation", "Vocabulary in Context"],
        horizontal=False,
        key="real_english_mode",
    )

    if mode == "Level Snapshot":
        _level_snapshot()
    elif mode == "Writing Snapshot":
        _writing_snapshot(ai)
    elif mode == "Real-life Conversation":
        _conversation_mission(ai)
    else:
        _vocabulary_mission(ai)


def _level_snapshot() -> None:
    st.markdown("### Real English · Level Snapshot")
    st.caption(
        "Quick starting-point check only — not a formal CEFR certificate. "
        "It helps LUMINA decide how much support and challenge to use."
    )

    answers = {}
    for item in BASELINE_ITEMS:
        choice = st.radio(
            f"{item['skill']} · {item['prompt']}",
            list(item["options"]),
            index=None,
            key=f"english_baseline_{item['id']}",
        )
        if choice is not None:
            answers[item["id"]] = list(item["options"]).index(choice)

    if st.button("Show my starting point", key="english_baseline_submit"):
        if len(answers) != len(BASELINE_ITEMS):
            st.warning("كمّلي كل الأسئلة الأول عشان الصورة تكون مفيدة.")
            return

        result = score_baseline(answers)
        st.session_state.english_profile = {
            "baseline_correct": result.correct,
            "baseline_total": result.total,
            "broad_band": result.broad_band,
            "support_note": result.note,
        }
        st.success(f"Starting band: {result.broad_band} · {result.correct}/{result.total}")
        st.write(result.note)
        st.info(
            "ده مجرد Starting Point. المستوى الحقيقي هيتحدث من الكتابة، القراءة، "
            "المحادثة، والاستماع مع الوقت — مش من اختبار واحد."
        )

    profile = st.session_state.get("english_profile", {})
    if profile:
        st.caption(
            f"Current Real English profile: {profile.get('broad_band', 'Not set')} · "
            f"baseline {profile.get('baseline_correct', 0)}/{profile.get('baseline_total', 0)}"
        )

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


