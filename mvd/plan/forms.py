from django import forms
from plan.models import Predmet,NIR,VR,DR,UMR,Plan,INR,Nagruzka,DocInfo
from django.forms import TextInput,Textarea

class ShapkaForm(forms.ModelForm):
    class Meta:
        model=DocInfo
        exclude = ['plan']

class SuperSearch(forms.widgets.TextInput):
    class Media:
        js = ("js/SuperSearch.js")

        css = ("css/SuperSearch.css")
#форма для предметов
class MAinTableForm(forms.ModelForm):
    class Meta:
        model=Plan
        exclude = ['prepod','year','name','document','name']

class NagruzkaForm(forms.ModelForm):
    class Meta:
        model=Nagruzka
        fields = ['document','year']


class Table1UploadForm(forms.ModelForm):
    class Meta:
        model=Predmet
        exclude = ['kafedra','prepodavatel','year','polugodie','status',
        'proverka_auditor_KR',
        'proverka_dom_KR',
        'proverka_practicuma',
        'proverka_lab',
        'priem_zashit_practic',
        'zacheti',
        'priem_vstupit',
        'ekzamenov',
        'priem_GIA',
        'priem_kandidtskih',
        'rucovodstvo_adunctami']

class Table1Form(forms.ModelForm):
    class Meta:
        model=Predmet
        exclude = ['kafedra','prepodavatel','year','polugodie','status']
        widgets = {
            'name':Textarea(attrs={'class':'textpole'}),
            'leccii':TextInput(attrs={'class':'thshki'}),
            'seminar':TextInput(attrs={'class':'thshki'}),
            'practici_v_gruppe':TextInput(attrs={'class':'thshki'}),
            'practici_v_podgruppe':TextInput(attrs={'class':'thshki'}),
            'krugliy_stol':TextInput(attrs={'class':'thshki'}),
            'konsultacii_pered_ekzamenom':TextInput(attrs={'class':'thshki'}),
            'tekushie_konsultacii':TextInput(attrs={'class':'thshki'}),
            'vneauditor_chtenie':TextInput(attrs={'class':'thshki'}),
            'rucovodstvo_practikoy':TextInput(attrs={'class':'thshki'}),
            'rucovodstvo_VKR':TextInput(attrs={'class':'thshki'}),
            'rucovodstvo_kursovoy':TextInput(attrs={'class':'thshki'}),
            'proverka_auditor_KR':TextInput(attrs={'class':'thshki'}),
            'proverka_dom_KR':TextInput(attrs={'class':'thshki'}),
            'proverka_practicuma':TextInput(attrs={'class':'thshki'}),
            'proverka_lab':TextInput(attrs={'class':'thshki'}),
            'priem_zashit_practic':TextInput(attrs={'class':'thshki'}),
            'zacheti_ust':TextInput(attrs={'class':'thshki'}),
            'zacheti_pism':TextInput(attrs={'class':'thshki'}),
            'priem_vstupit':TextInput(attrs={'class':'thshki'}),
            'ekzamenov':TextInput(attrs={'class':'thshki'}),
            'priem_GIA':TextInput(attrs={'class':'thshki'}),
            'priem_kandidtskih':TextInput(attrs={'class':'thshki'}),
            'rucovodstvo_adunctami':TextInput(attrs={'class':'thshki'}),
            'ucheb_nagruzka':TextInput(attrs={'class':'thshki'}),
            'auditor_nagruzka':TextInput(attrs={'class':'thshki'})
        }
    class Media:
        js = ("js/shaper.js")
 #формы для нир умр
class Table2Form(forms.ModelForm):
    class Meta:
        model=UMR
        exclude = ['prepodavatel','year','polugodie']
        widgets = {
        'vid':TextInput(attrs={'id':'lang'})
        }

class Table3Form(forms.ModelForm):
    class Meta:
        model=NIR
        exclude = ['prepodavatel','year','polugodie']
        widgets = {
        'vid':TextInput(attrs={'id':'lang'})
        }

#форма для других видов и вр
class Table4Form(forms.ModelForm):
    class Meta:
        model=VR
        exclude = ['prepodavatel','year','polugodie']
        widgets = {
        'vid':TextInput(attrs={'id':'lang'})
        }

class Table5Form(forms.ModelForm):
    class Meta:
        model=DR
        exclude = ['prepodavatel','year','polugodie']
        widgets = {
        'vid':TextInput(attrs={'id':'lang'})
        }

class Table6Form(forms.ModelForm):
    class Meta:
        model=INR
        exclude = ['prepodavatel','year','polugodie']
        widgets = {
        'vid':TextInput(attrs={'id':'lang'})
        }
