from django.db import models
from django.contrib.auth.models import User
from django.conf.urls import url
from django.core.exceptions import ValidationError
from django.urls import reverse
# Create your models here.
 #кафедра
#талица для записи инфы о преподе в документ
class Article(models.Model):

    body=models.TextField()

    def __str__(self):
        return self.body

def validate_decimals(value):
    try:
        return round(float(value), 2)
    except:
        raise ValidationError(('%(value)s is not an integer or a float number'), params={'value': value}, )

class Kafedra(models.Model):
     name=models.CharField(max_length=501)
     fullname=models.CharField(max_length=250,blank=True)
     def __str__(self):
         return self.fullname
#модель учебной нагррузки
class Nagruzka(models.Model):
    year=models.IntegerField(default=2019)

    PROGRESS=(
         ('Планируемая', 'Планируемая'),
         ('Фактическая', 'Фактическая'),)
    status=models.CharField(max_length=20,choices=PROGRESS,default="Планируемая")
    kafedra=models.ForeignKey(Kafedra, related_name='nagruzki',on_delete=models.CASCADE)
    document=models.FileField(upload_to='files',default='settings.MEDIA_ROOT/plan.docx')
    def __str__(self):
         return "Нагрузка по кафедре "+str(self.kafedra.fullname)+" "+self.status
#профили пользователей
class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile',on_delete=models.CASCADE,primary_key=True)
    kafedra=models.ForeignKey(Kafedra, related_name='prepods',on_delete=models.CASCADE,null=True,blank=True)
    dolzhnost=models.CharField(max_length=1000,blank=True)
    fullname=models.CharField(max_length=250,blank=True)
    stepen=models.CharField(max_length=250,blank=True)
    #право доступа, 1- обычный пользователь 2-привелигированный
    role = models.IntegerField(default=1)
    status=models.BooleanField(default=True)
    def __str__(self):
        return " "+self.fullname+" "+self.user.username+" "+self.user.email+" "

class ProfileInfo(models.Model):
    fio=models.CharField(max_length=250,blank=True)
    dolznost=models.CharField(max_length=250,blank=True)
    stavka=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    uchzv=models.CharField(max_length=250,blank=True)
    uchst=models.CharField(max_length=250,blank=True)
    visluga=models.IntegerField(default=0,blank=True)
    kafedra=models.CharField(max_length=250,blank=True)
    profile=models.OneToOneField(Profile,related_name='info',on_delete=models.CASCADE,primary_key=True)

    def __str__(self):
        return self.fio

#  основная модель плана
class Plan(models.Model):
    name=models.CharField(max_length=250,default='plan')
    year=models.IntegerField(default=2019)
    prepod=models.ForeignKey(Profile,related_name='plans',on_delete=models.CASCADE)
    document=models.FileField(upload_to='media',default='settings.MEDIA_ROOT/plan.docx')
    ucheb_r_1_p=models.FloatField(default=0)
    ucheb_r_2_p=models.FloatField(default=0)
    PROGRESS=(
        ('Выполнена', 'Выполнена'),
        ('Выполнена частично', 'Выполнена частично'),
        ('Не выполнена', 'Не выполнена'),
        (' ', ' '))

    ucheb_med_r_1_p=models.CharField(max_length=20,choices=PROGRESS,default=" ")
    ucheb_med_r_2_p=models.CharField(max_length=20,choices=PROGRESS,default=" ")
    nir_1_p=models.CharField(max_length=20,choices=PROGRESS,default=" ")
    nir_1_p=models.CharField(max_length=20,choices=PROGRESS,default=" ")
    nir_2_p=models.CharField(max_length=20,choices=PROGRESS,default=" ")
    vr_1_p=models.CharField(max_length=20,choices=PROGRESS,default=" ")
    vr_2_p=models.CharField(max_length=20,choices=PROGRESS,default=" ")
    inr_1_p=models.CharField(max_length=20,choices=PROGRESS,default=" ")
    inr_2_p=models.CharField(max_length=20,choices=PROGRESS,default=" ")
    dr_1_p=models.CharField(max_length=20,choices=PROGRESS,default=" ")
    dr_2_p=models.CharField(max_length=20,choices=PROGRESS,default=" ")
    def __str__(self):
        return self.name+" "+str(self.year)
    def all_values(self):
        return(
            str(self.ucheb_r_1_p),
            str(self.ucheb_r_2_p),
            str(self.ucheb_med_r_1_p),
            str(self.ucheb_med_r_2_p),
            str(self.nir_1_p),
            str(self.nir_2_p),
            str(self.vr_1_p),
            str(self.vr_2_p),
            str(self.inr_1_p),
            str(self.inr_2_p),
            str(self.dr_1_p),
            str(self.dr_2_p),


        )

