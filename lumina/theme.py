import streamlit as st


GLOBAL_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap');
* { font-family:'Cairo',sans-serif; }
.stApp { background:linear-gradient(155deg,#100d2d 0%,#231a54 45%,#151a3d 100%); color:#f7f4ff; }
.block-container { max-width:760px; padding-top:1rem; padding-bottom:5rem; }
[data-testid="stHeader"] { background:transparent; }
/* Nour-facing app: hide Streamlit's unlabeled developer toolbar so mobile users
   only see LUMINA controls with explicit text labels. App management remains
   available from Streamlit Community Cloud. */
[data-testid="stToolbar"] { display:none !important; }
[data-testid="stDecoration"] { display:none !important; }
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
.track-card { background:rgba(255,255,255,.055); border:1px solid rgba(255,255,255,.1); border-radius:18px; padding:14px; margin-bottom:10px; }
.stButton>button { width:100%; border-radius:14px; min-height:46px; font-weight:800; border:0; background:linear-gradient(135deg,#ff758c,#ff7eb3 50%,#7873f5); color:white; }
.stTextInput input,.stTextArea textarea { border-radius:14px !important; }
div[data-testid="stTabs"] button { font-weight:800; }
@media (max-width:640px){ .block-container{padding-left:.8rem;padding-right:.8rem}.brand{font-size:1.85rem}.hello{font-size:1.18rem}.stat{min-height:78px;padding:9px} }
</style>
"""


def apply_theme() -> None:
    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)
