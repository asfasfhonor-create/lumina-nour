import streamlit as st

from lumina.ai_service import GeminiService


def render_ai_world(ai: GeminiService) -> None:
    st.markdown('<div class="section-title">🤖 عالم الذكاء الاصطناعي</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="mission"><b>جرّبي → تحققي → قارني → استنتجي</b><br>'
        '<span class="muted">هنا نور تتعلم تستخدم AI بعقلها: تسأل أحسن، تراجع الإجابات، وتكتشف الكلام غير الموثوق.</span></div>',
        unsafe_allow_html=True,
    )

    mode = st.radio(
        "اختاري تحدي",
        ["تحدّي كتابة Prompt", "محقق الذكاء الاصطناعي", "التحقق من معلومة"],
        key="ai_lab_mode",
    )

    if mode == "تحدّي كتابة Prompt":
        _prompt_challenge(ai)
    elif mode == "محقق الذكاء الاصطناعي":
        _ai_detective(ai)
    else:
        _fact_checker(ai)


def _need_ai(ai: GeminiService) -> bool:
    if not ai.available:
        st.warning("التحدي الذكي ده لسه مش مفعّل. تقدري تكمّلي باقي أجزاء البرنامج عادي.")
        return False
    return True


def _prompt_challenge(ai: GeminiService) -> None:
    st.markdown("### تحدّي كتابة Prompt")
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
    st.markdown("### محقق الذكاء الاصطناعي")
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
        if answer.startswith("الـAI ممكن"):
            st.success("بالضبط. أسلوب الكلام الواثق مش دليل على صحة المعلومة.")
            st.info("قاعدة التحقق: ادعاء → دليل → مصدر → مقارنة.")
        else:
            st.warning("جربي تاني: هل طريقة صياغة الإجابة تكفي لإثبات الحقيقة؟")


def _fact_checker(ai: GeminiService) -> None:
    st.markdown("### التحقق من معلومة")
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
