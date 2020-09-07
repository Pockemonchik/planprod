from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from django.views.generic import View
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
# from snippets.serializers import SnippetSerializer
from plan.models import Profile, Kafedra, ProfileInfo
from rating.models import URR, ORMR, PCR, MRR, Rating
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rating.ratingDocx import createRatingDocx
from rating.forms import URRForm, ORMRForm, PCRForm, MRRForm
from .serializers import KafedraSerializer, ProfileSerializer, RatingSerializer, PlaceSerializer, Place, \
    SaveMRRSerializer, SaveORMRSerializer, SavePCRSerializer, SaveURRSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated

import os
from io import StringIO, BytesIO

"""Ренедеринг основных страниц"""
def rate_otsenka(request, slug, year):
    profile = get_object_or_404(Profile, user=request.user)
    profile1 = get_object_or_404(Profile, user__username=slug)
    rating = get_object_or_404(Rating, profile=profile1, year=year)

    try:
        urr = get_object_or_404(URR, profile=profile1, year=year)
    except:
        urr = None
    try:
        ormr = get_object_or_404(ORMR, profile=profile1, year=year)
    except:
        ormr = None
    try:
        pcr = get_object_or_404(PCR, profile=profile1, year=year)
    except:
        pcr = None

    urrform = URRForm(instance=urr)
    ormrform = ORMRForm(instance=ormr)
    pcrform = PCRForm(instance=pcr)
    mrrformset = modelformset_factory(MRR, form=MRRForm, extra=0)
    formset = mrrformset(queryset=MRR.objects.filter(profile=profile1, year=year))
    print(MRR.objects.filter(profile=profile1, year=year))
    title = "Рейтинговая оценка " + ''.join(
        [profile1.fullname.split(' ')[0], ' ', profile1.fullname.split(' ')[1][0], '.',
         profile1.fullname.split(' ')[1][0]])+" "+year
    return render(request, 'rate_otsenka.html', {
        'formset': formset,
        'urrform': urrform,
        'ormrform': ormrform,
        'pcrform': pcrform,
        'profile': profile,
        'profile1': profile1,
        'rating': rating,

        'urr': urr,
        'ormr': ormr,
        'pcr': pcr,
        'title': title

    })


def nach_kaf(request):
    profile = get_object_or_404(Profile, user=request.user)
    if profile.role == 3:
        return render(request, 'sotr_umr.html')
    kafedra = profile.kafedra.fullname
    return render(request, 'nach_kaf.html', {
        'kafedra': kafedra,
    })


def sotr_umr(request):
    return render(request, 'sotr_umr.html')


"""Получение данных о пользователях, кафедрах и друге"""
class GraphView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        dolzhnost = request.query_params.get('dolzhnost')
        year = request.query_params.get('year')
        kafedra = request.query_params.get('kafedra')
        if kafedra == "Рейтинг по кафедрам":
            rating = Rating.objects.filter(year=year)
            kafedras = Kafedra.objects.all()
            graphdata = []
            buff = []
            for k in kafedras:
                profiles=k.prepods.all()
                
                # for p in k.prepods:
                #     print(p.fullname)

            return Response(graphdata)
        else:
            if dolzhnost == "Все должности" and kafedra == "Все кафедры":
                rating = Rating.objects.filter(year=year)
            else:
                if kafedra == "Все кафедры":
                    rating = Rating.objects.filter(profile__dolzhnost=dolzhnost, year=year)
                else:
                    if dolzhnost == "Все должности":
                        rating = Rating.objects.filter(profile__kafedra__fullname=kafedra, year=year)
                    else:
                        rating = Rating.objects.filter(profile__kafedra__fullname=kafedra, profile__dolzhnost=dolzhnost,
                                                       year=year)
            print(rating)
            print(request.query_params.get('kafedra'))

            year = request.query_params.get('year')

            print(rating)
            graphdata = []
            buff = []
            for r in rating:
                print(r.profile.fullname)
                buff.append(r.urr)
            graphdata.append({
                "name": 'Учебная работа',
                "data": buff
            })
            buff = []
            for r in rating:
                print(r.profile.fullname)
                buff.append(r.ormr)
            graphdata.append({
                "name": 'Организационно методическая работа',
                "data": buff
            })
            buff = []
            for r in rating:
                print(r.profile.fullname)
                buff.append(r.mrr)
            graphdata.append({
                "name": 'Подготовка учебно-методических материалов',
                "data": buff
            })
            buff = []
            for r in rating:
                print(r.profile.fullname)
                buff.append(r.pcr)
            graphdata.append({
                "name": 'Педагогический контроль',
                "data": buff
            })

            return Response(graphdata)


