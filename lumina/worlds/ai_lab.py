import streamlit as st

from lumina.ai_service import AIServiceError, GeminiService
from lumina.learning.rewards import apply_success_reward
from lumina.persistence.session_store import get_learning_store
from lumina.persistence.profile_state import persist_profile_state


AI_MODULE = "ai"
AI_UNIT = "ai_literacy"

AI_SKILL_LABELS = {
    "prompting": "Prompting",
    "comparison": "Comparing Answers",
    "verification": "Verification",
    "evidence": "Evidence Quality",
    "uncertainty": "Handling Uncertainty",
}

ACTIVITY_SKILL = {
    "ai_prompt_design": "prompting",
    "ai_answer_comparison": "comparison",
    "ai_evidence_verification": "evidence",
    "ai_detective": "uncertainty",
}


def _update_ai_profile(activity_type: str, correct: bool) -> None:
    skill = ACTIVITY_SKILL.get(activity_type)
    if not skill:
        return

    profile = dict(st.session_state.get("ai_profile") or {})
    skills = dict(profile.get("skills") or {})
    item = dict(skills.get(skill) or {"correct": 0, "attempts": 0})
    item["attempts"] = int(item.get("attempts", 0)) + 1
    if correct:
        item["correct"] = int(item.get("correct", 0)) + 1
    skills[skill] = item
    profile["skills"] = skills
    profile["completed_skills"] = sum(
        1 for values in skills.values()
        if int(values.get("correct", 0)) >= 1
    )
    st.session_state.ai_profile = profile
    persist_profile_state()


def _record_ai_attempt(
    *,
    lesson_id: str,
    check_id: str,
    answer: str,
    correct: bool,
    activity_type: str,
) -> int:
    store = get_learning_store()
    store.record_attempt(
        {
            "module_id": AI_MODULE,
            "unit_id": AI_UNIT,
            "lesson_id": lesson_id,
            "check_id": check_id,
            "evidence_id": check_id,
            "answer": answer,
            "correct": correct,
            "source_pages": "LUMINA AI Literacy",
            "activity_type": activity_type,
        }
    )
    _update_ai_profile(activity_type, correct)

    if correct:
        store.resolve_mistake(lesson_id, check_id)
        store.complete_review(lesson_id, check_id)
        return apply_success_reward(
            module_id=AI_MODULE,
            lesson_id=lesson_id,
            evidence_id=check_id,
            activity_type=activity_type,
        )

    store.record_mistake(
        {
            "module_id": AI_MODULE,
            "unit_id": AI_UNIT,
            "lesson_id": lesson_id,
            "lesson_title": lesson_id.replace("_", " ").title(),
            "check_id": check_id,
            "question": check_id,
            "answer": answer,
            "mistake_type": "ai_literacy",
            "hint": "فكري في الهدف، الدليل، والمصدر قبل اختيار الإجابة.",
            "source_pages": "LUMINA AI Literacy",
            "resolved": False,
        }
    )
    store.queue_review(
        {
            "module_id": AI_MODULE,
            "lesson_id": lesson_id,
            "lesson_title": lesson_id.replace("_", " ").title(),
            "check_id": check_id,
            "status": "due",
            "reason": "ai_literacy_retry",
            "source_pages": "LUMINA AI Literacy",
        }
    )
    return 0


def _success(message: str, xp: int) -> None:
    st.success(message)
    if xp:
        st.caption(f"+{xp} XP لأنك أثبتّي مهارة AI جديدة.")


