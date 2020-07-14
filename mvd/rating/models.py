from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.conf.urls import url
from django.core.exceptions import ValidationError
from django.urls import reverse
from plan.models import Profile


class Rating(models.Model):
    profile = models.ForeignKey(Profile, related_name='rating', on_delete=models.CASCADE, null=True)
    urr=models.FloatField(default=0)
    ormr = models.FloatField(default=0)
    pcr = models.FloatField(default=0)
    mrr = models.FloatField(default=0)
    summ = models.FloatField(default=0)

    kafedraplace = models.IntegerField(default=10)
    dolzhnostplace = models.IntegerField(default=10)
    unikplace = models.IntegerField(default=10)

    kolvomes = models.IntegerField(default=1)
    year = models.IntegerField(default=2020)

    def getsumm(self):
        return self.urr + self.ormr + self.pcr + self.mrr

    # def __str__(self):
    #     return self.profile.fullname+" рейтинг за "+str(self.year)+" год"


class URR(models.Model):
    profile = models.ForeignKey(Profile, related_name='urr', on_delete=models.CASCADE, null=True)
    obsh=models.FloatField(default=0)
    sootn=models.FloatField(default=0)
    zansprakt=models.FloatField(default=0)
    viezdsprakt=models.FloatField(default=0)
    ppsfp=models.FloatField(default=0)
    ppsdr = models.FloatField(default=0)
    vneaudotor=models.FloatField(default=0)

    obshbal = models.FloatField(default=0)
    sootnbal = models.FloatField(default=0)
    zanspraktbal = models.FloatField(default=0)
    viezdspraktbal = models.FloatField(default=0)
    ppsfpbal = models.FloatField(default=0)
    ppsdrbal = models.FloatField(default=0)
    vneaudotorbal = models.FloatField(default=0)

    obshpodtv = models.CharField(max_length=250,blank=True)
    sootnpodtv = models.CharField(max_length=250,blank=True)
    zanspraktpodtv = models.CharField(max_length=250,blank=True)
    viezdspraktpodtv = models.CharField(max_length=250,blank=True)
    ppsfppodtv = models.CharField(max_length=250,blank=True)
    ppsdrpodtv = models.CharField(max_length=250,blank=True)
    vneaudotorpodtv = models.CharField(max_length=250,blank=True)
    year = models.IntegerField(default=2020)
    def getDataForDoc(self):
        data=[]
        data.extend(["1.1","Общий объем учебной нагрузки",str(self.obshbal)])
        data.extend(["1.2","Соотношение учебной аудиторной нагрузки к общей учетной нагрузке более 70%",str(self.sootnbal)])
        data.extend(["1.3","Проведение занятий с сотруниками практических подразделений",str(self.zanspraktbal)])
        data.extend(["1.4","Проведение выездных занятий с обучающимися в практических подразделениях",str(self.viezdspraktbal)])
        data.extend(["1.5","Поведение занятий с ППC в рамках профессиональной, служебной, физической подготовки (огневая, физическая подготовка)",str(self.ppsfpbal)])
        data.extend(["1.6","Поведение занятий с ППC в рамках единого дня государственно-правового информирования, морально-психологической подготовки с сотрудниками Университета, и пр.; проведение инструктивно-методических занятий с ППС кафедр(ы) Университета в рамках работы в ЦСО",str(self.ppsdrbal)])
        data.extend(["1.7","Проведение во вне учебное время внеаудиторных мероприятий по дисциплинам кафедры - викторин, интеллектуальных игр, экскурсий по тематике преподаваемых дисциплин и т.п.",str(self.vneaudotorbal)])
        return data
    def getsumm(self):
        return self.obshbal + self.sootnbal + self.zanspraktbal + self.viezdspraktbal + self.ppsfpbal+self.ppsdrbal+self.vneaudotorbal

    def __str__(self):
        return self.profile.user.username