class DocInfo(models.Model):
    shapka=models.CharField(max_length=250,blank=True)
    fionach=models.CharField(max_length=250,blank=True)
    data=models.CharField(max_length=250,blank=True)
    na_kakoygod=models.IntegerField(default=2019,blank=True,null=True)
    na_kakoygod1=models.IntegerField(default=2020,blank=True,null=True)
    fio=models.CharField(max_length=250,blank=True)
    dolznost=models.CharField(max_length=250,blank=True)
    stavka=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    uchzv=models.CharField(max_length=250,blank=True)
    uchst=models.CharField(max_length=250,blank=True)
    visluga=models.IntegerField(default=0,blank=True)
    kafedra=models.CharField(max_length=250,blank=True)
    plan=models.OneToOneField(Plan,related_name='shapka',on_delete=models.CASCADE,primary_key=True)
    def all_values(self):
        try:
            if self.stavka.is_integer():
                self.stavka=int(self.stavka)
        except:
            self.stavka=0
        let=''
        k = self.visluga % 10
        if (self.visluga>9)and(self.visluga<20)or(self.visluga>110)or(k>4)or(k==0):
            let=' лет.'
        else:
            if k==1: let=" год."
            else: let=" года."
        if self.uchst=='' and self.uchzv=='':
            return([
            self.shapka,
            self.fionach,
            self.data,
            'На '+str(self.na_kakoygod)+' / '+str(self.na_kakoygod1)+' учебный год',
            self.fio,
            self.dolznost+', '+str(self.stavka)+' ст.',
            self.kafedra,
            str(self.visluga)+let
            ])
        if self.uchst=='':
            return([
            self.shapka,
            self.fionach,
            self.data,
            'На '+str(self.na_kakoygod)+' / '+str(self.na_kakoygod1)+' учебный год',
            self.fio,
            self.dolznost+', '+str(self.stavka)+' ст.',
            self.kafedra,
            self.uchzv+', '+str(self.visluga)+let+let
            ])
        if self.uchzv=='':
            return([
            self.shapka,
            self.fionach,
            self.data,
            'На '+str(self.na_kakoygod)+' / '+str(self.na_kakoygod1)+' учебный год',
            self.fio,
            self.dolznost+', '+str(self.stavka)+' ст.',
            self.kafedra,
            self.uchst+', '+str(self.visluga)+let
            ])
        return([
        self.shapka,
        self.fionach,
        self.data,
        'На '+str(self.na_kakoygod)+' / '+str(self.na_kakoygod1)+' учебный год',
        self.fio,
        self.dolznost+', '+str(self.stavka)+' ст.',
        self.kafedra,
        self.uchst+', '+self.uchzv+', '+str(self.visluga)+let
        ])
    def __str__(self):
        if self.fio == "":
            return self.plan.name
        else:
             return self.fio