def render_ai_world(ai: GeminiService) -> None:
    st.markdown('<div class="section-title">🤖 عالم الذكاء الاصطناعي</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="mission"><b>جرّبي → تحققي → قارني → استنتجي</b><br>'
        '<span class="muted">هنا نور تتعلم تستخدم AI بعقلها: تسأل أحسن، تراجع الإجابات، وتختبر الدليل بدل ما تصدق الكلام لمجرد إنه مكتوب بثقة.</span></div>',
        unsafe_allow_html=True,
    )

    st.caption(
        "ابدئي من أي تحدّي يعجبك. كل مهمة قصيرة، والغلط فيها تدريب مش عقوبة."
    )

    mode = st.radio(
        "اختاري تحدّي",
        [
            "🛠️ صلّحي الـPrompt",
            "⚖️ قارني إجابتين من AI",
            "🔎 تحققي بالدليل",
            "✍️ اكتبي Prompt من الصفر",
            "🕵️ محقق الذكاء الاصطناعي",
            "🧭 ابني خطة تحقق",
        ],
        key="ai_lab_mode",
    )

    if mode == "🛠️ صلّحي الـPrompt":
        _fix_the_prompt(ai)
    elif mode == "⚖️ قارني إجابتين من AI":
        _compare_ai_answers()
    elif mode == "🔎 تحققي بالدليل":
        _verify_with_evidence()
    elif mode == "✍️ اكتبي Prompt من الصفر":
        _prompt_challenge(ai)
    elif mode == "🕵️ محقق الذكاء الاصطناعي":
        _ai_detective(ai)
    else:
        _fact_checker(ai)


def _need_ai(ai: GeminiService) -> bool:
    if not ai.available:
        st.warning("الجزء الذكي ده مش متاح دلوقتي، لكن تقدري تكمّلي التحديات اللي مش محتاجة اتصال AI.")
        return False
    return True


def _fix_the_prompt(ai: GeminiService) -> None:
    st.markdown("### 🛠️ صلّحي الـPrompt")
    st.write("الـPrompt الضعيف:")
    st.code("اشرح photosynthesis", language=None)
    st.caption("المهمة: خليه أوضح بحيث الـAI يعرف **لمين بيشرح، وبأي طريقة، وإيه المطلوب بعد الشرح**.")

    improved = st.text_area(
        "اكتبي النسخة الأحسن",
        placeholder=(
            "مثال للفكرة فقط: حددي الموضوع، المستوى، طريقة الشرح، المثال، "
            "وإزاي تتأكدي إنك فهمتي."
        ),
        key="ai_fix_prompt_text",
    )

    if st.button("اختبر الـPrompt بتاعي", key="ai_fix_prompt_check", use_container_width=True):
        text = improved.strip().lower()
        signals = {
            "الموضوع": "photosynthesis" in text,
            "المستوى / الجمهور": any(token in text for token in ("14", "student", "طالبة", "prep", "سنة")),
            "طريقة الشرح": any(token in text for token in ("simple", "بسيط", "step", "خطوة", "arabic", "عربي")),
            "مثال": any(token in text for token in ("example", "مثال")),
            "تأكد من الفهم": any(token in text for token in ("question", "سؤال", "check", "اختبر")),
        }
        score = sum(signals.values())
        for label, ok in signals.items():
            st.write(("✅ " if ok else "⬜ ") + label)

        if score >= 4:
            xp = _record_ai_attempt(
                lesson_id="fix_the_prompt",
                check_id="prompt_rubric",
                answer=improved,
                correct=True,
                activity_type="ai_prompt_design",
            )
            _success("ممتاز — الـPrompt بقى محدد ومفيد، مش مجرد طلب عام.", xp)
        else:
            _record_ai_attempt(
                lesson_id="fix_the_prompt",
                check_id="prompt_rubric",
                answer=improved or "empty",
                correct=False,
                activity_type="ai_prompt_design",
            )
            st.info("كويس كبداية. زوّدي العناصر الناقصة واحدة واحدة بدل ما نكتب Prompt طويل مرة واحدة.")

    if improved.strip() and ai.available:
        if st.button("👀 ورّيني الفرق بين النتيجتين", key="ai_fix_prompt_compare", use_container_width=True):
            try:
                weak = ai.generate(
                    "Explain photosynthesis briefly to a school student."
                )
                strong = ai.generate(improved)
                st.markdown("#### نتيجة الـPrompt الضعيف")
                st.markdown(weak)
                st.markdown("#### نتيجة الـPrompt المحسّن")
                st.markdown(strong)
                st.caption("قارني: هل النسخة الثانية أقرب فعلًا لهدفك؟ الفكرة إن جودة الـPrompt تساعد، لكنها لا تضمن صحة كل معلومة.")
            except AIServiceError as exc:
                st.warning(str(exc))


