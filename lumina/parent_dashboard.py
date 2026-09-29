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
from lumina.config import BUILD_LABEL
from lumina.curriculum.trusted_sources import (
    SourceUpload,
    build_trusted_record,
    NEON_OBJECT_STORAGE,
    SOURCE_ROLE_OFFICIAL,
    SOURCE_ROLE_SUPPLEMENTARY,
    SOURCE_ROLE_LABELS,
)
from lumina.curriculum.trusted_source_storage import StorageConfig, NeonTrustedSourceStorage
from lumina.persistence.trusted_source_catalog import NeonTrustedSourceCatalog


def _suggest_source_profile(filename: str) -> dict[str, str]:
    name = (filename or "").lower()

    subject = "english"
    display_name = filename
    resource_use = "support"
    resource_use_label = "مساعد عام"

    if "math" in name:
        subject = "math"
    elif "science" in name or "ساينس" in name or "prep3 notebook" in name:
        subject = "science"
    elif "english" in name:
        subject = "english"

    if ("guide" in name and "answer" in name) or (subject == "math" and "p3" in name):
        resource_use = "answer_guide"
        resource_use_label = "مرجع تصحيح"
    elif "assessment" in name or "final revision" in name or "p2" in name:
        resource_use = "assessment_revision"
        resource_use_label = "اختبارات ومراجعة"
    elif "notebook" in name:
        resource_use = "revision_exam"
        resource_use_label = "مراجعة وامتحانات"
    else:
        resource_use = "main_book"
        resource_use_label = "شرح وتدريب"

    if subject == "math":
        if resource_use == "main_book":
            display_name = "El-Moasser Maths · Main Book · Prep 3 · Term 1 · 2027"
        elif resource_use == "assessment_revision":
            display_name = "El-Moasser Maths · Assessments & Final Revision · Prep 3 · Term 1 · 2027"
        else:
            display_name = "El-Moasser Maths · Guide Answers · Prep 3 · Term 1 · 2027"
    elif subject == "science":
        if resource_use == "main_book":
            display_name = "El-Moasser Science · Main Book · Prep 3 · Term 1 · 2027"
        else:
            display_name = "El-Moasser Science · Notebook · Prep 3 · Term 1 · 2027"
    elif subject == "english":
        display_name = "El-Moasser English · Guide Answers · Prep 3 · Term 1 · 2027"

    return {
        "subject": subject,
        "display_name": display_name,
        "resource_use": resource_use,
        "resource_use_label": resource_use_label,
        "term_label": "Term 1",
        "publisher": "المعاصر",
        "edition_label": "2027",
    }


