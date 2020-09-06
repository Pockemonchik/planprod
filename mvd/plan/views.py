#
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from rating.models import URR, ORMR, PCR, MRR, Rating
from rating.views import setplace
from plan.models import Article, Mesyac, Profile, Kafedra, Plan, Predmet, NIR, VR, DR, UMR, INR, Nagruzka, DocInfo, ProfileInfo
from plan.forms import MesyacForm,ChangePassForm, UserAddForm, docUploadForm, ShapkaForm, Table1Form, Table2Form, Table3Form,Table4Form, Table6Form, Table5Form, MAinTableForm, Table1UploadForm, NagruzkaForm, ProfileInfoForm
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
from plan.Parser_and_overview import createDoc2, createDoc, takeTable, takeXls, writeInfoDoc, xlsPrepod
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
from io import StringIO, BytesIO
from rest_framework.decorators import api_view

"""Рендер основных страниц"""

def detail_plan(request, slug, year):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user=request.user)
        profile1 = get_object_or_404(Profile, user__username=slug)
        Table0FormSet = modelformset_factory(Predmet, form=Table1Form, extra=0)
        Table1FormSet = modelformset_factory(Predmet, form=Table1Form, extra=5)
        Table2FormSet = modelformset_factory(UMR, form=Table2Form, extra=5)
        Table3FormSet = modelformset_factory(NIR, form=Table3Form, extra=5)
        Table4FormSet = modelformset_factory(VR, form=Table4Form, extra=5)
        Table5FormSet = modelformset_factory(DR, form=Table5Form, extra=5)
        Table6FormSet = modelformset_factory(INR, form=Table6Form, extra=5)
        MesyacFormSet = modelformset_factory(Mesyac, form=MesyacForm)
        plan = get_object_or_404(Plan, prepod=profile1, year=year)
        try:
            querymes = Mesyac.objects.filter(prepodavatel=profile1, year=year, polugodie=1, status=False)

            if not querymes:
                mesyacprofile = get_object_or_404(Profile, user__username='admin')
                mesyac = MesyacFormSet(
                    queryset=Mesyac.objects.filter(prepodavatel=mesyacprofile, year=2019, polugodie=1, status=False))
            else:
                mesyac = MesyacFormSet(
                    queryset=Mesyac.objects.filter(prepodavatel=profile1, year=year, polugodie=1, status=False))
        except:
            mesyac = MesyacFormSet()
        mainForm = MAinTableForm(instance=plan)
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
        kafedri = Kafedra.objects.all()
        if profile.role == 2:
            kafedri = Kafedra.objects.filter(name=profile.kafedra.name)
        try:
            docinf = DocInfo.objects.get(plan=plan)
            shapka = ShapkaForm(instance=docinf)
        except DocInfo.DoesNotExist:
            shapka = ShapkaForm()

        title = "Индивидуальный план  " + ''.join(
            [profile1.fullname.split(' ')[0], ' ', profile1.fullname.split(' ')[1][0], '.',
             profile1.fullname.split(' ')[1][0]])
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
            'title': title

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

        title = "Главная " + ''.join([profile.fullname.split(' ')[0], ' ', profile.fullname.split(' ')[1][0], '.',
                                      profile.fullname.split(' ')[1][0]])

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
                                        profile.fullname.split(' ')[1][0]])
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
                Rating.objects.get(profile=profile, year=year)
                return Response([{

                    "text": "Такой рейтинг уже существует",

                }])
            except:
                try:
                    newrating = Rating()
                    print(newrating)
                    newrating.profile = profile
                    newrating.year = year
                    itog = Predmet.objects.get(prepodavatel=profile, year=year, name="Итого за учебный год:")
                    try:
                        newurr = URR.objects.get(profile=profile, year=year)
                    except:
                        newurr = URR()
                    newurr.profile = profile
                    newurr.year = year
                    newurr.obsh = itog.get_obshaya_nagruzka()
                    newurr.obshbal = itog.get_obshaya_nagruzka()
                    sootn = int(itog.get_auditor_nagruzka() / itog.get_obshaya_nagruzka() * 100)
                    newurr.sootn = sootn
                    if sootn > 70:
                        newurr.sootnbal = sootn - 70
                    else:
                        newurr.sootnbal = 0
                    print(newurr.sootn)

                    print(newurr.sootnbal)
                    newurr.save()
                    umrs = UMR.objects.filter(prepodavatel=profile, year=year, include_rating=True)
                    summmrr = 0
                    for u in umrs:
                        if ("азработка основной профессиональной образовательной" in u.vid or
                                "азработка примерной основной профессиональной образовательной" in u.vid or
                                "оздание структуры и содержания электронного учебного курса" in u.vid or
                                "нтеграция тестовых заданий в программную оболочку" in u.vid):
                            newmrr = MRR()
                            newmrr.profile = profile
                            newmrr.name = u.vid
                            print(newmrr.name)
                            newmrr.bal = 20
                            newmrr.year = year
                            summmrr += 20
                            newmrr.save()
                        if ("азработка примерной рабочей программы учебной дисциплины" in u.vid or
                                "азработка примерной дополнительной профессиональной программы (программы повышения квалификации, программы профессиональной переподготовки)" in u.vid or
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
                                "азработка cборника образцов процессуальных и служебных документов, макета дела, комплекта ситуационных задач по дисциплине" in u.vid):
                            newmrr = MRR()
                            newmrr.profile = profile
                            newmrr.name = u.vid
                            print(newmrr.name)
                            newmrr.bal = 5
                            newmrr.year = year
                            summmrr += 5
                            newmrr.save()

                        newrating.summ = newurr.getsumm() + summmrr
                        newrating.save()
                        print("zaebis")
                except Exception as e:
                    print(e)
                    return Response([{

                        "text": "Ошибка при созданиии рейтинга, сначала аполните ИП на этот год",

                    }])

    return Response([{

        "text": "Рейтинг успешно сформирован",
        "href": "rating/rate_otsenka/" + profile.user.username + "/" + year + "/",

    }])


