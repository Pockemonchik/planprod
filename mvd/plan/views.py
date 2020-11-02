from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from rating.models import URR, ORMR, PCR, MRR, Rating
from rating.views import setplace
from plan.models import Article, Mesyac, Profile, Kafedra, Plan, Predmet, NIR, VR, DR, UMR, INR, Nagruzka, DocInfo, \
    ProfileInfo,Zamech
from plan.forms import ZamechForm,ZamechAdminForm,MesyacForm, ChangePassForm, UserAddForm, docUploadForm, ShapkaForm, Table1Form, Table2Form, \
    Table3Form, Table4Form, Table6Form, Table5Form, MainTableForm, Table1UploadForm, NagruzkaForm, ProfileInfoForm
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
from plan.Parser_and_overview import createDoc2, checkPrepods, createDoc, takeTable, takeXls, writeInfoDoc, xlsPrepod, \
    checkDocumentXLS
from django.core.files.base import ContentFile
from django.core.files import File
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.conf import settings
from django.db.models import Q
from rest_framework.response import Response
# from .tasks import saveallnagr
import json
from django.http import HttpResponse
import random
from docx import Document
import os
import datetime as dt
from io import StringIO, BytesIO
from rest_framework.decorators import api_view
from itertools import chain

"""Рендер основных страниц"""


def detail_plan(request, slug, year):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user=request.user)
        profile1 = get_object_or_404(Profile, user__username=slug)
        if profile.role == 3 or profile.role == 2:
            Table0FormSet = modelformset_factory(Predmet, form=Table1Form, extra=5)
        else:
            Table0FormSet = modelformset_factory(Predmet, form=Table1Form, extra=0)
        Table1FormSet = modelformset_factory(Predmet, form=Table1Form, extra=5)
        Table2FormSet = modelformset_factory(UMR, form=Table2Form, extra=5)
        Table3FormSet = modelformset_factory(NIR, form=Table3Form, extra=5)
        Table4FormSet = modelformset_factory(VR, form=Table4Form, extra=5)
        Table5FormSet = modelformset_factory(DR, form=Table5Form, extra=5)
        Table6FormSet = modelformset_factory(INR, form=Table6Form, extra=5)
        MesyacFormSet = modelformset_factory(Mesyac, form=MesyacForm, extra=0)
        if profile.role == 3:
            ZamechFormSet = modelformset_factory(Zamech, form=ZamechAdminForm, extra=5)
        else:
            ZamechFormSet = modelformset_factory(Zamech, form=ZamechForm, extra=0)
        try:
            plan = get_object_or_404(Plan, prepod=profile1, year=year)
        except Exception as e:
            print(e)
            return render(request, 'error.html', {'content': "Произошла ошибка, обратитесь к администрации"})
        try:
            querymes = Mesyac.objects.filter(prepodavatel=profile1, year=year, polugodie=1, status=False)

            if not querymes:
                mesyacprofile = profile1

                mes1 = Mesyac.objects.create(name='АВГУСТ', prepodavatel=mesyacprofile, year=year, polugodie=1,
                                             status=False, kafedra=mesyacprofile.kafedra)
                mes2 = Mesyac.objects.create(name='СЕНТЯБРЬ', prepodavatel=mesyacprofile, year=year, polugodie=1,
                                             status=False, kafedra=mesyacprofile.kafedra)
                mes3 = Mesyac.objects.create(name='ОКТЯБРЬ', prepodavatel=mesyacprofile, year=year, polugodie=1,
                                             status=False, kafedra=mesyacprofile.kafedra)
                mes4 = Mesyac.objects.create(name='НОЯБРЬ', prepodavatel=mesyacprofile, year=year, polugodie=1,
                                             status=False, kafedra=mesyacprofile.kafedra)
                mes5 = Mesyac.objects.create(name='ДЕКАБРЬ', prepodavatel=mesyacprofile, year=year, polugodie=1,
                                             status=False, kafedra=mesyacprofile.kafedra)
                mes6 = Mesyac.objects.create(name='Итого за 1 полугодие:', prepodavatel=mesyacprofile, year=year,
                                             polugodie=1, status=False, kafedra=mesyacprofile.kafedra)
                mes7 = Mesyac.objects.create(name='ЯНВАРЬ', prepodavatel=mesyacprofile, year=year, polugodie=2,
                                             status=False, kafedra=mesyacprofile.kafedra)
                mes8 = Mesyac.objects.create(name='ФЕВРАЛЬ', prepodavatel=mesyacprofile, year=year, polugodie=2,
                                             status=False, kafedra=mesyacprofile.kafedra)
                mes9 = Mesyac.objects.create(name='МАРТ', prepodavatel=mesyacprofile, year=year, polugodie=2,
                                             status=False, kafedra=mesyacprofile.kafedra)
                mes10 = Mesyac.objects.create(name='АПРЕЛЬ', prepodavatel=mesyacprofile, year=year, polugodie=2,
                                              status=False, kafedra=mesyacprofile.kafedra)
                mes11 = Mesyac.objects.create(name='МАЙ', prepodavatel=mesyacprofile, year=year, polugodie=2,
                                              status=False, kafedra=mesyacprofile.kafedra)
                mes12 = Mesyac.objects.create(name='ИЮНЬ', prepodavatel=mesyacprofile, year=year, polugodie=2,
                                              status=False, kafedra=mesyacprofile.kafedra)
                mes13 = Mesyac.objects.create(name='ИЮЛЬ', prepodavatel=mesyacprofile, year=year, polugodie=2,
                                              status=False, kafedra=mesyacprofile.kafedra)
                mes14 = Mesyac.objects.create(name='Итого за 2 полугодие:', prepodavatel=mesyacprofile, year=year,
                                              polugodie=2, status=False, kafedra=mesyacprofile.kafedra)
                mes15 = Mesyac.objects.create(name='Итого за учебный год:', prepodavatel=mesyacprofile, year=year,
                                              polugodie=2, status=False, kafedra=mesyacprofile.kafedra)
                qs = Mesyac.objects.filter(prepodavatel=mesyacprofile, year=year, status=False)

                mesyac = MesyacFormSet(
                    queryset=qs)

            else:
                print('not empty mes')
                mesyac = MesyacFormSet(
                    queryset=Mesyac.objects.filter(prepodavatel=profile1, year=year, status=False))
        except Exception as e:
            print(e)
            mesyac = MesyacFormSet()
        mainForm = MainTableForm(instance=plan)
        docForm = docUploadForm()
        formset = Table0FormSet(
            queryset=Predmet.objects.filter(prepodavatel=profile1, year=year, polugodie=1, status=False))
        formset2 = Table0FormSet(
            queryset=Predmet.objects.filter(prepodavatel=profile1, year=year, polugodie=2, status=False))
        formset3 = Table1FormSet(
            queryset=Predmet.objects.filter(prepodavatel=profile1, year=year, polugodie=1, status=True))
        formset4 = Table1FormSet(
            queryset=Predmet.objects.filter(prepodavatel=profile1, year=year, polugodie=2, status=True))
        formset5 = Table2FormSet(queryset=UMR.objects.filter(prepodavatel=profile1, year=year, polugodie=1))
        formset6 = Table2FormSet(queryset=UMR.objects.filter(prepodavatel=profile1, year=year, polugodie=2))
        formset7 = Table3FormSet(queryset=NIR.objects.filter(prepodavatel=profile1, year=year, polugodie=1))
        formset8 = Table3FormSet(queryset=NIR.objects.filter(prepodavatel=profile1, year=year, polugodie=2))
        formset9 = Table4FormSet(queryset=VR.objects.filter(prepodavatel=profile1, year=year, polugodie=1))
        formset10 = Table4FormSet(queryset=VR.objects.filter(prepodavatel=profile1, year=year, polugodie=2))
        formset11 = Table5FormSet(queryset=DR.objects.filter(prepodavatel=profile1, year=year, polugodie=1))
        formset12 = Table5FormSet(queryset=DR.objects.filter(prepodavatel=profile1, year=year, polugodie=2))
        formset13 = Table6FormSet(queryset=INR.objects.filter(prepodavatel=profile1, year=year, polugodie=1))
        formset14 = Table6FormSet(queryset=INR.objects.filter(prepodavatel=profile1, year=year, polugodie=2))
        zamech_formset = ZamechFormSet(queryset=Zamech.objects.filter(profile=profile1, year=year))
        kafedri = Kafedra.objects.all()
        try:
            kolvomes = Rating.objects.get(profile=profile1, year=year).kolvomes
        except Exception as e:
            print(e)
            kolvomes = 0
        if profile.role == 2:
            kafedri = Kafedra.objects.filter(name=profile.kafedra.name)
        try:
            docinf = DocInfo.objects.get(plan=plan)
            shapka = ShapkaForm(instance=docinf)
        except DocInfo.DoesNotExist:
            shapka = ShapkaForm()

        try:
            title = "Индивидуальный план  " + ''.join(
                [profile1.fullname.split(' ')[0], ' ', profile1.fullname.split(' ')[1][0], '.',
                 profile1.fullname.split(' ')[2][0]]) + " " + str(year) + "-" + str(int(year) + 1)
        except:
            title = "Индивидуальный план  " + profile1.fullname + " " + str(year) + "-" + str(int(year) + 1)
        return render(request, 'detail_plan.html', {
            'mainForm': mainForm,
            'formset': formset,
            'formset2': formset2,
            'formset3': formset3,
            'formset4': formset4,
            'formset5': formset5,
            'formset6': formset6,
            'formset7': formset7,
            'formset8': formset8,
            'formset9': formset9,
            'formset10': formset10,
            'formset11': formset11,
            'formset12': formset12,
            'formset13': formset13,
            'formset14': formset14,
            'kafedri': kafedri,
            'plan': plan,
            'profile': profile,
            'profile1': profile1,
            'shapka': shapka,
            'docForm': docForm,
            'mesyac': mesyac,
            'title': title,
            'kolvomes': kolvomes,
            'zamech_formset':zamech_formset

        })
    else:
        return redirect('log')


def index(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user=request.user)
        plans = Plan.objects.filter(prepod=profile)
        kafedri = Kafedra.objects.all()
        sotr = ''
        if profile.role == 2:
            kafedri = Kafedra.objects.filter(name=profile.kafedra.name)
            sotr = Profile.objects.filter(kafedra=profile.kafedra)
        nagruzkadocs = Nagruzka.objects.filter(kafedra=profile.kafedra)
        nagruzka = NagruzkaForm()
        useraddform = UserAddForm()
        ratings = Rating.objects.filter(profile=profile)
        try:
            info = ProfileInfo.objects.get(profile=profile)
            infoform = ProfileInfoForm(instance=info)
        except:
            infoform = ProfileInfoForm()
        try:
            title = "Главная " + ''.join([profile.fullname.split(' ')[0], ' ', profile.fullname.split(' ')[1][0], '.',
                                          profile.fullname.split(' ')[2][0]])
        except:
            title = "Главная " + profile.fullname
        if profile.role < 3:
            return render(request, 'plan.html', {
                'profile': profile,
                'kafedri': kafedri,
                'plans': plans,
                'nagruzka': nagruzka,
                'nagruzkadocs': nagruzkadocs,
                'useraddform': useraddform,
                'sotr': sotr,
                'ratings': ratings,
                'infoform': infoform,
                'title': title
            })
        if profile.role == 3:
            return render(request, 'plan_sotr.html', {
                'profile': profile,
                'kafedri': kafedri,
                'plans': plans,
                'nagruzka': nagruzka,
                'nagruzkadocs': nagruzkadocs,
                'useraddform': useraddform,
                'sotr': sotr,
                'ratings': ratings,
                'infoform': infoform,
                'title': title
            })
    else:
        return redirect('log')


def kafedra_view(request, kafedra, year):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user=request.user)
        plans = Plan.objects.filter(prepod__kafedra__name=kafedra, year=year)
        kafedri = Kafedra.objects.all()
        if profile.role == 2:
            kafedri = Kafedra.objects.filter(name=profile.kafedra.name)
        arr = []
        # for kaf in kafedri:
        #     arr.append(kaf.fullname)
        # print(arr)
        return render(request, 'strprepod.html', {
            'profile': profile,
            'kafedri': kafedri,
            'plans': plans
        })
    else:
        return redirect('log')
        # выгружаем данные в документ


def spravka(request):
    if request.user.is_authenticated:

        return render(request, 'spravka.html')
    else:
        return redirect('log')


"""Работа на главной странице"""


@api_view(['GET'])
def supertable(request):
    kafname = request.GET['kafname']
    kafedra = Kafedra.objects.get(name=kafname)
    data = []
    profiles = Profile.objects.filter(kafedra=kafedra)
    for p in profiles:
        data.append(
            {
                "name": p.fullname,
                "login": p.user.username,
                "password": p.user.email
            }
        )
    return Response(data)


@api_view(['POST'])
def createplan(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user=request.user)
        year = request.POST['year']
        if request.method == "POST":
            try:
                Plan.objects.get(prepod=profile, year=request.POST['year'])
                return Response([{

                    "text": "Такой план уже существует"

                }])


            except:
                newplan = Plan()
                newplan.user = request.user
                newplan.prepod = profile
                newplan.year = request.POST['year']

                newplan.name = ''.join([profile.fullname.split(' ')[0], ' ', profile.fullname.split(' ')[1][0], '.',
                                        profile.fullname.split(' ')[2][0]])
                print("sozadanie plana " + newplan.name)
                newplan.save()

    return Response([{

        "text": "План успешно создан",
        "href": "plan/" + profile.user.username + "/" + year + "/",

    }])


