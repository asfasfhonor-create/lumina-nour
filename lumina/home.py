from datetime import date
from pathlib import Path

import streamlit as st

from lumina.learning.missions import choose_mission
from lumina.persistence.session_store import get_learning_store
from lumina.module_registry import get_module, get_school_subjects
from lumina.session_state import current_level
from lumina.persistence.profile_state import persist_profile_state
from lumina.learning.missions import get_lesson_by_id, get_module_for_lesson_id
from lumina.context_help import help_text, render_home_help
from lumina.language_policy import PARENT_AREA_LABEL, ui_label, world_action, world_title


ONBOARDING_VERSION = 2


def _load_nour_photo_b64() -> str:
    parts_dir = Path("assets/nour_avatar_parts_v2")
    ordered_names = ("00a.txt", "00b.txt", "02.txt", "03.txt", "04.txt", "05.txt", "06.txt", "07.txt")
    parts = [parts_dir / name for name in ordered_names]
    if not all(part.exists() for part in parts):
        return ""
    return "".join(part.read_text(encoding="utf-8").strip() for part in parts)


def render_home_foundation() -> None:
    """Render the current Nour's World foundation without owning learning business logic."""
    photo_col, hero_col = st.columns([1.55, 4], vertical_alignment="center")
    with photo_col:
        photo_b64 = _load_nour_photo_b64()
        st.markdown(
            f"""
            <div class="nour-photo-wrap" aria-label="Nour photo">
              <div class="nour-photo-glow">
                <img src="data:image/jpeg;base64,{photo_b64}" alt="Nour photo" />
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
          <div class="hello">Hi Nour ✨ Ready to discover something new today?</div>
          <div class="muted">Your world for learning, discovery, English & AI.<br><small>One small step, every day.</small></div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    _render_first_run_welcome()
    if int(st.session_state.get("onboarding_version", 0)) < ONBOARDING_VERSION:
        return

    level_number = current_level()
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            f'<div class="stat">⭐ <b>{st.session_state.xp} XP</b><span class="muted">Your points</span></div>',
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            f'<div class="stat">🔥 <b>{st.session_state.streak} days</b><span class="muted">Learning streak</span></div>',
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            f'<div class="stat">🌱 <b>Level {level_number}</b><span class="muted">Explorer</span></div>',
            unsafe_allow_html=True,
        )

    badges = st.session_state.get("badges", [])
    if badges:
        st.caption("🏅 Your badges: " + " · ".join(badges))

    _render_start_studying()
    _render_daily_mission()
    _render_learning_worlds()

    st.markdown("---")
    if st.button("🔎 " + ui_label("curriculum_search"), key="open_curriculum_search", use_container_width=True, help=help_text("curriculum_search")):
        st.session_state.active_world = "curriculum_search"
        st.rerun()

    top_left, top_right = st.columns(2)
    with top_left:
        if st.button("📅 " + ui_label("weekly_plan"), key="open_weekly_plan", use_container_width=True, help=help_text("weekly_plan")):
            st.session_state.active_world = "weekly"
            st.rerun()
    with top_right:
        if st.button("🧪 " + ui_label("exam_mode"), key="open_exam_mode", use_container_width=True, help=help_text("exam_mode")):
            st.session_state.active_world = "exam"
            st.rerun()

    if st.button("📝 " + ui_label("review_center"), key="open_review_center", use_container_width=True, help=help_text("review_center")):
        st.session_state.active_world = "review"
        st.rerun()

    with st.expander("👨‍👧 " + PARENT_AREA_LABEL, expanded=False):
        st.caption("A separate area for parents to follow progress and learning sources.")
        if st.button("Open Parent Dashboard", key="open_parent_dashboard", use_container_width=True):
            st.session_state.active_world = "parent"
            st.rerun()

    render_home_help()


def _render_first_run_welcome() -> None:
    if int(st.session_state.get("onboarding_version", 0)) >= ONBOARDING_VERSION:
        return

    st.markdown(
        """
        <div class="mission">
          <b>✨ A little surprise before you start</b><br>
          <span class="muted">
          This world was built with AI to help you learn, explore, and create.
          You do not need to know coding to start building an idea —
          Ask well, try, test, and improve.
          </span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.caption("Your first tour takes only a few minutes. No test. No grades.")

    left, right = st.columns(2)
    with left:
        if st.button(
            "🤖 Show me how to build an idea with AI",
            key="first_run_ai",
            use_container_width=True,
        ):
            st.session_state.first_run_complete = True
            st.session_state.onboarding_version = ONBOARDING_VERSION
            st.session_state.ai_lab_mode = "✨ Build an idea with AI"
            persist_profile_state()
            st.session_state.active_world = "ai"
            st.rerun()
    with right:
        if st.button(
            "🌍 Let me choose something to explore",
            key="first_run_choose",
            use_container_width=True,
        ):
            st.session_state.first_run_complete = True
            st.session_state.onboarding_version = ONBOARDING_VERSION
            persist_profile_state()
            st.rerun()


def _render_start_studying() -> None:
    """Put the learner's primary action above dashboard/utility content."""
    st.markdown('<div class="section-title">🎓 Start Studying</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="mission"><b>Not sure what to do?</b><br>'
        '<span class="muted">LUMINA can choose a lesson for you, or you can pick a subject yourself.</span></div>',
        unsafe_allow_html=True,
    )

    if st.button("▶ Start today's lesson", key="start_studying_now", use_container_width=True):
        store = get_learning_store()
        mission = choose_mission(store)
        if mission is not None:
            st.session_state.daily_mission_lesson_id = mission.lesson_id
            st.session_state.daily_mission_date = date.today().isoformat()
            st.session_state.active_world = "mission"
            persist_profile_state()
            st.rerun()
        else:
            st.info("No lesson is available right now. Choose a subject below.")

    left, right = st.columns(2)
    with left:
        if st.button("📚 Choose a subject", key="start_choose_subject", use_container_width=True):
            st.session_state.show_subject_picker = True
    with right:
        if st.button("🔁 Review & Practice", key="start_review", use_container_width=True):
            st.session_state.active_world = "review"
            st.rerun()

    if st.session_state.get("show_subject_picker", False):
        subject_options = [
            ("English Adventure", "english"),
            ("Science Lab", "science"),
            ("Math Quest", "math"),
            ("Arabic World", "arabic"),
            ("Social Studies", "social"),
            ("Religion Journey", "religion"),
            ("ICT Lab", "ict"),
        ]
        labels = [label for label, _ in subject_options]
        selected = st.selectbox("What do you want to study?", labels, key="study_subject_picker")
        selected_id = dict(subject_options)[selected]
        if st.button("Open this subject", key="open_selected_subject", use_container_width=True):
            st.session_state.active_world = selected_id
            st.session_state.show_subject_picker = False
            st.rerun()


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

    st.markdown(f'<div class="section-title">🎯 {ui_label("daily_mission")}</div>', unsafe_allow_html=True)
    st.markdown(
        f'<div class="mission"><b>{mission.subject_label} · {mission.lesson_title}</b><br>'
        f'<span class="muted">{mission.reason} · {mission.source_pages}</span></div>',
        unsafe_allow_html=True,
    )

    if st.button(ui_label("start_daily_mission"), key="open_daily_mission"):
        st.session_state.active_world = "mission"
        st.rerun()


def _render_learning_worlds() -> None:
    st.markdown(f'<div class="section-title">📚 {ui_label("learning_worlds")}</div>', unsafe_allow_html=True)
    cols = st.columns(2)

    for index, module in enumerate(get_school_subjects()):
        with cols[index % 2]:
            st.markdown(
                f'<div class="subject"><h4>{module.icon} {world_title(module.id, module.title)}</h4>'
                f'<span class="muted">{module.description}</span><br>'
                '<small>Structured learning world</small></div>',
                unsafe_allow_html=True,
            )
            if module.id in {"english", "science", "math", "ict", "arabic", "social", "religion"}:
                label = world_action(module.id)
                if st.button(label, key=f"open_world_{module.id}", help=help_text(module.id)):
                    st.session_state.active_world = module.id
                    st.rerun()
            else:
                st.button(
                    "Coming soon",
                    key=f"open_world_{module.id}",
                    disabled=True,
                    help="This world will open after it is connected to the learning engine.",
                )

    ai_module = get_module("ai")
    if ai_module:
        st.markdown(
            f'<div class="section-title">{ai_module.icon} {world_title("ai", ai_module.title)}</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div class="mission"><b>AI Detective · Prompt challenges · Information verification</b><br>'
            '<span class="muted">Learn to ask better questions, check answers, and look for evidence instead of trusting AI blindly.</span></div>',
            unsafe_allow_html=True,
        )
        if st.button(world_action("ai"), key="open_world_ai", help=help_text("ai")):
            st.session_state.active_world = "ai"
            st.rerun()
