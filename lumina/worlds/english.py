import streamlit as st

from lumina.ai_service import GeminiService


def render_english_world(ai: GeminiService) -> None:
    st.markdown('<div class="section-title">🇬🇧 English Adventure</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="mission"><b>Two tracks, one goal: stronger English.</b><br>'
        '<span class="muted">School English follows Nour\'s curriculum. Real English grows her actual language level beyond the school grade.</span></div>',
        unsafe_allow_html=True,
    )

    school_tab, real_tab = st.tabs(["📘 School English", "🚀 Real English"])

    with school_tab:
        _render_school_track()

    with real_tab:
        _render_real_english(ai)


def _render_school_track() -> None:
    st.markdown(
        '<div class="track-card"><b>School English</b><br>'
        '<span class="muted">This track will be connected to Nour\'s indexed curriculum source before it is allowed to answer curriculum questions. '
        'We will not pretend generic AI knowledge is the school book.</span></div>',
        unsafe_allow_html=True,
    )
    st.info("Curriculum-grounded School English is waiting for the curriculum retrieval layer. The source book is already inventoried.")


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
