from datetime import date
import base64
from pathlib import Path

import streamlit as st

from lumina.learning.missions import choose_mission
from lumina.persistence.session_store import get_learning_store
from lumina.module_registry import get_module, get_school_subjects
from lumina.session_state import current_level
from lumina.persistence.profile_state import persist_profile_state
from lumina.learning.missions import get_lesson_by_id, get_module_for_lesson_id
from lumina.context_help import help_text, render_home_help


def render_home_foundation() -> None:
    """Render the current Nour's World foundation without owning learning business logic."""
    photo_col, hero_col = st.columns([1.25, 4], vertical_alignment="center")
    with photo_col:
        photo_bytes = Path("assets/nour_avatar.jpg").read_bytes()
        photo_b64 = base64.b64encode(photo_bytes).decode("ascii")
        st.markdown(
            f"""
            <div class="nour-photo-wrap" aria-label="صورة نور">
              <div class="nour-photo-glow">
                <img src="data:image/jpeg;base64,{photo_b64}" alt="نور" />
              </div>
              <div class="nour-photo-badge">✨ NOUR</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with hero_col:
        st.markdown(
        """
        <div class="hero">
          <div class="brand">LUMINA · NOUR'S WORLD</div>
          <div class="hello">أهلاً يا نور ✨ جاهزة نبدأ حاجة حلوة النهارده؟</div>
          <div class="muted">عالمك للمذاكرة والاكتشاف والإنجليزي والذكاء الاصطناعي — خطوة صغيرة كل يوم.</div>
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
            f'<div class="stat">🔥 <b>{st.session_state.streak} أيام</b><span class="muted">أيام التعلّم المتتالية</span></div>',
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            f'<div class="stat">🌱 <b>المستوى {level_number}</b><span class="muted">مستكشفة</span></div>',
            unsafe_allow_html=True,
        )

    badges = st.session_state.get("badges", [])
    if badges:
        st.caption("🏅 شاراتك: " + " · ".join(badges))

    _render_daily_mission()
    _render_learning_worlds()

    st.markdown("---")
    if st.button("🔎 ابحثي في المنهج", key="open_curriculum_search", use_container_width=True, help=help_text("curriculum_search")):
        st.session_state.active_world = "curriculum_search"
        st.rerun()

    top_left, top_right = st.columns(2)
    with top_left:
        if st.button("📅 خطتي", key="open_weekly_plan", use_container_width=True, help=help_text("weekly_plan")):
            st.session_state.active_world = "weekly"
            st.rerun()
    with top_right:
        if st.button("🧪 وضع الاختبار", key="open_exam_mode", use_container_width=True, help=help_text("exam_mode")):
            st.session_state.active_world = "exam"
            st.rerun()

    bottom_left, bottom_right = st.columns(2)
    with bottom_left:
        if st.button("📝 مراجعاتي", key="open_review_center", use_container_width=True, help=help_text("review_center")):
            st.session_state.active_world = "review"
            st.rerun()
    with bottom_right:
        if st.button("👨‍👧 لوحة وليّ الأمر", key="open_parent_dashboard", use_container_width=True):
            st.session_state.active_world = "parent"
            st.rerun()

    render_home_help()


def _render_daily_mission() -> None:
    store = get_learning_store()
    today = date.today().isoformat()

    if st.session_state.get("daily_mission_date") != today:
        st.session_state.daily_mission_date = today
        st.session_state.daily_mission_lesson_id = None

    mission = None
    target_id = st.session_state.get("daily_mission_lesson_id")
    if target_id:
        lesson = get_lesson_by_id(target_id)
        module_id = get_module_for_lesson_id(target_id)
        if lesson is not None and module_id is not None:
            from lumina.curriculum.mapped_curriculum import SUBJECT_LABELS
            from lumina.learning.missions import MissionRecommendation
            mission = MissionRecommendation(
                module_id=module_id,
                subject_label=SUBJECT_LABELS.get(module_id, module_id),
                lesson_id=lesson.id,
                lesson_title=lesson.title,
                source_pages=lesson.source_pages,
                reason="مهمة اليوم المختارة",
            )

    if mission is None:
        mission = choose_mission(store)
        if mission is None:
            return
        st.session_state.daily_mission_lesson_id = mission.lesson_id
        st.session_state.daily_mission_date = today
        persist_profile_state()

    st.markdown('<div class="section-title">🎯 مهمة اليوم</div>', unsafe_allow_html=True)
    st.markdown(
        f'<div class="mission"><b>{mission.subject_label} · {mission.lesson_title}</b><br>'
        f'<span class="muted">{mission.reason} · {mission.source_pages}</span></div>',
        unsafe_allow_html=True,
    )

    if st.button("ابدئي مهمة اليوم", key="open_daily_mission"):
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
                '<small>عالم تعلّم منظم</small></div>',
                unsafe_allow_html=True,
            )
            if module.id in {"english", "science", "math", "ict", "arabic", "social", "religion"}:
                labels = {
                    "english": "ابدئي مغامرة الإنجليزي",
                    "science": "ادخلي معمل العلوم",
                    "math": "ابدئي تحدّي الرياضيات",
                    "ict": "ادخلي معمل الكمبيوتر",
                    "arabic": "ادخلي عالم العربي",
                    "social": "ابدئي مغامرة الدراسات",
                    "religion": "ابدئي رحلة الدين",
                }
                label = labels[module.id]
                if st.button(label, key=f"open_world_{module.id}", help=help_text(module.id)):
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
            '<div class="mission"><b>محقق الذكاء الاصطناعي · تحديات كتابة الأوامر · التحقق من المعلومات</b><br>'
            '<span class="muted">نتعلم نسأل صح، نراجع الإجابات، ونبحث عن الدليل بدل الثقة العمياء.</span></div>',
            unsafe_allow_html=True,
        )
        if st.button("ادخلي عالم الذكاء الاصطناعي", key="open_world_ai", help=help_text("ai")):
            st.session_state.active_world = "ai"
            st.rerun()
