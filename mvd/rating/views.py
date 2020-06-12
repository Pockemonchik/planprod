from django.shortcuts import render, redirect, get_object_or_404;
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from snippets.serializers import SnippetSerializer
from plan.models import Profile,Kafedra
from rating.models import URR, ORMR, PCR, MRR,Rating
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from .serializers import KafedraSerializer, ProfileSerializer, RatingSerializer,PlaceSerializer,Place,SaveMRRSerializer,SaveORMRSerializer,SavePCRSerializer,SaveURRSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated


def rate_otsenka(request):
    return render(request,'rate_otsenka.html');

def nach_kaf(request):
    return render(request,'nach_kaf.html');

def sotr_umr(request):
    return render(request,'sotr_umr.html');



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

class SaveURRView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        profile = Profile.objects.get(fullname=request.data.get('profile'))
        year = request.data.get('year')
        print(year)
        if request.method == 'POST':
            serializer = SaveURRSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                urrfordel=URR.objects.filter(profile=profile,year=year)

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

