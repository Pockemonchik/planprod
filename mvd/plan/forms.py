from django import forms
from plan.models import Predmet, NIR, VR, DR, UMR, Plan, INR, Nagruzka, DocInfo, ProfileInfo
from django.forms import TextInput, Textarea, NumberInput, FileInput


class UserAddForm(forms.Form):
    fio = forms.CharField(max_length=100)
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)


class ChangePassForm(forms.Form):
    fio = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=50)


class SuperSearch(forms.widgets.TextInput):
    class Media:
        js = ("js/SuperSearch.js")

        css = ("css/SuperSearch.css")


# форма для предметов



class NagruzkaForm(forms.ModelForm):
    class Meta:
        model = Nagruzka
        fields = ['document', 'year', 'status']


class Table1UploadForm(forms.ModelForm):
    class Meta:
        model = Predmet
        exclude = ['kafedra', 'prepodavatel', 'year', 'polugodie', 'status',
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


class docUploadForm(forms.Form):
    file = forms.FileField()
    widgets = {
        'file': FileInput(attrs={'class': 'custom-file-input', 'id': 'inputGroupFile01'}),
    }


class MainTableForm(forms.ModelForm):
    class Meta:
        model = Plan
        exclude = ['prepod', 'year', 'name', 'document']


class ProfileInfoForm(forms.ModelForm):
    class Meta:
        model = ProfileInfo
        exclude = ['profile', ]
        widgets = {

            'fio': TextInput(attrs={'class': 'form-control', 'placeholder': 'Петрова Петра Петровича'}),
            'dolznost': TextInput(attrs={'class': 'form-control', 'placeholder': 'начальник кафедры'}),
            'kafedra': TextInput(attrs={'class': 'form-control', 'placeholder': 'кафедры административного права'}),
            'visluga': NumberInput(attrs={'class': 'form-control', 'placeholder': '6'}),
            'uchzv': TextInput(attrs={'class': 'form-control', 'placeholder': 'доцент'}),
            'uchst': TextInput(attrs={'class': 'form-control', 'placeholder': 'д.э.н.'}),
            'stavka': NumberInput(attrs={'class': 'form-control', 'placeholder': '0.5'}),
        }


"""Формы основных таблиц"""


class ShapkaForm(forms.ModelForm):
    class Meta:
        model = DocInfo
        exclude = ['plan']
        widgets = {
            'shapka': TextInput(attrs={'placeholder':
                                           'Начальник кафедры административного права МосУ МВД России имени В.Я. Кикотя полковник полиции',
                                       'class': 'form-control',
                                       'id': 'address2'}),
            'fionach': TextInput(attrs={'placeholder': 'И.И.Иванов', 'class': 'form-control',
                                        'id': 'address2'}),
            'data': TextInput(attrs={'placeholder': '31 февраля 2019', 'class': 'form-control',
                                     'id': 'address'}),
            'na_kakoygod': TextInput(attrs={'placeholder': '2019', 'class': 'form-control',
                                            'id': 'address'}),
            'na_kakoygod1': TextInput(attrs={'placeholder': '2020', 'class': 'form-control',
                                             'id': 'address'}),
            'fio': TextInput(attrs={'placeholder': 'Петрова Петра Петровича'}),
            'dolznost': TextInput(attrs={'placeholder': 'начальник кафедры'}),
            'kafedra': TextInput(attrs={'placeholder': 'кафедры административного права'}),
            'visluga': TextInput(attrs={'placeholder': '6'}),
            'uchzv': TextInput(attrs={'placeholder': 'доцент'}),
            'uchst': TextInput(attrs={'placeholder': 'д.э.н.'}),
            'stavka': TextInput(attrs={'placeholder': '0.5'}),

        }


class MesyacForm(forms.ModelForm):
    class Meta:
        model = Predmet
        exclude = ['kafedra', 'prepodavatel', 'year', 'polugodie', 'status']
        widgets = {
            'name': Textarea(
                attrs={'class': 'form-control', 'spellcheck': 'true', 'readonly': 'readonly', 'rows': '2', }),
            'leccii': NumberInput(attrs={'class': 'form-control'}),
            'seminar': NumberInput(attrs={'class': 'form-control'}),
            'practici_v_gruppe': NumberInput(attrs={'class': 'form-control'}),
            'practici_v_podgruppe': NumberInput(attrs={'class': 'form-control'}),
            'krugliy_stol': NumberInput(attrs={'class': 'form-control'}),
            'konsultacii_pered_ekzamenom': NumberInput(attrs={'class': 'form-control'}),
            'tekushie_konsultacii': NumberInput(attrs={'class': 'form-control'}),
            'vneauditor_chtenie': NumberInput(attrs={'class': 'form-control'}),
            'rucovodstvo_practikoy': NumberInput(attrs={'class': 'form-control'}),
            'rucovodstvo_VKR': NumberInput(attrs={'class': 'form-control'}),
            'rucovodstvo_kursovoy': NumberInput(attrs={'class': 'form-control'}),
            'proverka_auditor_KR': NumberInput(attrs={'class': 'form-control'}),
            'proverka_dom_KR': NumberInput(attrs={'class': 'form-control'}),
            'proverka_practicuma': NumberInput(attrs={'class': 'form-control'}),
            'proverka_lab': NumberInput(attrs={'class': 'form-control'}),
            'priem_zashit_practic': NumberInput(attrs={'class': 'form-control'}),
            'zacheti_ust': NumberInput(attrs={'class': 'form-control'}),
            'zacheti_pism': NumberInput(attrs={'class': 'form-control'}),
            'priem_vstupit': NumberInput(attrs={'class': 'form-control'}),
            'ekzamenov': NumberInput(attrs={'class': 'form-control'}),
            'priem_GIA': NumberInput(attrs={'class': 'form-control'}),
            'priem_kandidtskih': NumberInput(attrs={'class': 'form-control'}),
            'rucovodstvo_adunctami': NumberInput(attrs={'class': 'form-control'}),
            'ucheb_nagruzka': NumberInput(attrs={'class': 'form-control', 'name': 'uchnagr'}),
            'auditor_nagruzka': NumberInput(attrs={'class': 'form-control', 'name': 'aunagr'})
        }

    class Media:
        js = ("js/shaper.js")


class Table1Form(forms.ModelForm):
    class Meta:
        model = Predmet
        exclude = ['kafedra', 'prepodavatel', 'year', 'polugodie', 'status']
        widgets = {
            'name': Textarea(attrs={'class': 'form-control with-important', 'spellcheck': 'true', 'rows': '2', }),
            'leccii': NumberInput(attrs={'class': 'form-control'}),
            'seminar': NumberInput(attrs={'class': 'form-control'}),
            'practici_v_gruppe': NumberInput(attrs={'class': 'form-control'}),
            'practici_v_podgruppe': NumberInput(attrs={'class': 'form-control'}),
            'krugliy_stol': NumberInput(attrs={'class': 'form-control'}),
            'konsultacii_pered_ekzamenom': NumberInput(attrs={'class': 'form-control'}),
            'tekushie_konsultacii': NumberInput(attrs={'class': 'form-control'}),
            'vneauditor_chtenie': NumberInput(attrs={'class': 'form-control'}),
            'rucovodstvo_practikoy': NumberInput(attrs={'class': 'form-control'}),
            'rucovodstvo_VKR': NumberInput(attrs={'class': 'form-control'}),
            'rucovodstvo_kursovoy': NumberInput(attrs={'class': 'form-control'}),
            'proverka_auditor_KR': NumberInput(attrs={'class': 'form-control'}),
            'proverka_dom_KR': NumberInput(attrs={'class': 'form-control'}),
            'proverka_practicuma': NumberInput(attrs={'class': 'form-control'}),
            'proverka_lab': NumberInput(attrs={'class': 'form-control'}),
            'priem_zashit_practic': NumberInput(attrs={'class': 'form-control'}),
            'zacheti_ust': NumberInput(attrs={'class': 'form-control'}),
            'zacheti_pism': NumberInput(attrs={'class': 'form-control'}),
            'priem_vstupit': NumberInput(attrs={'class': 'form-control'}),
            'ekzamenov': NumberInput(attrs={'class': 'form-control'}),
            'priem_GIA': NumberInput(attrs={'class': 'form-control'}),
            'priem_kandidtskih': NumberInput(attrs={'class': 'form-control'}),
            'rucovodstvo_adunctami': NumberInput(attrs={'class': 'form-control'}),
            'ucheb_nagruzka': NumberInput(attrs={'class': 'form-control', 'name': 'uchnagr'}),
            'auditor_nagruzka': NumberInput(attrs={'class': 'form-control', 'name': 'aunagr'})
        }

    class Media:
        js = ("js/shaper.js")


# формы для нир умр
class Table2Form(forms.ModelForm):
    class Meta:
        model = UMR
        exclude = ['prepodavatel', 'year', 'polugodie']
        widgets = {
            'vid': Textarea(attrs={'id': 'lang', 'class': 'form-control', 'spellcheck': 'true', 'rows': '2'}),
            'otmetka': TextInput(attrs={'class': 'form-control', }),
            'srok': TextInput(attrs={'class': 'form-control', 'id': 'mes'})
        }


class Table3Form(forms.ModelForm):
    class Meta:
        model = NIR
        exclude = ['prepodavatel', 'year', 'polugodie']
        widgets = {
            'vid': Textarea(attrs={'id': 'lang', 'class': 'form-control', 'spellcheck': 'true', 'rows': '2'}),
            'otmetka': TextInput(attrs={'class': 'form-control', }),
            'srok': TextInput(attrs={'class': 'form-control', 'id': 'mes'})
        }


# форма для других видов и вр
class Table4Form(forms.ModelForm):
    class Meta:
        model = VR
        exclude = ['prepodavatel', 'year', 'polugodie']
        widgets = {
            'vid': Textarea(attrs={'id': 'lang', 'class': 'form-control', 'spellcheck': 'true', 'rows': '2'}),
            'otmetka': TextInput(attrs={'class': 'form-control', }),
            'srok': TextInput(attrs={'class': 'form-control', 'id': 'mes'})
        }


class Table5Form(forms.ModelForm):
    class Meta:
        model = DR
        exclude = ['prepodavatel', 'year', 'polugodie']
        widgets = {
            'vid': Textarea(attrs={'id': 'lang', 'class': 'form-control', 'spellcheck': 'true', 'rows': '2'}),
            'otmetka': TextInput(attrs={'class': 'form-control', }),
            'srok': TextInput(attrs={'class': 'form-control', 'id': 'mes'})
        }


class Table6Form(forms.ModelForm):
    class Meta:
        model = INR
        exclude = ['prepodavatel', 'year', 'polugodie']
        widgets = {
            'vid': Textarea(attrs={'id': 'lang', 'class': 'form-control', 'spellcheck': 'true', 'rows': '2'}),
            'otmetka': TextInput(attrs={'class': 'form-control', }),
            'srok': TextInput(attrs={'class': 'form-control', 'id': 'mes'})
        }
