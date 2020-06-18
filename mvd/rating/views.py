from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from django.views.generic import View
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
#from snippets.serializers import SnippetSerializer
from plan.models import Profile,Kafedra
from rating.models import URR, ORMR, PCR, MRR,Rating
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rating.forms import URRForm,ORMRForm,PCRForm,MRRForm
from .serializers import KafedraSerializer, ProfileSerializer, RatingSerializer,PlaceSerializer,Place,SaveMRRSerializer,SaveORMRSerializer,SavePCRSerializer,SaveURRSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated


def rate_otsenka(request,slug,year):
    profile = get_object_or_404(Profile, user=request.user)
    profile1 = get_object_or_404(Profile, user__username=slug)
    rating = get_object_or_404(Rating, profile=profile1, year=year)

    try:
        urr=get_object_or_404(URR, profile=profile1, year=year)
    except:
        urr=None
    try:
        ormr = get_object_or_404(URR, profile=profile1, year=year)
    except:
        ormr = None
    try:
        pcr = get_object_or_404(PCR, profile=profile1, year=year)
    except:
        pcr = None
    urrform=URRForm(instance=urr)
    ormrform=ORMRForm(instance=ormr)
    pcrform=PCRForm(instance=pcr)
    mrrformset = modelformset_factory(MRR, form=MRRForm, extra=5)
    formset = mrrformset(queryset=MRR.objects.filter(profile=profile1, year=year))
    print(MRR.objects.filter(profile=profile1, year=year))
    return render(request,'rate_otsenka.html',{
        'formset': formset,
        'urrform': urrform,
        'ormrform':ormrform,
        'pcrform': pcrform,
        'profile': profile,
        'profile1': profile1,
        'rating':rating,



    })

def nach_kaf(request):
    return render(request,'nach_kaf.html');

def sotr_umr(request):
    return render(request,'sotr_umr.html');



class GraphView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        dolzhnost = request.query_params.get('dolzhnost')
        year = request.query_params.get('year')
        kafedra = request.query_params.get('kafedra')
        if dolzhnost == "Все должности" and kafedra == "Все кафедры":
            rating = Rating.objects.filter(year=year)
        else:
            if kafedra == "Все кафедры":
                rating = Rating.objects.filter(profile__dolzhnost=dolzhnost,year=year)
            else:
                if dolzhnost == "Все должности":
                    rating = Rating.objects.filter(profile__kafedra__fullname=kafedra,year=year)
                else:
                    rating = Rating.objects.filter(profile__kafedra__fullname=kafedra,profile__dolzhnost=dolzhnost,year=year)
        print(rating)
        print(request.query_params.get('kafedra'))


        year = request.query_params.get('year')

        print(rating)
        graphdata=[]
        buff=[]
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
    #получение all
    permission_classes = [AllowAny]
    def get(self, request):
        kafedras = Kafedra.objects.all()
        serializer_context = {
            'request': request,
        }
        serializer = KafedraSerializer(kafedras, context=serializer_context,many=True)
        return Response(serializer.data)
class ProfileAllView(APIView):
    #получение all
    permission_classes = [AllowAny]
    def get(self, request):
        kafedra=request.query_params.get('kafedra')
        profiles = Profile.objects.filter(kafedra__fullname=kafedra)
        serializer_context = {
            'request': request,
        }
        serializer = ProfileSerializer(profiles, context=serializer_context,many=True)
        return Response(serializer.data)
class ProfileFilterView(APIView):
    #получение all
    permission_classes = [AllowAny]
    def get(self, request):
        kafedra=request.query_params.get('kafedra')
        dolzhnost = request.query_params.get('dolzhnost')
        year=request.query_params.get('year')
        if dolzhnost == "Все должности" and kafedra == "Все кафедры":
            profiles = Rating.objects.filter(year=year)
            print(profiles)
        else:
            if kafedra == "Все кафедры":
                profiles = Rating.objects.filter(profile__dolzhnost=dolzhnost,year=year)
            else:
                if dolzhnost == "Все должности":
                    profiles = Rating.objects.filter(profile__kafedra__fullname=kafedra,year=year)
                else:
                    profiles = Rating.objects.filter(profile__kafedra__fullname=kafedra, dolzhnost=dolzhnost,year=year)

        data=[]
        for p in profiles:
            data.append({'fullname':p.profile.fullname})

        return Response(data)

class YearView(APIView):
    #получение all
    permission_classes = [AllowAny]
    def get(self, request):
        profile=get_object_or_404(Profile,fullname=request.query_params.get('profile'))
        profileratings=Rating.objects.filter(profile=profile)
        years=[]
        for p in profileratings:
            years.append({"year":p.year})

        return Response(years)

class ProfileRatingView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        profile = request.query_params.get('profile')
        year = request.query_params.get('year')
        rating = Rating.objects.filter(profile__fullname=profile,year=year)
        serializer_context = {
            'request': request,
        }
        serializer = RatingSerializer(rating, context=serializer_context, many=True)
        return Response(serializer.data)

class ProfilePlaceView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        profilefullnname = request.query_params.get('profile')
        profile=get_object_or_404(Profile,fullname=profilefullnname)
        year= request.query_params.get('year')
        profilerating=get_object_or_404(Rating,profile=profile,year=year)

        #allrating = Rating.objects.all()
        # kafedraplace=allrating.filter(profile__kafedra=profile.kafedra,year=year,summ__gte=profilerating.summ).count()
        # dolzhnostplace=allrating.filter(profile__dolzhnost=profile.dolzhnost,year=year).exclude(summ__gte=profilerating.summ).count()
        # unikplace=allrating.filter(year=year).exclude(summ__gte=profilerating.summ).count()
        place = Place(profilerating.summ,profilerating.kafedraplace,profilerating.dolzhnostplace,profilerating.unikplace)
        serializer_context = {
            'request': request,
        }
        serializer = PlaceSerializer(place, context=serializer_context)
        return Response([serializer.data])

class SaveURRView(View):

    def post(self, request):
        if request.user.is_authenticated:
            if request.method == "POST":
                print(request.POST)
                profile = get_object_or_404(Profile, user=request.user)
                year=request.POST['year']
                if profile.role == 3 or profile.role == 2:
                    profile = get_object_or_404(Profile, user__username=request.POST['profile'])

                form = URRForm(request.POST)


                if form.is_valid():
                    try:
                        urrdel = get_object_or_404(URR, profile=profile,year=year)
                        urrdel.delete()
                    except:
                        print("ne")

                    urr = form.save(commit=False)
                    urr.profile = profile
                    urr.save()
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
                    urr.save()
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
                    urr.save()
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
                    mrrdel = MRR.objects.filter(profile=profile,year=year)
                    for u in mrrdel:
                        u.delete()
                    for form in formset:
                        mrr = form.save(commit=False)
                        mrr.profile = profile
                        mrr.year = request.POST['year']
                        mrr.save()

                else:
                    print(formset.errors)
                    return HttpResponse("Ошибка при сохранении таблицы")
            return HttpResponse("Успешно сохранено")
        else:
            return redirect('log')