class Predmet(models.Model):
    name=models.CharField(max_length=250,blank=True)
    ###поля в таблице
    leccii=models.FloatField(default=0,blank=True,validators=[validate_decimals],null=True)
    seminar=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    practici_v_gruppe=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    practici_v_podgruppe=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    krugliy_stol=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    konsultacii_pered_ekzamenom=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    tekushie_konsultacii=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    vneauditor_chtenie=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    rucovodstvo_practikoy=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    rucovodstvo_VKR=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    rucovodstvo_kursovoy=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    proverka_auditor_KR=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    proverka_dom_KR=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    proverka_practicuma=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    proverka_lab=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    priem_zashit_practic=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    zacheti_ust=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    zacheti_pism=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    priem_vstupit=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    ekzamenov=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    priem_GIA=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    priem_kandidtskih=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    rucovodstvo_adunctami=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    ucheb_nagruzka=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    auditor_nagruzka=models.FloatField(default=0,blank=True,validators=[validate_decimals])

    kafedra=models.ForeignKey(Kafedra, related_name='predmets',on_delete=models.CASCADE)
    prepodavatel=models.ForeignKey(Profile,related_name='predmets',on_delete=models.CASCADE)
    year=models.IntegerField(default=2019,blank=True)
    polugodie=models.IntegerField(default=1,blank=True)
    status=models.BooleanField(default=False,blank=True)#tru если выполена false если план
    def get_arr_all(self):
        return(([self.leccii,
        self.seminar,
        self.practici_v_gruppe,
        self.practici_v_podgruppe,
        self.krugliy_stol,
        self.konsultacii_pered_ekzamenom,
        self.tekushie_konsultacii,
        self.vneauditor_chtenie,
        self.rucovodstvo_practikoy,
        self.rucovodstvo_VKR,
        self.rucovodstvo_kursovoy,
        self.proverka_auditor_KR,
        self.proverka_dom_KR,
        self.proverka_practicuma,
        self.proverka_lab,
        self.priem_zashit_practic,
        self.zacheti_ust,
        self.zacheti_pism,
        self.priem_vstupit,
        self.ekzamenov,
        self.priem_GIA,
        self.priem_kandidtskih,
        self.rucovodstvo_adunctami]))
    def get_obshaya_nagruzka(self):
        return(self.leccii+
        self.seminar+
        self.practici_v_gruppe+
        self.practici_v_podgruppe+
        self.krugliy_stol+
        self.konsultacii_pered_ekzamenom+
        self.tekushie_konsultacii+
        self.vneauditor_chtenie+
        self.rucovodstvo_practikoy+
        self.rucovodstvo_VKR+
        self.rucovodstvo_kursovoy+
        self.proverka_auditor_KR+
        self.proverka_dom_KR+
        self.proverka_practicuma+
        self.proverka_lab+
        self.priem_zashit_practic+
        self.zacheti_ust+
        self.zacheti_pism+
        self.priem_vstupit+
        self.ekzamenov+
        self.priem_GIA+
        self.priem_kandidtskih+
        self.rucovodstvo_adunctami)

    def get_auditor_nagruzka(self):
        return(self.leccii+
        self.seminar+
        self.practici_v_gruppe+
        self.practici_v_podgruppe+
        self.krugliy_stol+
        self.konsultacii_pered_ekzamenom+
        self.priem_zashit_practic+
        self.zacheti_ust+
        self.zacheti_pism+
        self.priem_vstupit+
        self.ekzamenov+
        self.priem_GIA+
        self.priem_kandidtskih)
    def __str__(self):
        return self.name

    def all_values(self):
        return  (self.name,
            str(self.leccii),
            str(self.seminar),
            str(self.practici_v_gruppe),
            str(self.practici_v_podgruppe),
            str(self.krugliy_stol),
            str(self.konsultacii_pered_ekzamenom),
            str(self.tekushie_konsultacii),
            str(self.vneauditor_chtenie),
            str(self.rucovodstvo_practikoy),
            str(self.rucovodstvo_VKR),
            str(self.rucovodstvo_kursovoy),
            str(self.proverka_auditor_KR),
            str(self.proverka_dom_KR),
            str(self.proverka_practicuma),
            str(self.proverka_lab),
            str(self.priem_zashit_practic),
            str(self.zacheti_ust),
            str(self.zacheti_pism),
            str(self.priem_vstupit),
            str(self.ekzamenov),
            str(self.priem_GIA),
            str(self.priem_kandidtskih),
            str(self.rucovodstvo_adunctami),
            str(self.ucheb_nagruzka),
            str(self.auditor_nagruzka))

    def save(self, *args, **kwargs):

        self.leccii=validate_decimals(self.leccii)
        self.seminar=validate_decimals(self.seminar)
        self.practici_v_gruppe=validate_decimals(self.practici_v_gruppe)
        self.practici_v_podgruppe=validate_decimals(self.practici_v_podgruppe)
        self.krugliy_stol=validate_decimals(self.krugliy_stol)
        self.konsultacii_pered_ekzamenom=validate_decimals(self.konsultacii_pered_ekzamenom)
        self.tekushie_konsultacii=validate_decimals(self.tekushie_konsultacii)
        self.vneauditor_chtenie=validate_decimals(self.vneauditor_chtenie)
        self.rucovodstvo_practikoy=validate_decimals(self.rucovodstvo_practikoy)
        self.rucovodstvo_VKR=validate_decimals(self.rucovodstvo_VKR)
        self.rucovodstvo_kursovoy=validate_decimals(self.rucovodstvo_kursovoy)
        self.proverka_auditor_KR=validate_decimals(self.proverka_auditor_KR)
        self.proverka_dom_KR=validate_decimals(self.proverka_dom_KR)
        self.proverka_practicuma=validate_decimals(self.proverka_practicuma)
        self.proverka_lab=validate_decimals(self.proverka_lab)
        self.priem_zashit_practic=validate_decimals(self.priem_zashit_practic)
        self.zacheti_ust=validate_decimals(self.zacheti_ust)
        self.zacheti_pism=validate_decimals(self.zacheti_pism)
        self.priem_vstupit=validate_decimals(self.priem_vstupit)
        self.ekzamenov=validate_decimals(self.ekzamenov)
        self.priem_GIA=validate_decimals(self.priem_GIA)
        self.priem_kandidtskih=validate_decimals(self.priem_kandidtskih)
        self.rucovodstvo_adunctami=validate_decimals(self.rucovodstvo_adunctami)
        self.auditor_nagruzka=validate_decimals(self.get_auditor_nagruzka())
        # print(self.auditor_nagruzka)
        self.ucheb_nagruzka=validate_decimals(self.get_obshaya_nagruzka())

        # print(self.get_obshaya_nagruzka())
        super(Predmet, self).save()
    def save1(self, *args, **kwargs):
        self.leccii=validate_decimals(self.leccii)
        self.seminar=validate_decimals(self.seminar)
        self.practici_v_gruppe=validate_decimals(self.practici_v_gruppe)
        self.practici_v_podgruppe=validate_decimals(self.practici_v_podgruppe)
        self.krugliy_stol=validate_decimals(self.krugliy_stol)
        self.konsultacii_pered_ekzamenom=validate_decimals(self.konsultacii_pered_ekzamenom)
        self.tekushie_konsultacii=validate_decimals(self.tekushie_konsultacii)
        self.vneauditor_chtenie=validate_decimals(self.vneauditor_chtenie)
        self.rucovodstvo_practikoy=validate_decimals(self.rucovodstvo_practikoy)
        self.rucovodstvo_VKR=validate_decimals(self.rucovodstvo_VKR)
        self.rucovodstvo_kursovoy=validate_decimals(self.rucovodstvo_kursovoy)
        self.proverka_auditor_KR=validate_decimals(self.proverka_auditor_KR)
        self.proverka_dom_KR=validate_decimals(self.proverka_dom_KR)
        self.proverka_practicuma=validate_decimals(self.proverka_practicuma)
        self.proverka_lab=validate_decimals(self.proverka_lab)
        self.priem_zashit_practic=validate_decimals(self.priem_zashit_practic)
        self.zacheti_ust=validate_decimals(self.zacheti_ust)
        self.zacheti_pism=validate_decimals(self.zacheti_pism)
        self.priem_vstupit=validate_decimals(self.priem_vstupit)
        self.ekzamenov=validate_decimals(self.ekzamenov)
        self.priem_GIA=validate_decimals(self.priem_GIA)
        self.priem_kandidtskih=validate_decimals(self.priem_kandidtskih)
        self.rucovodstvo_adunctami=validate_decimals(self.rucovodstvo_adunctami)
        self.auditor_nagruzka=validate_decimals(self.auditor_nagruzka)
        # print(self.auditor_nagruzka)
        self.ucheb_nagruzka=validate_decimals(self.ucheb_nagruzka)



        # print(self.get_obshaya_nagruzka())
        super(Predmet, self).save()

