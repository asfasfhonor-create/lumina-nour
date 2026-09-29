from datetime import datetime, timedelta, timezone

import streamlit as st

from lumina.curriculum.mapped_curriculum import MAPPED_CURRICULUM, SUBJECT_LABELS, all_mapped_lessons
from lumina.curriculum.coverage import SOURCE_COVERAGE
from lumina.learning.progress import derive_mastery, mastery_label
from lumina.persistence.session_store import get_learning_store, persistence_status
from lumina.persistence.base import PersistenceError
from lumina.persistence.backup import export_learning_backup, restore_learning_backup
from lumina.learning.evidence_cache import group_by_lesson
from lumina.readiness import build_release_readiness, is_release_ready, release_blockers


def render_parent_dashboard(parent_pin: str | None, *, ai_available: bool = False, app_pin_configured: bool = False) -> None:
    st.markdown('<div class="section-title">👨‍👧 لوحة وليّ الأمر</div>', unsafe_allow_html=True)

    if not parent_pin:
        st.info(
            "Parent Dashboard is protected by design. Configure PARENT_PIN in Streamlit secrets "
            "before enabling this area."
        )
        return

    if not st.session_state.get("parent_unlocked", False):
        entered = st.text_input("رمز وليّ الأمر", type="password", key="parent_pin_input")
        if st.button("فتح لوحة وليّ الأمر", key="parent_unlock"):
            if entered == parent_pin:
                st.session_state.parent_unlocked = True
                st.rerun()
            else:
                st.error("PIN غير صحيح.")
        return

    if st.button("قفل لوحة وليّ الأمر", key="parent_lock"):
        st.session_state.parent_unlocked = False
        st.rerun()

    store = get_learning_store()
    status = persistence_status()

    st.markdown("### حالة النظام")
    if status["durable"]:
        st.success(f"الحفظ الدائم يعمل: {status['label']}")
        if st.button("اختبر اتصال الحفظ السحابي", key="parent_test_persistence"):
            try:
                if store.health_check():
                    st.session_state.persistence_verified = True
                    st.success("اتصال قاعدة البيانات والجداول المطلوبة يعملان الآن.")
                    st.rerun()
                else:
                    st.session_state.persistence_verified = False
                    st.warning("الاتصال موجود لكن مخطط قاعدة البيانات غير مكتمل أو غير جاهز.")
            except PersistenceError as exc:
                st.session_state.persistence_verified = False
                st.error(str(exc))
    elif status["mode"] == "session_fallback":
        st.warning("الحفظ السحابي غير متاح في الجلسة الحالية. نزّل نسخة احتياطية قبل الإغلاق.")
    else:
        st.warning("الحفظ الدائم غير مفعّل حاليًا؛ التقدّم محفوظ داخل الجلسة فقط.")

    st.markdown("### جاهزية النسخة")
    readiness = build_release_readiness(
        ai_available=ai_available,
        app_pin_configured=app_pin_configured,
        parent_pin_configured=bool(parent_pin),
        storage_status=status,
        storage_verified=bool(st.session_state.get("persistence_verified", False)),
    )
    if is_release_ready(readiness):
        st.success("كل متطلبات النسخة الأساسية جاهزة.")
    else:
        blockers = release_blockers(readiness)
        st.warning(
            "متطلبات لسه محتاجة إكمال: "
            + " · ".join(item.label for item in blockers)
        )

    for item in readiness:
        if item.ready:
            icon = "✅"
        elif item.required:
            icon = "⚠️"
        else:
            icon = "ℹ️"
        requirement = "" if item.required else " · اختياري"
        st.write(f"{icon} **{item.label}** — {item.detail}{requirement}")

    attempts = store.get_attempts()
    all_mistakes = store.get_mistakes()
    mistakes = [item for item in all_mistakes if not item.get("resolved", False)]
    reviews = store.get_reviews("due")
    attempts_by_lesson = group_by_lesson(attempts)
    mistakes_by_lesson = group_by_lesson(all_mistakes)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("محاولات التعلّم", len(attempts))
    with c2:
        st.metric("أخطاء للمراجعة", len(mistakes))
    with c3:
        st.metric("مراجعات مستحقة", len(reviews))

    st.markdown("### ملخص آخر 7 أيام")
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
    recent_mistakes = [item for item in all_mistakes if _is_recent(item)]
    active_subjects = sorted({
        item.get("module_id")
        for item in recent_attempts
        if item.get("module_id")
    })

    w1, w2, w3 = st.columns(3)
    with w1:
        st.metric("المحاولات · 7 أيام", len(recent_attempts))
    with w2:
        st.metric("الإجابات الصحيحة · 7 أيام", recent_correct)
    with w3:
        st.metric("أخطاء جديدة · 7 أيام", len(recent_mistakes))

    if active_subjects:
        st.caption(
            "المواد النشطة هذا الأسبوع: "
            + " · ".join(SUBJECT_LABELS.get(sid, sid) for sid in active_subjects)
        )
    else:
        st.caption("لسه مفيش نشاط تعلّم مسجل خلال آخر 7 أيام.")

    badges = st.session_state.get("badges", [])
    if badges:
        st.caption("الشارات المكتسبة: " + " · ".join(badges))

    profile = st.session_state.get("english_profile", {})
    st.markdown("### مستوى Real English")
    if profile:
        st.write(
            f"Starting band: **{profile.get('broad_band', '—')}** · "
            f"baseline {profile.get('baseline_correct', 0)}/{profile.get('baseline_total', 0)}"
        )
        if profile.get("support_note"):
            st.caption(profile["support_note"])
    else:
        st.caption("لسه ما اتعملش اختبار تحديد المستوى لـ Real English.")

    st.markdown("### تغطية المصادر المعتمدة")
    st.caption("LUMINA لا يفترض Term غير موجود في المصادر الموثوقة.")
    for subject_id, coverage in SOURCE_COVERAGE.items():
        st.write(
            f"**{SUBJECT_LABELS.get(subject_id, subject_id)}** — "
            + ", ".join(coverage.supplied_terms)
        )

    st.markdown("### تقدّم المنهج — كل المواد")
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
                attempts_by_lesson.get(lesson.id, []),
                mistakes_by_lesson.get(lesson.id, []),
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
                    derive_mastery(
                        attempts_by_lesson.get(lesson.id, []),
                        mistakes_by_lesson.get(lesson.id, []),
                    ).state
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
        st.markdown("### نقاط محتاجة مراجعة")
        seen_weak_lessons = set()
        for mistake in mistakes:
            lesson_id = mistake.get("lesson_id")
            if not lesson_id or lesson_id in seen_weak_lessons:
                continue
            seen_weak_lessons.add(lesson_id)

            subject = SUBJECT_LABELS.get(mistake.get("module_id"), mistake.get("module_id", ""))
            with st.container(border=True):
                st.write(
                    f"**{subject}** · {mistake.get('lesson_title', lesson_id)} — "
                    f"{mistake.get('mistake_type', 'learning mistake')}"
                )
                if mistake.get("source_pages"):
                    st.caption(f"Source: {mistake['source_pages']}")
                if st.button(
                    "افتحي نقطة الضعف",
                    key=f"parent_open_weak_{lesson_id}",
                    use_container_width=True,
                ):
                    st.session_state.focus_lesson_id = lesson_id
                    st.session_state.active_world = "lesson_focus"
                    st.rerun()

    st.caption(
        f"Mapped curriculum lessons across all subjects: {total_mapped} · "
        f"started: {total_started} · progress is based on evidence, not button clicks."
    )

    _render_backup_tools(store)


def _render_backup_tools(store) -> None:
    st.markdown("### النسخة الاحتياطية والاستعادة")
    st.caption(
        "Portable safety copy. When Neon is active, the database remains the primary source of truth. "
        "The backup contains learning progress, never database passwords or API keys."
    )

    st.download_button(
        "تنزيل نسخة احتياطية",
        data=export_learning_backup(store),
        file_name="lumina_nour_learning_backup.json",
        mime="application/json",
        key="download_learning_backup",
    )

    uploaded = st.file_uploader(
        "استعادة نسخة احتياطية",
        type=["json"],
        key="restore_learning_backup_file",
    )
    if uploaded and st.button("استعادة هذه النسخة", key="restore_learning_backup_button"):
        ok, message = restore_learning_backup(uploaded.getvalue().decode("utf-8"), store)
        if ok:
            st.success(message)
            st.rerun()
        else:
            st.error(message)
