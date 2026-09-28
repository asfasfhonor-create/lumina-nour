import streamlit as st
from google import genai
from google.genai import types
from PIL import Image

# إعداد الصفحة لتلائم الهواتف الذكية تماماً
st.set_page_config(
    page_title="LUMINA | Nour M. Hussein",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# تخصيص واجهة عصرية وفائقة الأناقة (Cyber-Pastel Glassmorphism)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&family=Plus+Jakarta+Sans:wght@500;700;800&display=swap');
    
    * {
        font-family: 'Cairo', sans-serif;
        direction: rtl;
    }
    
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: #f1f2f6;
    }
    
    .hero-card {
        background: rgba(255, 255, 255, 0.07);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 24px;
        padding: 24px 16px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }
    
    .brand-title {
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 2.8rem;
        font-weight: 900;
        background: linear-gradient(120deg, #ff76ac, #a29bfe, #74b9ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: 2px;
        margin: 0;
        direction: ltr;
    }
    
    .author-badge {
        font-family: 'Plus Jakarta Sans', 'Cairo', sans-serif;
        display: inline-block;
        background: linear-gradient(90deg, rgba(255, 118, 172, 0.2), rgba(162, 155, 254, 0.2));
        border: 1px solid rgba(255, 118, 172, 0.4);
        color: #ff9ff3;
        font-size: 0.95rem;
        font-weight: 700;
        padding: 4px 16px;
        border-radius: 50px;
        margin-top: 8px;
        margin-bottom: 8px;
        direction: ltr;
    }
    
    .sub-tagline {
        color: #dcdde1;
        font-size: 0.9rem;
        font-weight: 600;
        margin-top: 5px;
    }
    
    .feature-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 18px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 16px;
        margin-bottom: 16px;
    }
    
    .stButton>button {
        width: 100%;
        border-radius: 16px;
        background: linear-gradient(135deg, #ff758c 0%, #ff7eb3 50%, #7873f5 100%);
        color: #ffffff !important;
        font-weight: 800;
        font-size: 1rem;
        border: none;
        padding: 0.75rem 1.5rem;
        box-shadow: 0 4px 18px rgba(255, 118, 172, 0.35);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 22px rgba(255, 118, 172, 0.5);
    }
    
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background: rgba(255, 255, 255, 0.08) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 14px !important;
        color: #ffffff !important;
    }
</style>
""", unsafe_allow_html=True)

# واجهة الهيدر الترحيبي
st.markdown("""
<div class="hero-card">
    <div class="brand-title">LUMINA</div>
    <div class="author-badge">👑 Designed Exclusively for Nour M. Hussein</div>
    <div class="sub-tagline">منظومة الذكاء الخارق ورفيقة التفوق في الشهادة الإعدادية ✨</div>
