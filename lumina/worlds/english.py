import streamlit as st

from lumina.context_help import render_context_help

from lumina.ai_service import GeminiService
from lumina.curriculum.catalog import ENGLISH_T1
from lumina.curriculum.english_curriculum import get_english_lessons
from lumina.curriculum.english_reviews import get_review
from lumina.curriculum.source_session import render_temporary_source_session
from lumina.learning.lesson_view import render_verified_unit
from lumina.learning.english_profile import (
    BASELINE_ITEMS,
    score_baseline,
    support_instruction,
    recommended_focus,
)
from lumina.persistence.profile_state import persist_profile_state
from lumina.persistence.session_store import get_learning_store


def _record_real_english_evidence(
    *,
    skill: str,
    activity_type: str,
    answer: str,
    correct: bool | None,
) -> None:
    store = get_learning_store()
    lesson_id = f"real_english_{skill.lower().replace('/', '_').replace(' ', '_')}"
    store.record_attempt(
        {
            "module_id": "english",
            "unit_id": "real_english",
            "lesson_id": lesson_id,
            "check_id": activity_type,
            "evidence_id": activity_type,
            "answer": answer,
            "correct": correct,
            "source_pages": "Real English",
            "activity_type": activity_type,
        }
    )

    profile = dict(st.session_state.get("english_profile") or {})
    evidence = dict(profile.get("activity_evidence") or {})
    item = dict(evidence.get(skill) or {"attempts": 0, "correct": 0, "completed": 0})
    item["attempts"] = int(item.get("attempts", 0)) + 1
    item["completed"] = int(item.get("completed", 0)) + 1
    if correct is True:
        item["correct"] = int(item.get("correct", 0)) + 1
    evidence[skill] = item
    profile["activity_evidence"] = evidence
    st.session_state.english_profile = profile
    persist_profile_state()


def render_english_world(ai: GeminiService) -> None:
    st.markdown('<div class="section-title">🇬🇧 مغامرة الإنجليزي · English Adventure</div>', unsafe_allow_html=True)
    render_context_help("english", label="💬 قوليلي العالم ده بيعمل إيه")
    st.markdown(
        '<div class="mission"><b>مساران، وهدف واحد: English أقوى.</b><br>'
        '<span class="muted">منهج المدرسة يمشي مع كتاب نور، وReal English يطوّر استخدامها الحقيقي للغة أبعد من حدود المنهج.</span></div>',
        unsafe_allow_html=True,
    )

    school_tab, real_tab = st.tabs(["📘 منهج المدرسة", "🚀 Real English"])

    with school_tab:
        _render_school_track(ai)

    with real_tab:
        _render_real_english(ai)


def _render_school_track(ai: GeminiService) -> None:
    source = ENGLISH_T1
    st.markdown(
        '<div class="track-card"><b>منهج المدرسة · School English</b><br>'
        '<span class="muted">المسار المدرسي يعتمد على المصدر المعتمد، وما يضيفش محتوى منهجي غير موجود.</span></div>',
        unsafe_allow_html=True,
    )

    st.caption(f"المصدر: {source.display_name}")
    unit_title = st.selectbox(
        "اختاري الوحدة أو المراجعة",
        [unit.title for unit in source.units],
        key="school_english_unit",
    )

    st.markdown("**خريطة الوحدات**")
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
            ai=ai,
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

    render_temporary_source_session(
        ai,
        source,
        section_title=unit_title,
        key_prefix="english_source_session",
    )


def _render_real_english(ai: GeminiService) -> None:
    st.markdown(
        '<div class="track-card"><b>Real English</b><br>'
        '<span class="muted">تدريب عملي على التواصل، مع ملاحظات قصيرة وتقليل المساعدة بالعربي تدريجيًا مع تحسن المستوى.</span></div>',
        unsafe_allow_html=True,
    )

    profile = st.session_state.get("english_profile", {})
    focus_label, focus_reason = recommended_focus(profile)
    st.info(f"🎯 اقتراح LUMINA النهارده: **{focus_label}** — {focus_reason}")

    mode = st.radio(
        "اختاري تدريب",
        [
            "تحديد نقطة البداية",
            "قراءة وفهم",
            "كتابة قصيرة",
            "محادثة واقعية",
            "كلمات في سياق",
        ],
        horizontal=False,
        key="real_english_mode",
    )

    if mode == "تحديد نقطة البداية":
        _level_snapshot()
    elif mode == "قراءة وفهم":
        _reading_mission()
    elif mode == "كتابة قصيرة":
        _writing_snapshot(ai)
    elif mode == "محادثة واقعية":
        _conversation_mission(ai)
    else:
        _vocabulary_mission(ai)