""" Работа с пользователями в главной таблице"""

@api_view(['POST'])
def deluser(request):
    if request.method == "POST":

        previos_username = request.data.get("login")
        previos_user = User.objects.get(username=previos_username)
        profile = Profile.objects.get(user=previos_user)

        try:
            profile.kafedra = NULL
            profile.save()
        except:
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
            fio = form.cleaned_data['fio']
            previos_user = User.objects.get(username=previos_username)
            if previos_username == username:
                try:
                    profile = Profile.objects.get(user=previos_user)
                    profile.user = usernew
                    profile.fullname = fio
                    profile.save()
                except Exception as e:
                    print(e)
                    return HttpResponse("Произошла ошибка при изменении данных пользователя")
            try:
                usernew = User.objects.create_user(username, password, password)
                usernew.save()
                profile = Profile.objects.get(user=previos_user)
                profile.user = usernew
                profile.fullname = fio
                profile.save()
            except Exception as e:
                print(e)
                return HttpResponse("Произошла ошибка при изменении данных пользователя")

        else:
            print('blen')
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
            except Exeption as e:
                print(e)
                return HttpResponse("Произошла ошибка при добавлении пользователя")
        else:
            return HttpResponse("Произошла ошибка при добавлении пользователя,ошибка при отправке формы")
    else:
        print('blen')
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
            summmrr = 0
            for u in umrs:
                if ("азработка основной профессиональной образовательной" in u.vid or
                        "азработка примерной основной профессиональной образовательной" in u.vid or
                        "оздание структуры и содержания электронного учебного курса" in u.vid or
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
                        "азработка примерной дополнительной профессиональной программы (программы повышения квалификации, программы профессиональной переподготовки)" in u.vid or
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
                        "азработка cборника образцов процессуальных и служебных документов, макета дела, комплекта ситуационных задач по дисциплине" in u.vid):
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
        except:
            try:
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
                    if ("азработка основной профессиональной образовательной" in u.vid or
                            "азработка примерной основной профессиональной образовательной" in u.vid or
                            "оздание структуры и содержания электронного учебного курса" in u.vid or
                            "нтеграция тестовых заданий в программную оболочку" in u.vid):
                        newmrr = MRR()
                        newmrr.profile = profile
                        newmrr.name = u.vid
                        print(newmrr.name)
                        newmrr.bal = 20
                        newmrr.year = year
                        summmrr += 20
                        newmrr.save()
                    if ("азработка примерной рабочей программы учебной дисциплины" in u.vid or
                            "азработка примерной дополнительной профессиональной программы (программы повышения квалификации, программы профессиональной переподготовки)" in u.vid or
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
                            "азработка cборника образцов процессуальных и служебных документов, макета дела, комплекта ситуационных задач по дисциплине" in u.vid):
                        newmrr = MRR()
                        newmrr.profile = profile
                        newmrr.name = u.vid
                        print(newmrr.name)
                        newmrr.bal = 5
                        newmrr.year = year
                        summmrr += 5
                        newmrr.save()

                newrating.summ = newurr.getsumm() + summmrr
                newrating.save()
                setplace(year, profile)
            except Exception as e:
                print(e)
                return render(request, 'error.html',
                              {'content': "Сначала заполните фактически выполненную работы за оба полугодия"})

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
                profile.dolznost = infodel.dolznost
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
                if table == 1:
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
                if table == 2:
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
                if table == 3:
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
                if table == 4:
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
                if table == 5:
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
                if table == 6:
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
                if table == 7:
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
                if table == 8:
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
                if table == 9:
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
            print("vrode norm")
            return redirect('detail_plan', slug=profile.user.username, year=request.POST['year'])
        else:
            return redirect('log')