</div>
""", unsafe_allow_html=True)

# استدعاء مفتاح الـ API
api_key = st.secrets.get("GEMINI_API_KEY", None)
if not api_key:
    api_key = st.sidebar.text_input("أدخلي مفتاح Gemini API:", type="password")
    if not api_key:
        st.warning("يرجى تفعيل مفتاح الـ API للبدء في تشغيل النظام 🔑")
        st.stop()

client = genai.Client(api_key=api_key)

# التبويبات العصرية
tabs = st.tabs([
    "📚 مذكرات وPDF", 
    "💬 صالون النخبة", 
    "📸 كاميرا المسائل", 
    "🗣️ لغات ومحادثة", 
    "🗝️ غرفة الهروب", 
    "💻 بايثون للمبدعات", 
    "🎯 مفكرتي"
])

# ==================== 1. مكتبة المناهج والتقييمات ====================
with tabs[0]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.markdown("### 📚 رفيقة المنهج والتقييمات الرسمية")
    st.write("ارفعي مذكراتك أو كتاب الوزارة (PDF) للترم الثاني، واسألي أي سؤال أو حلي نماذج الامتحانات مباشرة!")
    
    uploaded_pdf = st.file_uploader("اسحبي ملف الـ PDF هنا:", type=["pdf"])
    if uploaded_pdf:
        pdf_bytes = uploaded_pdf.read()
        st.success(f"تم استقبال الملف بنجاح: {uploaded_pdf.name} 💖")
        
        pdf_part = types.Part.from_bytes(data=pdf_bytes, mime_type="application/pdf")
        
        option = st.radio(
            "ماذا تريدين أن نستخرج من هذا الملف؟",
            ["حل واستفسار عن سؤال محدد", "امتحان تدريبي مطابق لأسلوب الوزارة", "ملخص ذكي للقوانين والتعريفات"],
            horizontal=True
        )
        
        if option == "حل واستفسار عن سؤال محدد":
            q = st.text_input("اكتبي استفسارك من المنهج:")
            if st.button("استخراج الإجابة الدقيقة 🔍"):
                if q:
                    with st.spinner("جاري قراءة المنهج بعناية..."):
                        p = f"أنت معلم خاص لنور محمد حسين (3 إعدادي بمصر). أجب بدقة ومن واقع الملف المرفق فقط على السؤال: {q}"
                        res = client.models.generate_content(model="gemini-2.5-flash", contents=[pdf_part, p])
                        st.markdown(res.text)
                        
        elif option == "امتحان تدريبي مطابق لأسلوب الوزارة":
            if st.button("توليد اختبار تدريبي مع الحل 📝"):
                with st.spinner("جاري صياغة الأسئلة الذكية..."):
                    p = "صغ 5 أسئلة امتحانات وتدريبات من واقع هذا الملف لنور محمد حسين، متضمنة خطوات التفكير ونموذج الإجابة."
                    res = client.models.generate_content(model="gemini-2.5-flash", contents=[pdf_part, p])
                    st.markdown(res.text)
                    
        elif option == "ملخص ذكي للقوانين والتعريفات":
            if st.button("إنشاء ملخص مركز 📑"):
                with st.spinner("جاري تلخيص أهم النقاط..."):
                    p = "استخرج أهم المفاهيم، القوانين، والتعريفات الأساسية من هذا الملف بأسلوب مرتب ولطيف لنور."
                    res = client.models.generate_content(model="gemini-2.5-flash", contents=[pdf_part, p])
                    st.markdown(res.text)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================== 2. صالون النخبة والشخصيات ====================
with tabs[1]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.markdown("### 💬 رفاق المذاكرة الأذكياء")
    buddy = st.selectbox(
        "اختاري من سيدرس معكِ الآن:",
        ["أستاذ ألبرت (عالم العلوم الحماسي 🔬)", "المحقق التاريخي (أسرار دراسات 3 إعدادي 📜)", "صديقتك الملهمة (تشجيع وتنظيم 🌸)"]
    )
    
    b_prompts = {
        "أستاذ ألبرت (عالم العلوم الحماسي 🔬)": "أنت العالم ألبرت، تشرح علوم 3 إعدادي بمصر لنور محمد حسين بأسلوب مشوق وتجارب وتشبيهات خيالية ممتعة. ناديها 'الباحثة العبقرية نور'.",
        "المحقق التاريخي (أسرار دراسات 3 إعدادي 📜)": "أنت المحقق شيرلوك للدراسات والتاريخ المصري لـ 3 إعدادي. تحل الألغاز التاريخية بأسلوب مشوق مع نور محمد حسين.",
        "صديقتك الملهمة (تشجيع وتنظيم 🌸)": "أنتِ الصديقة المقربة والمدربة المحفزة لنور محمد حسين، تدعمينها في يومها الدراسي بحماس ولطف وتنظيم وقت."
    }
    
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
        
    for m in st.session_state.chat_history:
        with st.chat_message(m["role"]):
            st.markdown(m["content"])
            
    c_in = st.chat_input("اكتبي ما يخطر ببالكِ يا نور...")
    if c_in:
        st.session_state.chat_history.append({"role": "user", "content": c_in})
        with st.chat_message("user"):
            st.markdown(c_in)
        r = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=c_in,
            config=types.GenerateContentConfig(system_instruction=b_prompts[buddy])
        )
        st.session_state.chat_history.append({"role": "assistant", "content": r.text})
        with st.chat_message("assistant"):
            st.markdown(r.text)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================== 3. كاميرا حل المسائل ====================
with tabs[2]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.markdown("### 📸 كاميرا المسائل الذكية")
    st.write("صوري أي رسم هندسي، دائرة كهربية، أو مسألة حسابية لتحليلها وشرحها فوراً!")
    cam_file = st.file_uploader("ارفعي صورة المسألة:", type=["jpg", "png", "jpeg"])
    if cam_file:
        img = Image.open(cam_file)
        st.image(img, use_container_width=True)
        if st.button("تحليل وشرح خطوات الحل 💡"):
            with st.spinner("جاري فك رموز المسألة..."):
                res_img = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=[img, "اشرح خطوات حل هذه المسألة بالتفصيل الدقيق وبطريقة مبسطة تناسب طالبة 3 إعدادي نور محمد حسين."]
                )
                st.markdown(res_img.text)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================== 4. مدرب الإنجليزية ====================
with tabs[3]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.markdown("### 🗣️ English Lounge with Nour")
    eng_input = st.text_area("Write something in English to practice:")
    if st.button("Improve & Polish My English ✨"):
        if eng_input:
            p = f"You are a friendly British mentor for a 15-year-old girl named Nour. Polish her sentence, show natural idioms, and give a motivating friendly reply: '{eng_input}'"
            eng_res = client.models.generate_content(model="gemini-2.5-flash", contents=p)
            st.markdown(eng_res.text)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================== 5. غرفة الهروب ====================
with tabs[4]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.markdown("### 🗝️ مغامرة غرفة الهروب")
    st.write("لغز دراسي غامض لن تفتحي الباب السري إلا بحله!")
    sub = st.selectbox("المادة:", ["علوم 3 إعدادي", "دراسات 3 إعدادي", "رياضيات 3 إعدادي"])
    if st.button("توليد غرفة ولغز جديد 🚪"):
        with st.spinner("جاري بناء الغرفة السحرية..."):
            p = f"اكتب سيناريو غرفة هروب سحرية ممتعة لنور محمد حسين، يعتمد حل الباب على سؤال ذكي من منهج {sub} وتكون الإجابة كلمة أو رقم واحد فقط."
            esc_res = client.models.generate_content(model="gemini-2.5-flash", contents=p)
            st.session_state["esc_puzzle"] = esc_res.text
            
    if "esc_puzzle" in st.session_state:
        st.info(st.session_state["esc_puzzle"])
        code_try = st.text_input("شفرة الخروج:")
        if st.button("تجربة فتح الباب"):
            check_p = f"اللغز: {st.session_state['esc_puzzle']}\nإجابة نور: {code_try}\nهل الإجابة صحيحة وتسمح بالهروب؟ أجب بحماس واحتفال إن كانت صحيحة."
            c_res = client.models.generate_content(model="gemini-2.5-flash", contents=check_p)
            st.success(c_res.text)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================== 6. أكاديمية بايثون ====================
with tabs[5]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.markdown("### 💻 كود بايثون للمبتكرات الصغيرات")
    st.write("اصنعي برامجك وألعابك البسيطة بنفسك:")
    code_val = st.text_area("محرر الأكواد:", 'name = "Nour"\nscore = 100\nprint(f"مبروك للمبرمجة {name} مجموعك هو {score}% ✨")')
    if st.button("شرح وتشغيل الكود بالذكاء الاصطناعي 🚀"):
        c_res = client.models.generate_content(
            model="gemini-2.5-flash", 
            contents=f"اشرح لنور محمد حسين بلطف وبساطة ماذا يفعل كود بايثون هذا وما هي مخرجاته المتوقعة: \n{code_val}"
        )
        st.markdown(c_res.text)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================== 7. مفكرتي وإنجازاتي ====================
with tabs[6]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.markdown("### 🎯 إنجازات نور اليومية")
    if "tasks_list" not in st.session_state:
        st.session_state.tasks_list = []
    t_add = st.text_input("إضافة هدف أو درس لليوم:")
    if st.button("إضافة للمفكرة 📌"):
        if t_add:
            st.session_state.tasks_list.append(t_add)
            st.rerun()
            
    for idx, item in enumerate(st.session_state.tasks_list):
        st.checkbox(item, key=f"t_{idx}")
        
    if st.button("🎉 طاقة إيجابية ورسالة ملهمة لليوم"):
        st.balloons()
        insp = client.models.generate_content(
            model="gemini-2.5-flash", 
            contents="اكتب رسالة صباحية غاية في الجمال والتحفيز لطالبة الشهادة الإعدادية المتميزة 'نور محمد حسين' لتشعر بالفخر والثقة."
        )
        st.success(insp.text)
    st.markdown('</div>', unsafe_allow_html=True)
