from django.shortcuts import render, redirect, get_object_or_404;
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from snippets.serializers import SnippetSerializer
from plan.models import Profile,Kafedra
from rating.models import URR, ORMR, PCR, MRR,Rating
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from .serializers import KafedraSerializer, ProfileSerializer, RatingSerializer
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

class ProfileRatingView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        profile = request.query_params.get('profile')
        rating = Rating.objects.filter(profile__fullname=profile)
        serializer_context = {
            'request': request,
        }
        serializer = RatingSerializer(rating, context=serializer_context, many=True)
        return Response(serializer.data)