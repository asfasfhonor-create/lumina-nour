import streamlit as st

from lumina.learning.weekly_plan import build_weekly_plan
from lumina.persistence.session_store import get_learning_store


def render_weekly_plan() -> None:
    store = get_learning_store()
    plan = build_weekly_plan(store, limit=5)

    st.markdown('<div class="section-title">📅 الخطة الأسبوعية</div>', unsafe_allow_html=True)
    st.caption("خطة صغيرة ومتوازنة: المراجعات المستحقة أولًا، ثم تعلم جديد من مواد مختلفة.")

    if not plan:
        st.success("كل المحتوى المرسوم مراجع حاليًا. هنستخدم الخطة لاحقًا لتثبيت الإتقان.")
        return

    for index, item in enumerate(plan, start=1):
        with st.container(border=True):
            st.write(f"{index}. {item.subject_label} · {item.lesson_title}")
            st.caption(f"{item.reason} · {item.source_pages}")
            if st.button(
                "ابدئي الدرس",
                key=f"weekly_open_{item.lesson_id}",
                use_container_width=True,
            ):
                st.session_state.focus_lesson_id = item.lesson_id
                st.session_state.active_world = "lesson_focus"
                st.rerun()

    st.info(
        "الخطة لا تعني إن نور لازم تخلص الخمس مهام مرة واحدة؛ "
        "هي ترتيب ذكي للأولوية ويتغير مع الأخطاء والمراجعات."
    )