#учебно методическая рабoта
class UMR(models.Model):
    dubl_to_in=models.BooleanField(default=False)
    # vid=models.CharField(max_length=10000,blank=True)
    vid = models.TextField(blank=True,null=True)
    srok=models.CharField(max_length=1000,blank=True)
    otmetka=models.CharField(max_length=1000,blank=True,default='___________ Протокол №__ от __.__.20__')
    include_rating = models.BooleanField(default=False)
    prepodavatel=models.ForeignKey(Profile,related_name='umr',on_delete=models.CASCADE)
    year=models.IntegerField(default=2019)
    polugodie=models.IntegerField(default=1)
    def __str__(self):
        return self.prepodavatel.user.username+" "+self.vid
    def all_values(self):
        return  (
            str(self.vid),

            str(self.srok),
            str(self.otmetka))

    def save(self, *args, **kwargs):
        if self.dubl_to_in==True:
            inr=INR()
            inr.vid=self.vid
            inr.srok=self.srok
            inr.otmetka=self.otmetka
            inr.polugodie=self.polugodie
            inr.prepodavatel=self.prepodavatel
            inr.year=self.year
            inr.save()
        # print(self.get_obshaya_nagruzka())
        super(UMR, self).save()
 #научyно сследовательская работа
class NIR(models.Model):
    # vid=models.CharField(max_length=10000,blank=True)
    vid = models.TextField(blank=True,null=True)
    srok=models.CharField(max_length=1000,blank=True)
    otmetka=models.CharField(max_length=1000,blank=True,default='___________ Протокол №__ от __.__.20__')
    prepodavatel=models.ForeignKey(Profile,related_name='nir',on_delete=models.CASCADE)
    year=models.IntegerField(default=2019)
    polugodie=models.IntegerField(default=1)
    def __str__(self):
        return self.prepodavatel.user.username+" "+self.vid
    def all_values(self):
        return  (
            str(self.vid),

            str(self.srok),
            str(self.otmetka))
