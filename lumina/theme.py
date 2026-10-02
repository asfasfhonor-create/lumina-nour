import streamlit as st


GLOBAL_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap');
* { font-family:'Cairo',sans-serif; }
.stApp { background:radial-gradient(circle at 8% 4%,rgba(255,157,205,.20),transparent 26%),radial-gradient(circle at 92% 10%,rgba(126,214,255,.16),transparent 25%),linear-gradient(155deg,#171337 0%,#29205d 48%,#172448 100%); color:#f7f4ff; }
.block-container { max-width:900px; padding-top:1rem; padding-bottom:5rem; }
.stApp p, .stApp label, .stApp [data-testid="stCaptionContainer"] { color:#eee9fb; }
.stApp [data-testid="stCaptionContainer"] { opacity:.9; }
.stApp hr { border-color:rgba(255,255,255,.10); }
div[data-testid="stVerticalBlockBorderWrapper"] { border-color:rgba(255,255,255,.12) !important; }
/* Remove Streamlit chrome from the learner-facing experience. The owner can
   still manage the app from Streamlit Community Cloud. */
[data-testid="stHeader"],
[data-testid="stToolbar"],
[data-testid="stToolbarActions"],
[data-testid="stDecoration"],
[data-testid="stSidebarCollapsedControl"],
[data-testid="stMainMenu"],
[data-testid="stAppDeployButton"],
[data-testid="stStatusWidget"],
[data-testid="stSidebarCollapseButton"],
.stAppToolbar,
.stDeployButton,
header[data-testid="stHeader"],
.stApp > header,
#MainMenu {
  display:none !important;
}
.hero {
  min-height:238px; display:flex; flex-direction:column; justify-content:center;
  background:
    radial-gradient(circle at 88% 18%,rgba(255,229,126,.14),transparent 18%),
    linear-gradient(135deg,rgba(255,118,172,.18),rgba(116,185,255,.13));
  border:1px solid rgba(255,255,255,.16); border-radius:28px; padding:24px;
  margin-bottom:14px; box-shadow:0 18px 54px rgba(0,0,0,.24);
}
.nour-photo-wrap { position:relative; width:190px; margin:0 auto 12px; text-align:center; }
.nour-photo-glow {
  width:190px; height:238px; border-radius:34px; padding:5px;
  background:linear-gradient(145deg,#ff8fc1,#b9a7ff 48%,#7ed6ff);
  box-shadow:
    0 18px 46px rgba(126,214,255,.20),
    0 12px 34px rgba(255,143,193,.18),
    inset 0 0 0 1px rgba(255,255,255,.28);
  overflow:hidden;
}
.nour-photo-glow img {
  display:block; width:100%; height:100%; object-fit:cover;
  object-position:center center; border-radius:29px;
  filter:none; image-rendering:auto;
}
.nour-photo-wrap::before,
.nour-photo-wrap::after {
  position:absolute; z-index:2; font-size:1.05rem; filter:drop-shadow(0 4px 8px rgba(0,0,0,.25));
}
.nour-photo-wrap::before { content:"✦"; top:-8px; right:-8px; color:#ffe67a; }
.nour-photo-wrap::after { content:"✧"; top:20px; left:-9px; color:#9fe7ff; }
.nour-photo-badge {
  display:inline-block; position:relative; margin-top:-15px; z-index:3;
  padding:5px 12px; border-radius:999px; font-family:'Plus Jakarta Sans',sans-serif;
  font-size:.72rem; font-weight:800; letter-spacing:.08em; color:#fff;
  background:rgba(26,20,66,.92); border:1px solid rgba(255,255,255,.20);
  box-shadow:0 7px 18px rgba(0,0,0,.24);
}
.brand { font-family:'Plus Jakarta Sans',sans-serif; direction:ltr; font-size:2.15rem; font-weight:800; margin:0; background:linear-gradient(100deg,#ff9dcc 0%,#c8b5ff 48%,#8cddff 100%); -webkit-background-clip:text; -webkit-text-fill-color:transparent; }
.hello { font-size:1.35rem; font-weight:800; margin:.35rem 0 .1rem; }
.muted { color:#d9d3eb; font-size:.92rem; }
.stat { background:rgba(255,255,255,.07); border:1px solid rgba(255,255,255,.1); border-radius:18px; padding:12px; text-align:center; min-height:86px; }
.stat b { display:block; font-size:1.15rem; }
.section-title { font-size:1.18rem; font-weight:900; margin:1.15rem 0 .5rem; }
.subject { background:linear-gradient(145deg,rgba(255,255,255,.085),rgba(255,255,255,.045)); border:1px solid rgba(255,255,255,.13); border-radius:22px; padding:16px; margin-bottom:9px; min-height:118px; box-shadow:0 10px 30px rgba(0,0,0,.10); transition:transform .18s ease,border-color .18s ease,background .18s ease; }
.subject:hover { transform:translateY(-2px); border-color:rgba(185,167,255,.34); background:linear-gradient(145deg,rgba(255,143,193,.10),rgba(126,214,255,.07)); }
.subject h4 { margin:0 0 4px; }
.mission { background:linear-gradient(135deg,rgba(255,118,172,.13),rgba(120,115,245,.14)); border:1px solid rgba(255,160,205,.24); border-radius:22px; padding:16px; }
.start-card { background:linear-gradient(145deg,rgba(255,255,255,.105),rgba(255,255,255,.055)); border:1px solid rgba(255,255,255,.18); border-radius:26px; padding:18px; margin:14px 0 18px; box-shadow:0 16px 40px rgba(0,0,0,.16); }
.start-lesson { background:linear-gradient(135deg,rgba(255,157,205,.17),rgba(200,181,255,.13),rgba(140,221,255,.10)); border:1px solid rgba(255,255,255,.16); border-radius:20px; padding:16px; margin:8px 0 12px; }
.start-kicker { font-family:'Plus Jakarta Sans',sans-serif; font-size:.68rem; letter-spacing:.10em; font-weight:800; opacity:.78; }
.start-title { font-size:1.18rem; font-weight:900; margin:.35rem 0 .2rem; }
.start-meta { font-size:.82rem; opacity:.78; }
.feature-card { background:rgba(255,255,255,.055); border:1px solid rgba(255,255,255,.1); border-radius:20px; padding:14px; margin-bottom:14px; }
.track-card { background:rgba(255,255,255,.055); border:1px solid rgba(255,255,255,.1); border-radius:18px; padding:14px; margin-bottom:10px; }
div[data-testid="stButton"] > button, .stButton > button, .stButton > button[kind="secondary"] { width:100%; border-radius:15px; min-height:48px; font-weight:800; border:1px solid rgba(255,255,255,.16) !important; background:linear-gradient(135deg,#ff7eb3 0%,#c27cff 52%,#62cfff 100%) !important; color:#ffffff !important; box-shadow:0 8px 24px rgba(109,75,190,.24),0 2px 8px rgba(255,126,179,.14); transition:transform .15s ease,filter .15s ease,box-shadow .15s ease; }
div[data-testid="stButton"] > button *, .stButton > button * { color:#ffffff !important; }
.stButton>button:hover { transform:translateY(-2px) scale(1.01); filter:brightness(1.08) saturate(1.06); box-shadow:0 13px 30px rgba(109,75,190,.30),0 4px 12px rgba(255,126,179,.18); }
.stButton>button:focus { color:white !important; border-color:rgba(255,255,255,.55); outline:2px solid rgba(255,230,122,.28); outline-offset:2px; }
.stButton>button:disabled { opacity:.52; transform:none; box-shadow:none; }
.stDownloadButton>button { border-radius:15px; min-height:46px; font-weight:800; }
.stTextInput input,.stTextArea textarea { border-radius:14px !important; background:rgba(255,255,255,.08) !important; color:#fff !important; border:1px solid rgba(255,255,255,.15) !important; }
.stTextInput input::placeholder,.stTextArea textarea::placeholder { color:#c9c1df !important; }
div[data-baseweb="select"] > div { background:rgba(255,255,255,.08); border-color:rgba(255,255,255,.15); }
div[data-testid="stExpander"] { background:rgba(255,255,255,.035); border:1px solid rgba(255,255,255,.10); border-radius:18px; }
.stTextInput input,.stTextArea textarea { border-radius:14px !important; }
div[data-testid="stTabs"] button { font-weight:800; }
@media (max-width:640px){
  .block-container{padding-left:.8rem;padding-right:.8rem;padding-top:.55rem}
  .brand{font-size:1.62rem}.hello{font-size:1.12rem}.stat{min-height:78px;padding:9px}
  .hero{min-height:auto;padding:18px;border-radius:22px}
  .nour-photo-wrap{width:148px;margin-bottom:10px}
  .nour-photo-glow{width:148px;height:185px;border-radius:27px;padding:4px}
  .nour-photo-glow img{border-radius:23px;object-position:center center}
  .nour-photo-badge{font-size:.64rem;padding:4px 9px}
}

/* Playful learner accents: warm, bright and polished — not childish. */
.start-card .section-title { color:#ffe67a; }
.start-card .start-kicker { color:#9fe7ff; }
.start-card .start-title { color:#fff8fd; }
.start-card .stButton:first-of-type > button { min-height:54px; font-size:1.02rem; background:linear-gradient(135deg,#ff78b4,#b875ff 55%,#62d2ff) !important; }
.subject:nth-of-type(3n+1) { box-shadow:0 10px 28px rgba(255,126,179,.09); }
.subject:nth-of-type(3n+2) { box-shadow:0 10px 28px rgba(185,167,255,.09); }
.subject:nth-of-type(3n) { box-shadow:0 10px 28px rgba(126,214,255,.09); }

</style>
"""


def apply_theme() -> None:
    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)
