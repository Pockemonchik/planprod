from django.test import TestCase


from django.shortcuts import render, redirect, get_object_or_404
from plan.models import Profile,Kafedra,Plan,Predmet,NIR,VR,DR,UMR,INR,Nagruzka,DocInfo
from plan.forms import ShapkaForm,Table1Form,Table2Form,Table3Form,Table4Form,Table6Form,Table5Form,MAinTableForm,Table1UploadForm,NagruzkaForm
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
from plan.Parser_and_overview import createDoc2,createDoc,takeTable,takeXls,writeInfoDoc,xlsPrepod
from django.core.files.base import ContentFile
from django.core.files import File
from django.contrib.auth.models import User
from django.http import JsonResponse
# from .tasks import saveallnagr

from django.http import HttpResponse
import random
from docx import Document
import os

# Create your tests here.
def nepustNagr():
    #check po xlxs
    # nagr=Nagruzka.objects.all()
    # data=[]
    # count=0
    # for n in nagr:
    #     kaf=n.kafedra
    #     profiles=Profile.objects.filter(kafedra=kaf)
    #     for p in profiles:
    #         plan=get_object_or_404(Plan,prepod=p,year=2019)
    #         a=takeXls(n.document.path,plan.name[0:-5])
    #
    #         if a=='nenorm':
    #             data.append(p.kafedra.fullname+" "+plan.name)
    #             count+=1
    #             print(count)
    #             print(p.kafedra.fullname+" "+plan.name)
    #
    #         else:
    #             count+=1
    #             print(count)
    #             # print("niceman")
    #             # print(p.kafedra.fullname+" "+plan.name)
    #
    #
    # print(data)
    profiles=Profile.objects.all()
    count=0
    for p in profiles:
            plan=get_object_or_404(Plan,prepod=p,year=2019)
            allpred=p.predmets.all()
            if not allpred.exists():
                print(p.fullname)
                print(p.kafedra.fullname)
                count+=1
    print(count)



nepustNagr()
