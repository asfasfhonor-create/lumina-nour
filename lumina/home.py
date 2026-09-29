from datetime import date

import streamlit as st

from lumina.learning.missions import choose_mission
from lumina.persistence.session_store import get_learning_store
from lumina.module_registry import get_module, get_school_subjects
from lumina.session_state import current_level


def render_home_foundation() -> None:
    """Render the current Nour's World foundation without owning learning business logic."""
    photo_col, hero_col = st.columns([1, 4])
    with photo_col:
        st.image("assets/nour_avatar.jpg", width=92)
    with hero_col:
        st.markdown(
        """
        <div class="hero">
          <div class="brand">LUMINA · NOUR'S WORLD</div>
          <div class="hello">أهلاً يا نور ✨ جاهزة لمهمة صغيرة النهارده؟</div>
          <div class="muted">مساحتك للمذاكرة، الاكتشاف، الإنجليزي والـ AI — خطوة ممتعة كل يوم.</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    level_number = current_level()
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            f'<div class="stat">⭐ <b>{st.session_state.xp} XP</b><span class="muted">نقاطك</span></div>',
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            f'<div class="stat">🔥 <b>{st.session_state.streak} أيام</b><span class="muted">Streak · تعلم فعلي</span></div>',
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            f'<div class="stat">🌱 <b>Level {level_number}</b><span class="muted">Explorer</span></div>',
            unsafe_allow_html=True,
        )

    badges = st.session_state.get("badges", [])
    if badges:
        st.caption("🏅 Badges: " + " · ".join(badges))

    _render_daily_mission()
    _render_learning_worlds()

    st.markdown("---")
    if st.button("🔎 ابحثي في المنهج", key="open_curriculum_search"):
        st.session_state.active_world = "curriculum_search"
        st.rerun()

    c_weekly, c_exam, c_review, c_parent = st.columns(4)
    with c_weekly:
        if st.button("📅 خطتي", key="open_weekly_plan"):
            st.session_state.active_world = "weekly"
            st.rerun()
    with c_exam:
        if st.button("🧪 Exam Mode", key="open_exam_mode"):
            st.session_state.active_world = "exam"
            st.rerun()
    with c_review:
        if st.button("📝 مراجعاتي", key="open_review_center"):
            st.session_state.active_world = "review"
            st.rerun()
    with c_parent:
        if st.button("👨‍👧 Parent Dashboard", key="open_parent_dashboard"):
            st.session_state.active_world = "parent"
            st.rerun()


def _render_daily_mission() -> None:
    store = get_learning_store()
    today = date.today().isoformat()

    if st.session_state.get("daily_mission_date") != today:
        st.session_state.daily_mission_date = today
        st.session_state.daily_mission_lesson_id = None

    mission = choose_mission(store)
    if mission is None:
        return

    st.markdown('<div class="section-title">🎯 مهمة اليوم</div>', unsafe_allow_html=True)
    st.markdown(
        f'<div class="mission"><b>{mission.subject_label} · {mission.lesson_title}</b><br>'
        f'<span class="muted">{mission.reason} · {mission.source_pages}</span></div>',
        unsafe_allow_html=True,
    )

    if st.button("ابدئي مهمة اليوم", key="open_daily_mission"):
        st.session_state.daily_mission_lesson_id = mission.lesson_id
        st.session_state.daily_mission_date = today
        st.session_state.active_world = "mission"
        st.rerun()


def _render_learning_worlds() -> None:
    st.markdown('<div class="section-title">📚 اختاري عالمك</div>', unsafe_allow_html=True)
    cols = st.columns(2)

    for index, module in enumerate(get_school_subjects()):
        with cols[index % 2]:
            st.markdown(
                f'<div class="subject"><h4>{module.icon} {module.title}</h4>'
                f'<span class="muted">{module.description}</span><br>'
                '<small>Structured learning world</small></div>',
                unsafe_allow_html=True,
            )
            if module.id in {"english", "science", "math", "ict", "arabic", "social", "religion"}:
                labels = {
                    "english": "ادخلي English Adventure",
                    "science": "ادخلي Science Lab",
                    "math": "ادخلي Math Quest",
                    "ict": "ادخلي ICT Lab",
                    "arabic": "ادخلي Arabic World",
                    "social": "ادخلي Social Detective",
                    "religion": "ادخلي Religion Journey",
                }
                label = labels[module.id]
                if st.button(label, key=f"open_world_{module.id}"):
                    st.session_state.active_world = module.id
                    st.rerun()
            else:
                st.button(
                    "قريبًا",
                    key=f"open_world_{module.id}",
                    disabled=True,
                    help="هنفتح العالم ده بعد ربطه بمحرك المنهج والتعلم.",
                )

    ai_module = get_module("ai")
    if ai_module:
        st.markdown(
            f'<div class="section-title">{ai_module.icon} {ai_module.title}</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div class="mission"><b>AI Detective + Prompt Challenges + Fact Checker</b><br>'
            '<span class="muted">نتعلم نسأل صح، نراجع الإجابات، ونبحث عن الدليل بدل الثقة العمياء.</span></div>',
            unsafe_allow_html=True,
        )
        if st.button("ادخلي AI Lab", key="open_world_ai"):
            st.session_state.active_world = "ai"
            st.rerun()