# воспитаттльная работа
class VR(models.Model):
    vid=models.CharField(max_length=10000,blank=True)
    srok=models.CharField(max_length=1000,blank=True)
    otmetka=models.CharField(max_length=1000,blank=True,default='___________ Протокол №__ от __.__.20__')
    prepodavatel=models.ForeignKey(Profile,related_name='vr',on_delete=models.CASCADE)
    year=models.IntegerField(default=2019)
    polugodie=models.IntegerField(default=1)
    def __str__(self):
        return self.prepodavatel.user.username+" "+self.vid
    def all_values(self):
        return  (
            str(self.vid),


            str(self.srok),
            str(self.otmetka))

class INR(models.Model):
    vid=models.CharField(max_length=10000,blank=True)
    srok=models.CharField(max_length=1000,blank=True)
    otmetka=models.CharField(max_length=1000,blank=True,default='___________ Протокол №__ от __.__.20__')
    prepodavatel=models.ForeignKey(Profile,related_name='inr',on_delete=models.CASCADE)
    year=models.IntegerField(default=2019)
    polugodie=models.IntegerField(default=1)
    def __str__(self):
        return self.prepodavatel.user.username+" "+self.vid
    def all_values(self):
        return  (
            str(self.vid),
            str(self.srok),
            str(self.otmetka))

class DR(models.Model):
    vid=models.CharField(max_length=10000,blank=True)
    srok=models.CharField(max_length=1000,blank=True)
    otmetka=models.CharField(max_length=1000,blank=True,default='___________ Протокол №__ от __.__.20__')
    prepodavatel=models.ForeignKey(Profile,related_name='dr',on_delete=models.CASCADE)
    year=models.IntegerField(default=2019)
    polugodie=models.IntegerField(default=1)
    def __str__(self):
        return self.prepodavatel.user.username+" "+self.vid
    def all_values(self):
        return  (
            str(self.vid),


            str(self.srok),
            str(self.otmetka))

