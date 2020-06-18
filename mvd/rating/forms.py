from django import forms
from django.forms import TextInput,Textarea, NumberInput
from rating.models import URR, ORMR, PCR, MRR,Rating



class URRForm(forms.ModelForm):
    class Meta:
        model=URR
        exclude = ['year','profile']
        widgets = {
        'obsh': NumberInput(attrs={"class":"form-control"}),
        'sootn': NumberInput(attrs={"class":"form-control"}),
        'zansprakt': NumberInput(attrs={"class": "form-control"}),
        'viezdsprakt': NumberInput(attrs={"class":"form-control"}),
        'ppsfp': NumberInput(attrs={"class":"form-control"}),
        'ppsdr': NumberInput(attrs={"class":"form-control"}),
        'vneaudotor': NumberInput(attrs={"class":"form-control"}),

        'obshbal':NumberInput(attrs={"class":"form-control"}),
        'zanspraktbal': NumberInput(attrs={"class": "form-control"}),
        'sootnbal':NumberInput(attrs={"class":"form-control"}),
        'viezdspraktbal':NumberInput(attrs={"class":"form-control"}),
        'ppsfpbal':NumberInput(attrs={"class":"form-control"}),
        'ppsdrbal':NumberInput(attrs={"class":"form-control"}),
        'vneaudotorbal':NumberInput(attrs={"class":"form-control"}),

        'obshpodtv': TextInput(attrs={"class":"form-control"}),
        'sootnpodtv': TextInput(attrs={"class":"form-control"}),
        'zanspraktpodtv': TextInput(attrs={"class": "form-control"}),
        'viezdspraktpodtv': TextInput(attrs={"class":"form-control"}),
        'ppsfppodtv': TextInput(attrs={"class":"form-control"}),
        'ppsdrpodtv': TextInput(attrs={"class":"form-control"}),
        'vneaudotorpodtv': TextInput(attrs={"class":"form-control"}),


        }
