from lumina.learning.lesson_models import LessonCheck, LessonData


ARABIC_U1_LESSONS = (
    LessonData(
        id="arabic_u1_l1", source_id="arabic_prep3_t1", unit_id="u1",
        title="آداب التعامل مع الوالدين", source_pages="Book page 15",
        objectives=("فهم نص الاستماع.", "استخلاص آداب الحوار والتعامل مع الوالدين."),
        key_terms=("الوالدان","الاحترام","الحوار","حسن الاستماع"),
        evidence_summary=("يفتتح الكتاب الوحدة الأولى بنص استماع بعنوان «آداب التعامل مع الوالدين».", "يرتبط الدرس بقيمة الاحترام والحوار وحسن التعامل داخل الأسرة."),
        checks=(LessonCheck(id="parents",prompt="أي سلوك ينسجم أكثر مع عنوان نص الاستماع؟",expected_points=("الاحترام وحسن الحوار",),hint="فكر في معنى «آداب التعامل».",options=("المقاطعة ورفع الصوت","الاحترام وحسن الحوار","تجاهل رأي الوالدين"),correct_index=1),),
    ),
    LessonData(
        id="arabic_u1_l2", source_id="arabic_prep3_t1", unit_id="u1",
        title="أغلى من الذهب + اسم الفاعل + الألف اللينة", source_pages="Book pages 20–34",
        objectives=("قراءة نص «أغلى من الذهب» وفهمه.", "تعلم اسم الفاعل.", "مراجعة الألف اللينة في الأسماء والأفعال والحروف.", "التدرب على نص إقناعي."),
        key_terms=("أغلى من الذهب","اسم الفاعل","الألف اللينة","نص إقناعي"),
        evidence_summary=("يجمع الدرس بين القراءة والقواعد النحوية والإملاء والتحدث والتعبير الكتابي.", "الموضوع النحوي هو اسم الفاعل، والإملائي هو الألف اللينة، والتعبير الكتابي كتابة نص إقناعي."),
        checks=(LessonCheck(id="active_participle",prompt="ما الموضوع النحوي المقرر في هذا الدرس؟",expected_points=("اسم الفاعل",),hint="راجع سطر القواعد النحوية في المحتويات.",options=("اسم الفاعل","اسم المفعول","اسم الزمان"),correct_index=0,activity_kind="recall",mastery_eligible=False),),
    ),
    LessonData(
        id="arabic_u1_l3", source_id="arabic_prep3_t1", unit_id="u1",
        title="الصداقة + اسم المفعول", source_pages="Book pages 36–47",
        objectives=("قراءة نص «الصداقة» للدكتور شوقي ضيف.", "تعلم اسم المفعول.", "تطبيق الألف اللينة.", "التدرب على التحدث والكتابة المرتبطين بموضوع الدرس."),
        key_terms=("الصداقة","اسم المفعول","الألف اللينة","التعبير الكتابي"),
        evidence_summary=("النص القرائي هو «الصداقة» للدكتور شوقي ضيف.", "الموضوع النحوي هو اسم المفعول، مع تطبيقات إملائية على الألف اللينة."),
        checks=(LessonCheck(id="passive_participle",prompt="ما الموضوع النحوي الذي يأتي مع نص «الصداقة»؟",expected_points=("اسم المفعول",),hint="انظري إلى تسلسل مكونات الدرس الثالث.",options=("اسم المفعول","صيغة المبالغة","اسم الآلة"),correct_index=0,activity_kind="recall",mastery_eligible=False),),
    ),
    LessonData(
        id="arabic_u1_l4", source_id="arabic_prep3_t1", unit_id="u1",
        title="تحية للشباب", source_pages="Book pages 49–58",
        objectives=("دراسة النص الشعري «تحية للشباب».", "مراجعة الوحدة الأولى وحصادها."),
        key_terms=("تحية للشباب","أحمد شوقي","شعر","مراجعة الوحدة"),
        evidence_summary=("الدرس الرابع نص شعري بعنوان «تحية للشباب» لأمير الشعراء أحمد شوقي.", "يعقبه تقويم على الوحدة الأولى ثم حصاد الوحدة."),
        checks=(LessonCheck(id="poet",prompt="من شاعر «تحية للشباب» كما يذكر الكتاب؟",expected_points=("أحمد شوقي",),hint="الاسم مذكور في فهرس الدرس الرابع.",options=("أحمد شوقي","معروف الرصافي","أحمد زكي"),correct_index=0,activity_kind="recall",mastery_eligible=False),),
    ),
)