class Mesyac(models.Model):
    name=models.CharField(max_length=250,blank=True)
    ###поля в таблице
    leccii=models.FloatField(default=0,blank=True,validators=[validate_decimals],null=True)
    seminar=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    practici_v_gruppe=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    practici_v_podgruppe=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    krugliy_stol=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    konsultacii_pered_ekzamenom=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    tekushie_konsultacii=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    vneauditor_chtenie=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    rucovodstvo_practikoy=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    rucovodstvo_VKR=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    rucovodstvo_kursovoy=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    proverka_auditor_KR=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    proverka_dom_KR=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    proverka_practicuma=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    proverka_lab=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    priem_zashit_practic=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    zacheti_ust=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    zacheti_pism=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    priem_vstupit=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    ekzamenov=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    priem_GIA=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    priem_kandidtskih=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    rucovodstvo_adunctami=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    ucheb_nagruzka=models.FloatField(default=0,blank=True,validators=[validate_decimals])
    auditor_nagruzka=models.FloatField(default=0,blank=True,validators=[validate_decimals])

    kafedra=models.ForeignKey(Kafedra, related_name='mes',on_delete=models.CASCADE)
    prepodavatel=models.ForeignKey(Profile,related_name='mes',on_delete=models.CASCADE)
    year=models.IntegerField(default=2019,blank=True)
    polugodie=models.IntegerField(default=1,blank=True)
    status=models.BooleanField(default=False,blank=True)#tru если выполена false если план

    def __str__(self):
        return self.name
    def get_arr_all(self):
        return(([self.leccii,
        self.seminar,
        self.practici_v_gruppe,
        self.practici_v_podgruppe,
        self.krugliy_stol,
        self.konsultacii_pered_ekzamenom,
        self.tekushie_konsultacii,
        self.vneauditor_chtenie,
        self.rucovodstvo_practikoy,
        self.rucovodstvo_VKR,
        self.rucovodstvo_kursovoy,
        self.proverka_auditor_KR,
        self.proverka_dom_KR,
        self.proverka_practicuma,
        self.proverka_lab,
        self.priem_zashit_practic,
        self.zacheti_ust,
        self.zacheti_pism,
        self.priem_vstupit,
        self.ekzamenov,
        self.priem_GIA,
        self.priem_kandidtskih,
        self.rucovodstvo_adunctami]))
    def get_obshaya_nagruzka(self):
        return(self.leccii+
        self.seminar+
        self.practici_v_gruppe+
        self.practici_v_podgruppe+
        self.krugliy_stol+
        self.konsultacii_pered_ekzamenom+
        self.tekushie_konsultacii+
        self.vneauditor_chtenie+
        self.rucovodstvo_practikoy+
        self.rucovodstvo_VKR+
        self.rucovodstvo_kursovoy+
        self.proverka_auditor_KR+
        self.proverka_dom_KR+
        self.proverka_practicuma+
        self.proverka_lab+
        self.priem_zashit_practic+
        self.zacheti_ust+
        self.zacheti_pism+
        self.priem_vstupit+
        self.ekzamenov+
        self.priem_GIA+
        self.priem_kandidtskih+
        self.rucovodstvo_adunctami)

    def get_auditor_nagruzka(self):
        return(self.leccii+
        self.seminar+
        self.practici_v_gruppe+
        self.practici_v_podgruppe+
        self.krugliy_stol+
        self.konsultacii_pered_ekzamenom+
        self.priem_zashit_practic+
        self.zacheti_ust+
        self.zacheti_pism+
        self.priem_vstupit+
        self.ekzamenov+
        self.priem_GIA+
        self.priem_kandidtskih)
    def __str__(self):
        return self.name

    def all_values(self):
        return(
            str(self.leccii),
            str(self.seminar),
            str(self.practici_v_gruppe),
            str(self.practici_v_podgruppe),
            str(self.krugliy_stol),
            str(self.konsultacii_pered_ekzamenom),
            str(self.tekushie_konsultacii),
            str(self.vneauditor_chtenie),
            str(self.rucovodstvo_practikoy),
            str(self.rucovodstvo_VKR),
            str(self.rucovodstvo_kursovoy),
            str(self.proverka_auditor_KR),
            str(self.proverka_dom_KR),
            str(self.proverka_practicuma),
            str(self.proverka_lab),
            str(self.priem_zashit_practic),
            str(self.zacheti_ust),
            str(self.zacheti_pism),
            str(self.priem_vstupit),
            str(self.ekzamenov),
            str(self.priem_GIA),
            str(self.priem_kandidtskih),
            str(self.rucovodstvo_adunctami),
            str(self.ucheb_nagruzka),
            str(self.auditor_nagruzka))

    def save(self, *args, **kwargs):

        self.leccii=validate_decimals(self.leccii)
        self.seminar=validate_decimals(self.seminar)
        self.practici_v_gruppe=validate_decimals(self.practici_v_gruppe)
        self.practici_v_podgruppe=validate_decimals(self.practici_v_podgruppe)
        self.krugliy_stol=validate_decimals(self.krugliy_stol)
        self.konsultacii_pered_ekzamenom=validate_decimals(self.konsultacii_pered_ekzamenom)
        self.tekushie_konsultacii=validate_decimals(self.tekushie_konsultacii)
        self.vneauditor_chtenie=validate_decimals(self.vneauditor_chtenie)
        self.rucovodstvo_practikoy=validate_decimals(self.rucovodstvo_practikoy)
        self.rucovodstvo_VKR=validate_decimals(self.rucovodstvo_VKR)
        self.rucovodstvo_kursovoy=validate_decimals(self.rucovodstvo_kursovoy)
        self.proverka_auditor_KR=validate_decimals(self.proverka_auditor_KR)
        self.proverka_dom_KR=validate_decimals(self.proverka_dom_KR)
        self.proverka_practicuma=validate_decimals(self.proverka_practicuma)
        self.proverka_lab=validate_decimals(self.proverka_lab)
        self.priem_zashit_practic=validate_decimals(self.priem_zashit_practic)
        self.zacheti_ust=validate_decimals(self.zacheti_ust)
        self.zacheti_pism=validate_decimals(self.zacheti_pism)
        self.priem_vstupit=validate_decimals(self.priem_vstupit)
        self.ekzamenov=validate_decimals(self.ekzamenov)
        self.priem_GIA=validate_decimals(self.priem_GIA)
        self.priem_kandidtskih=validate_decimals(self.priem_kandidtskih)
        self.rucovodstvo_adunctami=validate_decimals(self.rucovodstvo_adunctami)
        self.auditor_nagruzka=validate_decimals(self.get_auditor_nagruzka())
        # print(self.auditor_nagruzka)
        self.ucheb_nagruzka=validate_decimals(self.get_obshaya_nagruzka())

        # print(self.get_obshaya_nagruzka())
        super(Mesyac, self).save()
    def save1(self, *args, **kwargs):
        self.leccii=validate_decimals(self.leccii)
        self.seminar=validate_decimals(self.seminar)
        self.practici_v_gruppe=validate_decimals(self.practici_v_gruppe)
        self.practici_v_podgruppe=validate_decimals(self.practici_v_podgruppe)
        self.krugliy_stol=validate_decimals(self.krugliy_stol)
        self.konsultacii_pered_ekzamenom=validate_decimals(self.konsultacii_pered_ekzamenom)
        self.tekushie_konsultacii=validate_decimals(self.tekushie_konsultacii)
        self.vneauditor_chtenie=validate_decimals(self.vneauditor_chtenie)
        self.rucovodstvo_practikoy=validate_decimals(self.rucovodstvo_practikoy)
        self.rucovodstvo_VKR=validate_decimals(self.rucovodstvo_VKR)
        self.rucovodstvo_kursovoy=validate_decimals(self.rucovodstvo_kursovoy)
        self.proverka_auditor_KR=validate_decimals(self.proverka_auditor_KR)
        self.proverka_dom_KR=validate_decimals(self.proverka_dom_KR)
        self.proverka_practicuma=validate_decimals(self.proverka_practicuma)
        self.proverka_lab=validate_decimals(self.proverka_lab)
        self.priem_zashit_practic=validate_decimals(self.priem_zashit_practic)
        self.zacheti_ust=validate_decimals(self.zacheti_ust)
        self.zacheti_pism=validate_decimals(self.zacheti_pism)
        self.priem_vstupit=validate_decimals(self.priem_vstupit)
        self.ekzamenov=validate_decimals(self.ekzamenov)
        self.priem_GIA=validate_decimals(self.priem_GIA)
        self.priem_kandidtskih=validate_decimals(self.priem_kandidtskih)
        self.rucovodstvo_adunctami=validate_decimals(self.rucovodstvo_adunctami)
        self.auditor_nagruzka=validate_decimals(self.auditor_nagruzka)
        # print(self.auditor_nagruzka)
        self.ucheb_nagruzka=validate_decimals(self.ucheb_nagruzka)



        # print(self.get_obshaya_nagruzka())
        super(Mesyac, self).save()
