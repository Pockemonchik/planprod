from django.db import models
from django.contrib.auth.models import User
from django.conf.urls import url
from django.urls import reverse
# Create your models here.
 #кафедра
#талица для записи инфы о преподе в документ



class Kafedra(models.Model):
     name=models.CharField(max_length=501)
     fullname=models.CharField(max_length=250,blank=True)
     def __str__(self):
         return self.fullname
#модель учебной нагррузки
class Nagruzka(models.Model):
     year=models.IntegerField(default=2019)
     kafedra=models.ForeignKey(Kafedra, related_name='nagruzki',on_delete=models.CASCADE)
     document=models.FileField(upload_to='files',default='settings.MEDIA_ROOT/plan.docx')
     def __str__(self):
         return "Нагрузка по кафедре "+str(self.kafedra.fullname)+" "+str(self.year)
#профили пользователей
class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile',on_delete="cascade",primary_key=True)
    kafedra=models.ForeignKey(Kafedra, related_name='prepods',on_delete=models.CASCADE)
    dolzhnost=models.CharField(max_length=500,blank=True)
    fullname=models.CharField(max_length=250,blank=True)
    stepen=models.CharField(max_length=250,blank=True)
    #право доступа, 1- обычный пользователь 2-привелигированный
    role = models.IntegerField(default=1)
    status=models.BooleanField(default=True)
    def __str__(self):
        return self.fullname+" "+self.user.username+" "+self.user.email

#  основная модель плана
class Plan(models.Model):
    name=models.CharField(max_length=250,default='plan')
    year=models.IntegerField(default=2019)
    prepod=models.ForeignKey(Profile,related_name='plans',on_delete=models.CASCADE,default='')
    document=models.FileField(upload_to='media',default='settings.MEDIA_ROOT/plan.docx')
    ucheb_r_1_p=models.FloatField(default=0)
    ucheb_r_2_p=models.FloatField(default=0)
    PROGRESS=(
        ('Выполнена', 'Выполнена'),
        ('Выполнена', 'Выполнена частично'),
        ('Выполнена', 'Не выполнена'))

    ucheb_med_r_1_p=models.CharField(max_length=20,choices=PROGRESS,default="Выполнена")
    ucheb_med_r_2_p=models.CharField(max_length=20,choices=PROGRESS,default="Выполнена")
    nir_1_p=models.CharField(max_length=20,choices=PROGRESS,default="Выполнена")
    nir_1_p=models.CharField(max_length=20,choices=PROGRESS,default="Выполнена")
    nir_2_p=models.CharField(max_length=20,choices=PROGRESS,default="Выполнена")
    vr_1_p=models.CharField(max_length=20,choices=PROGRESS,default="Выполнена")
    vr_2_p=models.CharField(max_length=20,choices=PROGRESS,default="Выполнена")
    inr_1_p=models.CharField(max_length=20,choices=PROGRESS,default="Выполнена")
    inr_2_p=models.CharField(max_length=20,choices=PROGRESS,default="Выполнена")
    dr_1_p=models.CharField(max_length=20,choices=PROGRESS,default="Выполнена")
    dr_2_p=models.CharField(max_length=20,choices=PROGRESS,default="Выполнена")
    def __str__(self):
        return self.name+" "+str(self.year)
    def all_values(self):
        return (
            str(self.ucheb_r_1_p),
            str(self.ucheb_r_2_p),
            str(self.ucheb_med_r_1_p),
            str(self.ucheb_med_r_2_p),
            str(self.nir_1_p),
            str(self.nir_2_p),
            str(self.vr_1_p),
            str(self.vr_2_p),
            str(self.dr_1_p),
            str(self.dr_2_p),
            str(self.inr_1_p),
            str(self.inr_2_p))

