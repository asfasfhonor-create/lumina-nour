import hmac

import streamlit as st


def require_app_access(app_pin: str | None) -> bool:
    """Optional whole-app gate.

    The app remains usable when no PIN is configured, which keeps development friction low.
    Production can enable the gate by setting NOUR_APP_PIN in Streamlit secrets.
    """
    if not app_pin:
        return True

    if st.session_state.get("app_unlocked", False):
        return True

    st.markdown("## 🔐 Nour's World")
    st.caption("ادخلي الـPIN لفتح عالم نور.")
    entered = st.text_input("PIN", type="password", key="nour_app_pin_input")

    if st.button("فتح LUMINA", key="nour_app_unlock"):
        if hmac.compare_digest(str(entered), str(app_pin)):
            st.session_state.app_unlocked = True
            st.rerun()
        else:
            st.error("PIN غير صحيح.")

    return False
