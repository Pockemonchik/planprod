from django import forms
from django.forms import TextInput,Textarea, NumberInput, CheckboxInput
from rating.models import URR, ORMR, PCR, MRR,Rating



class URRForm(forms.ModelForm):
    class Meta:
        model=URR
        exclude = ['year','profile']
        widgets = {
        'obsh': NumberInput(attrs={"class":"form-control", "v-model":"obsh", "readonly":"readonly"}),
        'sootn': NumberInput(attrs={"class":"form-control", "v-model":"sootn", "readonly":"readonly"}),
        'zansprakt': NumberInput(attrs={"class": "form-control", "v-model":"zansprakt"}),
        'viezdsprakt': NumberInput(attrs={"class":"form-control", "v-model":"viezdsprakt"}),
        'ppsfp': NumberInput(attrs={"class":"form-control", "v-model":"ppsfp"}),
        'ppsdr': NumberInput(attrs={"class":"form-control", "v-model":"ppsdr"}),
        'vneaudotor': NumberInput(attrs={"class":"form-control", "v-model":"vneaudotor"}),


        'obshbal':NumberInput(attrs={"class":"form-control", "v-model":"obshbal", "readonly":"readonly"}),
        'sootnbal':NumberInput(attrs={"class":"form-control", "v-model":"sootnbal", "readonly":"readonly"}),
        'zanspraktbal': NumberInput(attrs={"class": "form-control", "v-model":"zanspraktbal", "readonly":"readonly"}),
        'viezdspraktbal':NumberInput(attrs={"class":"form-control", "v-model":"viezdspraktbal", "readonly":"readonly"}),
        'ppsfpbal':NumberInput(attrs={"class":"form-control", "v-model":"ppsfpbal", "readonly":"readonly"}),
        'ppsdrbal':NumberInput(attrs={"class":"form-control", "v-model":"ppsdrbal", "readonly":"readonly"}),
        'vneaudotorbal':NumberInput(attrs={"class":"form-control", "v-model":"vneaudotorbal", "readonly":"readonly"}),

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
                'resocenki1': NumberInput(attrs={"class":"form-control", "v-model":"resocenki1", "readonly":"readonly"}),
                'resocenki6': NumberInput(attrs={"class":"form-control", "v-model":"resocenki6", "readonly":"readonly"}),
                'resocenki11': NumberInput(attrs={"class":"form-control", "v-model":"resocenki11", "readonly":"readonly"}),
                'resocenki16': NumberInput(attrs={"class":"form-control", "v-model":"resocenki16", "readonly":"readonly"}),
                'resocenki26': NumberInput(attrs={"class":"form-control", "v-model":"resocenki26", "readonly":"readonly"}),
                'inovac': NumberInput(attrs={"class":"form-control", "v-model":"inovac"}),


                'ruksecbal': NumberInput(attrs={"class":"form-control", "v-model":"ruksecbal", "readonly":"readonly"}),
                'rukpredmsekbal': NumberInput(attrs={"class":"form-control", "v-model":"rukpredmsekbal", "readonly":"readonly"}),
                'rabotarukbal': NumberInput(attrs={"class":"form-control", "v-model":"rabotarukbal", "readonly":"readonly"}),
                'rabotachlenbal': NumberInput(attrs={"class":"form-control", "v-model":"rabotachlenbal", "readonly":"readonly"}),
                'rukkafnachbal': NumberInput(attrs={"class":"form-control", "v-model":"rukkafnachbal", "readonly":"readonly"}),
                'rukkafzambal': NumberInput(attrs={"class":"form-control", "v-model":"rukkafzambal", "readonly":"readonly"}),
                'bestprepodmirbal': NumberInput(attrs={"class":"form-control", "v-model":"bestprepodmirbal", "readonly":"readonly"}),
                'bestprepodrusbal': NumberInput(attrs={"class":"form-control", "v-model":"bestprepodrusbal", "readonly":"readonly"}),
                'bestprepodregbal': NumberInput(attrs={"class":"form-control", "v-model":"bestprepodregbal", "readonly":"readonly"}),
                'bestprepodunikbal': NumberInput(attrs={"class":"form-control", "v-model":"bestprepodunikbal", "readonly":"readonly"}),
                'uchastiebestprepodmirbal': NumberInput(attrs={"class":"form-control", "v-model":"uchastiebestprepodmirbal", "readonly":"readonly"}),
                'uchastiebestprepodrusbal': NumberInput(attrs={"class":"form-control", "v-model":"uchastiebestprepodrusbal", "readonly":"readonly"}),
                'uchastiebestprepodregbal': NumberInput(attrs={"class":"form-control", "v-model":"uchastiebestprepodregbal", "readonly":"readonly"}),
                'uchastiebestprepodunikbal': NumberInput(attrs={"class":"form-control", "v-model":"uchastiebestprepodunikbal", "readonly":"readonly"}),
                'ekspertbal': NumberInput(attrs={"class":"form-control", "v-model":"ekspertbal", "readonly":"readonly"}),
                'metodkonk1bal': NumberInput(attrs={"class":"form-control", "v-model":"metodkonk1bal", "readonly":"readonly"}),
                'metodkonk2bal': NumberInput(attrs={"class":"form-control", "v-model":"metodkonk2bal", "readonly":"readonly"}),
                'metodkonk3bal': NumberInput(attrs={"class":"form-control", "v-model":"metodkonk3bal", "readonly":"readonly"}),
                'metodkonk4bal': NumberInput(attrs={"class": "form-control", "v-model":"metodkonk4bal", "readonly":"readonly"}),
                'profmasterbal': NumberInput(attrs={"class":"form-control", "v-model":"profmasterbal", "readonly":"readonly"}),
                'podgsbornmirbal': NumberInput(attrs={"class":"form-control", "v-model":"podgsbornmirbal", "readonly":"readonly"}),
                'podgsbornrusbal': NumberInput(attrs={"class":"form-control", "v-model":"podgsbornrusbal", "readonly":"readonly"}),
                'podgsbornregbal': NumberInput(attrs={"class":"form-control", "v-model":"podgsbornregbal", "readonly":"readonly"}),
                'podgsbornunikbal': NumberInput(attrs={"class":"form-control", "v-model":"podgsbornunikbal", "readonly":"readonly"}),
                'vulkanbal': NumberInput(attrs={"class":"form-control", "v-model":"vulkanbal", "readonly":"readonly"}),
                'plenarbal': NumberInput(attrs={"class":"form-control", "v-model":"plenarbal", "readonly":"readonly"}),
                'obrprogrammabal': NumberInput(attrs={"class":"form-control", "v-model":"obrprogrammabal", "readonly":"readonly"}),
                'proverkafbal': NumberInput(attrs={"class":"form-control", "v-model":"proverkafbal", "readonly":"readonly"}),
                'inpectunikbal': NumberInput(attrs={"class":"form-control", "v-model":"inpectunikbal", "readonly":"readonly"}),
                'resocenki1bal': NumberInput(attrs={"class":"form-control", "v-model":"resocenki1bal", "readonly":"readonly"}),
                'resocenki6bal': NumberInput(attrs={"class":"form-control", "v-model":"resocenki6bal", "readonly":"readonly"}),
                'resocenki11bal': NumberInput(attrs={"class":"form-control", "v-model":"resocenki11bal", "readonly":"readonly"}),
                'resocenki16bal': NumberInput(attrs={"class": "form-control", "v-model":"resocenki16bal", "readonly":"readonly"}),
                'resocenki26bal': NumberInput(attrs={"class": "form-control", "v-model":"resocenki26bal", "readonly":"readonly"}),
                'inovacbal': NumberInput(attrs={"class": "form-control", "v-model":"inovacbal", "readonly":"readonly"}),

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


            'otkrbal': NumberInput(attrs={"class": "form-control", "v-model":"otkrbal", "readonly":"readonly"}),
            'kontrudbal': NumberInput(attrs={"class": "form-control", "v-model":"kontrudbal", "readonly":"readonly"}),
            'kontrneudbal': NumberInput(attrs={"class": "form-control", "v-model":"kontrneudbal", "readonly":"readonly"}),
            'srivbal': NumberInput(attrs={"class": "form-control", "v-model":"srivbal", "readonly":"readonly"}),
            'opozdaniebal': NumberInput(attrs={"class": "form-control", "v-model":"opozdaniebal", "readonly":"readonly"}),

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
            'soavtr': NumberInput(attrs={"class":"form-control", "@change":"soavtrChange($event)"}),
            'dgsk' : CheckboxInput(attrs={"@change":"dgskChange($event)"}),
            'bal': NumberInput(attrs={"class": "form-control", "readonly":"readonly"}),
            'name': TextInput(attrs={"class": "form-control"}),
        }
