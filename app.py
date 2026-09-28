import streamlit as st
from google import genai
from google.genai import types

# إعداد الصفحة وتصميم الهاتف
st.set_page_config(
    page_title="Lumina by Nour M. Hussein ✨",
    page_icon="🔮",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# تخصيص واجهة أنيقة وفاخرة
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;800&family=Montserrat:wght@600;800&display=swap');
    
    * {
        font-family: 'Cairo', sans-serif;
        direction: rtl;
    }
    
    .brand-title {
        font-family: 'Montserrat', sans-serif;
        text-align: center;
        background: linear-gradient(135deg, #6C5CE7, #a29bfe, #fd79a8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.3rem;
        font-weight: 800;
        letter-spacing: 1.5px;
        margin-bottom: 2px;
        direction: ltr;
    }
    
    .signature-badge {
        font-family: 'Montserrat', 'Cairo', sans-serif;
        text-align: center;
        color: #6c5ce7;
        font-size: 1.05rem;
        font-weight: 600;
        margin-bottom: 8px;
        letter-spacing: 0.5px;
        direction: ltr;
    }
    
    .sub-tagline {
        text-align: center;
        color: #636e72;
        font-size: 0.95rem;
        margin-bottom: 25px;
    }
    
    .stButton>button {
        border-radius: 12px;
        background: linear-gradient(135deg, #6C5CE7, #8e44ad);
        color: white;
        font-weight: bold;
        border: none;
        padding: 0.6rem 1.4rem;
        box-shadow: 0 4px 15px rgba(108, 92, 231, 0.25);
    }
</style>
""", unsafe_allow_html=True)

# واجهة الشعار الفاخر
st.markdown('<div class="brand-title">LUMINA</div>', unsafe_allow_html=True)
st.markdown('<div class="signature-badge">by Nour M. Hussein</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-tagline">منظومة الذكاء الاصطناعي والدراسة الفائقة | الشهادة الإعدادية</div>', unsafe_allow_html=True)

# التأكد من وجود مفتاح الـ API
api_key = st.secrets.get("GEMINI_API_KEY", None)

if not api_key:
    api_key = st.sidebar.text_input("أدخل مفتاح Gemini API المجاني للتشغيل:", type="password")
    if not api_key:
        st.warning("يرجى إدخال مفتاح الـ API من القائمة الجانبية لتفعيل النظام.")
        st.stop()

client = genai.Client(api_key=api_key)

# التبويبات الرئيسية
tabs = st.tabs(["💬 صالون النخبة", "🗝️ غرفة الهروب", "🎯 بوصلة الإنجاز", "⚡ مختبر الابتكار"])

# ==================== القسم الأول: صالون النخبة ====================
with tabs[0]:
    st.subheader("صالون المذاكرة التفاعلي 💡")
    character = st.selectbox(
        "اختاري الشخصية التفاعلية:",
        ["أستاذ ألبرت (خبير العلوم والابتكار 🔬)", "المحقق التاريخي (أسرار دراسات 3 إعدادي 📜)", "مستشار التخطيط الشخصي 🚀"]
    )
    
    prompts = {
        "أستاذ ألبرت (خبير العلوم والابتكار 🔬)": "أنت 'أستاذ ألبرت'، عالم علوم ذكي ودمك خفيف يشرح منهج علوم الصف الثالث الإعدادي في مصر بطريقة حماسية وتشبيهات عصرية مدهشة. خاطب الطالبة 'نور محمد حسين' بلقب 'الباحثة نور' أو 'نور' باعتزاز وتشجيع دائم.",
        "المحقق التاريخي (أسرار دراسات 3 إعدادي 📜)": "أنت المحقق التاريخي الذكي، تناقش منهج الدراسات والتاريخ لـ 3 إعدادي في مصر بأسلوب درامي وألغاز وثائقية مع الطالبة 'نور محمد حسين'.",
        "مستشار التخطيط الشخصي 🚀": "أنت المستشار والمدرب الخاص بنور محمد حسين، تدعمها في تنظيم الوقت والدراسة الفعالة وبناء الثقة بالنفس والتحفيز المستمر."
    }

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_input = st.chat_input("اكتبي استفسارك الدراسي أو موضوع النقاش يا نور...")
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_input,
            config=types.GenerateContentConfig(
                system_instruction=prompts[character],
                temperature=0.7,
            )
        )
        
        reply = response.text
        st.session_state.messages.append({"role": "assistant", "content": reply})
        with st.chat_message("assistant"):
            st.markdown(reply)

# ==================== القسم الثاني: غرفة الهروب ====================
with tabs[1]:
    st.subheader("تحدي غرفة الهروب الذكية 🗝️")
    st.write("أنتِ في مقر الأبحاث السري! فك الشفرة للخروج يتطلب حل لغز دراسي من منهجك.")
    
    subject = st.radio("اختاري مسار التحدي:", ["علوم 3 إعدادي", "دراسات 3 إعدادي", "رياضيات 3 إعدادي"], horizontal=True)
    
    if st.button("توليد لغز جديد 🚪"):
        with st.spinner("جاري صياغة اللغز الدراسي..."):
            escape_prompt = f"أنشئ لغزاً دراسياً محكماً وممتعاً في مادة {subject} لطالبة متميزة في 3 إعدادي اسمها نور محمد حسين. اللغز يجب أن ينتهي بسؤال تكون إجابته كلمة أو رقم سري لفتح الباب."
            res = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=escape_prompt
            )
            st.session_state["current_puzzle"] = res.text

    if "current_puzzle" in st.session_state:
        st.info(st.session_state["current_puzzle"])
        ans = st.text_input("أدخلي رمز فك الشفرة:")
        if st.button("تحقق من الشفرة"):
            verify_prompt = f"اللغز كان: {st.session_state['current_puzzle']}\nإجابة نور هي: {ans}\nهل الإجابة صحيحة لفك الشفرة؟ أجب بأسلوب مشوق ومشجع لنور محمد حسين."
            v_res = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=verify_prompt
            )
            st.success(v_res.text)

# ==================== القسم الثالث: بوصلة الإنجاز ====================
with tabs[2]:
    st.subheader("مفكرة إنجازات نور 🎯")
    st.write("سجلي أهداف اليوم لمتابعة أدائك اليومي:")
    
    if "tasks" not in st.session_state:
        st.session_state.tasks = []
        
    new_task = st.text_input("إضافة مهمة دراسية جديدة:")
    if st.button("إضافة المهمة"):
        if new_task:
            st.session_state.tasks.append(new_task)
            st.rerun()

    for i, t in enumerate(st.session_state.tasks):
        st.checkbox(t, key=f"task_{i}")
        
    if st.button("✨ رسالة تحفيزية خاصة بيومي"):
        tasks_text = ", ".join(st.session_state.tasks) if st.session_state.tasks else "المراجعة العامة والتركيز"
        inspire_res = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"اكتب رسالة صباحية ملهمة ومحفزة جداً لـ 'نور محمد حسين' طالبة الشهادة الإعدادية. مهامها لليوم: {tasks_text}. اجعل النبرة تدعو للفخر بالطموح والإنجاز."
        )
        st.balloons()
        st.success(inspire_res.text)

# ==================== القسم الرابع: مختبر الابتكار ====================
with tabs[3]:
    st.subheader("مختبر هندسة الأوامر ⚡ (AI Studio)")
    st.write("هنا تتدربين على كيفية توجيه وبرمجة عقول الذكاء الاصطناعي.")
    
    st.markdown("""
    تطبيقك **Lumina** يعمل بفضل الأوامر التوجيهية (System Instructions). يمكنك تجربة صياغة عقل مخصص بنفسك:
    """)
    
    custom_sys = st.text_area("1. حددي دور وشخصية الـ AI:", "أنت خبير في علم الفلك والفيزياء الكونية...")
    custom_user = st.text_input("2. السؤال الموجه له:", "كيف تتكون الثقوب السوداء؟")
    
    if st.button("تشغيل النموذج 🚀"):
        test_res = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=custom_user,
            config=types.GenerateContentConfig(
                system_instruction=custom_sys,
                temperature=0.8
            )
        )
        st.code(test_res.text, language="markdown")
        st.caption("رائع يا نور! قمتِ للتو بهندسة واختبار سلوك ذكاء اصطناعي مخصص.")