def render_parent_dashboard(parent_pin: str | None, *, ai_available: bool = False, app_pin_configured: bool = False) -> None:
    st.markdown('<div class="section-title">👨‍👧 لوحة وليّ الأمر</div>', unsafe_allow_html=True)

    if parent_pin:
        if not st.session_state.get("parent_unlocked", False):
            entered = st.text_input("رمز وليّ الأمر", type="password", key="parent_pin_input")
            if st.button("فتح لوحة وليّ الأمر", key="parent_unlock"):
                if entered == parent_pin:
                    st.session_state.parent_unlocked = True
                    st.rerun()
                else:
                    st.error("الرمز غير صحيح.")
            return

        if st.button("قفل لوحة وليّ الأمر", key="parent_lock"):
            st.session_state.parent_unlocked = False
            st.rerun()
    else:
        st.warning("حماية لوحة وليّ الأمر برمز دخول غير مفعّلة حاليًا. تقدر تستخدم اللوحة الآن، ويفضل تفعيل الرمز قبل الاعتماد النهائي.")

    store = get_learning_store()
    status = persistence_status()

    st.markdown("### حالة النظام")
    st.caption(f"نسخة التطبيق الحالية: {BUILD_LABEL}")
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
            f"المستوى المبدئي: **{profile.get('broad_band', '—')}** · "
            f"اختبار البداية {profile.get('baseline_correct', 0)}/{profile.get('baseline_total', 0)}"
        )
        if profile.get("support_note"):
            st.caption(profile["support_note"])
    else:
        st.caption("لسه ما اتعملش اختبار تحديد المستوى لـ Real English.")

    st.markdown("### تقدّم مهارات AI")
    ai_profile = st.session_state.get("ai_profile") or {}
    ai_skills = ai_profile.get("skills") or {}
    ai_skill_labels = {
        "prompting": "كتابة Prompt",
        "comparison": "مقارنة إجابات AI",
        "verification": "التحقق",
        "evidence": "تقييم جودة الدليل",
        "uncertainty": "التعامل مع عدم اليقين",
    }
    if ai_skills:
        for skill_id, label in ai_skill_labels.items():
            values = ai_skills.get(skill_id)
            if not values:
                continue
            attempts_count = int(values.get("attempts", 0))
            correct_count = int(values.get("correct", 0))
            st.write(f"• **{label}** — نجاح {correct_count}/{attempts_count}")
        st.caption(
            f"مهارات ظهر فيها دليل نجاح: "
            f"{ai_profile.get('completed_skills', 0)}/{len(ai_skill_labels)}"
        )
    else:
        st.caption("لسه مفيش نشاط AI Literacy مسجل لنور.")

    st.markdown("### تغطية المصادر المعتمدة")
    st.caption("LUMINA ما بيفترضش ترم أو جزء دراسي غير موجود في المصادر المعتمدة.")
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
            f"{SUBJECT_LABELS.get(subject_id, subject_id)} · بدأ {started}/{len(subject_lessons)}",
            expanded=False,
        ):
            st.write(
                f"محتاج مراجعة: **{needs_review}** · متقن: **{mastered}** · "
                f"الدروس المرتبطة: **{len(subject_lessons)}**"
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
                    f"{unit_title}: بدأ {unit_started}/{len(lessons)} · "
                    f"مراجعة {unit_review} · متقن {unit_mastered}"
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
                    f"{mistake.get('mistake_type', 'خطأ تعلّم')}"
                )
                if mistake.get("source_pages"):
                    st.caption(f"المصدر: {mistake['source_pages']}")
                if st.button(
                    "افتحي نقطة الضعف",
                    key=f"parent_open_weak_{lesson_id}",
                    use_container_width=True,
                ):
                    st.session_state.focus_lesson_id = lesson_id
                    st.session_state.active_world = "lesson_focus"
                    st.rerun()

    st.caption(
        f"إجمالي الدروس المرتبطة: {total_mapped} · "
        f"بدأ منها: {total_started} · التقدّم يعتمد على دليل تعلّم حقيقي، مش مجرد الضغط على الأزرار."
    )

    _render_trusted_sources()
    _render_backup_tools(store)



