import streamlit as st
from lumina.ai_service import AIServiceError, GeminiService
from lumina.persistence.base import PersistenceError
from lumina.access_control import require_app_access
from lumina.config import APP_ICON, APP_INITIAL_SIDEBAR_STATE, APP_LAYOUT, APP_TITLE
from lumina.home import render_home_foundation
from lumina.session_state import initialize_session_state
from lumina.quick_access import render_quick_access
from lumina.persistence.profile_state import hydrate_profile_state, verify_persistence_after_hydration
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
verify_persistence_after_hydration()

api_key = st.secrets.get("GEMINI_API_KEY", None)
ai = GeminiService(api_key)
parent_pin = st.secrets.get("PARENT_PIN", None)

persistence_warning = st.session_state.get("persistence_warning")
if persistence_warning:
    st.warning(persistence_warning)
    st.caption("الحفظ التلقائي متوقف مؤقتًا في هذه الجلسة. يفضّل عدم إغلاق الصفحة قبل حفظ نسخة احتياطية من لوحة وليّ الأمر.")

try:
    if not render_active_world(ai, parent_pin=parent_pin, app_pin_configured=bool(app_pin)):
        render_home_foundation()
        render_quick_access(ai)
except AIServiceError as exc:
    st.warning(str(exc))
    st.caption("لم يتم تسجيل هذه المحاولة ضمن التقدّم لأن الأداة الذكية لم تُكمل عملها.")
except PersistenceError as exc:
    st.session_state.persistence_disabled_for_session = True
    st.session_state.persistence_warning = str(exc)
    st.warning(str(exc))
    st.caption("سيستمر البرنامج مؤقتًا داخل هذه الجلسة، لكن يُفضّل عدم إغلاق الصفحة حتى يعود الحفظ التلقائي.")

storage = persistence_status()
if storage["durable"] and st.session_state.get("persistence_verified", False):
    st.caption("✨ LUMINA · عالم نور · التقدّم محفوظ تلقائيًا")
elif storage["durable"]:
    st.caption("✨ LUMINA · عالم نور · جارٍ التحقق من الحفظ التلقائي")
else:
    st.caption("✨ LUMINA · عالم نور")
