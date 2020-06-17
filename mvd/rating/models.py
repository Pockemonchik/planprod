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
    summ = models.IntegerField(default=0)

    kafedraplace = models.IntegerField(default=0)
    dolzhnostplace = models.IntegerField(default=0)
    unikplace = models.IntegerField(default=0)

    year = models.IntegerField(default=2020)

    def getsumm(self):
        return self.urr + self.ormr + self.pcr + self.mrr

    def __str__(self):
        return self.profile.fullname+" рейтинг за "+str(self.year)+" год"


class URR(models.Model):
    profile = models.ForeignKey(Profile, related_name='urr', on_delete=models.CASCADE, null=True)
    obsh=models.IntegerField(default=0)
    sootn=models.IntegerField(default=0)
    zansprakt=models.IntegerField(default=0)
    viezdsprakt=models.IntegerField(default=0)
    ppsfp=models.IntegerField(default=0)
    ppsdr = models.IntegerField(default=0)
    vneaudotor=models.IntegerField(default=0)

    obshbal = models.IntegerField(default=0)
    sootnbal = models.IntegerField(default=0)
    zanspraktbal = models.IntegerField(default=0)
    viezdspraktbal = models.IntegerField(default=0)
    ppsfpbal = models.IntegerField(default=0)
    ppsdrbal = models.IntegerField(default=0)
    vneaudotorbal = models.IntegerField(default=0)

    obshpodtv = models.CharField(max_length=250,blank=True)
    sootnpodtv = models.CharField(max_length=250,blank=True)
    zanspraktpodtv = models.CharField(max_length=250,blank=True)
    viezdspraktpodtv = models.CharField(max_length=250,blank=True)
    ppsfppodtv = models.CharField(max_length=250,blank=True)
    ppsdrpodtv = models.CharField(max_length=250,blank=True)
    vneaudotorpodtv = models.CharField(max_length=250,blank=True)
    year = models.IntegerField(default=2020)

    def getsumm(self):
        return self.obsh + self.sootn + self.zansprakt + self.sriv + self.opozdanie

    def __str__(self):
        return self.profile.user.username


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
   year = models.IntegerField(default=2020)


   ruksecbal = models.IntegerField(default=0)
   rukpredmsekbal = models.IntegerField(default=0)
   rabotarukbal = models.IntegerField(default=0)
   rabotachlenbal = models.IntegerField(default=0)
   rukkafnachbal = models.IntegerField(default=0)
   rukkafzambal = models.IntegerField(default=0)
   bestprepodmirbal = models.IntegerField(default=0)
   bestprepodrusbal = models.IntegerField(default=0)
   bestprepodregbal = models.IntegerField(default=0)
   bestprepodunikbal = models.IntegerField(default=0)
   uchastiebestprepodmirbal = models.IntegerField(default=0)
   uchastiebestprepodrusbal = models.IntegerField(default=0)
   uchastiebestprepodregbal = models.IntegerField(default=0)
   uchastiebestprepodunikbal = models.IntegerField(default=0)
   ekspertbal = models.IntegerField(default=0)
   metodkonk1bal = models.IntegerField(default=0)
   metodkonk1bal = models.IntegerField(default=0)
   metodkonk2bal = models.IntegerField(default=0)
   metodkonk3bal = models.IntegerField(default=0)
   profmasterbal = models.IntegerField(default=0)
   podgsbornmirbal = models.IntegerField(default=0)
   podgsbornrusbal = models.IntegerField(default=0)
   podgsbornregbal = models.IntegerField(default=0)
   podgsbornunikbal = models.IntegerField(default=0)
   vulkanbal = models.IntegerField(default=0)
   plenarbal = models.IntegerField(default=0)
   obrprogrammabal = models.IntegerField(default=0)
   proverkafbal = models.IntegerField(default=0)
   inpectunikbal = models.IntegerField(default=0)
   resocenki1bal = models.IntegerField(default=0)
   resocenki6bal = models.IntegerField(default=0)
   resocenki11bal = models.IntegerField(default=0)

   ruksecpodtv = models.CharField(max_length=250, blank=True)
   rukpredmsekpodtv = models.CharField(max_length=250, blank=True)
   rabotarukpodtv = models.CharField(max_length=250, blank=True)
   rabotachlenpodtv = models.CharField(max_length=250, blank=True)
   rukkafnachpodtv = models.CharField(max_length=250, blank=True)
   rukkafzampodtv = models.CharField(max_length=250, blank=True)
   bestprepodmirpodtv = models.CharField(max_length=250, blank=True)
   bestprepodruspodtv = models.CharField(max_length=250, blank=True)
   bestprepodregpodtv = models.CharField(max_length=250, blank=True)
   bestprepodunikpodtv = models.CharField(max_length=250, blank=True)
   uchastiebestprepodmirpodtv = models.CharField(max_length=250, blank=True)
   uchastiebestprepodruspodtv = models.CharField(max_length=250, blank=True)
   uchastiebestprepodregpodtv = models.CharField(max_length=250, blank=True)
   uchastiebestprepodunikpodtv = models.CharField(max_length=250, blank=True)
   ekspertpodtv = models.CharField(max_length=250, blank=True)
   metodkonk1podtv = models.CharField(max_length=250, blank=True)
   metodkonk1podtv = models.CharField(max_length=250, blank=True)
   metodkonk2podtv = models.CharField(max_length=250, blank=True)
   metodkonk3podtv = models.CharField(max_length=250, blank=True)
   profmasterpodtv = models.CharField(max_length=250, blank=True)
   podgsbornmirpodtv = models.CharField(max_length=250, blank=True)
   podgsbornruspodtv = models.CharField(max_length=250, blank=True)
   podgsbornregpodtv = models.CharField(max_length=250, blank=True)
   podgsbornunikpodtv = models.CharField(max_length=250, blank=True)
   vulkanpodtv = models.CharField(max_length=250, blank=True)
   plenarpodtv = models.CharField(max_length=250, blank=True)
   obrprogrammapodtv = models.CharField(max_length=250, blank=True)
   proverkafpodtv = models.CharField(max_length=250, blank=True)
   inpectunikpodtv = models.CharField(max_length=250, blank=True)
   resocenki1podtv = models.CharField(max_length=250, blank=True)
   resocenki6podtv = models.CharField(max_length=250, blank=True)
   resocenki11podtv = models.CharField(max_length=250, blank=True)
   resocenki16podtv = models.CharField(max_length=250, blank=True)
   resocenki26podtv = models.CharField(max_length=250, blank=True)
   inovacpodtv = models.CharField(max_length=250, blank=True)

   def __str__(self):
       return self.profile.user.username



class PCR(models.Model):
    profile = models.ForeignKey(Profile, related_name='pcr', on_delete=models.CASCADE, null=True)
    otkr = models.IntegerField(default=0)
    kontrud = models.IntegerField(default=0)
    kontrneud = models.IntegerField(default=0)
    sriv = models.IntegerField(default=0)
    opozdanie = models.IntegerField(default=0)
    year = models.IntegerField(default=2020)
    def __str__(self):
        return self.profile.user.username
    def getsumm(self):
        return self.otkr+self.kontrud+self.kontrneud+self.sriv+self.opozdanie


class MRR(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    razr1 = models.IntegerField(default=0)
    razr2 = models.IntegerField(default=0)
    razr3 = models.IntegerField(default=0)
    year = models.IntegerField(default=2020)
    def __str__(self):
        return self.profile.user.username

    def getsumm(self):
        return self.razr1 + self.razr2 + self.razr3