@api_view(['POST'])
def createratinghome(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user=request.user)
        year = request.POST['year']
        if request.method == "POST":
            try:
                try:
                    newrating = Rating.objects.get(profile=profile, year=year)
                    newrating.profile = profile
                    newrating.year = year
                    print("menyaem")
                    itog = Predmet.objects.get(prepodavatel=profile, year=year, name="Итого за учебный год:",
                                               status=True)
                    try:
                        newurr = URR.objects.get(profile=profile, year=year)
                    except:
                        newurr = URR()
                    newurr.profile = profile
                    newurr.year = year
                    newurr.obsh = itog.get_obshaya_nagruzka()
                    newurr.obshbal = int(itog.get_obshaya_nagruzka() / 45)
                    # не забыть поменять на флоат
                    sootn = int(itog.get_auditor_nagruzka() / itog.get_obshaya_nagruzka() * 100)
                    newurr.sootn = sootn
                    print(newurr.sootn)

                    print(newurr.sootnbal)
                    if sootn > 70:
                        newurr.sootnbal = sootn - 70
                    else:
                        newurr.sootnbal = 0
                    print(newurr.sootn)

                    print(newurr.sootnbal)
                    newurr.save()
                    umrs = UMR.objects.filter(prepodavatel=profile, year=year, include_rating=True)
                    mmrs_for_del = MRR.objects.filter(profile=profile, year=year)
                    for name in MRR.objects.filter(profile=profile).values_list('name', flat=True).distinct():
                        MRR.objects.filter(
                            pk__in=MRR.objects.filter(name=name).values_list('id', flat=True)[1:]).delete()

                    for u in umrs:
                        mmrs_for_del = mmrs_for_del.exclude(name=u.vid)
                    mmrs_for_del.delete()

                    summmrr = 0
                    for u in umrs:
                        if MRR.objects.filter(name=u.vid, profile=profile, year=year).exists():
                            continue
                        if ("азработка основной профессиональной образовательной" in u.vid or
                                "азработка примерной основной профессиональной образовательной" in u.vid or
                                "электронного учебного курса" in u.vid or
                                "нтеграция тестовых заданий в программную оболочку" in u.vid):
                            newmrr = MRR()
                            newmrr.profile = profile
                            newmrr.name = u.vid
                            print(newmrr.name)
                            newmrr.bal = 20
                            newmrr.default = 20
                            newmrr.year = year
                            summmrr += 20
                            newmrr.save()
                        if ("азработка примерной рабочей программы учебной дисциплины" in u.vid or
                                "азработка примерной дополнительной профессиональной " in u.vid or
                                "азработка дополнительной профессиональной программы" in u.vid or
                                "азработка фондовой лекции" in u.vid or
                                "азработка материалов для проведения конкурса профессионального мастерств" in u.vid or
                                "азработка сценария для учебного фильма" in u.vid or
                                "азработка компьютерной программы" in u.vid
                        ):
                            newmrr = MRR()
                            newmrr.profile = profile
                            newmrr.name = u.vid
                            print(newmrr.name)
                            newmrr.bal = 10
                            newmrr.default = 10
                            newmrr.year = year
                            summmrr += 10
                            newmrr.save()
                        if ("азработка рабочей программы учебной дисциплины" in u.vid or
                                "азработка рабочей программы государственной итоговой " in u.vid or
                                "азработка натурных объектов на контрольные экспертизы" in u.vid or
                                "азработка тестов для проведения мероприятий по указанию МВД России" in u.vid or
                                "азработка практикума по дисциплине" in u.vid or
                                "азработка материалов для вступительных испытаний" in u.vid or
                                "азработка материалов для проведения кандидатского экзамен" in u.vid or
                                "азработка материалов для мультимедийного сопровождения дисциплины" in u.vid or
                                "азработка сборника образцов процессуальных и служебных документов" in u.vid):
                            newmrr = MRR()
                            newmrr.profile = profile
                            newmrr.name = u.vid
                            print(newmrr.name)
                            newmrr.bal = 5
                            newmrr.default = 5
                            newmrr.year = year
                            summmrr += 5
                            newmrr.save()
                    newrating.summ = newurr.getsumm() + summmrr
                    newrating.save()
                    setplace(year, profile)
                    return Response([{

                        "text": "Рейтинг успешно переформирован",

                    }])
                except Exception as e:
                    print(e)
                    return Response([{

                        "text": "Ошибка при переформировании рейтинга",

                    }])
            except Exception as e:
                print(e)
                try:
                    try:
                        newrating = Rating.objects.get(profile=profile, year=year)
                    except:
                        newrating = Rating()
                    print(newrating)
                    print("sozd nwe rat")
                    newrating.profile = profile
                    newrating.year = year
                    itog = Predmet.objects.get(prepodavatel=profile, year=year, name="Итого за учебный год:",
                                               status=True)
                    try:
                        newurr = URR.objects.get(profile=profile, year=year)
                    except:
                        newurr = URR()
                    newurr.profile = profile
                    newurr.year = year
                    newurr.obsh = itog.get_obshaya_nagruzka()
                    newurr.obshbal = int(itog.get_obshaya_nagruzka() / 45)
                    sootn = int(itog.get_auditor_nagruzka() / itog.get_obshaya_nagruzka() * 100)
                    newurr.sootn = sootn
                    print(newurr.sootn)
                    if sootn > 70:
                        newurr.sootnbal = sootn - 70
                    else:
                        newurr.sootnbal = 0
                    print(newurr.sootnbal)
                    newurr.save()
                    umrs = UMR.objects.filter(prepodavatel=profile, year=year, include_rating=True)
                    summmrr = 0
                    for u in umrs:
                        if MRR.objects.filter(name=u.vid, profile=profile, year=year).exists():
                            continue
                        if ("азработка основной профессиональной образовательной" in u.vid or
                                "азработка примерной основной профессиональной образовательной" in u.vid or
                                "электронного учебного курса" in u.vid or
                                "нтеграция тестовых заданий в программную оболочку" in u.vid):
                            newmrr = MRR()
                            newmrr.profile = profile
                            newmrr.name = u.vid
                            print(newmrr.name)
                            newmrr.bal = 20
                            newmrr.default = 20
                            newmrr.year = year
                            summmrr += 20
                            newmrr.save()
                        if ("азработка примерной рабочей программы учебной дисциплины" in u.vid or
                                "азработка примерной дополнительной профессиональной программы" in u.vid or
                                "азработка дополнительной профессиональной программы" in u.vid or
                                "азработка фондовой лекции" in u.vid or
                                "азработка материалов для проведения конкурса профессионального мастерств" in u.vid or
                                "азработка сценария для учебного фильма" in u.vid or
                                "азработка компьютерной программы (обучающей, тестовой, прочее)" in u.vid
                        ):
                            newmrr = MRR()
                            newmrr.profile = profile
                            newmrr.name = u.vid
                            print(newmrr.name)
                            newmrr.bal = 10
                            newmrr.year = year
                            newmrr.default = 10
                            summmrr += 10
                            newmrr.save()
                        if ("азработка рабочей программы учебной дисциплины" in u.vid or
                                "азработкар рабочей программы государственной итоговой аттестации, программы практики" in u.vid or
                                "азработка натурных объектов на контрольные экспертизы" in u.vid or
                                "азработка тестов для проведения мероприятий по указанию МВД России" in u.vid or
                                "азработка практикума по дисциплине" in u.vid or
                                "азработка материалов для вступительных испытаний" in u.vid or
                                "азработка материалов для проведения кандидатского экзамен" in u.vid or
                                "азработка материалов для мультимедийного сопровождения дисциплины" in u.vid or
                                "азработка сборника образцов процессуальных и служебных документов" in u.vid):
                            newmrr = MRR()
                            newmrr.profile = profile
                            newmrr.name = u.vid
                            print(newmrr.name)
                            newmrr.bal = 5
                            newmrr.default = 5
                            newmrr.year = year
                            summmrr += 5
                            newmrr.save()

                    newrating.summ = newurr.getsumm() + summmrr
                    newrating.save()
                    setplace(year, profile)
                    return Response([{

                        "text": "Рейтинг успешно сформирован",

                    }])
                except Exception as e:
                    print(e)
                    return Response([{

                        "text": "Ошибка! Сначала заполните фактически выполненную работы за оба полугодия, а также данные\
                                             в шапке и профиле",
                    }])

            return Response([{

                "text": "Рейтинг успешно сформирован",
                "href": "rating/rate_otsenka/" + profile.user.username + "/" + year + "/",

            }])


"""Вывод информации в таблицу заполненности ИП"""


@api_view(['GET'])
def supertable_plan(request):
    year = request.GET['year']
    kafname = request.GET['kafname']
    if kafname == "all":
        profiles = Profile.objects.all()
    else:
        profiles = Profile.objects.filter(kafedra__name=kafname)
    data = []
    for profile in profiles:
        try:
            percent = 0
            zapoln = []
            dolhznost = profile.dolzhnost
            predmets_plan = Predmet.objects.filter(prepodavatel=profile, year=year, status=False).exists()
            predmets_fact = Predmet.objects.filter(prepodavatel=profile, year=year, status=True).exists()
            mes = Mesyac.objects.filter(prepodavatel=profile, year=year) \
                .exclude(name__contains="Итого", ucheb_nagruzka=0).exists()
            umr = UMR.objects.filter(prepodavatel=profile, year=year).exists()
            nir = NIR.objects.filter(prepodavatel=profile, year=year).exists()
            vr = VR.objects.filter(prepodavatel=profile, year=year).exists()
            inr = INR.objects.filter(prepodavatel=profile, year=year).exists()
            dr = DR.objects.filter(prepodavatel=profile, year=year).exists()
            info = ProfileInfo.objects.filter(profile=profile).exists()
            plan = Plan.objects.filter(year=year, prepod=profile).first()
            docinfo = DocInfo.objects.filter(plan=plan).exists()
            if info:
                if ProfileInfo.objects.filter(profile=profile).first().dolznost != "":
                    dolhznost = ProfileInfo.objects.filter(profile=profile).first().dolznost
                percent += 1
                zapoln.append("Профиль : Да")
            else:
                zapoln.append("Профиль : Нет")
            if docinfo:
                percent += 1
                zapoln.append("Шапка : Да")
            else:
                zapoln.append("Шапка : Нет")
            if predmets_plan:
                percent += 1
                zapoln.append("План : Да")
            else:
                zapoln.append("План : Нет")
            if predmets_fact:
                percent += 1
                zapoln.append("Факт : Да")
            else:
                zapoln.append("Факт : Нет")
            if mes:
                percent += 1
                zapoln.append("Ежемес.учет : Да")
            else:
                zapoln.append("Ежемес.учет : Нет")

            if umr:
                percent += 1
                zapoln.append("Метод.р : Да")
            else:
                zapoln.append("Метод.р : Нет")
            if nir:
                percent += 1
                zapoln.append("НИР : Да")
            else:
                zapoln.append("НИР : Нет")
            if vr:
                percent += 1
                zapoln.append("МПР : Да")
            else:
                zapoln.append("МПР : Нет")
            if inr:
                percent += 1
                zapoln.append("Иностр : Да")
            else:
                zapoln.append("Иностр : Нет")
            if dr:
                percent += 1
                zapoln.append("Иные : Да")
            else:
                zapoln.append("Иные : Нет")
            rating_query = Rating.objects.filter(profile=profile, year=year).exclude(summ=0).exists()
            try:
                stavka = ProfileInfo.objects.get(profile=profile).stavka
            except Exception as e:
                print(e)
                stavka = 'нет данных'
            if rating_query:
                rating = "+"
            else:
                rating = "-"

            data.append(
                {'fio': profile.fullname.split(" ")[0],
                 'kafedra': profile.kafedra.fullname,
                 'rating': rating,
                 'stavka': stavka,
                 'plan': str(percent * 10) + " %",
                 'username': profile.user.username,
                 'zapoln': zapoln,
                 'dolzhnost': dolhznost
                 }
            )
        except Exception as e:
            print(e)

    return Response(data)


"""Вывод информации в таблицу нагрузок всех кафедр"""


@api_view(['GET'])
def nagruzka_table(request):
    nagruzkas = Nagruzka.objects.all().order_by('kafedra__fullname')
    data = []
    for nagruzka in nagruzkas:
        try:
            change_date = dt.datetime.fromtimestamp(os.path.getctime(nagruzka.document.path)).strftime("%d %m %Y, %H:%M")
        except Exception as e:
            change_date = "файл не найден"

        data.append(
            {
                'kafedra':nagruzka.kafedra.fullname,
                'vid_nagruzki':nagruzka.status,
                'year':str(nagruzka.year)+"-"+str(nagruzka.year+1),
                'change_date': change_date,
                'href':nagruzka.document.url
            }
        )
    return Response(data)
    
@api_view(['GET'])
def zamech_table(request):
    kafname = request.GET.get('kafname')
    if kafname == 'all':
        zamech = Zamech.objects.all().order_by('profile__fullname')
    else:
        zamech = Zamech.objects.filter(profile__kafedra__name=kafname).order_by('profile__fullname')
    data = []
    for z in zamech:
        if z.status == False:
            date_2 = "-"
            status = 'не исправлено'
        else:
            date_2 = z.date_2.strftime("%m/%d/%Y")
            status = 'исправлено'
        data.append(
            {
                'profile':z.profile.fullname,
                'kafedra':z.profile.kafedra.fullname,
                'date_1':z.date_1.strftime("%m/%d/%Y"),
                'date_2':date_2,
                'status': status,
                'year':str(z.year)+"-"+str(z.year+1)
            }
        )
    return Response(data)


""" Работа с пользователями в главной таблице по кафедре"""


def deluser(request):
    if request.method == "POST":

        previos_username = request.POST["login"]
        previos_user = User.objects.get(username=previos_username)
        profile = Profile.objects.get(user=previos_user)

        try:
            profile.kafedra = None
            profile.save()
        except Exception as e:
            print(e)
            return HttpResponse("Ошибка при удалении пользователя")

        return HttpResponse("Пользователь удален, чтобы восстановить обратитесь к администации")
    else:
        return redirect('log')