def documentSave(request, year, slug):
    if request.user.is_authenticated:
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
        data += [" "] * (375)
        ##normalno po mesyacam
        # u admina dolzhna bit tablisa zapolnena
        # mesyac=Mesyac.objects.filter(prepodavatel=profile,year=year)
        # for m in mesyac:
        #     arr=m.all_values()
        #     for a in arr:
        #        if a=='0':
        #            data.append(" ")
        #        else:
        #            data.append(a)

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

        # shapka
        try:
            docinf = DocInfo.objects.get(plan=plan)
        except:
            docinf = DocInfo(plan=plan)
        listInfo = docinf.all_values()
        # print(indexRow)
        # print(data)
        #

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
                    return Response([{

                        "text": "Нагрузка успешно заменена",
                        "kafname": "Нагрузка по кафедре " + nagruzka.kafedra.fullname + " " + nagruzka.status

                    }])
                except Nagruzka.DoesNotExist:

                    nagruzka = form.save(commit=False)
                    nagruzka.kafedra = profile.kafedra
                    nagruzka.save()
                    return Response([{

                        "text": "Нагрузка успешно добавлена",
                        "kafname": "Нагрузка по кафедре " + nagruzka.kafedra.fullname + " " + nagruzka.status

                    }])
            else:
                print('blen')
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
        user = User.objects.get(username=slug)
        profile = get_object_or_404(Profile, user=user)
        plan = get_object_or_404(Plan, prepod=profile, year=year)
        nagruzkadoc = get_object_or_404(
            Nagruzka.objects.filter(year=year, kafedra=profile.kafedra).exclude(status='Фактическая'))
        predmetsdel = Predmet.objects.filter(prepodavatel=profile, status=False)
        predmetsdel.delete()

        try:
            plans = Plan.objects.filter(prepod__kafedra=profile.kafedra)
            count = 0
            for p in plans:
                if p.name[0:-4] == plan.name[0:-4]:
                    count += 1
                # print(p)
                # print(p)
            if count == 2:
                data = takeXls(nagruzkadoc.document.path, plan.name, True)
            else:
                data = takeXls(nagruzkadoc.document.path, plan.name[0:-4], True)
        except:
            return render(request, 'error.html', {
                'content': "Произошла ошибка при заполнении плана из загруженного XLSX учебной нагрузки файла, пожалуйста проверьте формат документа(см.справку)"})

        # for i in range(len(data)):
        #     for j in range(len(data[i])):
        #         print(data[i][j])
        # # print('')
        # print(data)

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

        predmetsdel = Predmet.objects.filter(prepodavatel=profile, status=True)
        predmetsdel.delete()
        print(nagruzkadoc.document.path)
        print(plan.name[0:-4])
        print('')
        try:
            plans = Plan.objects.filter(prepod__kafedra=profile.kafedra)
            count = 0
            for p in plans:
                if p.name[0:-4] == plan.name[0:-4]:
                    count += 1
                # print(p)
                # print(p)
            if count == 2:
                data = takeXls(nagruzkadoc.document.path, plan.name, False)
            else:
                data = takeXls(nagruzkadoc.document.path, plan.name[0:-4], False)
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
            plan = get_object_or_404(Plan, prepod=profile, year=request.POST['year'])
            # заполняем
            # try:
            #
            #     form=MAinTableForm(request.POST,instance=plan)
            #     print(form.errors)
            #     if form.is_valid():
            #         newplan=form.save(commit=False)
            #         predmets=Predmet.objects.filter(prepodavatel=profile)
            #         for p in predmets:
            #             if p.name=="Итого за 1 полугодие:":
            #                 newplan.ucheb_med_r_1_p=p.ucheb_nagruzka
            #             if p.name=="Итого за 2 полугодие:":
            #                 newplan.ucheb_med_r_2_p=p.ucheb_nagruzka
            #         newplan.year=request.POST['year']
            #         newplan.name=plan.name
            #         newplan.save()
            #
            #     else:
            #         print('blen')
            # except:
            #     return render(request,'error.html',{'content':""})

            form = MAinTableForm(request.POST)
            print(form.errors)
            if form.is_valid():

                newplan = form.save(commit=False)
                predmets = Predmet.objects.filter(prepodavatel=profile, status=True)
                for p in predmets:
                    if p.name == "Итого за 1 полугодие:":
                        newplan.ucheb_med_r_1_p = p.ucheb_nagruzka
                        print(newplan.ucheb_med_r_1_p)
                    if p.name == "Итого за 2 полугодие:":
                        newplan.ucheb_med_r_2_p = p.ucheb_nagruzka
                        print(newplan.ucheb_med_r_2_p)
                newplan.year = request.POST['year']
                newplan.name = plan.name
                newplan.prepod = profile
                print(newplan.name)

                newplan.save()
                plan.delete()


            else:
                print('blen')

        return redirect('detail_plan', slug=profile.user.username, year=request.POST['year'])
    else:
        return redirect('log')