def _render_trusted_sources() -> None:
    st.markdown("### المصادر الدائمة")
    st.caption("أضف كتابًا أو مذكرة مرة واحدة كمصدر معتمد يفضل محفوظ بعد إغلاق البرنامج.")

    database_url = str(st.secrets.get("NEON_DATABASE_URL", "") or "").strip()
    learner_key = str(st.secrets.get("NOUR_LEARNER_KEY", "") or "").strip()
    storage_config = StorageConfig.from_mapping(st.secrets)

    if not database_url or not learner_key:
        st.info("الحفظ الدائم للمصادر غير جاهز لأن إعداد قاعدة البيانات ناقص.")
        return

    if storage_config is None:
        st.info("تخزين الملفات الدائم لسه محتاج تفعيل بيانات التخزين الآمنة في إعدادات التطبيق.")
        return

    storage = NeonTrustedSourceStorage(storage_config)
    catalog = NeonTrustedSourceCatalog(database_url, learner_key)

    if not storage.health_check():
        st.warning("تخزين الملفات الدائم غير متاح دلوقتي. جرّب مرة تانية لاحقًا.")
        return

    uploaded_files = st.file_uploader(
        "أضف كتابًا أو مذكرة كمصدر دائم",
        type=["pdf", "jpg", "jpeg", "png", "webp"],
        accept_multiple_files=True,
        key="parent_trusted_source_upload",
    )

    if uploaded_files:
        st.caption(
            f"تم اختيار **{len(uploaded_files)}** ملف. "
            "LUMINA هيصنّف كتب المعاصر المعروفة تلقائيًا، وتقدر تحفظهم كلهم بضغطة واحدة."
        )

        batch_profiles = []
        for uploaded in uploaded_files:
            profile = _suggest_source_profile(uploaded.name)
            batch_profiles.append((uploaded, profile))
            with st.container(border=True):
                st.write(f"**{profile['display_name']}**")
                st.caption(
                    f"{SUBJECT_LABELS.get(profile['subject'], profile['subject'])} · "
                    f"{profile['term_label']} · {profile['resource_use_label']} · "
                    f"{profile['publisher']} · {profile['edition_label']}"
                )

        if st.button(
            f"اعتماد وحفظ كل الملفات ({len(uploaded_files)})",
            key="parent_trusted_source_save_all",
            use_container_width=True,
        ):
            created_count = 0
            duplicate_count = 0
            failed = []

            for uploaded, profile in batch_profiles:
                try:
                    upload = SourceUpload(
                        filename=uploaded.name,
                        mime_type=uploaded.type,
                        data=uploaded.getvalue(),
                    )
                    storage_key = storage.put(upload, learner_key=learner_key)
                    record = build_trusted_record(
                        upload,
                        learner_key=learner_key,
                        display_name=profile["display_name"],
                        subject=profile["subject"],
                        term_label=profile["term_label"],
                        unit_label=None,
                        storage_provider=NEON_OBJECT_STORAGE,
                        storage_key=storage_key,
                        metadata={
                            "resource_use": profile["resource_use"],
                            "resource_use_label": profile["resource_use_label"],
                        },
                        source_role=SOURCE_ROLE_SUPPLEMENTARY,
                        publisher=profile["publisher"],
                        edition_label=profile["edition_label"],
                    )
                    created = catalog.register(record)
                    if created:
                        created_count += 1
                    else:
                        duplicate_count += 1
                except (ValueError, PersistenceError) as exc:
                    failed.append(f"{uploaded.name}: {exc}")
                except Exception:
                    failed.append(f"{uploaded.name}: تعذر الحفظ")

            if created_count:
                st.success(f"تم حفظ واعتماد {created_count} مصدر بشكل دائم ✅")
            if duplicate_count:
                st.info(f"{duplicate_count} ملف كان محفوظ بالفعل وتم منع التكرار.")
            if failed:
                st.error("تعذر حفظ بعض الملفات: " + " · ".join(failed))
            if not failed:
                st.rerun()

    try:
        sources = catalog.list_active()
    except PersistenceError as exc:
        st.warning(str(exc))
        return

    if sources:
        st.markdown("#### المصادر المعتمدة حاليًا")
        for source in sources:
            with st.container(border=True):
                metadata = source.get("metadata") or {}
                source_role = str(metadata.get("source_role", "supplied"))
                role_label = SOURCE_ROLE_LABELS.get(source_role, "مصدر معتمد")
                st.write(
                    f"**{source['display_name']}** · "
                    f"{SUBJECT_LABELS.get(source['subject'], source['subject'])} · "
                    f"{source['term_label']}"
                )
                st.caption(f"الأولوية: {role_label}")
                if metadata.get("publisher"):
                    st.caption(f"الناشر / السلسلة: {metadata['publisher']}")
                if metadata.get("edition_label"):
                    st.caption(f"الطبعة / السنة: {metadata['edition_label']}")
                if metadata.get("resource_use_label"):
                    st.caption(f"الاستخدام داخل LUMINA: {metadata['resource_use_label']}")
                if source.get("unit_label"):
                    st.caption(f"الوحدة / الفصل: {source['unit_label']}")
                st.caption(f"الملف: {source['filename']}")
                if st.button("أرشفة المصدر", key=f"archive_source_{source['source_id']}"):
                    try:
                        catalog.archive(source["source_id"])
                        st.success("تمت أرشفة المصدر بدون حذف سجل التعلّم المرتبط به.")
                        st.rerun()
                    except PersistenceError as exc:
                        st.error(str(exc))


def _render_backup_tools(store) -> None:
    st.markdown("### النسخة الاحتياطية والاستعادة")
    st.caption(
        "نسخة أمان قابلة للتنزيل تحتوي على تقدّم التعلّم فقط، ولا تحتوي على كلمات مرور أو مفاتيح سرية."
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
