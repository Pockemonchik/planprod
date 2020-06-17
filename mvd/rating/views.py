from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from django.views.generic import View
#from snippets.serializers import SnippetSerializer
from plan.models import Profile,Kafedra
from rating.models import URR, ORMR, PCR, MRR,Rating
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rating.forms import URRForm,ORMRForm
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
    urrform=URRForm(instance=urr)
    ormrform=ORMRForm(instance=ormr)
    return render(request,'rate_otsenka.html',{
        'urrform': urrform,
        'ormrform':ormrform,
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
            return HttpResponse("Успешно сохранено")
        else:
            return redirect('log')

class SaveORMRView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        profile = Profile.objects.get(fullname=request.data.get('profile'))
        year = request.data.get('year')
        print(year)
        if request.method == 'POST':
            serializer = SaveORMRSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                urrfordel=ORMR.objects.filter(profile=profile,year=year)

                if urrfordel:
                    urrfordel.delete()
                    serializer.save(profile=profile, year=year)
                    print('delete')


                else:
                    serializer.save(profile=profile, year=year)
                return Response(serializer.data)
            else:
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)


class SavePCRView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        profile = Profile.objects.get(fullname=request.data.get('profile'))
        year = request.data.get('year')
        print(year)
        if request.method == 'POST':
            serializer = SavePCRSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                urrfordel=PCR.objects.filter(profile=profile,year=year)

                if urrfordel:
                    urrfordel.delete()
                    serializer.save(profile=profile, year=year)
                    print('delete')


                else:
                    serializer.save(profile=profile, year=year)
                return Response(serializer.data)
            else:
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)
class SaveMRRView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        profile = Profile.objects.get(fullname=request.data.get('profile'))
        year = request.data.get('year')
        print(year)
        if request.method == 'POST':
            serializer = SaveMRRSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                urrfordel=MRR.objects.filter(profile=profile,year=year)

                if urrfordel:
                    urrfordel.delete()
                    serializer.save(profile=profile, year=year)
                    print('delete')


                else:
                    serializer.save(profile=profile, year=year)
                return Response(serializer.data)
            else:
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)

