from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.conf.urls import url
from django.core.exceptions import ValidationError
from django.urls import reverse
from plan.models import Profile
class Rating(models.Model):
    profile = models.ForeignKey(Profile, related_name='rating', on_delete=models.CASCADE, null=True)
    urr=models.IntegerField(default=0)
    ormr = models.IntegerField(default=0)
    pcr = models.IntegerField(default=0)
    mrr = models.IntegerField(default=0)
class URR(models.Model):
    profile = models.ForeignKey(Profile, related_name='urr', on_delete=models.CASCADE, null=True)
    obsh=models.IntegerField(default=0)
    sootn=models.IntegerField(default=0)
    zansprakt=models.IntegerField(default=0)
    viezdsprakt=models.IntegerField(default=0)
    ppsfp=models.IntegerField(default=0)
    ppsdr = models.IntegerField(default=0)
    vneaudotor=models.IntegerField(default=0)

    def getsumm(self):
        return self.obsh + self.sootn + self.zansprakt + self.sriv + self.opozdanie

class ORMR(models.Model):
   profile=models.ForeignKey(Profile, related_name='ormr', on_delete=models.CASCADE, null=True)
   ruksec=models.IntegerField(default=0)
   rukpredmsek=models.IntegerField(default=0)
   rabotaruk=models.IntegerField(default=0)
   rabotachlen=models.IntegerField(default=0)
   rukkafnach=models.IntegerField(default=0)
   rukkafzam=models.IntegerField(default=0)
   bestprepodmir=models.IntegerField(default=0)
   bestprepodrus=models.IntegerField(default=0)
   bestprepodreg=models.IntegerField(default=0)
   bestprepodunik=models.IntegerField(default=0)
   uchastiebestprepodmir = models.IntegerField(default=0)
   uchastiebestprepodrus = models.IntegerField(default=0)
   uchastiebestprepodreg = models.IntegerField(default=0)
   uchastiebestprepodunik = models.IntegerField(default=0)
   ekspert=models.IntegerField(default=0)
   metodkonk1=models.IntegerField(default=0)
   metodkonk1 = models.IntegerField(default=0)
   metodkonk2 = models.IntegerField(default=0)
   metodkonk3 = models.IntegerField(default=0)
   profmaster = models.IntegerField(default=0)
   podgsbornmir=models.IntegerField(default=0)
   podgsbornrus=models.IntegerField(default=0)
   podgsbornreg=models.IntegerField(default=0)
   podgsbornunik=models.IntegerField(default=0)
   vulkan=models.IntegerField(default=0)
   plenar=models.IntegerField(default=0)
   obrprogramma=models.IntegerField(default=0)
   proverkaf=models.IntegerField(default=0)
   inpectunik=models.IntegerField(default=0)
   resocenki1=models.IntegerField(default=0)
   resocenki6 = models.IntegerField(default=0)
   resocenki11 = models.IntegerField(default=0)
   resocenki16 = models.IntegerField(default=0)
   resocenki26 = models.IntegerField(default=0)
   inovac = models.IntegerField(default=0)

   def __str__(self):
       return self.profile.user.username



class PCR(models.Model):
    profile = models.ForeignKey(Profile, related_name='pcr', on_delete=models.CASCADE, null=True)
    otkr = models.IntegerField(default=0)
    kontrud = models.IntegerField(default=0)
    kontrneud = models.IntegerField(default=0)
    sriv = models.IntegerField(default=0)
    opozdanie = models.IntegerField(default=0)

    def __str__(self):
        return self.profile.user.username
    def getsumm(self):
        return self.otkr+self.kontrud+self.kontrneud+self.sriv+self.opozdanie


class MRR(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    razr1 = models.IntegerField(default=0)
    razr2 = models.IntegerField(default=0)
    razr3 = models.IntegerField(default=0)
    def __str__(self):
        return self.profile.user.username

    def getsumm(self):
        return self.razr1 + self.razr2 + self.razr3