class KafedraAllView(APIView):
    # получение all
    permission_classes = [AllowAny]

    def get(self, request):
        kafedras = Kafedra.objects.all()
        serializer_context = {
            'request': request,
        }
        serializer = KafedraSerializer(kafedras, context=serializer_context, many=True)
        return Response(serializer.data)


class ProfileAllView(APIView):
    # получение all
    permission_classes = [AllowAny]

    def get(self, request):
        kafedra = request.query_params.get('kafedra')
        profiles = Profile.objects.filter(kafedra__fullname=kafedra)
        serializer_context = {
            'request': request,
        }
        serializer = ProfileSerializer(profiles, context=serializer_context, many=True)
        return Response(serializer.data)


class ProfileFilterView(APIView):
    # получение all
    permission_classes = [AllowAny]

    def get(self, request):
        kafedra = request.query_params.get('kafedra')
        dolzhnost = request.query_params.get('dolzhnost')
        year = request.query_params.get('year')
        if dolzhnost == "Все должности" and kafedra == "Все кафедры":
            profiles = Rating.objects.filter(year=year)
            print(profiles)
        else:
            if kafedra == "Все кафедры":
                profiles = Rating.objects.filter(profile__dolzhnost=dolzhnost, year=year)
            else:
                if dolzhnost == "Все должности":
                    profiles = Rating.objects.filter(profile__kafedra__fullname=kafedra, year=year)
                else:
                    profiles = Rating.objects.filter(profile__kafedra__fullname=kafedra, dolzhnost=dolzhnost, year=year)

        data = []
        for p in profiles:
            data.append({'fullname': p.profile.fullname})

        return Response(data)


class YearView(APIView):
    # получение all
    permission_classes = [AllowAny]

    def get(self, request):
        profile = get_object_or_404(Profile, fullname=request.query_params.get('profile'))
        profileratings = Rating.objects.filter(profile=profile)
        years = []
        for p in profileratings:
            years.append({"year": p.year})

        return Response(years)


class ProfileRatingView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        profile = request.query_params.get('profile')
        year = request.query_params.get('year')
        rating = Rating.objects.filter(profile__fullname=profile, year=year)
        serializer_context = {
            'request': request,
        }
        serializer = RatingSerializer(rating, context=serializer_context, many=True)
        return Response(serializer.data)


class ProfilePlaceView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        profilefullnname = request.query_params.get('profile')
        profile = get_object_or_404(Profile, fullname=profilefullnname)
        year = request.query_params.get('year')
        try:
            profilerating = Rating.objects.get(profile=profile, year=year)
        except:
            return HttpResponse("Ре")

        place = Place(profilerating.summ, profilerating.kafedraplace, profilerating.dolzhnostplace,
                      profilerating.unikplace)
        serializer_context = {
            'request': request,
        }
        serializer = PlaceSerializer(place, context=serializer_context)
        return Response([serializer.data])


"""Сохранение основных таблиц"""
class SaveURRView(View):

    def post(self, request):
        if request.user.is_authenticated:
            if request.method == "POST":
                print(request.POST)
                profile = get_object_or_404(Profile, user=request.user)
                year = request.POST['year']
                if profile.role == 3 or profile.role == 2:
                    profile = get_object_or_404(Profile, user__username=request.POST['profile'])

                form = URRForm(request.POST)

                if form.is_valid():
                    try:
                        urrdel = get_object_or_404(URR, profile=profile, year=year)
                        urrdel.delete()
                    except:
                        print("ne")

                    urr = form.save(commit=False)
                    urr.profile = profile
                    urr.year = year
                    urr.save()
                    setplace(year, profile)

                else:
                    print('blen')
                    return HttpResponse("Ошибка при сохранении таблицы")
            return HttpResponse("Успешно сохранено")
        else:
            return redirect('log')


