from datetime import datetime, timedelta, timezone

import streamlit as st

from lumina.curriculum.mapped_curriculum import MAPPED_CURRICULUM, SUBJECT_LABELS, all_mapped_lessons
from lumina.curriculum.coverage import SOURCE_COVERAGE
from lumina.learning.progress import derive_mastery, mastery_label
from lumina.persistence.session_store import get_learning_store
from lumina.persistence.backup import export_learning_backup, restore_learning_backup


def render_parent_dashboard(parent_pin: str | None) -> None:
    st.markdown('<div class="section-title">👨‍👧 Parent Dashboard</div>', unsafe_allow_html=True)

    if not parent_pin:
        st.info(
            "Parent Dashboard is protected by design. Configure PARENT_PIN in Streamlit secrets "
            "before enabling this area."
        )
        return

    if not st.session_state.get("parent_unlocked", False):
        entered = st.text_input("Parent PIN", type="password", key="parent_pin_input")
        if st.button("Open Parent Dashboard", key="parent_unlock"):
            if entered == parent_pin:
                st.session_state.parent_unlocked = True
                st.rerun()
            else:
                st.error("PIN غير صحيح.")
        return

    if st.button("Lock Parent Dashboard", key="parent_lock"):
        st.session_state.parent_unlocked = False
        st.rerun()

    store = get_learning_store()
    attempts = store.get_attempts()
    mistakes = store.get_mistakes(unresolved_only=True)
    reviews = store.get_reviews("due")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Learning attempts", len(attempts))
    with c2:
        st.metric("Mistakes to review", len(mistakes))
    with c3:
        st.metric("Reviews due", len(reviews))

    st.markdown("### Weekly learning snapshot")
    cutoff = datetime.now(timezone.utc) - timedelta(days=7)

    def _is_recent(item: dict) -> bool:
        raw = item.get("created_at")
        if not raw:
            return False
        try:
            when = raw if isinstance(raw, datetime) else datetime.fromisoformat(str(raw))
            if when.tzinfo is None:
                when = when.replace(tzinfo=timezone.utc)
            return when >= cutoff
        except (TypeError, ValueError):
            return False

    recent_attempts = [item for item in attempts if _is_recent(item)]
    recent_correct = sum(1 for item in recent_attempts if item.get("correct") is True)
    recent_mistakes = [item for item in store.get_mistakes() if _is_recent(item)]
    active_subjects = sorted({
        item.get("module_id")
        for item in recent_attempts
        if item.get("module_id")
    })

    w1, w2, w3 = st.columns(3)
    with w1:
        st.metric("Attempts · 7 days", len(recent_attempts))
    with w2:
        st.metric("Successful · 7 days", recent_correct)
    with w3:
        st.metric("New mistakes · 7 days", len(recent_mistakes))

    if active_subjects:
        st.caption(
            "Subjects active this week: "
            + " · ".join(SUBJECT_LABELS.get(sid, sid) for sid in active_subjects)
        )
    else:
        st.caption("No timestamped learning evidence in the last 7 days yet.")

    badges = st.session_state.get("badges", [])
    if badges:
        st.caption("Badges earned: " + " · ".join(badges))

    profile = st.session_state.get("english_profile", {})
    st.markdown("### Real English profile")
    if profile:
        st.write(
            f"Starting band: **{profile.get('broad_band', '—')}** · "
            f"baseline {profile.get('baseline_correct', 0)}/{profile.get('baseline_total', 0)}"
        )
        if profile.get("support_note"):
            st.caption(profile["support_note"])
    else:
        st.caption("No Real English baseline completed yet.")

    st.markdown("### Trusted source coverage")
    st.caption("LUMINA لا يفترض Term غير موجود في المصادر الموثوقة.")
    for subject_id, coverage in SOURCE_COVERAGE.items():
        st.write(
            f"**{SUBJECT_LABELS.get(subject_id, subject_id)}** — "
            + ", ".join(coverage.supplied_terms)
        )

    st.markdown("### Curriculum progress — all subjects")
    total_started = 0
    total_mapped = 0

    for subject_id, units in MAPPED_CURRICULUM.items():
        subject_lessons = all_mapped_lessons(subject_id)
        total_mapped += len(subject_lessons)
        started = 0
        needs_review = 0
        mastered = 0

        for lesson in subject_lessons:
            snapshot = derive_mastery(
                store.get_attempts(lesson.id),
                store.get_mistakes(lesson.id),
            )
            if snapshot.state != "not_started":
                started += 1
            if snapshot.state == "needs_review":
                needs_review += 1
            if snapshot.state == "mastered":
                mastered += 1

        total_started += started
        with st.expander(
            f"{SUBJECT_LABELS.get(subject_id, subject_id)} · {started}/{len(subject_lessons)} started",
            expanded=False,
        ):
            st.write(
                f"Needs review: **{needs_review}** · Mastered: **{mastered}** · "
                f"Mapped lessons: **{len(subject_lessons)}**"
            )
            for unit_title, lessons in units.items():
                unit_states = [
                    derive_mastery(store.get_attempts(lesson.id), store.get_mistakes(lesson.id)).state
                    for lesson in lessons
                ]
                unit_started = sum(state != "not_started" for state in unit_states)
                unit_review = sum(state == "needs_review" for state in unit_states)
                unit_mastered = sum(state == "mastered" for state in unit_states)
                st.caption(
                    f"{unit_title}: started {unit_started}/{len(lessons)} · "
                    f"review {unit_review} · mastered {unit_mastered}"
                )

    if mistakes:
        st.markdown("### Current weak points")
        for mistake in mistakes:
            subject = SUBJECT_LABELS.get(mistake.get("module_id"), mistake.get("module_id", ""))
            st.write(
                f"• **{subject}** · {mistake.get('lesson_title', mistake.get('lesson_id'))} — "
                f"{mistake.get('mistake_type', 'learning mistake')}"
            )

    st.caption(
        f"Mapped curriculum lessons across all subjects: {total_mapped} · "
        f"started: {total_started} · progress is based on evidence, not button clicks."
    )

    _render_backup_tools()


def _render_backup_tools() -> None:
    st.markdown("### Backup / Restore")
    st.caption(
        "Portable safety copy. When Neon is active, the database remains the primary source of truth. "
        "The backup contains learning progress, never database passwords or API keys."
    )

    st.download_button(
        "Download learning backup",
        data=export_learning_backup(),
        file_name="lumina_nour_learning_backup.json",
        mime="application/json",
        key="download_learning_backup",
    )

    uploaded = st.file_uploader(
        "Restore a learning backup",
        type=["json"],
        key="restore_learning_backup_file",
    )
    if uploaded and st.button("Restore this backup", key="restore_learning_backup_button"):
        ok, message = restore_learning_backup(uploaded.getvalue().decode("utf-8"))
        if ok:
            st.success(message)
            st.rerun()
        else:
            st.error(message)