class DocInfo(models.Model):
    shapka=models.CharField(max_length=250,blank=True)
    fionach=models.CharField(max_length=250,blank=True)
    data=models.CharField(max_length=250,blank=True)
    na_kakoygod=models.IntegerField(default=2019,blank=True)
    na_kakoygod1=models.IntegerField(default=2020,blank=True)
    fio=models.CharField(max_length=250,blank=True)
    dolznost=models.CharField(max_length=250,blank=True)
    stavka=models.FloatField(default=0,blank=True)
    uchzv=models.CharField(max_length=250,blank=True)
    uchst=models.CharField(max_length=250,blank=True)
    visluga=models.IntegerField(default=0,blank=True)
    kafedra=models.CharField(max_length=250,blank=True)
    plan=models.OneToOneField(Plan,related_name='shapka',on_delete="cascade",primary_key=True)
    def all_values(self):
        return([
        self.shapka,
        self.fionach,
        self.data,
        'На '+str(self.na_kakoygod)+' / '+str(self.na_kakoygod1)+' учебный год',
        self.fio,
        self.dolznost+', '+str(self.stavka)+' ст.',
        self.kafedra,
        self.uchst+', '+self.uchzv+', '+str(self.visluga)
        ])
    def __str__(self):
        return self.plan.name


class Predmet(models.Model):
    name=models.CharField(max_length=250,blank=True)
    ###поля в таблице
    leccii=models.IntegerField(default=0,blank=True)
    seminar=models.IntegerField(default=0,blank=True)
    practici_v_gruppe=models.IntegerField(default=0,blank=True)
    practici_v_podgruppe=models.IntegerField(default=0,blank=True)
    krugliy_stol=models.IntegerField(default=0,blank=True)
    konsultacii_pered_ekzamenom=models.IntegerField(default=0,blank=True)
    tekushie_konsultacii=models.IntegerField(default=0,blank=True)
    vneauditor_chtenie=models.IntegerField(default=0,blank=True)
    rucovodstvo_practikoy=models.IntegerField(default=0,blank=True)
    rucovodstvo_VKR=models.IntegerField(default=0,blank=True)
    rucovodstvo_kursovoy=models.IntegerField(default=0,blank=True)
    proverka_auditor_KR=models.IntegerField(default=0,blank=True)
    proverka_dom_KR=models.IntegerField(default=0,blank=True)
    proverka_practicuma=models.IntegerField(default=0,blank=True)
    proverka_lab=models.IntegerField(default=0,blank=True)
    priem_zashit_practic=models.IntegerField(default=0,blank=True)
    zacheti_ust=models.IntegerField(default=0,blank=True)
    zacheti_pism=models.IntegerField(default=0,blank=True)
    priem_vstupit=models.IntegerField(default=0,blank=True)
    ekzamenov=models.IntegerField(default=0,blank=True)
    priem_GIA=models.IntegerField(default=0,blank=True)
    priem_kandidtskih=models.IntegerField(default=0,blank=True)
    rucovodstvo_adunctami=models.IntegerField(default=0,blank=True)
    ucheb_nagruzka=models.IntegerField(default=0,blank=True)
    auditor_nagruzka=models.IntegerField(default=0,blank=True)

    kafedra=models.ForeignKey(Kafedra, related_name='predmets',on_delete=models.CASCADE)
    prepodavatel=models.ForeignKey(Profile,related_name='predmets',on_delete=models.CASCADE)
    year=models.IntegerField(default=2019,blank=True)
    polugodie=models.IntegerField(default=1,blank=True)
    status=models.BooleanField(default=False,blank=True)#tru если выполена false если план
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
        return self.name
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
        self.ucheb_nagruzka=self.get_obshaya_nagruzka()
        # print(self.get_obshaya_nagruzka())
        super(Predmet, self).save()



#учебно методическая рабoта
class UMR(models.Model):
    vid=models.CharField(max_length=500,blank=True)
    srok=models.CharField(max_length=500,blank=True)
    otmetka=models.CharField(max_length=500,blank=True)
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
 #научyно сследовательская работа
class NIR(models.Model):
    vid=models.CharField(max_length=500,blank=True)
    srok=models.CharField(max_length=500,blank=True)
    otmetka=models.CharField(max_length=500,blank=True)
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
    vid=models.CharField(max_length=500,blank=True)
    srok=models.CharField(max_length=500,blank=True)
    otmetka=models.CharField(max_length=500,blank=True)
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
    vid=models.CharField(max_length=500,blank=True)
    srok=models.CharField(max_length=500,blank=True)
    otmetka=models.CharField(max_length=500,blank=True)
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
    vid=models.CharField(max_length=500,blank=True)
    srok=models.CharField(max_length=500,blank=True)
    otmetka=models.CharField(max_length=500,blank=True)
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
