import streamlit as st
from lumina.ai_service import AIServiceError, GeminiService
from lumina.persistence.base import PersistenceError
from lumina.access_control import require_app_access
from lumina.config import APP_ICON, APP_INITIAL_SIDEBAR_STATE, APP_LAYOUT, APP_TITLE
from lumina.home import render_home_foundation
from lumina.session_state import initialize_session_state
from lumina.quick_access import render_quick_access
from lumina.persistence.profile_state import hydrate_profile_state
from lumina.persistence.session_store import persistence_status
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

app_pin = st.secrets.get("NOUR_APP_PIN", None)
if not require_app_access(app_pin):
    st.stop()

hydrate_profile_state()

api_key = st.secrets.get("GEMINI_API_KEY", None)
if not api_key:
    api_key = st.sidebar.text_input("Gemini API Key", type="password")
    if not api_key:
        st.info("الأدوات الذكية تحتاج Gemini API Key. Nour's World نفسها تعمل بدون المفتاح.")

ai = GeminiService(api_key)
parent_pin = st.secrets.get("PARENT_PIN", None)

persistence_warning = st.session_state.get("persistence_warning")
if persistence_warning:
    st.warning(persistence_warning)
    st.caption("الحفظ السحابي متوقف لهذه الجلسة؛ لا تغلقي الجلسة قبل تنزيل Backup من Parent Dashboard.")

try:
    if not render_active_world(ai, parent_pin=parent_pin, app_pin_configured=bool(app_pin)):
        render_home_foundation()
        render_quick_access(ai)
except AIServiceError as exc:
    st.warning(str(exc))
    st.caption("المحاولة لم تُسجل كنجاح أو Mastery بسبب فشل خدمة الذكاء الاصطناعي.")
except PersistenceError as exc:
    st.session_state.persistence_disabled_for_session = True
    st.session_state.persistence_warning = str(exc)
    st.warning(str(exc))
    st.caption("تم التحويل مؤقتًا للحفظ داخل الجلسة الحالية حتى لا يتوقف البرنامج.")

storage = persistence_status()
storage_note = "الحفظ الدائم فعال" if storage["durable"] else "الحفظ الدائم غير مفعل"
st.caption(
    f"LUMINA · built for Nour ✨ | Development branch · "
    f"{storage_note} · {storage['label']}"
)