def _level_snapshot() -> None:
    st.markdown("### Real English · نقطة البداية")
    st.caption(
        "اختبار بداية سريع فقط، مش شهادة مستوى رسمية. "
        "بيساعد LUMINA يحدد قد إيه تحتاجي مساعدة وقد إيه نزوّد التحدي."
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

    if st.button("اعرضي نقطة البداية", key="english_baseline_submit"):
        if len(answers) != len(BASELINE_ITEMS):
            st.warning("كمّلي كل الأسئلة الأول عشان الصورة تكون مفيدة.")
            return

        result = score_baseline(answers)
        st.session_state.english_profile = {
            "baseline_correct": result.correct,
            "baseline_total": result.total,
            "broad_band": result.broad_band,
            "support_note": result.note,
            "skill_scores": result.skill_scores,
        }
        persist_profile_state()
        st.success(f"نقطة البداية: {result.broad_band} · {result.correct}/{result.total}")
        st.write(result.note)
        st.info(
            "دي مجرد نقطة بداية. المستوى الحقيقي هيتحدث من الكتابة، القراءة، "
            "المحادثة، والاستماع مع الوقت — مش من اختبار واحد."
        )

    profile = st.session_state.get("english_profile", {})
    if profile:
        st.caption(
            f"مستوى Real English الحالي: {profile.get('broad_band', 'لسه متحددش')} · "
            f"اختبار البداية {profile.get('baseline_correct', 0)}/{profile.get('baseline_total', 0)}"
        )
        skill_scores = profile.get("skill_scores") or {}
        if skill_scores:
            st.markdown("**صورة مبدئية للمهارات**")
            for skill, values in skill_scores.items():
                st.write(f"• {skill}: {values.get('correct', 0)}/{values.get('total', 0)}")

def _reading_mission() -> None:
    st.markdown("### 📖 Reading Detective")
    st.caption("قصة قصيرة، سؤال واحد، واستنتاج من المعنى — مش حفظ كلمات.")

    passage = (
        "Nora joined a school club because she wanted to become more confident. "
        "At first, she rarely spoke during meetings. After a few weeks, she started "
        "sharing one idea each time. Her friends listened and encouraged her."
    )
    st.info(passage)

    answer = st.radio(
        "What changed about Nora?",
        [
            "She became more willing to share her ideas.",
            "She stopped attending the club.",
            "She decided she disliked her friends.",
        ],
        index=None,
        key="real_english_reading_answer",
    )

    if st.button("Check my idea", key="real_english_reading_check", use_container_width=True):
        if answer is None:
            st.warning("اختاري إجابة الأول.")
            return
        correct = answer.startswith("She became")
        _record_real_english_evidence(
            skill="Reading",
            activity_type="real_english_reading_inference",
            answer=answer,
            correct=correct,
        )
        if correct:
            st.success("Exactly 👏 You used the story to infer the change in her confidence.")
            st.caption("Inference = نفهم معنى غير مكتوب حرفيًا لكن الدليل في القصة بيوصّل له.")
        else:
            st.warning("Look again at what she did at first, then what she started doing after a few weeks.")


def _need_ai(ai: GeminiService) -> bool:
    if not ai.available:
        st.warning("التدريب الذكي ده مش مفعّل حاليًا. باقي Real English شغال عادي.")
        return False
    return True


def _writing_snapshot(ai: GeminiService) -> None:
    st.caption("ده تدريب لتحديد المستوى، مش شهادة CEFR رسمية.")
    writing = st.text_area(
        "اكتبي 4–6 جمل بالإنجليزي عن نفسك أو يومك أو حاجة بتحبيها.",
        key="english_world_writing",
        placeholder="My name is Nour. I like...",
    )
    if st.button("راجعي كتابتي", key="english_world_check") and writing and _need_ai(ai):
        profile = st.session_state.get("english_profile", {})
        support = support_instruction(profile)
        prompt = f"""You are Nour's English coach. This track is designed to improve her real English beyond her school grade.
Adaptive support rule: {support}

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
        response = ai.generate(prompt)
        st.markdown(response)
        _record_real_english_evidence(
            skill="Writing",
            activity_type="real_english_writing_practice",
            answer=writing,
            correct=None,
        )


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
        profile = st.session_state.get("english_profile", {})
        support = support_instruction(profile)
        prompt = f"""Act as a friendly English conversation partner for Nour.
Adaptive support rule: {support}
Situation: {situation}
Nour's reply: {answer if answer else "[no reply yet]"}

Rules:
- Keep the conversation realistic and age-appropriate.
- If she has not replied, start with one short line and ask her to answer.
- If she replied, respond naturally, correct only one important issue, then ask the next short question.
- Do not turn this into a grammar lecture.
- Keep most of the response in English; use one brief Arabic hint only if needed."""
        response = ai.generate(prompt)
        st.markdown(response)
        _record_real_english_evidence(
            skill="Speaking/Use",
            activity_type="real_english_conversation_practice",
            answer=answer if answer else "[started conversation]",
            correct=None,
        )


def _vocabulary_mission(ai: GeminiService) -> None:
    topic = st.selectbox(
        "اختاري موضوع",
        ["Daily life", "Friends", "Technology", "Stories", "Travel", "School"],
        key="english_world_vocab_topic",
    )
    if st.button("ابدئي تحدّي الكلمات", key="english_world_vocab_go") and _need_ai(ai):
        profile = st.session_state.get("english_profile", {})
        support = support_instruction(profile)
        prompt = f"""Create a tiny vocabulary mission for Nour about: {topic}.
She is improving real English beyond her school grade.
Adaptive support rule: {support}

Include exactly:
- 3 useful words/expressions in context, not isolated translation lists.
- one very short example for each;
- one mini challenge that makes her use at least two of them;
- brief Arabic support only for difficult meaning.
Keep it concise and practical."""
        response = ai.generate(prompt)
        st.markdown(response)
        _record_real_english_evidence(
            skill="Vocabulary",
            activity_type="real_english_vocabulary_practice",
            answer=topic,
            correct=None,
        )


