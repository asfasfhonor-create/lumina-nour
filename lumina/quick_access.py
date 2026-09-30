import streamlit as st
from google.genai import types
from PIL import Image

from lumina.ai_service import GeminiService


def _need_ai(ai: GeminiService) -> bool:
    if not ai.available:
        st.warning("الأداة الذكية دي لسه مش مفعّلة. باقي البرنامج شغال عادي.")
        return False
    return True


def render_quick_access(ai: GeminiService) -> None:
    """Keep power tools available without overwhelming Nour's first screen."""
    with st.expander("⚡ أدوات إضافية لما تحتاجيها", expanded=False):
        st.caption("مش لازم تفتحي أي حاجة هنا دلوقتي. دي أدوات زيادة وقت ما تحتاجيها.")
        tabs = st.tabs(["📄 ملف PDF", "💬 مساعد ذكي", "📸 حل مسألة", "🇬🇧 English", "🗝️ مغامرة", "💻 Python", "🎯 أهدافي"])

        with tabs[0]:
            _render_pdf_tool(ai)
        with tabs[1]:
            _render_ai_buddy(ai)
        with tabs[2]:
            _render_problem_coach(ai)
        with tabs[3]:
            _render_english_helper(ai)
        with tabs[4]:
            _render_escape_room(ai)
        with tabs[5]:
            _render_python_helper(ai)
        with tabs[6]:
            _render_goals(ai)


def _render_pdf_tool(ai: GeminiService) -> None:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.subheader("اسألي من ملف أو مذكرة")
    uploaded_pdf = st.file_uploader("ارفعي كتابًا أو مذكرة PDF", type=["pdf"], key="pdf")

    if uploaded_pdf:
        pdf_bytes = uploaded_pdf.read()
        st.success(f"تم استقبال الملف: {uploaded_pdf.name} 💖")
        pdf_part = types.Part.from_bytes(data=pdf_bytes, mime_type="application/pdf")
        option = st.radio(
            "عايزة نعمل إيه؟",
            ["سؤال من الملف", "اختبار تدريبي", "ملخص ذكي"],
            horizontal=True,
        )

        if option == "سؤال من الملف":
            question = st.text_input("سؤالك", key="pdf_q")
            if st.button("جاوبني من الملف", key="pdf_answer") and question and _need_ai(ai):
                with st.spinner("بقرأ الملف..."):
                    text = ai.generate([
                        pdf_part,
                        (
                            "أنت مدرس لنور في الصف الثالث الإعدادي بمدرسة لغات في مصر. "
                            "أجب من الملف فقط، وبمصطلحات المنهج الأصلية، واشرح بالعربية عند الحاجة. "
                            f"لا تخمن معلومة غير موجودة. السؤال: {question}"
                        ),
                    ])
                    st.markdown(text)

        elif option == "اختبار تدريبي" and st.button("اعمل اختبار", key="pdf_exam") and _need_ai(ai):
            text = ai.generate([
                pdf_part,
                (
                    "أنشئ 5 أسئلة تدريبية مناسبة للصف الثالث الإعدادي من هذا الملف "
                    "وتقيس الفهم والتطبيق قدر الإمكان. ضع نموذج الإجابة في نهاية منفصلة."
                ),
            ])
            st.markdown(text)

        elif option == "ملخص ذكي" and st.button("لخّص", key="pdf_summary") and _need_ai(ai):
            text = ai.generate([
                pdf_part,
                (
                    "لخص أهم المفاهيم والتعريفات والقوانين في هذا الملف لطالبة ثالثة إعدادي، "
                    "مع الحفاظ على مصطلحات المنهج وعدم إضافة معلومات غير موجودة."
                ),
            ])
            st.markdown(text)

    st.markdown("</div>", unsafe_allow_html=True)


def _render_ai_buddy(ai: GeminiService) -> None:
    buddy = st.selectbox(
        "اختاري أسلوب المساعدة",
        ["أستاذ ألبرت 🔬", "المحقق التاريخي 📜", "صديقتك الملهمة 🌸"],
    )
    prompts = {
        "أستاذ ألبرت 🔬": (
            "اشرح علوم ثالثة إعدادي لنور بأسلوب بسيط وتجريبي. "
            "ابدأ بالفهم، اسألها سؤالًا صغيرًا، واستخدم تلميحات قبل الإجابة النهائية."
        ),
        "المحقق التاريخي 📜": (
            "اشرح دراسات ثالثة إعدادي لنور كتحقيق وقصة. "
            "شجع الاستنتاج والربط ولا تخترع تفاصيل منهجية."
        ),
        "صديقتك الملهمة 🌸": "ساعد نور على تنظيم مذاكرتها وشجعها بلطف ومن دون مبالغة أو ضغط.",
    }

    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    message = st.chat_input("اكتبي سؤالك يا نور...")
    if message and _need_ai(ai):
        st.session_state.chat_history.append({"role": "user", "content": message})
        text = ai.generate(message, system_instruction=prompts[buddy])
        st.session_state.chat_history.append({"role": "assistant", "content": text})
        st.rerun()


