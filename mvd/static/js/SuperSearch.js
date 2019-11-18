//



    // задаем массив в качестве источника слов для автозаполнения.
  $(function(){
    var langs = ["Разработка тематического плана дисциплины","Разработка графика последовательности прохождения дисциплины","Разработка примерной рабочей программы учебной дисциплины","Разработка рабочей программы учебной дисциплины","Разработка рабочей программы государственной итоговой аттестации,программы практики","Разработка примерной основной профессиональной образовательной программы профессионального обучения (программы профессиональной подготовки, программы переподготовки,программы повышения квалификации)","Разработка основной профессиональной образовательной программы профессионального обучения (программы профессиональной подготовки, программы переподготовки,программы повышения квалификации)","Разработка примерной дополнительной профессиональной программы(программы повышения квалификации, программы профессиональной переподготовки)","Разработка Дополнительной профессиональной программы (программы повышения квалификации, программы профессиональной переподготовки)","Разработка методических рекомендации по организации самостоятельной работы обучающихся по очной форме","Разработка методических рекомендации по организации самостоятельной работы обучающихся по заочной форме","Разработка тезисов лекции","Разработка фондовой лекции","Разработка методической разработки проведения аудиторного занятия,письменной работы‚ внеаудиторного мероприятия (в рамках кафедры)","Разработка методической разработки аудиторного занятия, письменной работы‚ внеаудиторного мероприятия (межкафедрального)","Разработка словаря основных понятий и терминов","Переработка тематического плана дисциплины","Переработка графика последовательности прохождения дисциплины","Переработка примерной рабочей программы учебной дисциплины","Переработка рабочей программы учебной дисциплины","Переработка рабочей программы государственной итоговой аттестации,программы практики","Переработка примерной основной профессиональной образовательной программы профессионального обучения (программы профессиональной подготовки, программы переподготовки,программы повышения квалификации)","Переработка основной профессиональной образовательной программы профессионального обучения (программы профессиональной подготовки, программы переподготовки,программы повышения квалификации)","Переработка примерной дополнительной профессиональной программы(программы повышения квалификации, программы профессиональной переподготовки)","Переработка Дополнительной профессиональной программы (программы повышения квалификации, программы профессиональной переподготовки)","Переработка методических рекомендации по организации самостоятельной работы обучающихся по очной форме","Переработка методических рекомендации по организации самостоятельной работы обучающихся по заочной форме","Переработка тезисов лекции","Переработка фондовой лекции","Переработка методической разработки проведения аудиторного занятия,письменной работы‚ внеаудиторного мероприятия (в рамках кафедры)","Переработка методической разработки аудиторного занятия, письменной работы‚ внеаудиторного мероприятия (межкафедрального)","Переработка словаря основных понятий и терминов","Переработка плана проведения семинаров, лабораторных и практических занятий с методическими рекомендациями для обучающихся","Переработка заданий на аудиторные контрольные работы","Переработка натурных объектов на контрольные экспертизы","Переработка тематики домашних контрольных работ","Переработка материалов для проведения конкурса профессионального мастерства","Переработка теста по дисциплине, по отдельной теме","Переработка тестов для проведения мероприятий по указанию МВД России","Переработка тематики (перечня тем) рефератов, курсовых работ(проектов)","Переработка тематики ВКР","Переработка методических указаний для обучающихся по написанию (выполнению) рефератов","Переработка методических указаний для обучающихся по написанию(выполнению) курсовых работ (проектов), ВКР,аттестационных дипломных работ","Переработка методических материалов для самоконтроля знаний И умений для обучающихся по очной форме","Переработка методических материалов для самоконтроля знаний И умений для обучающихся по заочной форме","Переработка практикума по дисциплине","Переработка материалов для проведения практики: индивидуальных заданий на практику, указаний, памяток И иное","Переработка перечня вопросов для промежуточных аттестаций, государственных итоговых аттестаций","Переработка Оценочные средства для контроля качества обучения в процессе освоения (изучения) учебной дисциплины(программы), для проведения текущего контроля успеваемости, промежуточной аттестации по учебной дисциплине, итоговой (государственной итоговой) аттестации, проверки остаточных знаний обучающихся (вопросы, билеты, тестовые задания (В.т.ч. тренировочные тесты, тесты по отдельным темам, тесты для входного (выходного) контроля), задания для самостоятельной работы обучающихся, практические задания (задачи, упражнения,творческие задания)","Переработка натурных объектов к практическим заданиям к билетам","Переработка материалов для вступительных испытаний","Переработка материалов для проведения кандидатского экзамена","Переработка сборника образцов процессуальных И служебныхдокументов, макета дела, комплекта ситуационных задач поматериалов для мультимедийного сопровождения занятия","Переработка требований на разработку компьютерной программы","Переработка Компьютерных программ","Переработка сценария для учебного фильма","Переработка Рабочего плана проведения занятия","Разработка плана проведения семинаров, лабораторных и практических занятий с методическими рекомендациями для обучающихся","Разработка заданий на аудиторные контрольные работы","Разработка натурных объектов на контрольные экспертизы","Разработка тематики домашних контрольных работ","Разработка материалов для проведения конкурса профессионального мастерства","Разработка теста по дисциплине, по отдельной теме","Разработка тестов для проведения мероприятий по указанию МВД России","Разработка тематики (перечня тем) рефератов, курсовых работ(проектов)","Разработка тематики ВКР","Разработка методических указаний для обучающихся по написанию (выполнению) рефератов","Разработка методических указаний для обучающихся по написанию(выполнению) курсовых работ (проектов), ВКР,аттестационных дипломных работ","Разработка методических материалов для самоконтроля знаний И умений для обучающихся по очной форме","Разработка методических материалов для самоконтроля знаний И умений для обучающихся по заочной форме","Разработка практикума по дисциплине","Разработка материалов для проведения практики: индивидуальных заданий на практику, указаний, памяток И иное","Разработка перечня вопросов для промежуточных аттестаций, государственных итоговых аттестаций","Разработка Оценочные средства для контроля качества обучения в процессе освоения (изучения) учебной дисциплины(программы), для проведения текущего контроля успеваемости, промежуточной аттестации по учебной дисциплине, итоговой (государственной итоговой) аттестации, проверки остаточных знаний обучающихся (вопросы, билеты, тестовые задания (В.т.ч. тренировочные тесты, тесты по отдельным темам, тесты для входного (выходного) контроля), задания для самостоятельной работы обучающихся, практические задания (задачи, упражнения,творческие задания)","Разработка натурных объектов к практическим заданиям к билетам","Разработка материалов для вступительных испытаний","Разработка материалов для проведения кандидатского экзамена","Разработка сборника образцов процессуальных И служебныхдокументов, макета дела, комплекта ситуационных задач поматериалов для мультимедийного сопровождения занятия","Разработка требований на разработку компьютерной программы","Разработка Компьютерных программ","Разработка сценария для учебного фильма","Разработка Рабочего плана проведения занятия","Создание структуры электронного учебного курса, включая дизайн (оформление) материалов электронного","Создание И интеграция текстового содержания в электронный учебный курс с настраиванием необходимых гиперссылок, включая графическое сопровождение:графики, таблицы, схемы И т.п.","Интеграция тестовых заданий в программную оболочку","Разработка компьютерной программы (обучающей,тестовой, прочее), в том числе для использования в СДОТ","Создание И интеграция аудио- видеоматериалов",
  "Контрольное посещение учебного занятия И его обсуждение","Взаимное посещение занятия","Участие в проведении показательных, открытых И пробных занятий","Подготовка к проведению показательных, открытых И пробных занятий","Проведение инструктивно—Методического занятия","Руководство учебно-методической секцией МВД России","Работа в составе учебно—методической секции МВД России","Руководство секцией методического совета Университета","Участие в работе секции (рабочей группы) методического совета Университета","Руководство предметно-методической секцией кафедры","Участие в работе предметно—методической секции кафедры","Руководство школой педагогического мастерства","Участие в работе методического совета","Участие в работе учебно—методических сборов","Участие в работе учебно—методических семинаров, в том числе с представителями филиалов","Заполнение электронного учебно-методического обеспечения дисциплины на образовательном портале Университета (сервере филиала)","Выполнение научно-исследовательской работы по плану МВД России","Выполнение научно-исследовательской работы по плану Университета","Выполнение научно-исследовательской работы по плану кафедры","Издание учебника, хрестоматии, монографии","Издание учебного, учебно—методического, учебно-практическогопособия, курса лекций, практикума, справочника, сборниказадач, альбома схем, аналитического обзора","Издание докладов и тезисов для научных конференций","Издание научных статей в сборниках научных трудов","Издание научных статей в сборниках материалов конференций","Издание научных статей в научных журналах (индексируемых в РИНЦ,рекомендованных ВАК, размещенных в международныхбазах цитирования)","Подготовка экспертных заключений по диссертациям,отзывов на диссертацию, на автореферат диссертации,официальных оппонентов, ведущей организации","Рецензирование статей в научных журналах И другихнаучных материалов","Рецензирование научно-Исследовательских работ,поступающих на конкурсы","Участие в работе научных конференций И Других научно—представительских мероприятиях","Организация И проведение научно—представительскихмероприятий","Руководство научным обществом, кружком, проблемнойгруппой, дискуссионным клубом И т.д.","Руководство научно—исследовательской работойобучающегося","Участие в работе комиссий И жюри конгрессов, в работе Ипроведении форумов, олимпиад, конкурсов научных работобучающихся","Руководство научной школой","Разработка диссертационного исследования","Обеспечение представительства","по научной деятельности, редакционно-издательскогосовета, совета молодых ученых, диссертационного советаУниверситета И др.","Участие в работе научно—методического И научно—технического советов МВД РОССИИ","Патриотическое воспитание","Профессионально-нравственное воспитание","Правовое воспитание","Психологическая работа","Социальная работа","Культурно-просветительская работа","Работа по укреплению служебной дисциплины и законности","Подготовка выступлений на торжественных митингах,собраниях И других торжественных мероприятиях сучастием обучающихся","Организация И проведение работы‚ в том числеэкскурсионной, педагогов-кураторов с обучающимися","Творческих встреч с практическими работниками, сдеятелями литературы И искусства с участием обучающихся","Участие в подведении итогов на факультетах","Со слабоуспевающими курсантами, слушателями,входящими в ГГШВ, допускаЮЩИМИ нарушения служебнойдисциплины","С подчиненными сотрудниками кафедры","Наставничество","Участие в работе Ученого совета Университета (Советафилиала)","Работа в качестве ответственного секретаря приёмнойкомиссии","Руководство кафедрой","Участие в работе оперативного совещания при начальникеуниверситета","Участие в работе совещания начальников кафедр при первомзаместителе начальника университета","Участие в работе совещания начальников кафедр прИзаместителе начальника университета по научной работе","Участие в составе аттестационной комиссии,инвентаризационной комиссии, КОМИССИИ по проверкекафедр, рабочих групп И т.п.","Участие в составе конкурсной комиссии, жюри, корпусасудей по организации И проведению различныхмероприятий","Участие в проведении представительских,профоринентационных мероприятий («ДНИ открытыхдверей», выставки, образовательные салоны И т.п.)","Профессиональная служебная И физическая подготовка","Стажировка","Переподготовка","Курсы повышения квалификации","Участие в заседаниях кафедры","Ведение индивидуальных планов","Ведение кафедральной документации‚ подготовкадокументов для управлений (отделов) Университета, работаответственных за ПСИФП, моб.готовность, морально-психологическую подготовку","Оформление рейтинговой документации кафедры","Ведение табеля учета служебного времени","Подготовка документов для закупок материальныхценностей, подготовка технического задания","Подготовка локальных нормативных актов (приказов Ираспоряжений)","Подготовка предложений в рамках мониторингаправоприменения в Университете","Дежурство по кафедре","Работа с обращениями граждан, поступившими вУниверситет через ОДИР","Дежурство ответственным по Университету от руководства","Патруль по Университету","Выездной караул","Текущее обслуживание полигонов, лабораторий,компьютерных классов, тиров, спортивных сооружений И техническое обслуживание оборудования"];
    $('textarea#lang').autocomplete({
        source: langs
    });



});