def _compare_ai_answers() -> None:
    st.markdown("### ⚖️ قارني إجابتين من AI")
    st.write("السؤال: **لو AI مش متأكد من معلومة، يعمل إيه؟**")

    with st.container(border=True):
        st.markdown("**الإجابة A**")
        st.write("يكتب أقرب إجابة تبدو منطقية وبثقة، لأن المهم إنه يجاوب بسرعة.")

    with st.container(border=True):
        st.markdown("**الإجابة B**")
        st.write("يوضح إنه غير متأكد، يحدد الجزء المحتاج تحقق، ويقترح الرجوع لمصدر مناسب قبل الاعتماد على الإجابة.")

    choice = st.radio(
        "مين الإجابة الأفضل؟",
        ["A", "B"],
        index=None,
        key="ai_compare_choice",
    )
    reason = st.radio(
        "إيه أهم سبب؟",
        [
            "لأنها أطول.",
            "لأنها بتعترف بعدم اليقين وبتطلب دليل قبل الاعتماد.",
            "لأن أي إجابة فيها كلمة مصدر تبقى صحيحة.",
        ],
        index=None,
        key="ai_compare_reason",
    )

    if st.button("أكشف النتيجة", key="ai_compare_check", use_container_width=True):
        if choice is None or reason is None:
            st.warning("اختاري الإجابة والسبب الأول.")
            return
        correct = choice == "B" and reason.startswith("لأنها بتعترف")
        xp = _record_ai_attempt(
            lesson_id="compare_ai_answers",
            check_id="uncertainty_quality",
            answer=f"{choice} | {reason}",
            correct=correct,
            activity_type="ai_answer_comparison",
        )
        if correct:
            _success("بالضبط. الإجابة الأفضل مش الأكثر ثقة؛ الأفضل هي اللي تفرق بين المعرفة وعدم اليقين وتطلب دليل عند الحاجة.", xp)
        else:
            st.warning("جربي تاني: ركزي على **الثقة مقابل الدليل**، مش طول الإجابة أو شكلها.")


def _verify_with_evidence() -> None:
    st.markdown("### 🔎 تحققي بالدليل")
    st.write(
        "سيناريو تدريبي: AI قال إن **مكتبة المدرسة بتقفل الساعة 4:00 مساءً اليوم**. "
        "قدامك 3 أدلة. مين الأقوى؟"
    )

    with st.container(border=True):
        st.markdown("**الدليل 1 — إعلان رسمي حديث من إدارة المدرسة**")
        st.write("«اليوم تغلق المكتبة الساعة 3:30 مساءً بسبب اجتماع العاملين.»")

    with st.container(border=True):
        st.markdown("**الدليل 2 — رسالة في جروب طلاب**")
        st.write("«أنا فاكر إنها بتقفل 4 تقريبًا.»")

    with st.container(border=True):
        st.markdown("**الدليل 3 — بوستر من السنة اللي فاتت**")
        st.write("«مواعيد المكتبة: حتى 4:00 مساءً.»")

    evidence = st.radio(
        "أي دليل تعتمدِي عليه أولًا؟",
        [
            "الإعلان الرسمي الحديث",
            "رسالة جروب الطلاب",
            "البوستر القديم",
        ],
        index=None,
        key="ai_evidence_source",
    )
    conclusion = st.radio(
        "إذن نعمل إيه مع إجابة الـAI؟",
        [
            "نصدق AI لأنه قالها بثقة.",
            "نصححها إلى 3:30 لأن الدليل الرسمي الحديث أقوى في السيناريو.",
            "نختار 4:00 لأن مصدرين قالوا رقم قريب منه.",
        ],
        index=None,
        key="ai_evidence_conclusion",
    )

    if st.button("تحققي من الاستنتاج", key="ai_evidence_check", use_container_width=True):
        if evidence is None or conclusion is None:
            st.warning("اختاري الدليل والاستنتاج الأول.")
            return
        correct = (
            evidence == "الإعلان الرسمي الحديث"
            and conclusion.startswith("نصححها إلى 3:30")
        )
        xp = _record_ai_attempt(
            lesson_id="verify_with_evidence",
            check_id="evidence_quality",
            answer=f"{evidence} | {conclusion}",
            correct=correct,
            activity_type="ai_evidence_verification",
        )
        if correct:
            _success("ممتاز. اتعلمتي أهم قاعدة: **الأحدث + الأقرب للمصدر الأصلي + الأنسب للسؤال** أقوى من الكلام المتكرر.", xp)
            st.info("قاعدة التحقق: ادعاء → دليل → جودة المصدر → حداثة المصدر → استنتاج.")
        else:
            st.warning("قربي أكتر من المصدر الأصلي والأحدث. عدد الناس اللي كرروا معلومة مش أقوى من دليل رسمي حديث.")


