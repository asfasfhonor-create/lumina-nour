import streamlit as st

from lumina.module_registry import get_module, get_school_subjects
from lumina.session_state import current_level


def render_home_foundation() -> None:
    """Render the current Nour's World foundation without owning learning business logic."""
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
            f'<div class="stat">🔥 <b>{st.session_state.streak} أيام</b><span class="muted">Streak · تجريبي</span></div>',
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            f'<div class="stat">🌱 <b>Level {level_number}</b><span class="muted">Explorer</span></div>',
            unsafe_allow_html=True,
        )

    _render_daily_mission()
    _render_learning_worlds()

    st.markdown("---")
    if st.button("👨‍👧 Parent Dashboard", key="open_parent_dashboard"):
        st.session_state.active_world = "parent"
        st.rerun()


def _render_daily_mission() -> None:
    st.markdown('<div class="section-title">🎯 مهمة اليوم</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="mission"><b>English Mini Mission</b><br>'
        '<span class="muted">اكتبي 3 جمل قصيرة عن يومك بالإنجليزي. هنراجعها معًا قبل تسجيل الـ XP.</span></div>',
        unsafe_allow_html=True,
    )
    daily_text = st.text_area(
        "مهمة اليوم",
        placeholder="Write 3 short sentences...",
        key="daily_text",
        label_visibility="collapsed",
    )

    if not st.session_state.daily_done:
        if st.button("راجعي المهمة وسجلي +20 XP", key="daily_xp"):
            sentences = [
                sentence.strip()
                for sentence in daily_text.replace("!", ".").replace("?", ".").split(".")
                if sentence.strip()
            ]
            if len(sentences) < 3:
                st.warning("اكتبي 3 جمل على الأقل الأول — المهم المحاولة 🌱")
            else:
                st.session_state.xp += 20
                st.session_state.daily_done = True
                st.balloons()
                st.rerun()
    else:
        st.success("مهمة اليوم اتسجلت 🎉 +20 XP — الحفظ الدائم هنفعله مع قاعدة البيانات.")


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
            if module.id in {"english", "science", "math"}:
                labels = {
                    "english": "ادخلي English Adventure",
                    "science": "ادخلي Science Lab",
                    "math": "ادخلي Math Quest",
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
            '<div class="mission"><b>قريبًا: AI Detective + Prompt Challenges + Creative Builder</b><br>'
            '<span class="muted">مش الهدف ناخد الإجابة من الـ AI؛ الهدف نتعلم نسأله صح، '
            'نراجعه، نكتشف أخطاءه ونصنع به حاجات جديدة.</span></div>',
            unsafe_allow_html=True,
        )