class ORMRForm(forms.ModelForm):
    class Meta:
        model=ORMR
        exclude = ['year','profile']
        widgets = {
                'ruksec': NumberInput(attrs={"class":"form-control"}),
                'rukpredmsek': NumberInput(attrs={"class":"form-control"}),
                'rabotaruk': NumberInput(attrs={"class":"form-control"}),
                'rabotachlen': NumberInput(attrs={"class":"form-control"}),
                'rukkafnach': NumberInput(attrs={"class":"form-control"}),
                'rukkafzam': NumberInput(attrs={"class":"form-control"}),
                'bestprepodmir': NumberInput(attrs={"class":"form-control"}),
                'bestprepodrus': NumberInput(attrs={"class":"form-control"}),
                'bestprepodreg': NumberInput(attrs={"class":"form-control"}),
                'bestprepodunik': NumberInput(attrs={"class":"form-control"}),
                'uchastiebestprepodmir': NumberInput(attrs={"class":"form-control"}),
                'uchastiebestprepodrus': NumberInput(attrs={"class":"form-control"}),
                'uchastiebestprepodreg': NumberInput(attrs={"class":"form-control"}),
                'uchastiebestprepodunik': NumberInput(attrs={"class":"form-control"}),
                'ekspert': NumberInput(attrs={"class":"form-control"}),
                'metodkonk1': NumberInput(attrs={"class":"form-control"}),
                'metodkonk1': NumberInput(attrs={"class":"form-control"}),
                'metodkonk2': NumberInput(attrs={"class":"form-control"}),
                'metodkonk3': NumberInput(attrs={"class":"form-control"}),
                'metodkonk4': NumberInput(attrs={"class": "form-control"}),
                'profmaster': NumberInput(attrs={"class":"form-control"}),
                'podgsbornmir': NumberInput(attrs={"class":"form-control"}),
                'podgsbornrus': NumberInput(attrs={"class":"form-control"}),
                'podgsbornreg': NumberInput(attrs={"class":"form-control"}),
                'podgsbornunik': NumberInput(attrs={"class":"form-control"}),
                'vulkan': NumberInput(attrs={"class":"form-control"}),
                'plenar': NumberInput(attrs={"class":"form-control"}),
                'obrprogramma': NumberInput(attrs={"class":"form-control"}),
                'proverkaf': NumberInput(attrs={"class":"form-control"}),
                'inpectunik': NumberInput(attrs={"class":"form-control"}),
                'resocenki1': NumberInput(attrs={"class":"form-control"}),
                'resocenki6': NumberInput(attrs={"class":"form-control"}),
                'resocenki11': NumberInput(attrs={"class":"form-control"}),
                'resocenki16': NumberInput(attrs={"class":"form-control"}),
                'resocenki26': NumberInput(attrs={"class":"form-control"}),
                'inovac': NumberInput(attrs={"class":"form-control"}),

                'ruksecbal': NumberInput(attrs={"class":"form-control"}),
                'rukpredmsekbal': NumberInput(attrs={"class":"form-control"}),
                'rabotarukbal': NumberInput(attrs={"class":"form-control"}),
                'rabotachlenbal': NumberInput(attrs={"class":"form-control"}),
                'rukkafnachbal': NumberInput(attrs={"class":"form-control"}),
                'rukkafzambal': NumberInput(attrs={"class":"form-control"}),
                'bestprepodmirbal': NumberInput(attrs={"class":"form-control"}),
                'bestprepodrusbal': NumberInput(attrs={"class":"form-control"}),
                'bestprepodregbal': NumberInput(attrs={"class":"form-control"}),
                'bestprepodunikbal': NumberInput(attrs={"class":"form-control"}),
                'uchastiebestprepodmirbal': NumberInput(attrs={"class":"form-control"}),
                'uchastiebestprepodrusbal': NumberInput(attrs={"class":"form-control"}),
                'uchastiebestprepodregbal': NumberInput(attrs={"class":"form-control"}),
                'uchastiebestprepodunikbal': NumberInput(attrs={"class":"form-control"}),
                'ekspertbal': NumberInput(attrs={"class":"form-control"}),
                'metodkonk1bal': NumberInput(attrs={"class":"form-control"}),
                'metodkonk1bal': NumberInput(attrs={"class":"form-control"}),
                'metodkonk2bal': NumberInput(attrs={"class":"form-control"}),
                'metodkonk3bal': NumberInput(attrs={"class":"form-control"}),
                'metodkonk4bal': NumberInput(attrs={"class": "form-control"}),
                'profmasterbal': NumberInput(attrs={"class":"form-control"}),
                'podgsbornmirbal': NumberInput(attrs={"class":"form-control"}),
                'podgsbornrusbal': NumberInput(attrs={"class":"form-control"}),
                'podgsbornregbal': NumberInput(attrs={"class":"form-control"}),
                'podgsbornunikbal': NumberInput(attrs={"class":"form-control"}),
                'vulkanbal': NumberInput(attrs={"class":"form-control"}),
                'plenarbal': NumberInput(attrs={"class":"form-control"}),
                'obrprogrammabal': NumberInput(attrs={"class":"form-control"}),
                'proverkafbal': NumberInput(attrs={"class":"form-control"}),
                'inpectunikbal': NumberInput(attrs={"class":"form-control"}),
                'resocenki1bal': NumberInput(attrs={"class":"form-control"}),
                'resocenki6bal': NumberInput(attrs={"class":"form-control"}),
                'resocenki11bal': NumberInput(attrs={"class":"form-control"}),
                'resocenki16bal': NumberInput(attrs={"class": "form-control"}),
                'resocenki26bal': NumberInput(attrs={"class": "form-control"}),
                'inovacbal': NumberInput(attrs={"class": "form-control"}),

                'ruksecpodtv': TextInput(attrs={"class":"form-control"}),
                'rukpredmsekpodtv': TextInput(attrs={"class":"form-control"}),
                'rabotarukpodtv': TextInput(attrs={"class":"form-control"}),
                'rabotachlenpodtv': TextInput(attrs={"class":"form-control"}),
                'rukkafnachpodtv': TextInput(attrs={"class":"form-control"}),
                'rukkafzampodtv': TextInput(attrs={"class":"form-control"}),
                'bestprepodmirpodtv': TextInput(attrs={"class":"form-control"}),
                'bestprepodruspodtv': TextInput(attrs={"class":"form-control"}),
                'bestprepodregpodtv': TextInput(attrs={"class":"form-control"}),
                'bestprepodunikpodtv': TextInput(attrs={"class":"form-control"}),
                'uchastiebestprepodmirpodtv': TextInput(attrs={"class":"form-control"}),
                'uchastiebestprepodruspodtv': TextInput(attrs={"class":"form-control"}),
                'uchastiebestprepodregpodtv': TextInput(attrs={"class":"form-control"}),
                'uchastiebestprepodunikpodtv': TextInput(attrs={"class":"form-control"}),
                'ekspertpodtv': TextInput(attrs={"class":"form-control"}),
                'metodkonk1podtv': TextInput(attrs={"class":"form-control"}),
                'metodkonk1podtv': TextInput(attrs={"class":"form-control"}),
                'metodkonk2podtv': TextInput(attrs={"class":"form-control"}),
                'metodkonk3podtv': TextInput(attrs={"class":"form-control"}),
                'metodkonk4podtv': TextInput(attrs={"class": "form-control"}),
                'profmasterpodtv': TextInput(attrs={"class":"form-control"}),
                'podgsbornmirpodtv': TextInput(attrs={"class":"form-control"}),
                'podgsbornruspodtv': TextInput(attrs={"class":"form-control"}),
                'podgsbornregpodtv': TextInput(attrs={"class":"form-control"}),
                'podgsbornunikpodtv': TextInput(attrs={"class":"form-control"}),
                'vulkanpodtv': TextInput(attrs={"class":"form-control"}),
                'plenarpodtv': TextInput(attrs={"class":"form-control"}),
                'obrprogrammapodtv': TextInput(attrs={"class":"form-control"}),
                'proverkafpodtv': TextInput(attrs={"class":"form-control"}),
                'inpectunikpodtv': TextInput(attrs={"class":"form-control"}),
                'resocenki1podtv': TextInput(attrs={"class":"form-control"}),
                'resocenki6podtv': TextInput(attrs={"class":"form-control"}),
                'resocenki11podtv': TextInput(attrs={"class":"form-control"}),
                'resocenki16podtv': TextInput(attrs={"class":"form-control"}),
                'resocenki26podtv': TextInput(attrs={"class":"form-control"}),
                'inovacpodtv': TextInput(attrs={"class":"form-control"}),

        }