class ORMR(models.Model):
   profile=models.ForeignKey(Profile, related_name='ormr', on_delete=models.CASCADE, null=True)
   ruksec=models.FloatField(default=0)
   rukpredmsek=models.FloatField(default=0)
   rabotaruk=models.FloatField(default=0)
   rabotachlen=models.FloatField(default=0)
   rukkafnach=models.FloatField(default=0)
   rukkafzam=models.FloatField(default=0)
   bestprepodmir=models.FloatField(default=0)
   bestprepodrus=models.FloatField(default=0)
   bestprepodreg=models.FloatField(default=0)
   bestprepodunik=models.FloatField(default=0)
   uchastiebestprepodmir = models.FloatField(default=0)
   uchastiebestprepodrus = models.FloatField(default=0)
   uchastiebestprepodreg = models.FloatField(default=0)
   uchastiebestprepodunik = models.FloatField(default=0)
   ekspert=models.FloatField(default=0)
   metodkonk1 = models.FloatField(default=0)
   metodkonk2 = models.FloatField(default=0)
   metodkonk3 = models.FloatField(default=0)
   metodkonk4 = models.FloatField(default=0)
   profmaster = models.FloatField(default=0)
   podgsbornmir=models.FloatField(default=0)
   podgsbornrus=models.FloatField(default=0)
   podgsbornreg=models.FloatField(default=0)
   podgsbornunik=models.FloatField(default=0)
   vulkan=models.FloatField(default=0)
   plenar=models.FloatField(default=0)
   obrprogramma=models.FloatField(default=0)
   proverkaf=models.FloatField(default=0)
   inpectunik=models.FloatField(default=0)
   resocenki1=models.FloatField(default=0)
   resocenki6 = models.FloatField(default=0)
   resocenki11 = models.FloatField(default=0)
   resocenki16 = models.FloatField(default=0)
   resocenki26 = models.FloatField(default=0)
   inovac = models.FloatField(default=0)
   year = models.IntegerField(default=2020)


   ruksecbal = models.FloatField(default=0)
   rukpredmsekbal = models.FloatField(default=0)
   rabotarukbal = models.FloatField(default=0)
   rabotachlenbal = models.FloatField(default=0)
   rukkafnachbal = models.FloatField(default=0)
   rukkafzambal = models.FloatField(default=0)
   bestprepodmirbal = models.FloatField(default=0)
   bestprepodrusbal = models.FloatField(default=0)
   bestprepodregbal = models.FloatField(default=0)
   bestprepodunikbal = models.FloatField(default=0)
   uchastiebestprepodmirbal = models.FloatField(default=0)
   uchastiebestprepodrusbal = models.FloatField(default=0)
   uchastiebestprepodregbal = models.FloatField(default=0)
   uchastiebestprepodunikbal = models.FloatField(default=0)
   ekspertbal = models.FloatField(default=0)
   metodkonk1bal = models.FloatField(default=0)
   metodkonk2bal = models.FloatField(default=0)
   metodkonk3bal = models.FloatField(default=0)
   metodkonk4bal = models.FloatField(default=0)
   profmasterbal = models.FloatField(default=0)
   podgsbornmirbal = models.FloatField(default=0)
   podgsbornrusbal = models.FloatField(default=0)
   podgsbornregbal = models.FloatField(default=0)
   podgsbornunikbal = models.FloatField(default=0)
   vulkanbal = models.FloatField(default=0)
   plenarbal = models.FloatField(default=0)
   obrprogrammabal = models.FloatField(default=0)
   proverkafbal = models.FloatField(default=0)
   inpectunikbal = models.FloatField(default=0)
   resocenki1bal = models.FloatField(default=0)
   resocenki6bal = models.FloatField(default=0)
   resocenki11bal = models.FloatField(default=0)
   resocenki16bal = models.FloatField(default=0)
   resocenki26bal = models.FloatField(default=0)
   inovacbal = models.FloatField(default=0)

   ruksecpodtv = models.CharField(max_length=250, blank=True)
   rukpredmsekpodtv = models.CharField(max_length=250, blank=True)
   rabotarukpodtv = models.CharField(max_length=250, blank=True)
   rabotachlenpodtv = models.CharField(max_length=250, blank=True)
   rukkafnachpodtv = models.CharField(max_length=250, blank=True)
   rukkafzampodtv = models.CharField(max_length=250, blank=True)
   bestprepodmirpodtv = models.CharField(max_length=250, blank=True)
   bestprepodruspodtv = models.CharField(max_length=250, blank=True)
   bestprepodregpodtv = models.CharField(max_length=250, blank=True)
   bestprepodunikpodtv = models.CharField(max_length=250, blank=True)
   uchastiebestprepodmirpodtv = models.CharField(max_length=250, blank=True)
   uchastiebestprepodruspodtv = models.CharField(max_length=250, blank=True)
   uchastiebestprepodregpodtv = models.CharField(max_length=250, blank=True)
   uchastiebestprepodunikpodtv = models.CharField(max_length=250, blank=True)
   ekspertpodtv = models.CharField(max_length=250, blank=True)
   metodkonk1podtv = models.CharField(max_length=250, blank=True)
   metodkonk2podtv = models.CharField(max_length=250, blank=True)
   metodkonk3podtv = models.CharField(max_length=250, blank=True)
   metodkonk4podtv = models.CharField(max_length=250, blank=True)
   profmasterpodtv = models.CharField(max_length=250, blank=True)
   podgsbornmirpodtv = models.CharField(max_length=250, blank=True)
   podgsbornruspodtv = models.CharField(max_length=250, blank=True)
   podgsbornregpodtv = models.CharField(max_length=250, blank=True)
   podgsbornunikpodtv = models.CharField(max_length=250, blank=True)
   vulkanpodtv = models.CharField(max_length=250, blank=True)
   plenarpodtv = models.CharField(max_length=250, blank=True)
   obrprogrammapodtv = models.CharField(max_length=250, blank=True)
   proverkafpodtv = models.CharField(max_length=250, blank=True)
   inpectunikpodtv = models.CharField(max_length=250, blank=True)
   resocenki1podtv = models.CharField(max_length=250, blank=True)
   resocenki6podtv = models.CharField(max_length=250, blank=True)
   resocenki11podtv = models.CharField(max_length=250, blank=True)
   resocenki16podtv = models.CharField(max_length=250, blank=True)
   resocenki26podtv = models.CharField(max_length=250, blank=True)
   inovacpodtv = models.CharField(max_length=250, blank=True)

   def getDataForDoc(self):
        data=[]
        data.extend(["2.1","Руководство секцией методического совет",str(self.ruksecbal)])
        data.extend(["2.2","Руководство предметно-методической секцией кафедры",str(self.rukpredmsekbal)])
        data.extend(["2.3","Работа в составе рабочих групп по развитию образовательной деятельности Университета: - руководитель рабочей группы",str(self.rabotarukbal)])
        data.extend(["2.4","Работа в составе рабочих групп по развитию образовательной деятельности Университета: - член рабочей группы",str(self.rabotachlenbal)])
        data.extend(["2.5","Руководство кафедрой: - в должности начальника (заведующего) кафедры",str(self.rukkafnachbal)])
        data.extend(["2.6","Руководство кафедрой: - в должности заместителя начальника (заведующего) кафедры, в том числе на общественных началах",str(self.rukkafzambal)])
        data.extend(["2.7","Призёр профессионального конкурса \"Лучший преподаватель\": - международного уровня",str(self.bestprepodmirbal)])
        data.extend(["2.8","Призёр профессионального конкурса \"Лучший преподаватель\": - всероссийского уровня",str(self.bestprepodrusbal)])
        data.extend(["2.9","Призёр профессионального конкурса \"Лучший преподаватель\": - регионального, ведомственного или межвузовского уровня",str(self.bestprepodregbal)])
        data.extend(["2.10","Призёр профессионального конкурса \"Лучший преподаватель\": - Университетского уровня",str(self.bestprepodunikbal)])
        data.extend(["2.11","Участие в профессиональном конкурсе \"Лучший преподаватель\": - международного уровня",str(self.uchastiebestprepodmirbal)])
        data.extend(["2.12","Участие в профессиональном конкурсе \"Лучший преподаватель\": - всероссийского уровня",str(self.uchastiebestprepodrusbal)])
        data.extend(["2.13","Участие в профессиональном конкурсе \"Лучший преподаватель\": - регионального, ведомственного или межвузовского уровня",str(self.uchastiebestprepodregbal)])
        data.extend(["2.14","Участие в профессиональном конкурсе \"Лучший преподаватель\": -Университетского уровня",str(self.uchastiebestprepodunikbal )])
        data.extend(["2.15","Работа в качестве эксперта в комиссиях по оценке результатов в конкурсе на лучшую методическую разработку",str(self.ekspertbal)])
        data.extend(["2.16","Участие в конкурсе на лучшую методическую разработку в Университете: - за 1 место",str(self.metodkonk1bal )])
        data.extend(["2.17","Участие в конкурсе на лучшую методическую разработку в Университете:- за 2 место",str(self.metodkonk2bal )])
        data.extend(["2.18","Участие в конкурсе на лучшую методическую разработку в Университете: - за 3 место",str(self.metodkonk3bal )])
        data.extend(["2.19","Участие в конкурсе на лучшую методическую разработку в Университете: - без призового места",str(self.metodkonk4bal )])
        data.extend(["2.20","Организация конкурса профессионального мастерства; работа в качестве эксперта в проведении конкурса профессионального мастерства (среди переменного состава и практических сотрудников)",str(self.profmasterbal )])
        data.extend(["2.21","Подготовка сборной команды Университета для участия в первенствах (интеллектуальные игры, олимпиады, конкурсы, оперативно-тактические учения, спортивные соревнования и т.п.) - международного уровня",str(self.podgsbornmirbal )])
        data.extend(["2.22","Подготовка сборной команды Университета для участия в первенствах (интеллектуальные игры, олимпиады, конкурсы, оперативно-тактические учения, спортивные соревнования и т.п.) - всероссийского уровня",str(self.podgsbornrusbal)])
        data.extend(["2.23","Подготовка сборной команды Университета для участия в первенствах (интеллектуальные игры, олимпиады, конкурсы, оперативно-тактические учения, спортивные соревнования и т.п.) - регионального, ведомственного или межвузовского уровня",str(self.podgsbornregbal )])
        data.extend(["2.24","Подготовка сборной команды Университета для участия в первенствах (интеллектуальные игры, олимпиады, конкурсы, оперативно-тактические учения, спортивные соревнования и т.п.)-Университетского уровня",str(self.podgsbornunikbal )])
        data.extend(["2.25","Подготовка команды первенства \"Вулкан\"",str(self.vulkanbal)])
        data.extend(["2.26","Выступление на пленарном заседании учебно-методического сбора",str(self.plenarbal )])
        data.extend(["2.27","Руководство реализацией образовательной программы",str(self.obrprogrammabal )])
        data.extend(["2.28","Выполнение функций председателя (заместителя председателя) комиссии при проведении проверок (комплексных, контрольных и целевых) деятельности кафед",str(self.proverkafbal )])
        data.extend(["2.29","Участие в инспектировании образовательных организаций МВД России",str(self.inpectunikbal )])
        data.extend(["2.30","Результаты рейтинговой оценки кафедры: - с 1 по 5 места",str(self.resocenki1bal )])
        data.extend(["2.31","Результаты рейтинговой оценки кафедры: - с 6 по 10 места",str(self.resocenki6bal )])
        data.extend(["2.32","Результаты рейтинговой оценки кафедры: с 11 по 15 места",str(self.resocenki11bal )])
        data.extend(["2.33","Результаты рейтинговой оценки кафедры: с 16 по 25 места",str(self.resocenki16bal )])
        data.extend(["2.34","Результаты рейтинговой оценки кафедры: ниже 25 места",str(self.resocenki26bal)])
        data.extend(["2.35","Инновационно-педагогическая деятельность, принятая на заседании методического совета Университета",str(self. inovacbal)])
        return data
   def __str__(self):
       return self.profile.user.username
   def getsumm(self):
        return (self.ruksecbal+
                self.rukpredmsekbal+
                self.rabotarukbal+
                self.rabotachlenbal+
                self.rukkafnachbal+
                self.rukkafzambal+
                self.bestprepodmirbal+
                self.bestprepodrusbal+
                self.bestprepodregbal+
                self.bestprepodunikbal+
                self.uchastiebestprepodmirbal+
                self.uchastiebestprepodrusbal+
                self.uchastiebestprepodregbal+
                self.uchastiebestprepodunikbal+
                self.ekspertbal+
                self.metodkonk1bal+
                self.metodkonk2bal+
                self.metodkonk3bal+
                self.metodkonk4bal+
                self.profmasterbal+
                self.podgsbornmirbal+
                self.podgsbornrusbal+
                self.podgsbornregbal+
                self.podgsbornunikbal+
                self.vulkanbal+
                self.plenarbal+
                self.obrprogrammabal+
                self.proverkafbal+
                self.inpectunikbal+
                self.resocenki1bal+
                self.resocenki6bal+
                self.resocenki11bal+
                self.resocenki16bal+
                self.resocenki26bal+
                self.inovacbal)


