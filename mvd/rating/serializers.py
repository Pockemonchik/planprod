from django.contrib.auth.models import User, Group
from rating.models import URR, ORMR, PCR, MRR, Rating
from plan.models import Profile,Kafedra
from rest_framework import serializers

class KafedraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kafedra
        fields = ('fullname',)

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('fullname',)

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('urr','ormr','pcr','mrr')