def _render_problem_coach(ai: GeminiService) -> None:
    camera_file = st.file_uploader("ارفعي صورة المسألة", type=["jpg", "jpeg", "png"], key="problem")
    if camera_file:
        image = Image.open(camera_file)
        st.image(image, use_container_width=True)
        if st.button("ابدئي معايا من أول تلميح", key="solve") and _need_ai(ai):
            text = ai.generate([
                image,
                (
                    "أنت مدرب واجبات لنور في ثالثة إعدادي. لا تعط الحل النهائي مباشرة. "
                    "حدد المطلوب، اسألها كيف تبدأ، ثم أعط تلميحًا أول واضحًا وطريقة التفكير المناسبة فقط."
                ),
            ])
            st.markdown(text)


def _render_english_helper(ai: GeminiService) -> None:
    st.subheader("تدريب English")
    assistance = st.select_slider(
        "درجة المساعدة",
        options=["مساعدة كبيرة", "متوسطة", "تحدي"],
        value="مساعدة كبيرة",
    )
    writing = st.text_area("Write 1–3 sentences in English", key="eng")

    if st.button("ساعدني أتحسن", key="eng_go") and writing and _need_ai(ai):
        prompt = f"""Nour is an Egyptian third-prep language-school student improving practical English.
Assistance level: {assistance}.
Her text: {writing}
Respond briefly and warmly:
1) preserve what she meant;
2) show a natural corrected version;
3) explain only the most useful mistake in short Arabic;
4) teach one useful word or expression in context;
5) give one tiny follow-up challenge.
Do not overwhelm her and do not treat every difference as an error."""
        st.markdown(ai.generate(prompt))


def _render_escape_room(ai: GeminiService) -> None:
    subject = st.selectbox(
        "المادة",
        ["علوم 3 إعدادي", "دراسات 3 إعدادي", "رياضيات 3 إعدادي"],
        key="escape_sub",
    )

    if st.button("ابدئي المغامرة", key="escape_new") and _need_ai(ai):
        st.session_state.esc_puzzle = ai.generate(
            f"اصنع لغز غرفة هروب قصيرًا لنور من {subject}. لا تكشف الإجابة. "
            "اجعل الحل كلمة أو رقمًا واحدًا، وفضّل سؤال فهم أو تطبيق بدل الحفظ المباشر."
        )

    if st.session_state.get("esc_puzzle"):
        st.info(st.session_state.esc_puzzle)
        answer = st.text_input("شفرة الخروج", key="escape_answer")
        if st.button("افتحي الباب", key="escape_check") and answer and _need_ai(ai):
            st.markdown(
                ai.generate(
                    f"اللغز: {st.session_state.esc_puzzle}\n"
                    f"إجابة نور: {answer}\n"
                    "تحقق من الإجابة. إن كانت خطأ أعط تلميحًا فقط ولا تكشف الحل، "
                    "وإن كانت صحيحة احتفل باختصار واشرح لماذا هي صحيحة في جملة."
                )
            )


def _render_python_helper(ai: GeminiService) -> None:
    code = st.text_area(
        "Python",
        'name = "Nour"\nscore = 100\nprint(f"Great job {name}! {score}%")',
        key="code",
    )
    if st.button("اشرح واديني تحدي صغير", key="code_explain") and _need_ai(ai):
        st.markdown(
            ai.generate(
                "اشرح هذا الكود لنور كمبتدئة، سطرًا سطرًا وباختصار، "
                "اطلب منها توقع الناتج قبل كشفه، ثم أعطها تعديلًا صغيرًا تكتبه بنفسها:\n"
                f"{code}"
            )
        )


def _render_goals(ai: GeminiService) -> None:
    task = st.text_input("هدف صغير لليوم", key="task")
    if st.button("أضيفيه", key="task_add") and task:
        st.session_state.tasks_list.append(task)
        st.rerun()

    for index, item in enumerate(st.session_state.tasks_list):
        st.checkbox(item, key=f"task_{index}")

    if st.button("🎉 رسالة تشجيع لليوم", key="motivate") and _need_ai(ai):
        st.balloons()
        st.success(
            ai.generate(
                "اكتب رسالة قصيرة ودافئة لنور، طالبة ثالثة إعدادي، "
                "تشجعها على خطوة صغيرة عملية اليوم بدون مبالغة أو ضغط."
            )
        )