def changepass(request):
    # profile=get_object_or_404(Profile,user=request.user)

    if request.method == "POST":
        form = ChangePassForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            previos_username = request.POST["prev_login"]
            previos_password = request.POST["prev_password"]
            fio = form.cleaned_data['fio']
            previos_user = User.objects.get(username=previos_username)
            if previos_username == username and previos_password == password:
                print("change fio")
                try:
                    profile = Profile.objects.get(user=previos_user)
                    profile.fullname = fio
                    profile.save()
                except Exception as e:
                    print(e)
                    return HttpResponse("Произошла ошибка при изменении данных пользователя")
            else:
                if previos_username == username and previos_password != password:
                    print("change pass")
                    try:
                        previos_user.set_password(password)
                        previos_user.email = password
                        previos_user.save()
                        profile = Profile.objects.get(user=previos_user)
                        profile.fullname = fio
                        profile.save()
                    except Exception as e:
                        print(e)
                        return HttpResponse("Произошла ошибка при изменении данных пользователя")
                else:
                    print("change pass login ")
                    try:
                        previos_user.username = username
                        previos_user.set_password(password)
                        previos_user.email = password
                        previos_user.save()
                        profile = Profile.objects.get(user=previos_user)
                        profile.fullname = fio
                        profile.save()

                    except Exception as e:
                        print(e)
                        return HttpResponse(
                            "Произошла ошибка при изменении данных пользователя, такой пользователь уже существует")

        else:
            return HttpResponse("Ошибка при сохранении")
            return HttpResponse("Произошла ошибка при изменении данных пользователя")

    return HttpResponse("Учетные данные успешно изменены")


def adduser(request):
    if request.method == "POST":
        form = UserAddForm(request.POST)
        profile = get_object_or_404(Profile, user=request.user)
        kafedra = profile.kafedra
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            fio = form.cleaned_data['fio']
            try:
                usernew = User.objects.create_user(username, password, password)
                profilenew = Profile()
                profilenew.user = usernew
                profilenew.fullname = fio
                profilenew.kafedra = kafedra
                usernew.save()
                profilenew.save()
            except Exception as e:
                print(e)
                return HttpResponse("Произошла ошибка при добавлении пользователя")
        else:
            return HttpResponse("Произошла ошибка при добавлении пользователя,ошибка при отправке формы")
    else:
        return HttpResponse("Ошибка при сохранении")
        return render(request, 'error.html', {'content': "Произошла ошибка при добавлении пользователя"})
    return HttpResponse("Сотрудник успешно добавлен")


def createrating(request, year, slug):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user__username=slug)
        try:
            newrating = Rating.objects.get(profile=profile, year=year)
            newrating.profile = profile
            newrating.year = year
            print("menyaem")
            itog = Predmet.objects.get(prepodavatel=profile, year=year, name="Итого за учебный год:", status=True)
            try:
                newurr = URR.objects.get(profile=profile, year=year)
            except:
                newurr = URR()
            newurr.profile = profile
            newurr.year = year
            newurr.obsh = itog.get_obshaya_nagruzka()
            newurr.obshbal = int(itog.get_obshaya_nagruzka() / 45)
            # не забыть поменять на флоат
            sootn = int(itog.get_auditor_nagruzka() / itog.get_obshaya_nagruzka() * 100)
            newurr.sootn = sootn
            print(newurr.sootn)

            print(newurr.sootnbal)
            if sootn > 70:
                newurr.sootnbal = sootn - 70
            else:
                newurr.sootnbal = 0
            print(newurr.sootn)

            print(newurr.sootnbal)
            newurr.save()
            umrs = UMR.objects.filter(prepodavatel=profile, year=year, include_rating=True)
            mmrs_for_del = MRR.objects.filter(profile=profile, year=year)
            for name in MRR.objects.filter(profile=profile).values_list('name', flat=True).distinct():
                MRR.objects.filter(pk__in=MRR.objects.filter(name=name).values_list('id', flat=True)[1:]).delete()
            for u in umrs:
                mmrs_for_del = mmrs_for_del.exclude(name=u.vid)
            mmrs_for_del.delete()

            summmrr = 0
            for u in umrs:
                if MRR.objects.filter(name=u.vid, profile=profile, year=year).exists():
                    continue
                if ("азработка основной профессиональной образовательной" in u.vid or
                        "азработка примерной основной профессиональной образовательной" in u.vid or
                        "электронного учебного курса" in u.vid or
                        "нтеграция тестовых заданий в программную оболочку" in u.vid):
                    newmrr = MRR()
                    newmrr.profile = profile
                    newmrr.name = u.vid
                    print(newmrr.name)
                    newmrr.bal = 20
                    newmrr.default = 20
                    newmrr.year = year
                    summmrr += 20
                    newmrr.save()
                if ("азработка примерной рабочей программы учебной дисциплины" in u.vid or
                        "азработка примерной дополнительной профессиональной" in u.vid or
                        "азработка дополнительной профессиональной программы" in u.vid or
                        "азработка фондовой лекции" in u.vid or
                        "азработка материалов для проведения конкурса профессионального мастерств" in u.vid or
                        "азработка сценария для учебного фильма" in u.vid or
                        "азработка компьютерной программы" in u.vid
                ):
                    newmrr = MRR()
                    newmrr.profile = profile
                    newmrr.name = u.vid
                    print(newmrr.name)
                    newmrr.bal = 10
                    newmrr.default = 10
                    newmrr.year = year
                    summmrr += 10
                    newmrr.save()
                if ("азработка рабочей программы учебной дисциплины" in u.vid or
                        "азработка рабочей программы государственной итоговой " in u.vid or
                        "азработка натурных объектов на контрольные экспертизы" in u.vid or
                        "азработка тестов для проведения мероприятий по указанию МВД России" in u.vid or
                        "азработка практикума по дисциплине" in u.vid or
                        "азработка материалов для вступительных испытаний" in u.vid or
                        "азработка материалов для проведения кандидатского экзамен" in u.vid or
                        "азработка материалов для мультимедийного сопровождения дисциплины" in u.vid or
                        "азработка сборника образцов процессуальных и служебных документов" in u.vid):
                    newmrr = MRR()
                    newmrr.profile = profile
                    newmrr.name = u.vid
                    print(newmrr.name)
                    newmrr.bal = 5
                    newmrr.default = 5
                    newmrr.year = year
                    summmrr += 5
                    newmrr.save()
            newrating.summ = newurr.getsumm() + summmrr
            newrating.save()
            setplace(year, profile)
        except Exception as e:
            print(e)
            try:
                try:
                    newrating = Rating.objects.get(profile=profile, year=year)
                except:
                    newrating = Rating()
                print(newrating)
                print("sozd nwe rat")
                newrating.profile = profile
                newrating.year = year
                itog = Predmet.objects.get(prepodavatel=profile, year=year, name="Итого за учебный год:", status=True)
                try:
                    newurr = URR.objects.get(profile=profile, year=year)
                except:
                    newurr = URR()
                newurr.profile = profile
                newurr.year = year
                newurr.obsh = itog.get_obshaya_nagruzka()
                newurr.obshbal = int(itog.get_obshaya_nagruzka() / 45)
                sootn = int(itog.get_auditor_nagruzka() / itog.get_obshaya_nagruzka() * 100)
                newurr.sootn = sootn
                print(newurr.sootn)
                if sootn > 70:
                    newurr.sootnbal = sootn - 70
                else:
                    newurr.sootnbal = 0
                print(newurr.sootnbal)
                newurr.save()
                umrs = UMR.objects.filter(prepodavatel=profile, year=year, include_rating=True)
                summmrr = 0
                for u in umrs:
                    if MRR.objects.filter(name=u.vid, profile=profile, year=year).exists():
                        continue
                    if ("азработка основной профессиональной образовательной" in u.vid or
                            "азработка примерной основной профессиональной образовательной" in u.vid or
                            "электронного учебного курса" in u.vid or
                            "нтеграция тестовых заданий в программную оболочку" in u.vid):
                        newmrr = MRR()
                        newmrr.profile = profile
                        newmrr.name = u.vid
                        print(newmrr.name)
                        newmrr.bal = 20
                        newmrr.default = 20
                        newmrr.year = year
                        summmrr += 20
                        newmrr.save()
                    if ("азработка примерной рабочей программы учебной дисциплины" in u.vid or
                            "азработка примерной дополнительной профессиональной программы" in u.vid or
                            "азработка дополнительной профессиональной программы" in u.vid or
                            "азработка фондовой лекции" in u.vid or
                            "азработка материалов для проведения конкурса профессионального мастерств" in u.vid or
                            "азработка сценария для учебного фильма" in u.vid or
                            "азработка компьютерной программы (обучающей, тестовой, прочее)" in u.vid
                    ):
                        newmrr = MRR()
                        newmrr.profile = profile
                        newmrr.name = u.vid
                        print(newmrr.name)
                        newmrr.bal = 10
                        newmrr.default = 10
                        newmrr.year = year
                        summmrr += 10
                        newmrr.save()
                    if ("азработка рабочей программы учебной дисциплины" in u.vid or
                            "азработкар рабочей программы государственной итоговой аттестации, программы практики" in u.vid or
                            "азработка натурных объектов на контрольные экспертизы" in u.vid or
                            "азработка тестов для проведения мероприятий по указанию МВД России" in u.vid or
                            "азработка практикума по дисциплине" in u.vid or
                            "азработка материалов для вступительных испытаний" in u.vid or
                            "азработка материалов для проведения кандидатского экзамен" in u.vid or
                            "азработка материалов для мультимедийного сопровождения дисциплины" in u.vid or
                            "азработка сборника образцов процессуальных и служебных документов" in u.vid):
                        newmrr = MRR()
                        newmrr.profile = profile
                        newmrr.name = u.vid
                        print(newmrr.name)
                        newmrr.bal = 5
                        newmrr.default = 10
                        newmrr.year = year
                        summmrr += 5
                        newmrr.save()

                newrating.summ = newurr.getsumm() + summmrr
                newrating.save()
                setplace(year, profile)
            except Exception as e:
                print(e)
                return render(request, 'error.html',
                              {
                                  'content': "Сначала заполните фактически выполненную работы за оба полугодия (проверьте наличие строк итого за год, итого за 1 полгодие и тд,если их нет то сохраните таблицы), а также данные в шапке и профиле"})

        return redirect('rate_otsenka', slug=profile.user.username, year=year)
    else:
        return redirect('log')


