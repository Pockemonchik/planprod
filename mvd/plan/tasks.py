from background_task import background
from django.shortcuts import render, redirect, get_object_or_404
from plan.models import Profile,Kafedra,Plan,Predmet,NIR,VR,DR,UMR,INR,Nagruzka,DocInfo
from plan.forms import ShapkaForm,Table1Form,Table2Form,Table3Form,Table4Form,Table6Form,Table5Form,MAinTableForm,Table1UploadForm,NagruzkaForm
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
from plan.Parser_and_overview import createDoc2,createDoc,takeTable,takeXls,writeInfoDoc,xlsPrepod
from django.core.files.base import ContentFile
from django.core.files import File
from django.contrib.auth.models import User

from django.http import HttpResponse
import random
from docx import Document
import os
@background(schedule=5)
def saveallnagr():
    obr=0
    all_profile=Profile.objects.all()
    # all_profile=Profile.objects.filter(kafedra__name='kaf4370')

    for profile in all_profile:
        if profile.role==2:
            # if (profile.user.username=="admin" or profile.user.username=="user" or profile.kafedra.fullname=="инф. и мат.":
            if profile.kafedra.fullname!="инф. и мат.":
                continue
            nagruzkadoc=get_object_or_404(Nagruzka,year=2019,kafedra=profile.kafedra)
            plan=get_object_or_404(Plan,prepod=profile,year=2019)
            predmetsdel=Predmet.objects.filter(prepodavatel=profile,status=False)
            predmetsdel.delete()
            # print(nagruzkadoc.document.path)
            # print(plan.name)
            try:

                data=takeXls(nagruzkadoc.document.path,plan.name[0:-4])
                fields=Predmet._meta.get_fields()
                for table in range(len(data)):
                    if table==0:
                        for row in range(len(data[table])):
                            count=0
                            predmet=Predmet()
                            # print(data)
                            # print(len(data[table]))
                            # print(data[table])

                            if data[table][row][0]=="0":
                                continue
                            for field in fields:
                                if field.name=="id":
                                    continue
                                if row==(len(data[table])-1) and field.name=="name":
                                    setattr(predmet,field.name, "Итого за 1 полугодие:")
                                    continue
                                if row==(len(data[table])-1) and field.name=="auditor_nagruzka":
                                    setattr(predmet,field.name, data[table][row][count])
                                    break
                                # print("suka")
                                setattr(predmet,field.name, data[table][row][count])

                                if count==25:
                                    break
                                count+=1
                            predmet.kafedra=profile.kafedra
                            # print(predmet.__dict__)
                            predmet.prepodavatel=profile
                            predmet.year="2019"
                            predmet.polugodie='1'
                            predmet.status=False
                            #tru если выполена false если план
                            # print(data)
                            predmet.save()

                    if table==1:
                        for row in range(len(data[table])):
                            count=0
                            predmet=Predmet()
                            # print(len(data[table]))
                            # print(data[table])
                            # print( data[table][row][0])
                            if data[table][row][0]=="0":

                                continue
                            for field in fields:
                                if field.name=="id":
                                    continue
                                if row==(len(data[table])-2) and field.name=="name":
                                    setattr(predmet,field.name, "Итого за 2 полугодие:")
                                    continue
                                if row==(len(data[table])-1) and field.name=="name":
                                    setattr(predmet,field.name, "Итого за учебный год:")
                                    continue

                                if row==(len(data[table])-2) and field.name=="auditor_nagruzka":
                                    setattr(predmet,field.name, data[table][row][count])
                                    break
                                if row==(len(data[table])-1) and field.name=="auditor_nagruzka":
                                    setattr(predmet,field.name, data[table][row][count])
                                    break
                                # print("suka2")
                                setattr(predmet,field.name, data[table][row][count])
                                # print(count)
                                if count==25:
                                    break
                                count+=1

                            predmet.kafedra=profile.kafedra
                            # print(predmet.__dict__)
                            predmet.prepodavatel=profile
                            predmet.year="2019"
                            predmet.polugodie='2'
                            predmet.status=False#tru если выполена false если план
                            # print(predmet.all_values())
                            predmet.save()


                print("успешно обработан план "+profile.fullname)
                obr+=1
                print(obr)
            except:
                print("неудалось в профиле "+ profile.fullname)
                continue