class PCR(models.Model):
    profile = models.ForeignKey(Profile, related_name='pcr', on_delete=models.CASCADE, null=True)
    otkr = models.FloatField(default=0)
    kontrud = models.FloatField(default=0)
    kontrneud = models.FloatField(default=0)
    sriv = models.FloatField(default=0)
    opozdanie = models.FloatField(default=0)
    year = models.IntegerField(default=2020)

    otkrpodtv = models.CharField(max_length=250, blank=True)
    kontrudpodtv =models.CharField(max_length=250, blank=True)
    kontrneudpodtv = models.CharField(max_length=250, blank=True)
    srivpodtv = models.CharField(max_length=250, blank=True)
    opozdaniepodtv = models.CharField(max_length=250, blank=True)


    otkrbal = models.FloatField(default=0)
    kontrudbal = models.FloatField(default=0)
    kontrneudbal = models.FloatField(default=0)
    srivbal = models.FloatField(default=0)
    opozdaniebal = models.FloatField(default=0)
    def getDataForDoc(self):
        data=[]
        data.extend(["4.1","Проведение открытых, показательных занятий",str(self.otkrbal)])
        data.extend(["4.2","Результаты контрольных посещений занятий: - при общей удовлетворительной оценке занятия",str(self.kontrudbal)])
        data.extend(["4.2","Результаты контрольных посещений занятий: - при общей отрицательной оценке занятия",str(self.kontrneudbal)])
        data.extend(["4.3","Срыв занятия",str(self.srivbal)])
        data.extend(["4.4","Не своевременное прибытие нае Не своевременное прибытие на занятие без уважительных причин занятие без уважительных причин",str(self.opozdaniebal)])
        return data
    def __str__(self):
        return self.profile.user.username
    def getsumm(self):
        return self.otkrbal+self.kontrudbal+self.kontrneudbal+self.srivbal+self.opozdaniebal


class MRR(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    name=models.CharField(max_length=250, blank=True)
    soavtr=models.IntegerField(default=1)
    dgsk=models.BooleanField(default=False)
    bal=models.FloatField(default=0)
    year = models.IntegerField(default=2020)
    def __str__(self):
        return self.profile.user.username

    def getsumm(self):
        return self.razr1bal + self.razr2bal + self.razr3bal