class SaveORMRView(View):
    def post(self, request):
        if request.user.is_authenticated:
            if request.method == "POST":
                print(request.POST)
                profile = get_object_or_404(Profile, user=request.user)
                year = request.POST['year']
                if profile.role == 3 or profile.role == 2:
                    profile = get_object_or_404(Profile, user__username=request.POST['profile'])

                form = ORMRForm(request.POST)

                if form.is_valid():
                    try:
                        urrdel = get_object_or_404(ORMR, profile=profile, year=year)
                        urrdel.delete()
                    except:

                        print("ne")

                    urr = form.save(commit=False)
                    urr.profile = profile
                    urr.year = year
                    urr.save()
                    setplace(year, profile)
                else:
                    print(form.errors)
                    return HttpResponse("Ошибка при сохранении таблицы")
            return HttpResponse("Успешно сохранено")
        else:
            return redirect('log')


class SavePCRView(View):
    def post(self, request):
        if request.user.is_authenticated:
            if request.method == "POST":
                print(request.POST)
                profile = get_object_or_404(Profile, user=request.user)
                year = request.POST['year']
                if profile.role == 3 or profile.role == 2:
                    profile = get_object_or_404(Profile, user__username=request.POST['profile'])

                form = PCRForm(request.POST)

                if form.is_valid():
                    try:
                        urrdel = get_object_or_404(PCR, profile=profile, year=year)
                        urrdel.delete()
                    except:

                        print("ne")

                    urr = form.save(commit=False)
                    urr.profile = profile
                    urr.year = year
                    urr.save()
                    setplace(year, profile)
                else:
                    print(form.errors)
                    return HttpResponse("Ошибка при сохранении таблицы")
            return HttpResponse("Успешно сохранено")
        else:
            return redirect('log')


class SaveMRRView(View):

    def post(self, request):
        if request.user.is_authenticated:
            if request.method == "POST":
                print(request.POST)
                profile = get_object_or_404(Profile, user=request.user)
                year = request.POST['year']
                if profile.role == 3 or profile.role == 2:
                    profile = get_object_or_404(Profile, user__username=request.POST['profile'])
                MRRFormSet = modelformset_factory(MRR, form=MRRForm)
                formset = MRRFormSet(request.POST, queryset=MRR.objects.filter(profile=profile))

                if formset.is_valid():
                    mrrdel = MRR.objects.filter(profile=profile, year=year)
                    for u in mrrdel:
                        u.delete()
                    for form in formset:
                        mrr = form.save(commit=False)
                        mrr.profile = profile
                        mrr.year = request.POST['year']
                        mrr.save()
                        setplace(year, profile)

                else:
                    print(formset.errors)
                    return HttpResponse("Ошибка при сохранении таблицы")
            return HttpResponse("Успешно сохранено")
        else:
            return redirect('log')


"""Обновление рейтингов для всех сотрудников по ссыылке"""
class RefreshRatingView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        year = request.query_params.get('year')

        return Response(refresh_places(year))


"""Класс для общей таблицы """
class RatingTableView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        year = request.query_params.get('year')
        allrating = Rating.objects.filter(year=year).order_by("summ").reverse()
        data = []
        for r in allrating:
            if r.summ != 0:
                data.append(
                    {'fio': r.profile.fullname,
                     'summ': r.summ,
                     'unikplace': r.unikplace,
                     'dolzhnostplace': r.dolzhnostplace,
                     'kafedraplace': r.kafedraplace
                     }
                )
        return Response(data)