def profileinfo(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            profile = get_object_or_404(Profile, user=request.user)

            form = ProfileInfoForm(request.POST)
            print(request.POST)

            if form.is_valid():
                try:
                    infodel = get_object_or_404(PofileInfo, plan=plan)
                    infodel.delete()
                except:
                    print("ne")

                infodel = form.save(commit=False)
                profile.dolzhnost = infodel.dolznost
                infodel.profile = profile
                profile.save()
                infodel.save()





            else:
                HttpResponse("Ошибка при сохранении данных")
        return HttpResponse("Успешно сохранено")
    else:
        return redirect('log')


""" Работа с документами """


def exelobr(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'examplexlsx.xlsx')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404


def exelobrfact(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'examplexlsxfact.xlsx')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404


def docxobr(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'exampleip.docx')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(),
                                    content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404


def handle_uploaded_file(f):
    with open('anal.docx', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def documentAnalize(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            file = request.FILES['file']
            year = request.POST['year']
            profile = get_object_or_404(Profile, user=request.user)
            if profile.role == 3 or profile.role == 2:
                profile = get_object_or_404(Profile, user__username=request.POST['profile'])
            print(profile.fullname)
            handle_uploaded_file(file)
            try:
                data = takeTable('anal.docx')
            except Exception as e:
                print(e)
                print("fail takeTable")
                return render(request, 'error.html', {
                    'content': "Произошла ошибка при заполнении плана из загруженного doc файла, пожалуйста проверьте формат документа(см.справку)"})

            if data == 'dolbaeb':
                print("fail docfile")
                return render(request, 'error.html', {
                    'content': "Произошла ошибка при заполнении плана из загруженного doc файла, пожалуйста проверьте формат документа(см.справку)"})
            print(data)
            for table in range(len(data)):
                if table == 0:
                    Mesyac.objects.filter(prepodavatel=profile, year=year).delete()
                    for row in range(len(data[table])):
                        count = 0
                        if row < 6:

                            mes = Mesyac()
                            mes.name = data[table][row][0]
                            mes.leccii = float(data[table][row][1])
                            mes.seminar = float(data[table][row][2])
                            mes.practici_v_gruppe = float(data[table][row][3])
                            mes.practici_v_podgruppe = float(data[table][row][4])
                            mes.krugliy_stol = float(data[table][row][5])
                            mes.konsultacii_pered_ekzamenom = float(data[table][row][6])
                            mes.tekushie_konsultacii = float(data[table][row][7])
                            mes.vneauditor_chtenie = float(data[table][row][8])
                            mes.rucovodstvo_practikoy = float(data[table][row][9])
                            mes.rucovodstvo_VKR = float(data[table][row][10])
                            mes.rucovodstvo_kursovoy = float(data[table][row][11])
                            mes.proverka_auditor_KR = float(data[table][row][12])
                            mes.proverka_dom_KR = float(data[table][row][13])
                            mes.proverka_practicuma = float(data[table][row][14])
                            mes.proverka_lab = float(data[table][row][15])
                            mes.priem_zashit_practic = float(data[table][row][16])
                            mes.zacheti_ust = float(data[table][row][17])
                            mes.zacheti_pism = float(data[table][row][18])
                            mes.priem_vstupit = float(data[table][row][19])
                            mes.ekzamenov = float(data[table][row][20])
                            mes.priem_GIA = float(data[table][row][21])
                            mes.priem_kandidtskih = float(data[table][row][22])
                            mes.rucovodstvo_adunctami = float(data[table][row][23])
                            mes.ucheb_nagruzka = float(data[table][row][24])
                            mes.auditor_nagruzka = float(data[table][row][25])

                            mes.prepodavatel = profile
                            mes.kafedra = profile.kafedra
                            mes.year = year
                            mes.polugodie = '1'
                            mes.save()
                        else:
                            mes = Mesyac()
                            mes.name = data[table][row][0]
                            mes.leccii = float(data[table][row][1])
                            mes.seminar = float(data[table][row][2])
                            mes.practici_v_gruppe = float(data[table][row][3])
                            mes.practici_v_podgruppe = float(data[table][row][4])
                            mes.krugliy_stol = float(data[table][row][5])
                            mes.konsultacii_pered_ekzamenom = float(data[table][row][6])
                            mes.tekushie_konsultacii = float(data[table][row][7])
                            mes.vneauditor_chtenie = float(data[table][row][8])
                            mes.rucovodstvo_practikoy = float(data[table][row][9])
                            mes.rucovodstvo_VKR = float(data[table][row][10])
                            mes.rucovodstvo_kursovoy = float(data[table][row][11])
                            mes.proverka_auditor_KR = float(data[table][row][12])
                            mes.proverka_dom_KR = float(data[table][row][13])
                            mes.proverka_practicuma = float(data[table][row][14])
                            mes.proverka_lab = float(data[table][row][15])
                            mes.priem_zashit_practic = float(data[table][row][16])
                            mes.zacheti_ust = float(data[table][row][17])
                            mes.zacheti_pism = float(data[table][row][18])
                            mes.priem_vstupit = float(data[table][row][19])
                            mes.ekzamenov = float(data[table][row][20])
                            mes.priem_GIA = float(data[table][row][21])
                            mes.priem_kandidtskih = float(data[table][row][22])
                            mes.rucovodstvo_adunctami = float(data[table][row][23])
                            mes.ucheb_nagruzka = float(data[table][row][24])
                            mes.auditor_nagruzka = float(data[table][row][25])
                            mes.prepodavatel = profile
                            mes.kafedra = profile.kafedra
                            mes.polugodie = '2'
                            mes.year = year
                            mes.save()
                            print("sohraninen")
                if table == 1:
                    for row in range(len(data[table])):
                        count = 0
                        umr = UMR()
                        umr.vid = data[table][row][1]
                        umr.srok = data[table][row][2]
                        umr.otmetka = data[table][row][3]
                        umr.prepodavatel = profile

                        umr.year = year
                        umr.polugodie = '1'
                        umr.save()
                        print("sohraninen")
                if table == 2:
                    for row in range(len(data[table])):
                        count = 0
                        umr = UMR()
                        count += 1
                        umr.vid = data[table][row][1]
                        umr.srok = data[table][row][2]
                        umr.otmetka = data[table][row][3]
                        umr.prepodavatel = profile
                        umr.year = year
                        umr.polugodie = '2'
                        umr.save()
                if table == 3:
                    for row in range(len(data[table])):
                        count = 0
                        umr = NIR()
                        umr.vid = data[table][row][1]
                        umr.srok = data[table][row][2]
                        umr.otmetka = data[table][row][3]
                        umr.prepodavatel = profile

                        umr.year = year
                        umr.polugodie = '1'
                        umr.save()
                        print("sohraninen")
                if table == 4:
                    for row in range(len(data[table])):
                        count = 0
                        umr = NIR()

                        count += 1
                        umr.vid = data[table][row][1]
                        umr.srok = data[table][row][2]
                        umr.otmetka = data[table][row][3]
                        umr.prepodavatel = profile
                        umr.year = year
                        umr.polugodie = '2'
                        umr.save()
                if table == 5:
                    for row in range(len(data[table])):
                        count = 0
                        umr = VR()
                        umr.vid = data[table][row][1]
                        umr.srok = data[table][row][2]
                        umr.otmetka = data[table][row][3]
                        umr.prepodavatel = profile

                        umr.year = year
                        umr.polugodie = '1'
                        umr.save()
                        print("sohraninen")
                if table == 6:
                    for row in range(len(data[table])):
                        count = 0
                        umr = VR()

                        count += 1
                        umr.vid = data[table][row][1]
                        umr.srok = data[table][row][2]
                        umr.otmetka = data[table][row][3]
                        umr.prepodavatel = profile
                        umr.year = year
                        umr.polugodie = '2'
                        umr.save()
                if table == 7:
                    for row in range(len(data[table])):
                        count = 0
                        umr = INR()

                        umr.vid = data[table][row][1]
                        umr.srok = data[table][row][2]
                        umr.otmetka = data[table][row][3]
                        umr.prepodavatel = profile

                        umr.year = year
                        umr.polugodie = '1'
                        umr.save()
                        print("sohraninen")
                if table == 8:
                    for row in range(len(data[table])):
                        count = 0
                        umr = INR()

                        count += 1
                        umr.vid = data[table][row][1]
                        umr.srok = data[table][row][2]
                        umr.otmetka = data[table][row][3]
                        umr.prepodavatel = profile
                        umr.year = year
                        umr.polugodie = '2'
                        umr.save()
                if table == 9:
                    for row in range(len(data[table])):
                        count = 0
                        umr = DR()
                        umr.vid = data[table][row][1]
                        umr.srok = data[table][row][2]
                        umr.otmetka = data[table][row][3]
                        umr.prepodavatel = profile

                        umr.year = year
                        umr.polugodie = '1'
                        umr.save()
                        print("sohraninen")
                if table == 10:
                    for row in range(len(data[table])):
                        count = 0
                        umr = DR()

                        count += 1
                        umr.vid = data[table][row][1]
                        umr.srok = data[table][row][2]
                        umr.otmetka = data[table][row][3]
                        umr.prepodavatel = profile
                        umr.year = year
                        umr.polugodie = '2'
                        umr.save()
            return redirect('detail_plan', slug=profile.user.username, year=request.POST['year'])
        else:
            return redirect('log')


def documentSave(request, year, slug):
    if request.user.is_authenticated:
        try:
            user = User.objects.get(username=slug)
            profile = get_object_or_404(Profile, user=user)
            plan = get_object_or_404(Plan, prepod=profile, year=year)
            data = []
            # count row for every table
            indexRow = []

            predmets = Predmet.objects.filter(prepodavatel=profile, polugodie=1, status=False, year=year)
            for p in predmets:
                arr = p.all_values()
                for a in arr:
                    if a == '0':
                        data.append(" ")
                    else:
                        data.append(a)

            indexRow.append(predmets.count())

            # data+=[" "]*(122-(predmets.count()*12))
            ##не забыть впихнуть 11 клеток итогов ра полугодие
            ##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            predmets = Predmet.objects.filter(prepodavatel=profile, polugodie=2, status=False, year=year)
            for p in predmets:
                arr = p.all_values()
                for a in arr:
                    if a == '0':
                        data.append(" ")
                    else:
                        data.append(a)
            indexRow.append(predmets.count())

            predmets = Predmet.objects.filter(prepodavatel=profile, polugodie=1, status=True, year=year)
            itog1 = ()
            itog2 = ()
            itogall = ()
            for p in predmets:

                arr = p.all_values()
                if arr[0] == 'Итого за 1 полугодие:':
                    itog1 = arr
                    continue
                for a in arr:
                    if a == '0':
                        data.append(" ")
                    else:
                        data.append(a)
            if itog1:
                for a in itog1:
                    if a == '0':
                        data.append(" ")
                    else:
                        data.append(a)

            indexRow.append(predmets.count())

            ##не забыть впихнуть 11 клеток итогов ра полугодие
            ##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            predmets = Predmet.objects.filter(prepodavatel=profile, polugodie=2, status=True, year=year)
            for p in predmets:
                arr = p.all_values()
                if arr[0] == 'Итого за 2 полугодие:':
                    itog2 = arr
                    continue
                if arr[0] == 'Итого за учебный год:':
                    itogall = arr
                    continue
                for a in arr:
                    if a == '0':
                        data.append(" ")
                    else:
                        data.append(a)
            indexRow.append(predmets.count())
            if itog2:
                for a in itog2:
                    if a == '0':
                        data.append(" ")
                    else:
                        data.append(a)
            if itogall:
                for a in itogall:
                    if a == '0':
                        data.append(" ")
                    else:
                        data.append(a)
            # по месяцам!!
            # data += [" "] * (375)
            ##normalno po mesyacam
            # u admina dolzhna bit tablisa zapolnena
            mesyac = Mesyac.objects.filter(prepodavatel=profile, year=year)
            for m in mesyac:
                arr = m.all_values()
                for a in arr:
                    if a == '0':
                        data.append(" ")
                    else:
                        data.append(a)

            # учебно метадоч работа
            umr = UMR.objects.filter(prepodavatel=profile, polugodie=1, year=year)
            count = 1
            for u in umr:
                arr = u.all_values()
                data.append(str(count))
                for a in arr:
                    if a == '0':
                        data.append(" ")
                    else:
                        data.append(a)
                count += 1
            indexRow.append(umr.count())

            umr = UMR.objects.filter(prepodavatel=profile, polugodie=2, year=year)
            count = 1
            for u in umr:
                arr = u.all_values()
                data.append(str(count))
                for a in arr:
                    if a == '0':
                        data.append(" ")
                    else:
                        data.append(a)
                count += 1
            indexRow.append(umr.count())
            # таблица научно исслеовтельских работа
            nir = NIR.objects.filter(prepodavatel=profile, polugodie=1, year=year)
            count = 1
            for u in nir:
                arr = u.all_values()
                data.append(str(count))
                for a in arr:
                    if a == '0':
                        data.append(" ")
                    else:
                        data.append(a)
                count += 1
            indexRow.append(nir.count())
            nir = NIR.objects.filter(prepodavatel=profile, polugodie=2, year=year)
            count = 1
            for u in nir:
                arr = u.all_values()
                data.append(str(count))
                for a in arr:
                    if a == '0':
                        data.append(" ")
                    else:
                        data.append(a)
                count += 1
            indexRow.append(nir.count())
            # для воспитаттльной работы
            vr = VR.objects.filter(prepodavatel=profile, polugodie=1, year=year)
            count = 1
            for u in vr:
                arr = u.all_values()
                data.append(str(count))
                for a in arr:
                    if a == '0':
                        data.append(" ")
                    else:
                        data.append(a)
                count += 1
            indexRow.append(vr.count())

            vr = VR.objects.filter(prepodavatel=profile, polugodie=2, year=year)
            count = 1
            for u in vr:
                arr = u.all_values()
                data.append(str(count))
                for a in arr:
                    if a == '0':
                        data.append(" ")
                    else:
                        data.append(a)
                count += 1
            indexRow.append(vr.count())
            # работа ин спец
            inr = INR.objects.filter(prepodavatel=profile, polugodie=1, year=year)
            count = 1
            for u in inr:
                arr = u.all_values()
                data.append(str(count))
                for a in arr:
                    if a == '0':
                        data.append(" ")
                    else:
                        data.append(a)
                count += 1
            indexRow.append(inr.count())

            inr = INR.objects.filter(prepodavatel=profile, polugodie=2, year=year)
            count = 1
            for u in inr:
                arr = u.all_values()
                data.append(str(count))
                for a in arr:
                    if a == '0':
                        data.append(" ")
                    else:
                        data.append(a)
                count += 1
            indexRow.append(inr.count())
            # для другой работы
            dr = DR.objects.filter(prepodavatel=profile, polugodie=1, year=year)
            count = 1
            for u in dr:
                arr = u.all_values()
                data.append(str(count))
                for a in arr:
                    if a == '0':
                        data.append(" ")
                    else:
                        data.append(a)
                count += 1
            indexRow.append(dr.count())

            dr = DR.objects.filter(prepodavatel=profile, polugodie=2, year=year)
            count = 1
            for u in dr:
                arr = u.all_values()
                data.append(str(count))
                for a in arr:
                    if a == '0':
                        data.append(" ")
                    else:
                        data.append(a)
                count += 1
            indexRow.append(dr.count())
            # главная таблица
            data += plan.all_values()
            
            #информация о замечаниях от умр
            zamech = Zamech.objects.filter(profile=profile,year=year)
            indexRow.append(zamech.count())
            for z in zamech:
                data.append(str(z.date_1.strftime("%m/%d/%Y")))
                data.append(z.name)
            # shapka
            try:
                docinf = DocInfo.objects.get(plan=plan)
            except:
                docinf = DocInfo(plan=plan)
            listInfo = docinf.all_values()
            # print(indexRow)
            # print(data)

            doc = writeInfoDoc(listInfo, data, indexRow)
            # doc=createDoc('testforsave',data)
            # plan.document.save("testsave",f,save=True)
            file_path = plan.document.path
            f = BytesIO()
            doc.save(f)
            response = HttpResponse(f.getvalue(),
                                    content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
            response['Content-Disposition'] = 'inline; filename=plan.docx'
            return response
        except Exception as e:

            return render(request, 'error.html', {
                'content': "Произошла ошибка при заполнении плана из загруженного доумента, пожалуйста проверьте "
                           "формат документа(см.справку)"})

        # print(data)
        # response = HttpResponse(doc,content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
        # return response
        return redirect('detail_plan', slug=profile.user.username, year=plan.year)

    else:
        return redirect('log')


def saveDB(request):
    saveallnagr()
    return redirect('index')


@api_view(['POST'])
def nagruzkaSave(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            profile = get_object_or_404(Profile, user=request.user)
            form = NagruzkaForm(request.POST, request.FILES)
            if form.is_valid():
                try:
                    nagruzka = form.save(commit=False)
                    my_object = Nagruzka.objects.get(kafedra=profile.kafedra, year=nagruzka.year,
                                                     status=nagruzka.status)
                    my_object.delete()
                    nagruzka.kafedra = profile.kafedra
                    nagruzka.save()
                    if nagruzka.status == 'Планируемая':
                        flag = True
                    else:
                        flag = False
                    print(nagruzka.status)
                    response = ""
                    response = checkDocumentXLS(nagruzka.document.path, flag)
                    print(nagruzka.document.path, flag, response)
                    profiles = Profile.objects.filter(kafedra=profile.kafedra)
                    for p in profiles:
                        try:

                            name = p.fullname.split(' ')[0]
                            prepod = checkPrepods(nagruzka.document.path, name)
                            response += "\n •   " + prepod + "\n"
                        except Exception as e:
                            print(e)
                            response += "Не нашлись данные " + p.fullname

                    print(response)
                    return Response([{

                        "text": "Нагрузка успешно заменена, ниже представлены сведения о документе \n" + response + '\n',
                        "kafname": "Нагрузка по кафедре " + nagruzka.kafedra.fullname + " " + nagruzka.status

                    }])
                except Nagruzka.DoesNotExist:

                    nagruzka = form.save(commit=False)
                    nagruzka.kafedra = profile.kafedra
                    nagruzka.save()
                    if nagruzka.status == 'Планируемая':
                        flag = True
                    else:
                        flag = False
                    response = ""
                    response = checkDocumentXLS(nagruzka.document.path, flag)
                    print(nagruzka.document.path, flag, response)
                    profiles = Profile.objects.filter(kafedra=profile.kafedra)
                    for p in profiles:
                        try:

                            name = p.fullname.split(' ')[0]
                            prepod = checkPrepods(nagruzka.document.path, name)
                            response += "\n •   " + prepod + "\n"
                        except Exception as e:
                            print(e)
                            response += "Не нашлись учетные данные " + p.fullname
                    return Response([{

                        "text": "Нагрузка успешно добавлена, ниже представлены сведения о документе \n" + response + '\n',
                        "kafname": "Нагрузка по кафедре " + nagruzka.kafedra.fullname + " " + nagruzka.status

                    }])
            else:
                return Response([{

                    "text": "Произошла ошибка при сохранении нагрузки",

                }])

    else:
        return redirect('log')


def deleteNgruzka(request, year):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user=request.user)
        print("1")
        if profile.role == 2:
            nagruzka = get_object_or_404(Nagruzka, year=year, kafedra=profile.kafedra)
            nagruzka.delete()
            return redirect('index')
    else:
        return redirect('log')


# анализ нагрузки
def nagruzka(request, year, slug):
    if request.user.is_authenticated:
        try:
            user = User.objects.get(username=slug)
            profile = get_object_or_404(Profile, user=user)
            plan = get_object_or_404(Plan, prepod=profile, year=year)
            nagruzkadoc = get_object_or_404(
                Nagruzka.objects.filter(year=year, kafedra=profile.kafedra).exclude(status='Фактическая'))

            try:
                plans = Plan.objects.filter(prepod__kafedra=profile.kafedra,year=year)
                count = 0
                for p in plans:
                    if p.name[0:-4] == plan.name[0:-4]:
                        count += 1
                if count == 2:
                    data = takeXls(nagruzkadoc.document.path, profile.fullname.split(' ', 1)[0], True)
                else:
                    data = takeXls(nagruzkadoc.document.path, profile.fullname.split(' ', 1)[0], True)
                if type(data) != list:
                    if data == '404':
                        return render(request, 'error.html', {
                            'content': "Произошла ошибка при заполнении плана из загруженного XLSX учебной нагрузки файла, пожалуйста проверьте формат документа(см.справку), ФИО преподавателя не найдено, проверьте написание"})

                    if data == 'лекции':
                        return render(request, 'error.html', {
                            'content': "Произошла ошибка при заполнении плана из загруженного XLSX учебной нагрузки файла, пожалуйста проверьте формат документа(см.справку), возможно орфографическая ошибка в слове " + data + ", либо строчка в exel документе с наименованием видов учебной работы(лекции, практики и т.д) находится не в соответствии с образцом, должна быть на 8 строчке"})

                    return render(request, 'error.html', {
                        'content': "Произошла ошибка при заполнении плана из загруженного XLSX учебной нагрузки файла, пожалуйста проверьте формат документа(см.справку), возможно орфографическая ошибка в слове " + data})

            except Exception as e:
                print(e)
                return render(request, 'error.html', {
                    'content': "Произошла ошибка при заполнении плана из загруженного XLSX учебной нагрузки файла, пожалуйста проверьте формат документа(см.справку)"})

            # for i in range(len(data)):
            #     for j in range(len(data[i])):
            #         print(data[i][j])
            # # print('')
            # print(data)
            predmetsdel = Predmet.objects.filter(prepodavatel=profile, year=year, status=False)
            predmetsdel.delete()
            fields = Predmet._meta.get_fields()
            for table in range(len(data)):
                if table == 0:
                    for row in range(len(data[table])):
                        count = 0
                        predmet = Predmet()
                        # print(data)
                        # print(len(data[table]))
                        # print(data[table])

                        if data[table][row][0] == "0":
                            continue
                        for field in fields:
                            if field.name == "id":
                                continue
                            if row == (len(data[table]) - 1) and field.name == "name":
                                setattr(predmet, field.name, "Итого за 1 полугодие:")
                                continue
                            if row == (len(data[table]) - 1) and field.name == "auditor_nagruzka":
                                setattr(predmet, field.name, data[table][row][count])
                                break

                            setattr(predmet, field.name, data[table][row][count])

                            if count == 25:
                                break
                            count += 1
                        predmet.kafedra = profile.kafedra
                        # print(predmet.__dict__)
                        predmet.prepodavatel = profile
                        predmet.year = year
                        predmet.polugodie = '1'
                        predmet.status = False
                        # tru если выполена false если план

                        # print(data)
                        predmet.save1()

                if table == 1:
                    for row in range(len(data[table])):
                        count = 0
                        predmet = Predmet()
                        # print(len(data[table]))
                        # print(data[table])
                        # print( data[table][row][0])
                        if data[table][row][0] == "0":
                            continue
                        for field in fields:
                            if field.name == "id":
                                continue
                            if row == (len(data[table]) - 2) and field.name == "name":
                                setattr(predmet, field.name, "Итого за 2 полугодие:")
                                continue
                            if row == (len(data[table]) - 1) and field.name == "name":
                                setattr(predmet, field.name, "Итого за учебный год:")
                                continue

                            if row == (len(data[table]) - 2) and field.name == "auditor_nagruzka":
                                setattr(predmet, field.name, data[table][row][count])
                                break
                            if row == (len(data[table]) - 1) and field.name == "auditor_nagruzka":
                                setattr(predmet, field.name, data[table][row][count])
                                break

                            setattr(predmet, field.name, data[table][row][count])
                            # print(count)
                            if count == 25:
                                break
                            count += 1
                            # print(field.name+str(data[table][row][count]))
                        predmet.kafedra = profile.kafedra
                        # print(predmet.__dict__)
                        predmet.prepodavatel = profile
                        predmet.year = year
                        predmet.polugodie = '2'
                        predmet.status = False  # tru если выполена false если план
                        # print(predmet.all_values())
                        predmet.save1()

            return redirect('detail_plan', slug=profile.user.username, year=year)
        except Exception as e:
            print(e)
            return render(request, 'error.html', {
                'content': "Произошла ошибка при заполнении плана из загруженного XLSX учебной нагрузки файла, пожалуйста проверьте формат документа(см.справку)"})

    else:
        return redirect('log')


def nagruzkafact(request, year, slug):
    if request.user.is_authenticated:
        user = User.objects.get(username=slug)
        profile = get_object_or_404(Profile, user=user)
        plan = get_object_or_404(Plan, prepod=profile, year=year)
        try:

            nagruzkadoc = get_object_or_404(Nagruzka, year=year, kafedra=profile.kafedra, status='Фактическая')
            print(nagruzkadoc)
        except:
            return render(request, 'error.html', {
                'content': "Произошла ошибка при заполнении плана из загруженного XLSX учебной нагрузки файла, пожалуйста проверьте формат документа(см.справку)"})
        print(plan.name)

        data = ""
        try:
            plans = Plan.objects.filter(prepod__kafedra=profile.kafedra,year=year)
            count = 0
            for p in plans:
                if p.name[0:-4] == plan.name[0:-4]:
                    count += 1
                # print(p)
                # print(p)
            if count == 2:
                data = takeXls(nagruzkadoc.document.path, plan.name, False)
            else:
                data = takeXls(nagruzkadoc.document.path, profile.fullname.split(' ', 1)[0], False)
        except:
            return render(request, 'error.html', {
                'content': "Произошла ошибка при заполнении плана из загруженного XLSX учебной нагрузки файла, пожалуйста проверьте формат документа(см.справку), возможно орфографическая ошибка в слове " + data})
        if type(data) != list:
            if data == 'лекции':
                return render(request, 'error.html', {
                    'content': "Произошла ошибка при заполнении плана из загруженного XLSX учебной нагрузки файла, пожалуйста проверьте формат документа(см.справку), возможно орфографическая ошибка в слове " + data + ", либо строчка в exel документе с наименованием видов учебной работы(лекции, практики и т.д) находится не в соответствии с образцом, должна быть на 8 строчке"})

            return render(request, 'error.html', {
                'content': "Произошла ошибка при заполнении плана из загруженного XLSX учебной нагрузки файла, пожалуйста проверьте формат документа(см.справку), возможно орфографическая ошибка в слове " + data})

        # for i in range(len(data)):
        #     for j in range(len(data[i])):
        #         print(data[i][j])
        # # print('')
        # print(data)
        predmetsdel = Predmet.objects.filter(prepodavatel=profile, year=year, status=True)
        predmetsdel.delete()
        fields = Predmet._meta.get_fields()
        for table in range(len(data)):
            if table == 0:
                for row in range(len(data[table])):
                    count = 0
                    predmet = Predmet()
                    # print(data)
                    # print(len(data[table]))
                    # print(data[table])

                    if data[table][row][0] == "0":
                        continue
                    for field in fields:
                        if field.name == "id":
                            continue
                        if row == (len(data[table]) - 1) and field.name == "name":
                            setattr(predmet, field.name, "Итого за 1 полугодие:")
                            continue
                        if row == (len(data[table]) - 1) and field.name == "auditor_nagruzka":
                            setattr(predmet, field.name, data[table][row][count])
                            break

                        setattr(predmet, field.name, data[table][row][count])

                        if count == 25:
                            break
                        count += 1
                    predmet.kafedra = profile.kafedra
                    # print(predmet.__dict__)
                    predmet.prepodavatel = profile
                    predmet.year = year
                    predmet.polugodie = '1'
                    predmet.status = True
                    # tru если выполена false если план

                    # print(data)
                    predmet.save1()

            if table == 1:
                for row in range(len(data[table])):
                    count = 0
                    predmet = Predmet()
                    # print(len(data[table]))
                    # print(data[table])
                    # print( data[table][row][0])
                    if data[table][row][0] == "0":
                        continue
                    for field in fields:
                        if field.name == "id":
                            continue
                        if row == (len(data[table]) - 2) and field.name == "name":
                            setattr(predmet, field.name, "Итого за 2 полугодие:")
                            continue
                        if row == (len(data[table]) - 1) and field.name == "name":
                            setattr(predmet, field.name, "Итого за учебный год:")
                            continue

                        if row == (len(data[table]) - 2) and field.name == "auditor_nagruzka":
                            setattr(predmet, field.name, data[table][row][count])
                            break
                        if row == (len(data[table]) - 1) and field.name == "auditor_nagruzka":
                            setattr(predmet, field.name, data[table][row][count])
                            break

                        setattr(predmet, field.name, data[table][row][count])
                        # print(count)
                        if count == 25:
                            break
                        count += 1
                        # print(field.name+str(data[table][row][count]))
                    predmet.kafedra = profile.kafedra
                    # print(predmet.__dict__)
                    predmet.prepodavatel = profile
                    predmet.year = year
                    predmet.polugodie = '2'
                    predmet.status = True  # tru если выполена false если план
                    print(predmet.all_values())
                    predmet.save1()
        return redirect('detail_plan', slug=profile.user.username, year=year)
    else:
        return redirect('log')


# подсчет вcей нагррузки
def mainTableCount(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            profile = get_object_or_404(Profile, user=request.user)
            plan = get_object_or_404(Plan, prepod=profile)
            # заполняем
            umr = UMR.objects.filter(prepodavatel=profile)
            nir = NIR.objects.filter(prepodavatel=profile)
            vr = VR.objects.filter(prepodavatel=profile)
            dr = DR.objects.filter(prepodavatel=profile)
            predmets = Predmet.objects.filter(prepodavatel=profile)
            ucheb_r_1_p = 0
            ucheb_r_2_p = 0
            ucheb_r_god_p = 0
            ucheb_med_r_1_p = 0
            ucheb_med_r_2_p = 0
            ucheb_med_r_god_p = 0
            nir_1_p = 0
            nir_2_p = 0
            nir_god_p = 0
            vr_1_p = 0
            vr_2_p = 0
            vr_god_p = 0
            dr_1_p = 0
            dr_2_p = 0
            dr_god_p = 0
            ucheb_r_1_f = 0
            ucheb_r_2_f = 0
            ucheb_r_god_f = 0
            ucheb_med_r_1_f = 0
            ucheb_med_r_2_f = 0
            ucheb_med_r_god_f = 0
            nir_1_f = 0
            nir_2_f = 0
            nir_god_f = 0
            vr_1_f = 0
            vr_2_f = 0
            vr_god_f = 0
            dr_1_f = 0
            dr_2_f = 0
            dr_god_f = 0
            summ_1_p = 0
            summ_2_p = 0
            summ_god_p = 0
            summ_1_f = 0
            summ_2_f = 0
            summ_god_f = 0

            def __str__(self):
                return self.name

            for p in predmets:
                if p.polugodie == 1 and p.status == False:
                    ucheb_r_1_p += int(p.get_obshaya_nagruzka())
                if p.polugodie == 2 and p.status == False:
                    ucheb_r_2_p += int(p.get_obshaya_nagruzka())
                if p.polugodie == 1 and p.status == True:
                    ucheb_r_1_f += int(p.get_obshaya_nagruzka())
                if p.polugodie == 2 and p.status == True:
                    ucheb_r_2_f += int(p.get_obshaya_nagruzka())

            for u in umr:
                if u.polugodie == 1:
                    ucheb_med_r_1_p += u.plan
                    ucheb_med_r_1_f += u.fact
                if u.polugodie == 2:
                    ucheb_med_r_2_p += u.plan
                    ucheb_med_r_2_f += u.fact
            for n in nir:
                if n.polugodie == 1:
                    nir_1_p += n.plan
                    nir_1_f += n.fact
                if n.polugodie == 2:
                    nir_2_p += n.plan
                    nir_2_f += n.fact
            for v in vr:
                if v.polugodie == 1:
                    vr_1_p += v.plan
                    vr_1_f += v.fact
                if n.polugodie == 2:
                    vr_2_p += v.plan
                    vr_2_f += v.fact
            for d in dr:
                if d.polugodie == 1:
                    dr_1_p += d.plan
                    dr_1_f += d.fact
                if n.polugodie == 2:
                    dr_2_p += d.plan
                    dr_2_f += d.fact

            plan.ucheb_r_1_p = ucheb_r_1_p
            plan.ucheb_r_2_p = ucheb_r_2_p
            plan.ucheb_r_1_f = ucheb_r_1_f
            plan.ucheb_r_2_f = ucheb_r_2_f
            plan.ucheb_r_god_p = ucheb_r_1_p + ucheb_r_2_p
            plan.ucheb_r_god_f = ucheb_r_1_f + ucheb_r_2_f

            plan.ucheb_med_r_1_p = ucheb_med_r_1_p
            plan.ucheb_med_r_2_p = ucheb_med_r_2_p
            plan.ucheb_med_r_1_f = ucheb_med_r_1_f
            plan.ucheb_med_r_2_f = ucheb_med_r_2_f
            plan.ucheb_med_r_god_p = ucheb_med_r_1_p + ucheb_med_r_2_p
            plan.ucheb_med_r_god_f = ucheb_med_r_1_f + ucheb_med_r_2_f

            plan.nir_1_p = nir_1_p
            plan.nir_1_f = nir_1_f
            plan.nir_2_p = nir_2_p
            plan.nir_2_f = nir_2_f
            plan.nir_god_p = nir_1_p + nir_2_p
            plan.nir_god_f = nir_2_f + nir_2_f

            plan.vr_1_p = vr_1_p
            plan.vr_1_f = vr_1_f
            plan.vr_2_p = vr_2_p
            plan.vr_2_f = vr_2_f
            plan.vr_god_p = vr_1_p + vr_2_p
            plan.vr_god_f = vr_2_f + vr_2_f

            plan.dr_1_p = dr_1_p
            plan.dr_1_f = dr_1_f
            plan.dr_2_p = dr_2_p
            plan.dr_2_f = dr_2_f
            plan.dr_god_p = dr_1_p + dr_2_p
            plan.dr_god_f = dr_2_f + dr_2_f

            plan.summ_1_p = (plan.ucheb_r_1_p + plan.ucheb_med_r_1_p + plan.nir_1_p +
                             plan.vr_1_p + plan.dr_1_p)

            plan.summ_2_p = (plan.ucheb_r_2_p + plan.ucheb_med_r_2_p + plan.nir_2_p +
                             plan.vr_2_p + plan.dr_2_p)
            plan.summ_god_p = plan.summ_2_p + plan.summ_1_p
            plan.summ_1_f = (plan.ucheb_r_1_f + plan.ucheb_med_r_1_f + plan.nir_1_f +
                             plan.vr_1_f + plan.dr_1_f)
            plan.summ_2_f = (plan.ucheb_r_2_f + plan.ucheb_med_r_2_f + plan.nir_2_f +
                             plan.vr_2_f + plan.dr_2_f)
            plan.summ_god_f = plan.summ_1_f + plan.summ_2_f
            plan.save()
            return redirect('detail_plan', slug=profile.user.username, year=request.POST['year'])
    else:
        return redirect('log')


def mainTableSave(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            profile = get_object_or_404(Profile, user=request.user)
            if profile.role == 3 or profile.role == 2:
                profile = get_object_or_404(Profile, user__username=request.POST['profile'])
            try:
                plan = get_object_or_404(Plan, prepod=profile, year=request.POST['year'])
            except Exception as e:
                Plan.objects.filter(prepod=profile, year=request.POST['year']).delete()
                plan = Plan()
            form = MainTableForm(request.POST, instance=plan)
            if form.is_valid():

                newplan = form.save(commit=False)
                predmets = Predmet.objects.filter(prepodavatel=profile, status=True, year=request.POST['year'])
                for p in predmets:
                    if p.name == "Итого за 1 полугодие:":
                        newplan.ucheb_r_1_p = p.ucheb_nagruzka
                        print(newplan.ucheb_med_r_1_p)
                    if p.name == "Итого за 2 полугодие:":
                        newplan.ucheb_r_2_p = p.ucheb_nagruzka
                        print(newplan.ucheb_med_r_2_p)
                newplan.year = request.POST['year']
                newplan.name = plan.name
                newplan.prepod = profile
                newplan.save()

                return HttpResponse("Успешно сохранено")
            else:
                return HttpResponse("Ошибка при сохранении таблицы")
    else:
        return redirect('log')


def saveT1(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            # print(request.POST)
            year = request.POST['year']
            profile = get_object_or_404(Profile, user=request.user)
            if profile.role == 3 or profile.role == 2:
                profile = get_object_or_404(Profile, user__username=request.POST['profile'])
            Table1FormSet = modelformset_factory(Predmet, form=Table1Form)
            formset3 = Table1FormSet(request.POST)
            try:
                for form in formset3:
                    if form.is_valid():
                        predmet = form.save(commit=False)
                        predmet.kafedra = profile.kafedra
                        predmet.polugodie = 1
                        predmet.status = False
                        # print(predmet.get_obshaya_nagruzka())
                        predmet.prepodavatel = profile
                        predmet.year = request.POST['year']
                        try:
                            predmetdel = Predmet.objects.get(id=predmet.id)
                            predmetdel.delete()
                        except Exception as e:
                            print(e)

                        predmetdel = Predmet.objects.filter(prepodavatel=profile, name='Итого за 1 полугодие:',
                                                            polugodie=1, status=False,
                                                            year=request.POST['year'])
                        predmetdel.delete()
                        if predmet.name != '' and predmet.name != 'Итого за 1 полугодие:' and predmet.name is not None:
                            predmet.save()
                        else:
                            try:
                                predmetdel = Predmet.objects.get(id=predmet.id)
                                predmetdel.delete()
                            except Exception as e:
                                print(e)

                itog = Predmet()
                predmets = Predmet.objects.filter(prepodavatel=profile, polugodie=1, status=False, year=year)
                fields = Predmet._meta.get_fields()
                setattr(itog, 'status', False)
                setattr(itog, 'polugodie', 1)
                setattr(itog, 'kafedra', profile.kafedra)
                setattr(itog, 'year', request.POST['year'])
                setattr(itog, 'prepodavatel', profile)

                for field in fields:
                    buff = 0
                    if field.name == "id" or field.name == "kafedra" or field.name == "polugodie" or field.name == "status" or field.name == "prepodavatel" or field.name == "year":
                        continue

                    if field.name == "name":
                        setattr(itog, field.name, 'Итого за 1 полугодие:')
                        continue
                    for p in predmets:
                        buff += getattr(p, field.name)
                        # print(getattr(p,field.name))

                    setattr(itog, field.name, buff)
                  
                    # print(str(buff)+field.name)
                itog.save()

            except Exception as e:
                print(e)
                return HttpResponse("Ошибка при сохранении")

        return HttpResponse("Успешно сохранено")
    else:
        return redirect('log')


def saveT2(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            year = request.POST['year']
            profile = get_object_or_404(Profile, user=request.user)
            if profile.role == 3 or profile.role == 2:
                profile = get_object_or_404(Profile, user__username=request.POST['profile'])
            Table1FormSet = modelformset_factory(Predmet, form=Table1Form)
            formset4 = Table1FormSet(request.POST)
            # predmets=formset.save()
            # формсет для первого полугодия
            try:

                for form in formset4:
                    if form.is_valid():
                        predmet = form.save(commit=False)
                        predmet.kafedra = profile.kafedra
                        predmet.polugodie = 2
                        predmet.status = False
                        # print(predmet.get_obshaya_nagruzka())
                        predmet.prepodavatel = profile
                        predmet.year = request.POST['year']
                        try:
                            predmetdel = Predmet.objects.get(id=predmet.id)
                            predmetdel.delete()
                        except Exception as e:
                            print(e)

                        predmetdel = Predmet.objects.filter(prepodavatel=profile, name='Итого за 2 полугодие:',
                                                            polugodie=2, status=False,
                                                            year=request.POST['year'])
                        predmetdel.delete()

                        predmetdel = Predmet.objects.filter(prepodavatel=profile, name='Итого за учебный год:',
                                                            polugodie=2, status=False,
                                                            year=request.POST['year'])
                        predmetdel.delete()
                        if predmet.name != '' and predmet.name != 'Итого за 2 полугодие:' and predmet.name != 'Итого за учебный год:' and predmet.name is not None:
                            predmet.save()
                        else:
                            try:
                                predmetdel = Predmet.objects.get(id=predmet.id)
                                predmetdel.delete()
                            except Exception as e:
                                print(e)

                itog = Predmet()
                predmets = Predmet.objects.filter(prepodavatel=profile, polugodie=2, status=False, year=year)
                fields = Predmet._meta.get_fields()
                setattr(itog, 'status', False)
                setattr(itog, 'polugodie', 2)
                setattr(itog, 'kafedra', profile.kafedra)
                setattr(itog, 'year', request.POST['year'])
                setattr(itog, 'prepodavatel', profile)

                for field in fields:
                    buff = 0
                    if field.name == "id" or field.name == "kafedra" or field.name == "polugodie" or field.name == "status" or field.name == "prepodavatel" or field.name == "year":
                        continue

                    if field.name == "name":
                        setattr(itog, field.name, 'Итого за 2 полугодие:')
                        print('Итого за 2 полугодие:')
                        continue
                    for p in predmets:
                        buff += getattr(p, field.name)
                        # print(getattr(p,field.name))

                    setattr(itog, field.name, buff)
                    print(str(buff) + field.name)
                itog.save()
                """Сохраняем год"""
                itogall = Predmet()
                try:
                    itog1 = Predmet.objects.get(name="Итого за 1 полугодие:", prepodavatel=profile, polugodie=1,
                                                status=False, year=year)
                    setattr(itogall, 'status', False)
                    setattr(itogall, 'polugodie', 2)
                    setattr(itogall, 'kafedra', profile.kafedra)
                    setattr(itogall, 'year', request.POST['year'])
                    setattr(itogall, 'prepodavatel', profile)
                    for field in fields:
                        buff = 0
                        if field.name == "id" or field.name == "kafedra" or field.name == "polugodie" or field.name == "status" or field.name == "prepodavatel" or field.name == "year":
                            continue

                        if field.name == "name":
                            setattr(itogall, field.name, 'Итого за учебный год:')
                            continue
                        setattr(itogall, field.name, (getattr(itog, field.name) + getattr(itog1, field.name)))

                    itogall.save()

                except:
                    setattr(itogall, 'status', False)
                    setattr(itogall, 'polugodie', 2)
                    setattr(itogall, 'kafedra', profile.kafedra)
                    setattr(itogall, 'year', request.POST['year'])
                    setattr(itogall, 'prepodavatel', profile)
                    for field in fields:
                        buff = 0
                        if field.name == "id" or field.name == "kafedra" or field.name == "polugodie" or field.name == "status" or field.name == "prepodavatel" or field.name == "year":
                            continue

                        if field.name == "name":
                            setattr(itogall, field.name, 'Итого за учебный год:')
                            continue
                        setattr(itogall, field.name, (getattr(itog, field.name)))

                    itogall.save()

            except Exception as e:
                print(e)
                return HttpResponse("Ошибка при сохранении")




            except Exception as e:
                return HttpResponse("Ошибка при сохранении")

        return HttpResponse("Успешно сохранено")
    else:
        return redirect('log')


def saveT3(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            # print(request.POST)
            year = request.POST['year']
            profile = get_object_or_404(Profile, user=request.user)
            if profile.role == 3 or profile.role == 2:
                profile = get_object_or_404(Profile, user__username=request.POST['profile'])
            Table1FormSet = modelformset_factory(Predmet, form=Table1Form, extra=5)
            formset3 = Table1FormSet(request.POST)
            # predmets=formset.save()
            # формсет для первого полугодия
            try:

                for form in formset3:
                    if form.is_valid():
                        predmet = form.save(commit=False)
                        predmet.kafedra = profile.kafedra
                        predmet.polugodie = 1
                        predmet.status = True
                        # print(predmet.get_obshaya_nagruzka())
                        predmet.prepodavatel = profile
                        predmet.year = request.POST['year']
                        try:
                            predmetdel = Predmet.objects.get(id=predmet.id)
                            predmetdel.delete()
                        except Exception as e:
                            print(e)

                        predmetdel = Predmet.objects.filter(prepodavatel=profile, name='Итого за 1 полугодие:',
                                                            polugodie=1, status=True,
                                                            year=request.POST['year'])
                        predmetdel.delete()
                        if predmet.name != '' and predmet.name != 'Итого за 1 полугодие:' and predmet.name is not None:
                            predmet.save()
                        else:
                            try:
                                predmetdel = Predmet.objects.get(id=predmet.id)
                                predmetdel.delete()
                            except Exception as e:
                                print(e)

                itog = Predmet()
                try:
                    itogmes = Mesyac.objects.get(name="Итого за 1 полугодие:", prepodavatel=profile, polugodie=1,
                                                 status=False, year=year)
                except Exception as e:
                    itogmesdel = Mesyac.objects.filter(name="Итого за 1 полугодие:", prepodavatel=profile, polugodie=1,
                                                       status=False, year=year)
                    itogmesdel.delete()
                    print("not itog 1")
                    itogmes = Mesyac()
                    setattr(itogmes, 'name', "Итого за 1 полугодие:")
                    setattr(itogmes, 'status', False)
                    setattr(itogmes, 'polugodie', 1)
                    setattr(itogmes, 'kafedra', profile.kafedra)
                    setattr(itogmes, 'year', request.POST['year'])
                    setattr(itogmes, 'prepodavatel', profile)
                predmets = Predmet.objects.filter(prepodavatel=profile, polugodie=1, status=True, year=year)
                fields = Predmet._meta.get_fields()
                setattr(itog, 'status', True)
                setattr(itog, 'polugodie', 1)
                setattr(itog, 'kafedra', profile.kafedra)
                setattr(itog, 'year', request.POST['year'])
                setattr(itog, 'prepodavatel', profile)

                for field in fields:
                    buff = 0
                    if field.name == "id" or field.name == "kafedra" or field.name == "polugodie" or field.name == "status" or field.name == "prepodavatel" or field.name == "year":
                        continue

                    if field.name == "name":
                        setattr(itog, field.name, 'Итого за 1 полугодие:')
                        continue
                    for p in predmets:
                        buff += getattr(p, field.name)
                        # print(getattr(p,field.name))

                    setattr(itog, field.name, buff)
                    setattr(itogmes, field.name, buff)
                    # print(str(buff)+field.name)
                itog.save()
                itogmes.save()
            except Exception as e:
                print(e)
                return HttpResponse("Ошибка при сохранении")

        return HttpResponse("Успешно сохранено")
    else:
        return redirect('log')


def saveT4(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            year = request.POST['year']
            profile = get_object_or_404(Profile, user=request.user)
            if profile.role == 3 or profile.role == 2:
                profile = get_object_or_404(Profile, user__username=request.POST['profile'])
            Table1FormSet = modelformset_factory(Predmet, form=Table1Form, extra=5)
            formset4 = Table1FormSet(request.POST)
            # predmets=formset.save()
            # формсет для первого полугодия
            try:

                for form in formset4:
                    if form.is_valid():
                        predmet = form.save(commit=False)
                        predmet.kafedra = profile.kafedra
                        predmet.polugodie = 2
                        predmet.status = True
                        # print(predmet.get_obshaya_nagruzka())
                        predmet.prepodavatel = profile
                        predmet.year = request.POST['year']
                        try:
                            predmetdel = Predmet.objects.get(id=predmet.id)
                            predmetdel.delete()
                        except Exception as e:
                            print(e)

                        predmetdel = Predmet.objects.filter(prepodavatel=profile, name='Итого за 2 полугодие:',
                                                            polugodie=2, status=True,
                                                            year=request.POST['year'])
                        predmetdel.delete()

                        predmetdel = Predmet.objects.filter(prepodavatel=profile, name='Итого за учебный год:',
                                                            polugodie=2, status=True,
                                                            year=request.POST['year'])
                        predmetdel.delete()
                        if predmet.name != '' and predmet.name != 'Итого за 2 полугодие:' and predmet.name != 'Итого за учебный год:' and predmet.name is not None:
                            predmet.save()
                        else:
                            try:
                                predmetdel = Predmet.objects.get(id=predmet.id)
                                predmetdel.delete()
                            except Exception as e:
                                print(e)

                itog = Predmet()
                try:
                    itogmes = Mesyac.objects.get(name="Итого за 2 полугодие:", prepodavatel=profile,
                                                 year=year)
                except Exception as e:
                    itogmes_del = Mesyac.objects.filter(name="Итого за 2 полугодие:", prepodavatel=profile,
                                                        year=year)
                    itogmes_del.delete()
                    print("not itog 2")
                    itogmes = Mesyac()
                    setattr(itogmes, 'name', "Итого за 2 полугодие:")
                    setattr(itogmes, 'status', False)
                    setattr(itogmes, 'polugodie', 2)
                    setattr(itogmes, 'kafedra', profile.kafedra)
                    setattr(itogmes, 'year', request.POST['year'])
                    setattr(itogmes, 'prepodavatel', profile)
                predmets = Predmet.objects.filter(prepodavatel=profile, polugodie=2, status=True, year=year)
                fields = Predmet._meta.get_fields()
                setattr(itog, 'status', True)
                setattr(itog, 'polugodie', 2)
                setattr(itog, 'kafedra', profile.kafedra)
                setattr(itog, 'year', request.POST['year'])
                setattr(itog, 'prepodavatel', profile)

                for field in fields:
                    buff = 0
                    if field.name == "id" or field.name == "kafedra" or field.name == "polugodie" or field.name == "status" or field.name == "prepodavatel" or field.name == "year":
                        continue

                    if field.name == "name":
                        setattr(itog, field.name, 'Итого за 2 полугодие:')
                        print('Итого за 2 полугодие:')
                        continue
                    for p in predmets:
                        buff += getattr(p, field.name)
                        # print(getattr(p,field.name))

                    setattr(itog, field.name, buff)
                    setattr(itogmes, field.name, buff)
                    print(str(buff) + field.name)
                itog.save()
                itogmes.save()
                """Сохраняем год"""
                itogall = Predmet()
                try:
                    itogmesall = Mesyac.objects.get(name="Итого за учебный год:", prepodavatel=profile,
                                                    year=year)
                except Exception as e:
                    itogmes_del = Mesyac.objects.filter(name="Итого за учебный год:", prepodavatel=profile,
                                                        year=year)
                    itogmes_del.delete()
                    print("not itog")
                    itogmesall = Mesyac()
                    setattr(itogmesall, 'name', "Итого за учебный год:")
                    setattr(itogmesall, 'status', False)
                    setattr(itogmesall, 'polugodie', 2)
                    setattr(itogmesall, 'kafedra', profile.kafedra)
                    setattr(itogmesall, 'year', request.POST['year'])
                    setattr(itogmesall, 'prepodavatel', profile)
                try:
                    itog1 = Predmet.objects.get(name="Итого за 1 полугодие:", prepodavatel=profile, polugodie=1,
                                                status=True, year=year)
                    setattr(itogall, 'status', True)
                    setattr(itogall, 'polugodie', 2)
                    setattr(itogall, 'kafedra', profile.kafedra)
                    setattr(itogall, 'year', request.POST['year'])
                    setattr(itogall, 'prepodavatel', profile)
                    for field in fields:
                        buff = 0
                        if field.name == "id" or field.name == "kafedra" or field.name == "polugodie" or field.name == "status" or field.name == "prepodavatel" or field.name == "year":
                            continue

                        if field.name == "name":
                            setattr(itogall, field.name, 'Итого за учебный год:')
                            continue
                        setattr(itogall, field.name, (getattr(itog, field.name) + getattr(itog1, field.name)))
                        setattr(itogmesall, field.name, (getattr(itog, field.name) + getattr(itog1, field.name)))
                    itogall.save()
                    itogmesall.save()
                except:
                    setattr(itogall, 'status', True)
                    setattr(itogall, 'polugodie', 2)
                    setattr(itogall, 'kafedra', profile.kafedra)
                    setattr(itogall, 'year', request.POST['year'])
                    setattr(itogall, 'prepodavatel', profile)
                    for field in fields:
                        buff = 0
                        if field.name == "id" or field.name == "kafedra" or field.name == "polugodie" or field.name == "status" or field.name == "prepodavatel" or field.name == "year":
                            continue

                        if field.name == "name":
                            setattr(itogall, field.name, 'Итого за учебный год:')
                            continue
                        setattr(itogall, field.name, (getattr(itog, field.name)))
                        setattr(itogmesall, field.name, (getattr(itog, field.name)))
                    itogall.save()
                    itogmesall.save()
            except Exception as e:
                print(e)
                return HttpResponse("Ошибка при сохранении")




            except Exception as e:
                return HttpResponse("Ошибка при сохранении")

        return HttpResponse("Успешно сохранено")
    else:
        return redirect('log')


def saveT5(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user=request.user)
        if request.method == "POST":
            print(request.POST)
            year = request.POST['year']
            profile = get_object_or_404(Profile, user=request.user)
            if profile.role == 3 or profile.role == 2:
                profile = get_object_or_404(Profile, user__username=request.POST['profile'])
            Table1FormSet = modelformset_factory(UMR, form=Table2Form, extra=5)
            formset4 = Table1FormSet(request.POST,
                                     queryset=UMR.objects.filter(prepodavatel=profile, polugodie=1, year=year))
            # predmets=formset.save()
            # формсет для первого полугодия
            try:
                for form in formset4:
                    if form.is_valid():
                        umr = form.save(commit=False)
                        umr.polugodie = 1
                        umr.prepodavatel = profile
                        umr.year = request.POST['year']
                        if umr.vid != '' and umr.vid is not None:

                            try:
                                umrdel = UMR.objects.filter(vid=umr.vid, year=umr.year, polugodie=umr.polugodie,
                                                            prepodavatel=umr.prepodavatel)

                                umrdel.delete()
                            except Exception as e:
                                print(e)
                            umr.save()
                        else:
                            try:
                                umrdel = UMR.objects.filter(id=umr.id)
                                umrdel.delete()
                            except Exception as e:
                                print(e)
                    else:
                        print(form.errors)
            except Exception as e:
                print(e)

            return HttpResponse("Успешно сохранено")
    else:
        return redirect('log')


def saveT6(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user=request.user)
        if request.method == "POST":
            profile = get_object_or_404(Profile, user=request.user)
            if profile.role == 3 or profile.role == 2:
                profile = get_object_or_404(Profile, user__username=request.POST['profile'])
            Table1FormSet = modelformset_factory(UMR, form=Table2Form, extra=5)
            formset4 = Table1FormSet(request.POST)
            # predmets=formset.save()
            # формсет для первого полугодия

            try:
                for form in formset4:
                    if form.is_valid():
                        umr = form.save(commit=False)
                        umr.polugodie = 2
                        umr.prepodavatel = profile
                        umr.year = request.POST['year']
                        if umr.vid != '' and umr.vid is not None:

                            try:
                                umrdel = UMR.objects.filter(vid=umr.vid, year=umr.year, polugodie=umr.polugodie,
                                                            prepodavatel=umr.prepodavatel)
                                umrdel.delete()
                            except Exception as e:
                                print(e)
                            umr.save()
                        else:
                            try:
                                umrdel = UMR.objects.filter(id=umr.id)
                                umrdel.delete()
                            except Exception as e:
                                print(e)
            except Exception as e:
                print(e)
                return HttpResponse("Ошибка при сохранении")
        return HttpResponse("Успешно сохранено")
    else:
        return redirect('log')


# tabler foe NIR
def saveT7(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user=request.user)
        if request.method == "POST":
            profile = get_object_or_404(Profile, user=request.user)
            if profile.role == 3 or profile.role == 2:
                profile = get_object_or_404(Profile, user__username=request.POST['profile'])
            Table1FormSet = modelformset_factory(NIR, form=Table3Form, extra=5)
            formset4 = Table1FormSet(request.POST)
            # predmets=formset.save()
            # формсет для первого полугодия

            try:
                for form in formset4:
                    if form.is_valid():
                        umr = form.save(commit=False)
                        umr.polugodie = 1
                        umr.prepodavatel = profile
                        umr.year = request.POST['year']
                        if umr.vid != '' and umr.vid is not None:

                            try:
                                umrdel = NIR.objects.filter(vid=umr.vid, year=umr.year, polugodie=umr.polugodie,
                                                            prepodavatel=umr.prepodavatel)
                                umrdel.delete()
                            except Exception as e:
                                print(e)
                            umr.save()
                        else:
                            try:
                                umrdel = NIR.objects.filter(id=umr.id)
                                umrdel.delete()
                            except Exception as e:
                                print(e)
            except Exception as e:
                print(e)
                return HttpResponse("Ошибка при сохранении")
        return HttpResponse("Успешно сохранено")
    else:
        return redirect('log')


def saveT8(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user=request.user)
        if request.method == "POST":
            profile = get_object_or_404(Profile, user=request.user)
            if profile.role == 3 or profile.role == 2:
                profile = get_object_or_404(Profile, user__username=request.POST['profile'])
            Table1FormSet = modelformset_factory(NIR, form=Table3Form, extra=5)
            formset4 = Table1FormSet(request.POST)
            # predmets=formset.save()
            # формсет для первого полугодия

            try:
                for form in formset4:
                    if form.is_valid():
                        umr = form.save(commit=False)
                        umr.polugodie = 2
                        umr.prepodavatel = profile
                        umr.year = request.POST['year']
                        if umr.vid != '' and umr.vid is not None:

                            try:
                                umrdel = NIR.objects.filter(vid=umr.vid, year=umr.year, polugodie=umr.polugodie,
                                                            prepodavatel=umr.prepodavatel)
                                umrdel.delete()
                            except Exception as e:
                                print(e)
                            umr.save()
                        else:
                            try:
                                umrdel = NIR.objects.filter(id=umr.id)
                                umrdel.delete()
                            except Exception as e:
                                print(e)
            except Exception as e:
                print(e)
                return HttpResponse("Ошибка при сохранении")
        return HttpResponse("Успешно сохранено")
    else:
        return redirect('log')


def saveT9(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user=request.user)
        if request.method == "POST":
            profile = get_object_or_404(Profile, user=request.user)
            if profile.role == 3 or profile.role == 2:
                profile = get_object_or_404(Profile, user__username=request.POST['profile'])
            Table1FormSet = modelformset_factory(VR, form=Table4Form, extra=5)
            formset4 = Table1FormSet(request.POST, queryset=VR.objects.filter(prepodavatel=profile, polugodie=1))
            # predmets=formset.save()
            # формсет для первого полугодия

            try:
                for form in formset4:
                    if form.is_valid():
                        umr = form.save(commit=False)
                        umr.polugodie = 1
                        umr.prepodavatel = profile
                        umr.year = request.POST['year']
                        if umr.vid != '' and umr.vid is not None:

                            try:
                                umrdel = VR.objects.filter(vid=umr.vid, year=umr.year, polugodie=umr.polugodie,
                                                           prepodavatel=umr.prepodavatel)
                                umrdel.delete()
                            except Exception as e:
                                print(e)
                            umr.save()
                        else:
                            try:
                                umrdel = VR.objects.filter(id=umr.id)
                                umrdel.delete()
                            except Exception as e:
                                print(e)
            except Exception as e:
                print(e)
                return HttpResponse("Ошибка при сохранении")
        return HttpResponse("Успешно сохранено")
    else:
        return redirect('log')


def saveT10(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user=request.user)
        if request.method == "POST":
            profile = get_object_or_404(Profile, user=request.user)
            if profile.role == 3 or profile.role == 2:
                profile = get_object_or_404(Profile, user__username=request.POST['profile'])
            Table1FormSet = modelformset_factory(VR, form=Table4Form, extra=5)
            formset4 = Table1FormSet(request.POST, queryset=VR.objects.filter(prepodavatel=profile, polugodie=2))
            # predmets=formset.save()
            # формсет для первого полугодия

            try:
                for form in formset4:
                    if form.is_valid():
                        umr = form.save(commit=False)
                        umr.polugodie = 2
                        umr.prepodavatel = profile
                        umr.year = request.POST['year']
                        if umr.vid != '' and umr.vid is not None:

                            try:
                                umrdel = VR.objects.filter(vid=umr.vid, year=umr.year, polugodie=umr.polugodie,
                                                           prepodavatel=umr.prepodavatel)
                                umrdel.delete()
                            except Exception as e:
                                print(e)
                            umr.save()
                        else:
                            try:
                                umrdel = VR.objects.filter(id=umr.id)
                                umrdel.delete()
                            except Exception as e:
                                print(e)
            except Exception as e:
                print(e)
                return HttpResponse("Ошибка при сохранении")
        return HttpResponse("Успешно сохранено")
    else:
        return redirect('log')


def saveT11(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user=request.user)
        if request.method == "POST":
            profile = get_object_or_404(Profile, user=request.user)
            if profile.role == 3 or profile.role == 2:
                profile = get_object_or_404(Profile, user__username=request.POST['profile'])
            Table1FormSet = modelformset_factory(DR, form=Table5Form, extra=5)
            formset4 = Table1FormSet(request.POST, queryset=DR.objects.filter(prepodavatel=profile, polugodie=1))
            # predmets=formset.save()
            # формсет для первого полугодия
            try:
                for form in formset4:
                    if form.is_valid():
                        umr = form.save(commit=False)
                        umr.polugodie = 1
                        umr.prepodavatel = profile
                        umr.year = request.POST['year']
                        if umr.vid != '' and umr.vid is not None:

                            try:
                                umrdel = DR.objects.filter(vid=umr.vid, year=umr.year, polugodie=umr.polugodie,
                                                           prepodavatel=umr.prepodavatel)
                                umrdel.delete()
                            except Exception as e:
                                print(e)
                            umr.save()
                        else:
                            try:
                                umrdel = DR.objects.filter(id=umr.id)
                                umrdel.delete()
                            except Exception as e:
                                print(e)
            except Exception as e:
                print(e)
                return HttpResponse("Ошибка при сохранении")
        return HttpResponse("Успешно сохранено")
    else:
        return redirect('log')


def saveT12(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user=request.user)
        if request.method == "POST":
            profile = get_object_or_404(Profile, user=request.user)
            if profile.role == 3 or profile.role == 2:
                profile = get_object_or_404(Profile, user__username=request.POST['profile'])
            Table1FormSet = modelformset_factory(DR, form=Table5Form, extra=5)
            formset4 = Table1FormSet(request.POST, queryset=DR.objects.filter(prepodavatel=profile, polugodie=2))
            # predmets=formset.save()
            # формсет для первого полугодия
            try:
                for form in formset4:
                    if form.is_valid():
                        umr = form.save(commit=False)
                        umr.polugodie = 2
                        umr.prepodavatel = profile
                        umr.year = request.POST['year']
                        if umr.vid != '' and umr.vid is not None:

                            try:
                                umrdel = DR.objects.filter(vid=umr.vid, year=umr.year, polugodie=umr.polugodie,
                                                           prepodavatel=umr.prepodavatel)
                                umrdel.delete()
                            except Exception as e:
                                print(e)
                            umr.save()
                        else:
                            try:
                                umrdel = DR.objects.filter(id=umr.id)
                                umrdel.delete()
                            except Exception as e:
                                print(e)
            except Exception as e:
                print(e)
                return HttpResponse("Ошибка при сохранении")
        return HttpResponse("Успешно сохранено")
    else:
        return redirect('log')
        # иностранные слушателями


def saveT13(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user=request.user)
        if request.method == "POST":
            profile = get_object_or_404(Profile, user=request.user)
            if profile.role == 3 or profile.role == 2:
                profile = get_object_or_404(Profile, user__username=request.POST['profile'])
            Table1FormSet = modelformset_factory(INR, form=Table6Form, extra=5)
            formset4 = Table1FormSet(request.POST, queryset=INR.objects.filter(prepodavatel=profile, polugodie=1))
            # predmets=formset.save()
            # формсет для первого полугодия
            try:
                for form in formset4:
                    if form.is_valid():
                        umr = form.save(commit=False)
                        umr.polugodie = 1
                        umr.prepodavatel = profile
                        umr.year = request.POST['year']
                        if umr.vid != '' and umr.vid is not None:

                            try:
                                umrdel = INR.objects.filter(vid=umr.vid, year=umr.year, polugodie=umr.polugodie,
                                                            prepodavatel=umr.prepodavatel)
                                umrdel.delete()
                            except Exception as e:
                                print(e)
                            umr.save()
                        else:
                            try:
                                umrdel = INR.objects.filter(id=umr.id)
                                umrdel.delete()
                            except Exception as e:
                                print(e)
                        for vid in INR.objects.values_list('vid', flat=True).distinct():
                            INR.objects.filter(
                                pk__in=INR.objects.filter(vid=vid, prepodavatel=profile, year=request.POST['year']).values_list('id',flat=True)[1:]).delete()
            except Exception as e:
                print(e)
                return HttpResponse("Ошибка при сохранении")
        return HttpResponse("Успешно сохранено")
    else:
        return redirect('log')


def saveT14(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user=request.user)
        if request.method == "POST":
            profile = get_object_or_404(Profile, user=request.user)
            if profile.role == 3 or profile.role == 2:
                profile = get_object_or_404(Profile, user__username=request.POST['profile'])
            Table1FormSet = modelformset_factory(INR, form=Table6Form, extra=5)
            formset4 = Table1FormSet(request.POST, queryset=INR.objects.filter(prepodavatel=profile, polugodie=2))
            # predmets=formset.save()
            # формсет для первого полугодия

            try:
                for form in formset4:
                    if form.is_valid():
                        umr = form.save(commit=False)
                        umr.polugodie = 2
                        umr.prepodavatel = profile
                        umr.year = request.POST['year']
                        if umr.vid != '' and umr.vid is not None:

                            try:
                                umrdel = INR.objects.filter(vid=umr.vid, year=umr.year, polugodie=umr.polugodie,
                                                            prepodavatel=umr.prepodavatel)
                                umrdel.delete()
                            except Exception as e:
                                print(e)
                            umr.save()
                        else:
                            try:
                                umrdel = INR.objects.filter(id=umr.id)
                                umrdel.delete()
                            except Exception as e:
                                print(e)
                        for vid in INR.objects.values_list('vid', flat=True).distinct():
                            INR.objects.filter(
                                pk__in=INR.objects.filter(vid=vid,prepodavatel=profile,year=request.POST['year']).values_list('id', flat=True)[1:]).delete()
            except Exception as e:
                print(e)
                return HttpResponse("Ошибка при сохранении")
        return HttpResponse("Успешно сохранено")
    else:
        return redirect('log')


def deltable(request):
    if request.user.is_authenticated and request.method == 'POST':
        print(request.POST)
    return JsonResponse("1", safe=False)


def shapka(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            profile = get_object_or_404(Profile, user=request.user)
            if profile.role == 3 or profile.role == 2:
                profile = get_object_or_404(Profile, user__username=request.POST['profile'])
            plan = get_object_or_404(Plan, prepod=profile, year=request.POST['year'])
            form = ShapkaForm(request.POST)
            if form.is_valid():
                try:
                    try:
                        shpkdel = get_object_or_404(DocInfo, plan=plan)
                        shpkdel.delete()
                    except:
                        print("ne bilo shapki")

                    shpk = form.save(commit=False)
                    shpk.plan = plan
                    try:
                        profileinfo = ProfileInfo.objects.get(profile=profile)
                        shpk.fio = profileinfo.fio
                        shpk.dolznost = profileinfo.dolznost
                        shpk.stavka = profileinfo.stavka
                        shpk.uchzv = profileinfo.uchzv
                        shpk.uchst = profileinfo.uchst
                        shpk.visluga = profileinfo.visluga
                        shpk.kafedra = profileinfo.kafedra


                    except:
                        return HttpResponse("Ошибка при сохранении, сначала заполните информацию на главной странице")

                    shpk.save()
                    kolvomes = request.POST['kolvomes']
                    try:
                        rating = Rating.objects.get(year=request.POST['year'], profile=profile)
                        rating.kolvomes = kolvomes
                        rating.save()
                    except:
                        rating = Rating()
                        rating.profile = profile
                        rating.kolvomes = kolvomes
                        rating.year = request.POST['year']
                        rating.save()
                except Exception as e:
                    print(e)
                    return HttpResponse("Ошибка при сохранении")

            else:

                return HttpResponse("Ошибка при сохранении")
        return HttpResponse("Успешно сохранено")
    else:
        return redirect('log')


def saveMesyac(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            profile = get_object_or_404(Profile, user=request.user)
            if profile.role == 3 or profile.role == 2:
                profile = get_object_or_404(Profile, user__username=request.POST['profile'])
            plan = get_object_or_404(Plan, prepod=profile, year=request.POST['year'])
            MesyacFormSet = modelformset_factory(Mesyac, form=MesyacForm)
            formset4 = MesyacFormSet(request.POST,
                                     queryset=Mesyac.objects.filter(prepodavatel=profile, year=request.POST['year']))
            if formset4.is_valid():
                try:
                    try:
                        mesyacdel = Mesyac.objects.filter(prepodavatel=profile, year=request.POST['year'])
                        for m in mesyacdel:
                            m.delete()

                    except Exception as e:
                        print(e)
                        print("ne")

                    for form in formset4:
                        umr = form.save(commit=False)
                        umr.prepodavatel = profile
                        umr.kafedra = profile.kafedra
                        umr.year = request.POST['year']
                        umr.save()
                except Exception as e:
                    print(e)
                    return HttpResponse("Ошибка при сохранении")


            else:
                print(formset4.errors)
                return HttpResponse("Ошибка при сохранении")
        return HttpResponse("Успешно сохранено")
    else:
        return redirect('log')

def zamechSave(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            profile = get_object_or_404(Profile, user=request.user)
            if profile.role == 3 or profile.role == 2:
                profile = get_object_or_404(Profile, user__username=request.POST['profile'])
            ZamechFormSet = modelformset_factory(Zamech, form=ZamechForm)
            formset4 = ZamechFormSet(request.POST,
                                     queryset=Zamech.objects.filter(profile=profile, year=request.POST['year']))
            if request.user.profile.role == 3:                         
                if formset4.is_valid():
                    print("umr")
                    try:
                        for form in formset4:
                            umr = form.save(commit=False)
                            umr.year = request.POST['year']
                            umr.profile = profile
                            try:
                                Zamech.objects.filter(name=umr.name,year=umr.year,profile=umr.profile).delete()
                            except Exception as e:
                                print(e)
                            if umr.status == True:
                                umr.date_2 = dt.date.today()
                            if umr.name == "" or umr.name == None:
                                try:
                                    Zamech.objects.filter(id=umr.id).delete()
                                    Zamech.objects.filter(name=umr.name,year=umr.year,profile=umr.profile).delete()
                                except Exception as e:
                                    print(e)
                                    continue
                                continue
                            print(umr.name)
                            umr.save()
                    except Exception as e:
                        print(e)
                        return HttpResponse("Ошибка при сохранении")
                else:
                    print(formset4.errors)
                    return HttpResponse("Ошибка при сохранении")
            else:
                if formset4.is_valid():
                    print("prepod")
                    print(request.POST)
                    try:
                        for form in formset4:
                            umr = form.save(commit=False)
                            umr.profile = profile
                            if umr.status == True:
                                umr.date_2 = dt.date.today()
                            umr.year = request.POST['year']
                            print(umr.name)
                            umr.save()
                    except Exception as e:
                        print(e)
                        return HttpResponse("Ошибка при сохранении")
                else:
                    print(formset4.errors)
                    return HttpResponse("Ошибка при сохранении")


            
        return HttpResponse("Успешно сохранено")
    else:
        return redirect('log')


@api_view(['GET'])
def update_plan_summ(request, year, slug):
    try:
        profile = Profile.objects.get(user__username=slug)
        predmets = Predmet.objects.filter(prepodavatel=profile, status=True, year=year)

        newplan = Plan.objects.get(prepod=profile, year=year)
        ucheb_r_1_p = 0
        ucheb_r_2_p = 0
        for p in predmets:
            print(p.name)
            if p.name == "Итого за 1 полугодие:":
                ucheb_r_1_p = p.ucheb_nagruzka
            if p.name == "Итого за 2 полугодие:":
                ucheb_r_2_p = p.ucheb_nagruzka
        newplan.save()
        return Response(
            [
                {
                    "first": ucheb_r_1_p,
                    "second": ucheb_r_2_p
                }
            ])
    except Exception as e:
        print(e)
        return HttpResponse("Ошибка при обновлении данных таблицы")