class PCRForm(forms.ModelForm):
    class Meta:
        model=PCR
        exclude = ['year','profile']
        widgets = {
            'otkr': NumberInput(attrs={"class":"form-control"}),
            'kontrud': NumberInput(attrs={"class": "form-control"}),
            'kontrneud': NumberInput(attrs={"class": "form-control"}),
            'sriv': NumberInput(attrs={"class": "form-control"}),
            'opozdanie': NumberInput(attrs={"class": "form-control"}),

            'otkrbal': NumberInput(attrs={"class": "form-control"}),
            'kontrudbal': NumberInput(attrs={"class": "form-control"}),
            'kontrneudbal': NumberInput(attrs={"class": "form-control"}),
            'srivbal': NumberInput(attrs={"class": "form-control"}),
            'opozdaniebal': NumberInput(attrs={"class": "form-control"}),

            'otkrpodtv': TextInput(attrs={"class":"form-control"}),
            'kontrudpodtv': TextInput(attrs={"class": "form-control"}),
            'kontrneudpodtv': TextInput(attrs={"class": "form-control"}),
            'srivpodtv': TextInput(attrs={"class": "form-control"}),
            'opozdaniepodtv': TextInput(attrs={"class": "form-control"}),


        }
class MRRForm(forms.ModelForm):
    class Meta:
        model=MRR
        exclude = ['year','profile']
        widgets = {
            'soavtr': NumberInput(attrs={"class":"form-control"}),
            'bal': NumberInput(attrs={"class": "form-control"}),
            'name': TextInput(attrs={"class": "form-control"}),
        }