"""Сохранение документа"""
def documentSave(request, year, slug):
    if request.user.is_authenticated:
        user = User.objects.get(username=slug)
        profile = get_object_or_404(Profile, user=user)
        rating = get_object_or_404(Rating, profile=profile, year=year)

        toptext = []
        tableLens = []
        inTable = [

        ]
        try:
            toptext.append(profile.kafedra.fullname)
            toptext.append(str(year))
            toptext.append(str((int(year) + 1)))
            toptext.append(profile.info.fio)
            toptext.append(profile.info.dolznost)
            toptext.append(str(profile.info.stavka))
            toptext.append(profile.info.uchst)
            toptext.append(profile.info.uchzv)
            toptext.append(" ")
        except:
            toptext = [" ", " ", " ", "Заполните главную страницу", " ", " ", " ", " ", " "]

        try:
            urr = get_object_or_404(URR, profile=profile, year=year)
            inTable.append(urr.getDataForDoc())
        except:
            urr = URR()
            urr.profile = profile
            urr.year = year
            inTable.append(urr.getDataForDoc())
        try:
            ormr = get_object_or_404(ORMR, profile=profile, year=year)
            inTable.append(ormr.getDataForDoc())
        except:
            ormr = ORMR()
            ormr.profile = profile
            ormr.year = year
            inTable.append(ormr.getDataForDoc())
        mrrdata = []
        mrr = MRR.objects.filter(profile=profile, year=year)
        for m in mrr:
            mrrdata.extend(["3.1", m.name, str(m.bal)])
        inTable.append(mrrdata)

        try:
            pcr = get_object_or_404(PCR, profile=profile, year=year)
            inTable.append(pcr.getDataForDoc())
        except:
            pcr = PCR()
            pcr.profile = profile
            pcr.year = year
            inTable.append(pcr.getDataForDoc())
        tableLens.extend([7, 35, mrr.count(), 5])

        sumBal = [str(rating.urr), str(rating.ormr), str(rating.mrr), str(rating.pcr), str(rating.summ)]

        doc = createRatingDocx(toptext, tableLens, inTable, sumBal)

        f = BytesIO()
        doc.save(f)
        response = HttpResponse(f.getvalue(),
                                content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
        response['Content-Disposition'] = 'inline; filename=rating.docx'
        return response



    else:
        return redirect('log')


"""Пересчет рейтинга и сумм баллов при сохраненни отдельных отаблиц"""
def setplace(year, profile):
    allrating = Rating.objects.filter(year=year)
    profilerating = Rating.objects.get(profile=profile, year=year)

    try:
        urrsumm = (URR.objects.get(profile=profile, year=year)).getsumm()
    except:
        urrsumm = 0
    try:
        ormrsumm = (ORMR.objects.get(profile=profile, year=year)).getsumm()
    except:
        ormrsumm = 0
    try:
        pcrsumm = (PCR.objects.get(profile=profile, year=year)).getsumm()
    except:
        pcrsumm = 0
    mrrsumm = 0
    mrrs = MRR.objects.filter(profile=profile, year=year)
    for m in mrrs:
        mrrsumm += m.bal
    profilerating.summ = urrsumm + ormrsumm + pcrsumm + mrrsumm
    profilerating.urr = urrsumm
    profilerating.ormr = ormrsumm
    profilerating.pcr = pcrsumm
    profilerating.mrr = mrrsumm
    profilerating.kafedraplace = allrating.filter(profile__kafedra=profile.kafedra, year=year,
                                                  summ__gte=profilerating.summ).count()
    profilerating.dolzhnostplace = allrating.filter(profile__dolzhnost=profile.dolzhnost, year=year,
                                                    summ__gte=profilerating.summ).count()
    profilerating.unikplace = allrating.filter(year=year, summ__gte=profilerating.summ).count()
    profilerating.save()
    print(profilerating.profile.fullname," ",profilerating.summ," ",profilerating.unikplace)

    #print(allrating.filter(year=year, summ__gte=profilerating.summ))


"""Пересчет рейтинга для всех сотрудников"""
def refresh_places(year):
    try:
        allrating = Rating.objects.filter(year=year)
        for r in allrating:
            setplace(year, r.profile)
        return "Успешно обновлены позиции"
    except Exception as e:
        print(e)
        return "Ошибка при обновлении позиций"
