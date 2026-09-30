from lumina.learning.lesson_models import LessonCheck, LessonData


ARABIC_U2_LESSONS = (
    LessonData(
        id="arabic_u2_l1", source_id="arabic_prep3_t1", unit_id="u2",
        title="ثمرة القراءة", source_pages="Book page 60",
        objectives=("فهم نص الاستماع «ثمرة القراءة».", "ربط الاستماع بفكرة القراءة وأثرها."),
        key_terms=("ثمرة القراءة","الاستماع","القراءة"),
        evidence_summary=("يفتتح الكتاب الوحدة الثانية بنص استماع بعنوان «ثمرة القراءة».",),
        checks=(LessonCheck(id="listening_title",prompt="ما عنوان نص الاستماع في بداية الوحدة الثانية؟",expected_points=("ثمرة القراءة",),hint="هو أول مكون في الوحدة.",options=("ثمرة القراءة","بناء المستقبل","آداب التعامل مع الوالدين"),correct_index=0,activity_kind="recall",mastery_eligible=False),),
    ),
    LessonData(
        id="arabic_u2_l2", source_id="arabic_prep3_t1", unit_id="u2",
        title="أفضل النعم + صيغة المبالغة + الهمزة", source_pages="Book pages 63–78",
        objectives=("قراءة نص «أفضل النعم».", "تعلم صيغة المبالغة.", "تعلم كتابة الهمزة في بداية الكلمة ووسطها.", "كتابة تقرير صحفي."),
        key_terms=("أفضل النعم","صيغة المبالغة","الهمزة","تقرير صحفي"),
        evidence_summary=("يجمع الدرس قراءة «أفضل النعم» مع صيغة المبالغة نحويًا.", "يتناول إملائيًا كتابة الهمزة في بداية الكلمة ووسطها، ويختم بتطبيق على كتابة تقرير صحفي."),
        checks=(LessonCheck(id="intensive_form",prompt="ما القاعدة النحوية في درس «أفضل النعم»؟",expected_points=("صيغة المبالغة",),hint="راجعي الفهرس.",options=("صيغة المبالغة","اسم الفاعل","اسم المكان"),correct_index=0,activity_kind="recall",mastery_eligible=False),),
    ),
    LessonData(
        id="arabic_u2_l3", source_id="arabic_prep3_t1", unit_id="u2",
        title="خبز جليس + اسم المكان", source_pages="Book pages 80–93",
        objectives=("قراءة نص «خبز جليس» للدكتور أحمد زكي.", "تعلم اسم المكان.", "تطبيق كتابة الهمزة.", "تطبيق كتابة تقرير صحفي."),
        key_terms=("خبز جليس","أحمد زكي","اسم المكان","الهمزة","تقرير صحفي"),
        evidence_summary=("النص القرائي هو «خبز جليس» للدكتور أحمد زكي.", "الموضوع النحوي اسم المكان، مع تطبيقات إملائية على الهمزة وتطبيق كتابي على التقرير الصحفي."),
        checks=(LessonCheck(id="place_noun",prompt="ما الموضوع النحوي المصاحب لنص «خبز جليس»؟",expected_points=("اسم المكان",),hint="انظري إلى سطر القواعد النحوية.",options=("اسم المكان","اسم الزمان","اسم الآلة"),correct_index=0,activity_kind="recall",mastery_eligible=False),),
    ),
    LessonData(
        id="arabic_u2_l4", source_id="arabic_prep3_t1", unit_id="u2",
        title="تاج الفضائل", source_pages="Book pages 95–104",
        objectives=("دراسة النص الشعري «تاج الفضائل».", "مراجعة الوحدة الثانية وحصادها."),
        key_terms=("تاج الفضائل","الإمام علي بن أبي طالب","شعر","مراجعة الوحدة"),
        evidence_summary=("الدرس الرابع نص شعري بعنوان «تاج الفضائل» منسوب في الكتاب إلى الإمام علي بن أبي طالب.", "يعقبه تقويم على الوحدة الثانية ثم حصاد الوحدة."),
        checks=(LessonCheck(id="poem_title",prompt="ما عنوان النص الشعري في ختام الوحدة الثانية؟",expected_points=("تاج الفضائل",),hint="هو الدرس الرابع في الفهرس.",options=("تحية للشباب","تاج الفضائل","اصنع بيدك مجدك"),correct_index=1,activity_kind="recall",mastery_eligible=False),),
    ),
)
