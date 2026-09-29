import streamlit as st
from google import genai
from google.genai import types
from PIL import Image

st.set_page_config(page_title="LUMINA | Nour's World", page_icon="✨", layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap');
* { font-family:'Cairo',sans-serif; }
.stApp { background:linear-gradient(155deg,#100d2d 0%,#231a54 45%,#151a3d 100%); color:#f7f4ff; }
.block-container { max-width:760px; padding-top:1rem; padding-bottom:5rem; }
[data-testid="stHeader"] { background:transparent; }
.hero { background:linear-gradient(135deg,rgba(255,118,172,.16),rgba(116,185,255,.12)); border:1px solid rgba(255,255,255,.15); border-radius:26px; padding:20px; margin-bottom:14px; box-shadow:0 16px 50px rgba(0,0,0,.22); }
.brand { font-family:'Plus Jakarta Sans',sans-serif; direction:ltr; font-size:2.15rem; font-weight:800; margin:0; background:linear-gradient(100deg,#ff8fc1,#b9a7ff,#7ed6ff); -webkit-background-clip:text; -webkit-text-fill-color:transparent; }
.hello { font-size:1.35rem; font-weight:800; margin:.35rem 0 .1rem; }
.muted { color:#d9d3eb; font-size:.92rem; }
.stat { background:rgba(255,255,255,.07); border:1px solid rgba(255,255,255,.1); border-radius:18px; padding:12px; text-align:center; min-height:86px; }
.stat b { display:block; font-size:1.15rem; }
.section-title { font-size:1.18rem; font-weight:900; margin:1.15rem 0 .5rem; }
.subject { background:rgba(255,255,255,.065); border:1px solid rgba(255,255,255,.11); border-radius:20px; padding:14px; margin-bottom:8px; min-height:118px; }
.subject h4 { margin:0 0 4px; }
.mission { background:linear-gradient(135deg,rgba(255,118,172,.13),rgba(120,115,245,.14)); border:1px solid rgba(255,160,205,.24); border-radius:22px; padding:16px; }
.feature-card { background:rgba(255,255,255,.055); border:1px solid rgba(255,255,255,.1); border-radius:20px; padding:14px; margin-bottom:14px; }
.stButton>button { width:100%; border-radius:14px; min-height:46px; font-weight:800; border:0; background:linear-gradient(135deg,#ff758c,#ff7eb3 50%,#7873f5); color:white; }
.stTextInput input,.stTextArea textarea { border-radius:14px !important; }
div[data-testid="stTabs"] button { font-weight:800; }
@media (max-width:640px){ .block-container{padding-left:.8rem;padding-right:.8rem}.brand{font-size:1.85rem}.hello{font-size:1.18rem}.stat{min-height:78px;padding:9px} }
</style>
""", unsafe_allow_html=True)

if "xp" not in st.session_state: st.session_state.xp = 120
if "streak" not in st.session_state: st.session_state.streak = 3
if "daily_done" not in st.session_state: st.session_state.daily_done = False

st.markdown("""
<div class="hero">
  <div class="brand">LUMINA · NOUR'S WORLD</div>
  <div class="hello">أهلاً يا نور ✨ جاهزة لمهمة صغيرة النهارده؟</div>
  <div class="muted">مساحتك للمذاكرة، التجربة، والإنجليزي — خطوة صغيرة كل يوم.</div>
</div>
""", unsafe_allow_html=True)

c1,c2,c3 = st.columns(3)
with c1: st.markdown(f'<div class="stat">⭐ <b>{st.session_state.xp} XP</b><span class="muted">نقاطك</span></div>', unsafe_allow_html=True)
with c2: st.markdown(f'<div class="stat">🔥 <b>{st.session_state.streak} أيام</b><span class="muted">Streak</span></div>', unsafe_allow_html=True)
with c3: st.markdown('<div class="stat">🌱 <b>Level 2</b><span class="muted">Explorer</span></div>', unsafe_allow_html=True)

st.markdown('<div class="section-title">🎯 مهمة اليوم</div>', unsafe_allow_html=True)
st.markdown('<div class="mission"><b>English Mini Mission</b><br><span class="muted">اكتبي 3 جمل قصيرة عن يومك بالإنجليزي. مش مهم تكون مثالية — المهم نجرب.</span></div>', unsafe_allow_html=True)
if not st.session_state.daily_done:
    if st.button("أنجزت المهمة +20 XP", key="daily_xp"):
        st.session_state.xp += 20
        st.session_state.daily_done = True
        st.balloons()
        st.rerun()
else:
    st.success("مهمة اليوم اتسجلت 🎉 +20 XP")

st.markdown('<div class="section-title">📚 اختاري عالمك</div>', unsafe_allow_html=True)
cols = st.columns(2)
subjects = [
    ("🔬 Science Lab", "افهمي الفكرة بالتجربة والتشبيه."),
    ("➗ Math Quest", "مسائل خطوة بخطوة من غير حفظ أعمى."),
    ("🌍 Social Studies", "تاريخ وجغرافيا كقصة وتحقيق."),
    ("🇬🇧 English Adventure", "محادثة، كلمات، وتصحيح بسيط."),
]
for i,(title,desc) in enumerate(subjects):
    with cols[i%2]:
        st.markdown(f'<div class="subject"><h4>{title}</h4><span class="muted">{desc}</span><br><small>🚧 Subject Hub — المرحلة القادمة</small></div>', unsafe_allow_html=True)

st.markdown('<div class="section-title">⚡ أدواتك الحالية</div>', unsafe_allow_html=True)
api_key = st.secrets.get("GEMINI_API_KEY", None)
if not api_key:
    api_key = st.sidebar.text_input("Gemini API Key", type="password")
    if not api_key:
        st.info("الأدوات الذكية تحتاج Gemini API Key. الواجهة الرئيسية تعمل بدون المفتاح.")
client = genai.Client(api_key=api_key) if api_key else None

def need_ai():
    if client is None:
        st.warning("فعّلي Gemini API Key أولاً لتشغيل الأداة.")
        return False
    return True

tabs = st.tabs(["📄 PDF", "💬 AI Buddy", "📸 مسألة", "🇬🇧 English", "🗝️ Escape", "💻 Python", "🎯 أهدافي"])

with tabs[0]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.subheader("رفيقة المنهج والـ PDF")
    uploaded_pdf = st.file_uploader("ارفعي كتابًا أو مذكرة PDF", type=["pdf"], key="pdf")
    if uploaded_pdf:
        pdf_part = types.Part.from_bytes(data=uploaded_pdf.read(), mime_type="application/pdf")
        option = st.radio("عايزة نعمل إيه؟", ["سؤال من الملف", "اختبار تدريبي", "ملخص ذكي"], horizontal=True)
        if option == "سؤال من الملف":
            q = st.text_input("سؤالك", key="pdf_q")
            if st.button("جاوبني من الملف", key="pdf_answer") and q and need_ai():
                with st.spinner("بقرأ الملف..."):
                    res=client.models.generate_content(model="gemini-2.5-flash",contents=[pdf_part,f"أنت مدرس لنور في الصف الثالث الإعدادي بمدرسة لغات في مصر. أجب من الملف فقط، وبمصطلحات المنهج الأصلية، واشرح بالعربية عند الحاجة. السؤال: {q}"])
                    st.markdown(res.text)
        elif option == "اختبار تدريبي" and st.button("اعمل اختبار", key="pdf_exam") and need_ai():
            res=client.models.generate_content(model="gemini-2.5-flash",contents=[pdf_part,"أنشئ 5 أسئلة تدريبية مناسبة للصف الثالث الإعدادي من هذا الملف، ثم ضع نموذج الإجابة بعد الأسئلة."])
            st.markdown(res.text)
        elif option == "ملخص ذكي" and st.button("لخّص", key="pdf_summary") and need_ai():
            res=client.models.generate_content(model="gemini-2.5-flash",contents=[pdf_part,"لخص أهم المفاهيم والتعريفات والقوانين في هذا الملف لطالبة ثالثة إعدادي، مع الحفاظ على مصطلحات المنهج."])
            st.markdown(res.text)
    st.markdown('</div>', unsafe_allow_html=True)

with tabs[1]:
    buddy=st.selectbox("مين يذاكر معاكي؟",["أستاذ ألبرت 🔬","المحقق التاريخي 📜","صديقتك الملهمة 🌸"])
    prompts={"أستاذ ألبرت 🔬":"اشرح علوم ثالثة إعدادي لنور بأسلوب بسيط وتجريبي، ولا تجعلها تحفظ قبل أن تفهم.","المحقق التاريخي 📜":"اشرح دراسات ثالثة إعدادي لنور كتحقيق وقصة مع الالتزام بالمنهج.","صديقتك الملهمة 🌸":"ساعد نور على تنظيم مذاكرتها وشجعها بلطف ومن دون مبالغة."}
    if "chat_history" not in st.session_state: st.session_state.chat_history=[]
    for m in st.session_state.chat_history:
        with st.chat_message(m["role"]): st.markdown(m["content"])
    msg=st.chat_input("اكتبي سؤالك يا نور...")
    if msg and need_ai():
        st.session_state.chat_history.append({"role":"user","content":msg})
        r=client.models.generate_content(model="gemini-2.5-flash",contents=msg,config=types.GenerateContentConfig(system_instruction=prompts[buddy]))
        st.session_state.chat_history.append({"role":"assistant","content":r.text})
        st.rerun()

with tabs[2]:
    cam=st.file_uploader("ارفعي صورة المسألة",type=["jpg","jpeg","png"],key="problem")
    if cam:
        img=Image.open(cam)
        st.image(img,use_container_width=True)
        if st.button("فهمني الحل",key="solve") and need_ai():
            r=client.models.generate_content(model="gemini-2.5-flash",contents=[img,"اشرح لنور، طالبة ثالثة إعدادي، طريقة التفكير والحل خطوة بخطوة. لا تكتفِ بالإجابة النهائية."])
            st.markdown(r.text)

with tabs[3]:
    st.subheader("English Adventure")
    level=st.select_slider("درجة المساعدة",options=["مساعدة كبيرة","متوسطة","تحدي"],value="مساعدة كبيرة")
    eng=st.text_area("Write 1–3 sentences in English",key="eng")
    if st.button("ساعدني أتحسن",key="eng_go") and eng and need_ai():
        p=f"Nour is an Egyptian third-prep language-school student whose English needs improvement. Assistance level: {level}. Correct this gently: {eng}. Show: 1) her sentence, 2) corrected version, 3) one short Arabic explanation, 4) one tiny follow-up challenge. Do not overwhelm her."
        r=client.models.generate_content(model="gemini-2.5-flash",contents=p)
        st.markdown(r.text)

with tabs[4]:
    sub=st.selectbox("المادة",["علوم 3 إعدادي","دراسات 3 إعدادي","رياضيات 3 إعدادي"],key="escape_sub")
    if st.button("ابدئي المغامرة",key="escape_new") and need_ai():
        r=client.models.generate_content(model="gemini-2.5-flash",contents=f"اصنع لغز غرفة هروب قصيرًا لنور من {sub}. لا تكشف الإجابة. اجعل الحل كلمة أو رقمًا واحدًا.")
        st.session_state.esc_puzzle=r.text
    if st.session_state.get("esc_puzzle"):
        st.info(st.session_state.esc_puzzle)
        ans=st.text_input("شفرة الخروج",key="escape_answer")
        if st.button("افتحي الباب",key="escape_check") and ans and need_ai():
            r=client.models.generate_content(model="gemini-2.5-flash",contents=f"اللغز: {st.session_state.esc_puzzle}\nإجابة نور: {ans}\nتحقق من الإجابة. إن كانت خطأ أعط تلميحًا فقط، وإن كانت صحيحة احتفل باختصار.")
            st.markdown(r.text)

with tabs[5]:
    code=st.text_area("Python",'name = "Nour"\nscore = 100\nprint(f"Great job {name}! {score}%")',key="code")
    if st.button("اشرح الكود",key="code_explain") and need_ai():
        r=client.models.generate_content(model="gemini-2.5-flash",contents=f"اشرح هذا الكود لنور كمبتدئة، سطرًا سطرًا، ثم أعطها تعديلًا صغيرًا تجرب كتابته بنفسها:\n{code}")
        st.markdown(r.text)

with tabs[6]:
    if "tasks_list" not in st.session_state: st.session_state.tasks_list=[]
    task=st.text_input("هدف صغير لليوم",key="task")
    if st.button("أضيفيه",key="task_add") and task:
        st.session_state.tasks_list.append(task)
        st.rerun()
    for i,item in enumerate(st.session_state.tasks_list):
        st.checkbox(item,key=f"task_{i}")

st.caption("LUMINA · built for Nour ✨ | النسخة التجريبية الجديدة على فرع التطوير")
