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
        fields = ('urr','ormr','pcr','mrr','kafedraplace','dolzhnostplace','unikplace','kolvomes')




class SaveURRSerializer(serializers.ModelSerializer):
    class Meta:
        model = URR
        exclude = ('year','profile',)
class SaveORMRSerializer(serializers.ModelSerializer):
    class Meta:
        model = ORMR
        exclude = ('year','profile',)
class SavePCRSerializer(serializers.ModelSerializer):
    class Meta:
        model = PCR
        exclude = ('year','profile',)
class SaveMRRSerializer(serializers.ModelSerializer):
    class Meta:
        model = MRR
        exclude = ('year','profile',)







class Place(object):
    def __init__(self, summ,kafedraplace, dolzhnostplace, unikplace):
        self.summ = summ
        self.kafedraplace = kafedraplace
        self.dolzhnostplace = dolzhnostplace
        self.unikplace = unikplace

class PlaceSerializer(serializers.Serializer):
    summ = serializers.IntegerField()
    kafedraplace=serializers.IntegerField()
    dolzhnostplace = serializers.IntegerField()
    unikplace = serializers.IntegerField()