def _prompt_challenge(ai: GeminiService) -> None:
    st.markdown("### ✍️ اكتبي Prompt من الصفر")
    st.write("عايزة الـAI يشرح لكِ **photosynthesis** بطريقة تناسب طالبة عمرها 14 سنة، بمثال بسيط، وبعدها يسألك سؤالًا واحدًا للتأكد من الفهم.")
    prompt = st.text_area("اكتبي الـPrompt بتاعك", key="ai_prompt_challenge")

    if st.button("قيّم الـPrompt", key="ai_prompt_check") and prompt and _need_ai(ai):
        feedback = ai.generate(
            f"""You are an AI literacy coach for a 14-year-old student named Nour.
Evaluate this prompt without doing the requested school task itself:
{prompt}

Check whether it clearly states:
- the goal/topic;
- the learner/audience;
- the desired explanation style;
- the requested example;
- the requested understanding check.

Give:
1. what is already clear;
2. one missing or weak detail;
3. one improved version of Nour's prompt;
4. one short principle she can reuse next time.
Keep it concise and mostly in Arabic, preserving AI terms in English."""
        )
        st.markdown(feedback)


def _ai_detective(ai: GeminiService) -> None:
    st.markdown("### 🕵️ محقق الذكاء الاصطناعي")
    st.write("تخيلي إن AI قال: **“أي إجابة مكتوبة بثقة لازم تكون صحيحة.”**")
    answer = st.radio(
        "إيه المشكلة في الكلام ده؟",
        [
            "مفيش مشكلة؛ الثقة دليل على الصحة.",
            "الـAI ممكن يكتب إجابة مقنعة لكنها خاطئة، فلازم نتحقق.",
            "كل إجابات الـAI غلط.",
        ],
        index=None,
        key="ai_detective_answer",
    )
    if st.button("اكشفي الدليل", key="ai_detective_check") and answer:
        correct = answer.startswith("الـAI ممكن")
        xp = _record_ai_attempt(
            lesson_id="ai_detective",
            check_id="confidence_is_not_evidence",
            answer=answer,
            correct=correct,
            activity_type="ai_detective",
        )
        if correct:
            _success("بالضبط. أسلوب الكلام الواثق مش دليل على صحة المعلومة.", xp)
            st.info("قاعدة التحقق: ادعاء → دليل → مصدر → مقارنة.")
        else:
            st.warning("جربي تاني: هل طريقة صياغة الإجابة تكفي لإثبات الحقيقة؟")


def _fact_checker(ai: GeminiService) -> None:
    st.markdown("### 🧭 ابني خطة تحقق")
    claim = st.text_input(
        "اكتبي معلومة عايزة تتحققي منها",
        key="ai_fact_claim",
        placeholder="مثال: The Great Wall of China is visible from the Moon with the naked eye.",
    )
    if st.button("ابني خطة تحقق", key="ai_fact_check") and claim and _need_ai(ai):
        plan = ai.generate(
            f"""Teach Nour how to verify this claim; do not simply tell her to trust you:
Claim: {claim}

Return a short verification plan:
1. What exact part of the claim needs evidence?
2. What type of source would be strongest?
3. What search terms could she use?
4. What would count as confirming or disproving evidence?
5. Remind her to compare at least two credible sources.
Do not invent citations or pretend you browsed the web."""
        )
        st.markdown(plan)