def saveT1(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user=request.user)
        plan = get_object_or_404(Plan, prepod=profile, year=year)
        if request.method == "POST":
            profile = get_object_or_404(Profile, user=request.user)
            Table1FormSet = modelformset_factory(Predmet, form=Table1Form, extra=5)
            formset = Table1FormSet(request.POST,
                                    queryset=Predmet.objects.filter(prepodavatel=profile, polugodie=1, status=False))
            # predmets=formset.save()
            # формсет для первого полугодия

            for form in formset:
                if form.is_valid():
                    predmet = form.save(commit=False)
                    predmet.kafedra = profile.kafedra
                    predmet.polugodie = 1
                    predmet.status = False
                    print(predmet.get_obshaya_nagruzka())
                    predmet.prepodavatel = profile
                    if predmet.name != '':
                        predmet.save()
                else:
                    print('blen')
        return redirect('detail_plan', slug=profile.user.username, year=plan.year)
    else:
        return redirect('log')

def saveT2(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user=request.user)
        if request.method == "POST":
            profile = get_object_or_404(Profile, user=request.user)
            Table1FormSet = modelformset_factory(Predmet, form=Table1Form, extra=5)
            formset2 = Table1FormSet(request.POST,
                                     queryset=Predmet.objects.filter(prepodavatel=profile, polugodie=2, status=False))
            # predmets=formset.save()
            # формсет для первого полугодия

            if formset2.is_valid():
                for form in formset2:
                    predmet = form.save(commit=False)
                    predmet.kafedra = profile.kafedra
                    predmet.polugodie = 2
                    predmet.status = False
                    print(predmet.get_obshaya_nagruzka())
                    predmet.prepodavatel = profile
                    if predmet.name != '':
                        predmet.save()
            else:
                print('blen')
        return HttpResponse("Успешно сохранено")
    else:
        return redirect('log')

