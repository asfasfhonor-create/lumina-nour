import streamlit as st
from lumina.ai_service import AIServiceError, GeminiService
from lumina.config import APP_ICON, APP_INITIAL_SIDEBAR_STATE, APP_LAYOUT, APP_TITLE
from lumina.home import render_home_foundation
from lumina.session_state import initialize_session_state
from lumina.quick_access import render_quick_access
from lumina.theme import apply_theme
from lumina.world_router import render_active_world

st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout=APP_LAYOUT,
    initial_sidebar_state=APP_INITIAL_SIDEBAR_STATE,
)

apply_theme()


initialize_session_state()

api_key = st.secrets.get("GEMINI_API_KEY", None)
if not api_key:
    api_key = st.sidebar.text_input("Gemini API Key", type="password")
    if not api_key:
        st.info("الأدوات الذكية تحتاج Gemini API Key. Nour's World نفسها تعمل بدون المفتاح.")

ai = GeminiService(api_key)

try:
    if not render_active_world(ai):
        render_home_foundation()
        render_quick_access(ai)
except AIServiceError as exc:
    st.warning(str(exc))
    st.caption("المحاولة لم تُسجل كنجاح أو Mastery بسبب فشل خدمة الذكاء الاصطناعي.")

st.caption("LUMINA · built for Nour ✨ | Development branch · التقدم الحالي تجريبي حتى تفعيل الحفظ الدائم")
