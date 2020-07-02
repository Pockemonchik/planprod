from django import forms
from django.forms import TextInput,Textarea, NumberInput
from rating.models import URR, ORMR, PCR, MRR,Rating



class URRForm(forms.ModelForm):
    class Meta:
        model=URR
        exclude = ['year','profile']
        widgets = {
        'obsh': NumberInput(attrs={"class":"form-control", "v-model":"obsh"}),
        'sootn': NumberInput(attrs={"class":"form-control", "v-model":"sootn"}),
        'zansprakt': NumberInput(attrs={"class": "form-control", "v-model":"zansprakt"}),
        'viezdsprakt': NumberInput(attrs={"class":"form-control", "v-model":"viezdsprakt"}),
        'ppsfp': NumberInput(attrs={"class":"form-control", "v-model":"ppsfp"}),
        'ppsdr': NumberInput(attrs={"class":"form-control", "v-model":"ppsdr"}),
        'vneaudotor': NumberInput(attrs={"class":"form-control", "v-model":"vneaudotor"}),


        'obshbal':NumberInput(attrs={"class":"form-control", "v-model":"obshbal"}),
        'sootnbal':NumberInput(attrs={"class":"form-control", "v-model":"sootnbal"}),
        'zanspraktbal': NumberInput(attrs={"class": "form-control", "v-model":"zanspraktbal"}),
        'viezdspraktbal':NumberInput(attrs={"class":"form-control", "v-model":"viezdspraktbal"}),
        'ppsfpbal':NumberInput(attrs={"class":"form-control", "v-model":"ppsfpbal"}),
        'ppsdrbal':NumberInput(attrs={"class":"form-control", "v-model":"ppsdrbal"}),
        'vneaudotorbal':NumberInput(attrs={"class":"form-control", "v-model":"vneaudotorbal"}),

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
                'ruksec': NumberInput(attrs={"class":"form-control", "v-model":"ruksec"}),
                'rukpredmsek': NumberInput(attrs={"class":"form-control", "v-model":"rukpredmsek"}),
                'rabotaruk': NumberInput(attrs={"class":"form-control", "v-model":"rabotaruk"}),
                'rabotachlen': NumberInput(attrs={"class":"form-control", "v-model":"rabotachlen"}),
                'rukkafnach': NumberInput(attrs={"class":"form-control", "v-model":"rukkafnach"}),
                'rukkafzam': NumberInput(attrs={"class":"form-control", "v-model":"rukkafzam"}),
                'bestprepodmir': NumberInput(attrs={"class":"form-control", "v-model":"bestprepodmir"}),
                'bestprepodrus': NumberInput(attrs={"class":"form-control", "v-model":"bestprepodrus"}),
                'bestprepodreg': NumberInput(attrs={"class":"form-control", "v-model":"bestprepodreg"}),
                'bestprepodunik': NumberInput(attrs={"class":"form-control", "v-model":"bestprepodunik"}),
                'uchastiebestprepodmir': NumberInput(attrs={"class":"form-control", "v-model":"uchastiebestprepodmir"}),
                'uchastiebestprepodrus': NumberInput(attrs={"class":"form-control", "v-model":"uchastiebestprepodrus"}),
                'uchastiebestprepodreg': NumberInput(attrs={"class":"form-control", "v-model":"uchastiebestprepodreg"}),
                'uchastiebestprepodunik': NumberInput(attrs={"class":"form-control", "v-model":"uchastiebestprepodunik"}),
                'ekspert': NumberInput(attrs={"class":"form-control", "v-model":"ekspert"}),
                'metodkonk1': NumberInput(attrs={"class":"form-control", "v-model":"metodkonk1"}),
                'metodkonk2': NumberInput(attrs={"class":"form-control", "v-model":"metodkonk2"}),
                'metodkonk3': NumberInput(attrs={"class":"form-control", "v-model":"metodkonk3"}),
                'metodkonk4': NumberInput(attrs={"class": "form-control", "v-model":"metodkonk4"}),
                'profmaster': NumberInput(attrs={"class":"form-control", "v-model":"profmaster"}),
                'podgsbornmir': NumberInput(attrs={"class":"form-control", "v-model":"podgsbornmir"}),
                'podgsbornrus': NumberInput(attrs={"class":"form-control", "v-model":"podgsbornrus"}),
                'podgsbornreg': NumberInput(attrs={"class":"form-control", "v-model":"podgsbornreg"}),
                'podgsbornunik': NumberInput(attrs={"class":"form-control", "v-model":"podgsbornunik"}),
                'vulkan': NumberInput(attrs={"class":"form-control", "v-model":"vulkan"}),
                'plenar': NumberInput(attrs={"class":"form-control", "v-model":"plenar"}),
                'obrprogramma': NumberInput(attrs={"class":"form-control", "v-model":"obrprogramma"}),
                'proverkaf': NumberInput(attrs={"class":"form-control", "v-model":"proverkaf"}),
                'inpectunik': NumberInput(attrs={"class":"form-control", "v-model":"inpectunik"}),
                'resocenki1': NumberInput(attrs={"class":"form-control", "v-model":"resocenki1"}),
                'resocenki6': NumberInput(attrs={"class":"form-control", "v-model":"resocenki6"}),
                'resocenki11': NumberInput(attrs={"class":"form-control", "v-model":"resocenki11"}),
                'resocenki16': NumberInput(attrs={"class":"form-control", "v-model":"resocenki16"}),
                'resocenki26': NumberInput(attrs={"class":"form-control", "v-model":"resocenki26"}),
                'inovac': NumberInput(attrs={"class":"form-control", "v-model":"inovac"}),


                'ruksecbal': NumberInput(attrs={"class":"form-control", "v-model":"ruksecbal"}),
                'rukpredmsekbal': NumberInput(attrs={"class":"form-control", "v-model":"rukpredmsekbal"}),
                'rabotarukbal': NumberInput(attrs={"class":"form-control", "v-model":"rabotarukbal"}),
                'rabotachlenbal': NumberInput(attrs={"class":"form-control", "v-model":"rabotachlenbal"}),
                'rukkafnachbal': NumberInput(attrs={"class":"form-control", "v-model":"rukkafnachbal"}),
                'rukkafzambal': NumberInput(attrs={"class":"form-control", "v-model":"rukkafzambal"}),
                'bestprepodmirbal': NumberInput(attrs={"class":"form-control", "v-model":"bestprepodmirbal"}),
                'bestprepodrusbal': NumberInput(attrs={"class":"form-control", "v-model":"bestprepodrusbal"}),
                'bestprepodregbal': NumberInput(attrs={"class":"form-control", "v-model":"bestprepodregbal"}),
                'bestprepodunikbal': NumberInput(attrs={"class":"form-control", "v-model":"bestprepodunikbal"}),
                'uchastiebestprepodmirbal': NumberInput(attrs={"class":"form-control", "v-model":"uchastiebestprepodmirbal"}),
                'uchastiebestprepodrusbal': NumberInput(attrs={"class":"form-control", "v-model":"uchastiebestprepodrusbal"}),
                'uchastiebestprepodregbal': NumberInput(attrs={"class":"form-control", "v-model":"uchastiebestprepodregbal"}),
                'uchastiebestprepodunikbal': NumberInput(attrs={"class":"form-control", "v-model":"uchastiebestprepodunikbal"}),
                'ekspertbal': NumberInput(attrs={"class":"form-control", "v-model":"ekspertbal"}),
                'metodkonk1bal': NumberInput(attrs={"class":"form-control", "v-model":"metodkonk1bal"}),
                'metodkonk2bal': NumberInput(attrs={"class":"form-control", "v-model":"metodkonk2bal"}),
                'metodkonk3bal': NumberInput(attrs={"class":"form-control", "v-model":"metodkonk3bal"}),
                'metodkonk4bal': NumberInput(attrs={"class": "form-control", "v-model":"metodkonk4bal"}),
                'profmasterbal': NumberInput(attrs={"class":"form-control", "v-model":"profmasterbal"}),
                'podgsbornmirbal': NumberInput(attrs={"class":"form-control", "v-model":"podgsbornmirbal"}),
                'podgsbornrusbal': NumberInput(attrs={"class":"form-control", "v-model":"podgsbornrusbal"}),
                'podgsbornregbal': NumberInput(attrs={"class":"form-control", "v-model":"podgsbornregbal"}),
                'podgsbornunikbal': NumberInput(attrs={"class":"form-control", "v-model":"podgsbornunikbal"}),
                'vulkanbal': NumberInput(attrs={"class":"form-control", "v-model":"vulkanbal"}),
                'plenarbal': NumberInput(attrs={"class":"form-control", "v-model":"plenarbal"}),
                'obrprogrammabal': NumberInput(attrs={"class":"form-control", "v-model":"obrprogrammabal"}),
                'proverkafbal': NumberInput(attrs={"class":"form-control", "v-model":"proverkafbal"}),
                'inpectunikbal': NumberInput(attrs={"class":"form-control", "v-model":"inpectunikbal"}),
                'resocenki1bal': NumberInput(attrs={"class":"form-control", "v-model":"resocenki1bal"}),
                'resocenki6bal': NumberInput(attrs={"class":"form-control", "v-model":"resocenki6bal"}),
                'resocenki11bal': NumberInput(attrs={"class":"form-control", "v-model":"resocenki11bal"}),
                'resocenki16bal': NumberInput(attrs={"class": "form-control", "v-model":"resocenki16bal"}),
                'resocenki26bal': NumberInput(attrs={"class": "form-control", "v-model":"resocenki26bal"}),
                'inovacbal': NumberInput(attrs={"class": "form-control", "v-model":"inovacbal"}),

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
            'otkr': NumberInput(attrs={"class":"form-control", "v-model":"otkr"}),
            'kontrud': NumberInput(attrs={"class": "form-control", "v-model":"kontrud"}),
            'kontrneud': NumberInput(attrs={"class": "form-control", "v-model":"kontrneud"}),
            'sriv': NumberInput(attrs={"class": "form-control", "v-model":"sriv"}),
            'opozdanie': NumberInput(attrs={"class": "form-control", "v-model":"opozdanie"}),


            'otkrbal': NumberInput(attrs={"class": "form-control", "v-model":"otkrbal"}),
            'kontrudbal': NumberInput(attrs={"class": "form-control", "v-model":"kontrudbal"}),
            'kontrneudbal': NumberInput(attrs={"class": "form-control", "v-model":"kontrneudbal"}),
            'srivbal': NumberInput(attrs={"class": "form-control", "v-model":"srivbal"}),
            'opozdaniebal': NumberInput(attrs={"class": "form-control", "v-model":"opozdaniebal"}),

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