def saveT3(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            # print(request.POST)

            profile = get_object_or_404(Profile, user=request.user)
            if profile.role == 3 or profile.role == 2:
                profile = get_object_or_404(Profile, user__username=request.POST['profile'])

            Table1FormSet = modelformset_factory(Predmet, form=Table1Form, extra=5, can_delete=True)
            formset3 = Table1FormSet(request.POST,
                                     queryset=Predmet.objects.filter(prepodavatel=profile, polugodie=1, status=True))
            # predmets=formset.save()
            # формсет для первого полугодия

            if formset3.is_valid():
                pdel = Predmet.objects.filter(prepodavatel=profile, polugodie=1, status=True)
                for p in pdel:
                    p.delete()
                for form in formset3:
                    predmet = form.save(commit=False)
                    predmet.kafedra = profile.kafedra
                    predmet.polugodie = 1
                    predmet.status = True
                    # print(predmet.get_obshaya_nagruzka())
                    predmet.prepodavatel = profile
                    predmet.year = request.POST['year']
                    if predmet.name != '' and predmet.name != 'Итого за 1 полугодие:':
                        predmet.save()
                itog = Predmet()
                predmets = Predmet.objects.filter(prepodavatel=profile, polugodie=1, status=True)
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
                    # print(str(buff)+field.name)
                itog.save()

            else:
                print('blen')

        return HttpResponse("Успешно сохранено")
    else:
        return redirect('log')

def saveT4(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            profile = get_object_or_404(Profile, user=request.user)
            if profile.role == 3 or profile.role == 2:
                profile = get_object_or_404(Profile, user__username=request.POST['profile'])
            Table1FormSet = modelformset_factory(Predmet, form=Table1Form, extra=5)
            formset4 = Table1FormSet(request.POST,
                                     queryset=Predmet.objects.filter(prepodavatel=profile, polugodie=2, status=True))
            # predmets=formset.save()
            # формсет для первого полугодия

            if formset4.is_valid():
                pdel = Predmet.objects.filter(prepodavatel=profile, polugodie=2, status=True)
                for p in pdel:
                    p.delete()
                for form in formset4:
                    predmet = form.save(commit=False)
                    predmet.kafedra = profile.kafedra
                    predmet.polugodie = 2
                    predmet.status = True
                    print(predmet.get_obshaya_nagruzka())
                    predmet.prepodavatel = profile
                    predmet.year = request.POST['year']
                    if predmet.name != '' and predmet.name != 'Итого за 2 полугодие:' and predmet.name != 'Итого за учебный год:':
                        predmet.save()
                itog = Predmet()
                predmets = Predmet.objects.filter(prepodavatel=profile, polugodie=2, status=True)
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
                    print(str(buff) + field.name)
                itog.save()
                itogall = Predmet()
                try:
                    itog1 = Predmet.objects.get(name="Итого за 1 полугодие:", prepodavatel=profile, polugodie=1,
                                                status=True)
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
                    itogall.save()
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
                    itogall.save()





            else:

                print('blen')

        return HttpResponse("Успешно сохранено")
    else:
        return redirect('log')

def saveT5(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user=request.user)
        if request.method == "POST":
            profile = get_object_or_404(Profile, user=request.user)
            if profile.role == 3 or profile.role == 2:
                profile = get_object_or_404(Profile, user__username=request.POST['profile'])
            Table1FormSet = modelformset_factory(UMR, form=Table2Form, extra=5)
            formset4 = Table1FormSet(request.POST, queryset=UMR.objects.filter(prepodavatel=profile, polugodie=1))
            # predmets=formset.save()
            # формсет для первого полугодия

            if formset4.is_valid():
                udel = UMR.objects.filter(prepodavatel=profile, polugodie=1)
                for u in udel:
                    u.delete()
                for form in formset4:
                    umr = form.save(commit=False)
                    umr.polugodie = 1
                    umr.prepodavatel = profile
                    umr.year = request.POST['year']
                    if umr.vid != '':
                        umr.save()
            else:
                print('blen')
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
            formset4 = Table1FormSet(request.POST, queryset=UMR.objects.filter(prepodavatel=profile, polugodie=2))
            # predmets=formset.save()
            # формсет для первого полугодия

            if formset4.is_valid():
                udel = UMR.objects.filter(prepodavatel=profile, polugodie=2)
                for u in udel:
                    u.delete()
                for form in formset4:
                    umr = form.save(commit=False)
                    umr.polugodie = 2
                    umr.prepodavatel = profile
                    umr.year = request.POST['year']
                    if umr.vid != '':
                        umr.save()
            else:
                print('blen')
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
            formset4 = Table1FormSet(request.POST, queryset=NIR.objects.filter(prepodavatel=profile, polugodie=1))
            # predmets=formset.save()
            # формсет для первого полугодия

            if formset4.is_valid():
                udel = NIR.objects.filter(prepodavatel=profile, polugodie=1)
                for u in udel:
                    u.delete()
                for form in formset4:
                    umr = form.save(commit=False)
                    umr.polugodie = 1
                    umr.prepodavatel = profile
                    umr.year = request.POST['year']
                    if umr.vid != '':
                        umr.save()
            else:
                print('blen')
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
            formset4 = Table1FormSet(request.POST, queryset=NIR.objects.filter(prepodavatel=profile, polugodie=2))
            # predmets=formset.save()
            # формсет для первого полугодия

            if formset4.is_valid():
                udel = NIR.objects.filter(prepodavatel=profile, polugodie=2)
                for u in udel:
                    u.delete()
                for form in formset4:
                    umr = form.save(commit=False)
                    umr.polugodie = 2
                    umr.prepodavatel = profile
                    umr.year = request.POST['year']
                    if umr.vid != '':
                        umr.save()
            else:
                print('blen')
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

            if formset4.is_valid():
                udel = VR.objects.filter(prepodavatel=profile, polugodie=1)
                for u in udel:
                    u.delete()
                for form in formset4:
                    umr = form.save(commit=False)
                    umr.polugodie = 1
                    umr.prepodavatel = profile
                    umr.year = request.POST['year']
                    if umr.vid != '':
                        umr.save()
            else:
                print('blen')
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

            if formset4.is_valid():
                udel = VR.objects.filter(prepodavatel=profile, polugodie=2)
                for u in udel:
                    u.delete()
                for form in formset4:
                    umr = form.save(commit=False)
                    umr.polugodie = 2
                    umr.prepodavatel = profile
                    umr.year = request.POST['year']
                    if umr.vid != '':
                        umr.save()
            else:
                print('blen')
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
            print(formset4.errors)
            if formset4.is_valid():
                udel = DR.objects.filter(prepodavatel=profile, polugodie=1)
                for u in udel:
                    u.delete()
                for form in formset4:
                    umr = form.save(commit=False)
                    umr.polugodie = 1
                    umr.prepodavatel = profile
                    umr.year = request.POST['year']
                    if umr.vid != '':
                        umr.save()
            else:
                print('blen')
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
            print(request.POST['year'])
            print(formset4.errors)
            if formset4.is_valid():
                udel = DR.objects.filter(prepodavatel=profile, polugodie=2)
                for u in udel:
                    u.delete()
                for form in formset4:
                    umr = form.save(commit=False)
                    umr.polugodie = 2
                    umr.prepodavatel = profile
                    umr.year = request.POST['year']
                    if umr.vid != '':
                        umr.save()
            else:
                print('blen')
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
            print(request.POST['year'])
            print(formset4.errors)
            if formset4.is_valid():
                udel = INR.objects.filter(prepodavatel=profile, polugodie=1)
                for u in udel:
                    u.delete()
                for form in formset4:
                    umr = form.save(commit=False)
                    umr.polugodie = 1
                    umr.prepodavatel = profile
                    umr.year = request.POST['year']
                    if umr.vid != '':
                        umr.save()
            else:
                print('blen')
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
            print(request.POST['year'])
            print(formset4.errors)
            if formset4.is_valid():
                udel = INR.objects.filter(prepodavatel=profile, polugodie=2)
                for u in udel:
                    u.delete()
                for form in formset4:
                    umr = form.save(commit=False)
                    umr.polugodie = 2
                    umr.prepodavatel = profile
                    umr.year = request.POST['year']
                    if umr.vid != '':
                        umr.save()
            else:
                print('blen')
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
            print(request.POST)

            if form.is_valid():
                try:
                    shpkdel = get_object_or_404(DocInfo, plan=plan)
                    shpkdel.delete()
                except:
                    print("ne")

                shpk = form.save(commit=False)
                shpk.plan = plan
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

            else:
                print('blen')
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
            formset4 = MesyacFormSet(request.POST, queryset=Mesyac.objects.filter(prepodavatel=profile, polugodie=1))
            if formset4.is_valid():
                try:
                    mesyacdel = Mesyac.objects.filter(prepodavatel=profile, polugodie=1)
                    for m in mesyacdel:
                        m.delete()

                except:
                    print("ne")

                for form in formset4:
                    umr = form.save(commit=False)
                    umr.prepodavatel = profile
                    umr.kafedra = profile.kafedra
                    umr.year = request.POST['year']
                    umr.save()
            else:
                print('blen')
        return HttpResponse("Успешно сохранено")
    else:
        return redirect('log')


