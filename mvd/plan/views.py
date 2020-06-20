#
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from rating.models import Rating
from plan.models import Article,Mesyac,Profile,Kafedra,Plan,Predmet,NIR,VR,DR,UMR,INR,Nagruzka,DocInfo
from plan.forms import MesyacForm,UserAddForm,docUploadForm,ShapkaForm,Table1Form,Table2Form,Table3Form,Table4Form,Table6Form,Table5Form,MAinTableForm,Table1UploadForm,NagruzkaForm
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
from plan.Parser_and_overview import createDoc2,createDoc,takeTable,takeXls,writeInfoDoc,xlsPrepod
from django.core.files.base import ContentFile
from django.core.files import File
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.conf import settings
from django.db.models import Q
# from .tasks import saveallnagr

from django.http import HttpResponse
import random
from docx import Document
import os
from io import StringIO,BytesIO

def deluser(request):
    if request.user.is_authenticated:
        profile=get_object_or_404(Profile,user=request.user)
        if profile.role==2:
            if request.method=="POST":
                # try:
                    print(request.POST['profile'])
                    profiledel=Profile.objects.get(fullname=request.POST['profile'])
                    plandel=Plan.objects.get(prepod=profiledel)
                    userdel=profiledel.user
                    profiledel.delete()
                    plandel.delete()
                    userdel.delete()
                # except:
                #     return render(request,'error.html',{'content':"Произошла ошибка при удалении пользователя"})




            return redirect('index')
    else:
        return redirect('log')



def adduser(request):
    if request.user.is_authenticated:
        if request.method=="POST":

            profile=get_object_or_404(Profile,user=request.user)
            if profile.role==2:
                form=UserAddForm(request.POST)
                if form.is_valid():
                    try:
                        usernew =User.objects.create_user(form.cleaned_data.get('username'),form.cleaned_data.get('password'),form.cleaned_data.get('password'))


                        profilenew=Profile()
                        profilenew.user=usernew
                        profilenew.fullname=form.cleaned_data.get('fio')
                        profilenew.kafedra=profile.kafedra
                        plan=Plan()
                        plan.prepod=profilenew
                        plan.name=''.join([form.cleaned_data.get('fio').split(' ')[0],' ',form.cleaned_data.get('fio').split(' ')[1][0],'.',form.cleaned_data.get('fio').split(' ')[1][0]])
                        print(plan.name)
                        usernew.save()
                        profilenew.save()
                        plan.save()

                    except:
                        print("ne")
                        return render(request,'error.html',{'content':"Произошла ошибка при добавлении пользователя"})
            else:

                print('blen')
                return render(request,'error.html',{'content':"Произошла ошибка при добавлении пользователя"})
        return redirect('index')
    else:
        return redirect('log')



def exelobr(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'examplexlsx.xlsx')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404
def exelobrfact(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'examplexlsxfact.xlsx')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404
def docxobr(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'exampleip.docx')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404



def handle_uploaded_file(f):
    with open('anal.docx', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
def documentAnalize(request):
                    if request.user.is_authenticated:
                        if request.method=="POST":
                            file=request.FILES['file']

                            profile=get_object_or_404(Profile,user=request.user)
                            if profile.role==3 or profile.role==2:
                                    profile=get_object_or_404(Profile,user__username=request.POST['profile'])
                            print(profile.fullname)
                            handle_uploaded_file(file)
                            try:
                                data=takeTable('anal.docx')
                            except:
                                print("fail takeTable")
                                return render(request,'error.html',{'content':"Произошла ошибка при заполнении плана из загруженного doc файла, пожалуйста проверьте формат документа(см.справку)"})


                            if data == 'dolbaeb':
                                print("fail docfile")
                                return render(request,'error.html',{'content':"Произошла ошибка при заполнении плана из загруженного doc файла, пожалуйста проверьте формат документа(см.справку)"})
                            print(data)
                            for table in range(len(data)):
                                if table==0:
                                    for row in range(len(data[table])):


                                        count=0
                                        umr=UMR()
                                        umr.vid=data[table][row][1]
                                        umr.srok=data[table][row][2]
                                        umr.otmetka=data[table][row][3]
                                        umr.prepodavatel=profile


                                        umr.year="2019"
                                        umr.polugodie='1'
                                        umr.save()
                                        print("sohraninen")
                                if table==1:
                                    for row in range(len(data[table])):


                                        count=0
                                        umr=UMR()
                                        count+=1
                                        umr.vid=data[table][row][1]
                                        umr.srok=data[table][row][2]
                                        umr.otmetka=data[table][row][3]
                                        umr.prepodavatel=profile
                                        umr.year="2019"
                                        umr.polugodie='2'
                                        umr.save()
                                if table==2:
                                    for row in range(len(data[table])):


                                        count=0
                                        umr=NIR()
                                        umr.vid=data[table][row][1]
                                        umr.srok=data[table][row][2]
                                        umr.otmetka=data[table][row][3]
                                        umr.prepodavatel=profile


                                        umr.year="2019"
                                        umr.polugodie='1'
                                        umr.save()
                                        print("sohraninen")
                                if table==3:
                                    for row in range(len(data[table])):


                                        count=0
                                        umr=NIR()

                                        count+=1
                                        umr.vid=data[table][row][1]
                                        umr.srok=data[table][row][2]
                                        umr.otmetka=data[table][row][3]
                                        umr.prepodavatel=profile
                                        umr.year="2019"
                                        umr.polugodie='2'
                                        umr.save()
                                if table==4:
                                    for row in range(len(data[table])):


                                        count=0
                                        umr=VR()
                                        umr.vid=data[table][row][1]
                                        umr.srok=data[table][row][2]
                                        umr.otmetka=data[table][row][3]
                                        umr.prepodavatel=profile


                                        umr.year="2019"
                                        umr.polugodie='1'
                                        umr.save()
                                        print("sohraninen")
                                if table==5:
                                    for row in range(len(data[table])):


                                        count=0
                                        umr=VR()

                                        count+=1
                                        umr.vid=data[table][row][1]
                                        umr.srok=data[table][row][2]
                                        umr.otmetka=data[table][row][3]
                                        umr.prepodavatel=profile
                                        umr.year="2019"
                                        umr.polugodie='2'
                                        umr.save()
                                if table==6:
                                    for row in range(len(data[table])):


                                        count=0
                                        umr=INR()

                                        umr.vid=data[table][row][1]
                                        umr.srok=data[table][row][2]
                                        umr.otmetka=data[table][row][3]
                                        umr.prepodavatel=profile


                                        umr.year="2019"
                                        umr.polugodie='1'
                                        umr.save()
                                        print("sohraninen")
                                if table==7:
                                    for row in range(len(data[table])):


                                        count=0
                                        umr=INR()

                                        count+=1
                                        umr.vid=data[table][row][1]
                                        umr.srok=data[table][row][2]
                                        umr.otmetka=data[table][row][3]
                                        umr.prepodavatel=profile
                                        umr.year="2019"
                                        umr.polugodie='2'
                                        umr.save()
                                if table==8:
                                    for row in range(len(data[table])):


                                        count=0
                                        umr=DR()
                                        umr.vid=data[table][row][1]
                                        umr.srok=data[table][row][2]
                                        umr.otmetka=data[table][row][3]
                                        umr.prepodavatel=profile


                                        umr.year="2019"
                                        umr.polugodie='1'
                                        umr.save()
                                        print("sohraninen")
                                if table==9:
                                    for row in range(len(data[table])):


                                        count=0
                                        umr=DR()

                                        count+=1
                                        umr.vid=data[table][row][1]
                                        umr.srok=data[table][row][2]
                                        umr.otmetka=data[table][row][3]
                                        umr.prepodavatel=profile
                                        umr.year="2019"
                                        umr.polugodie='2'
                                        umr.save()
                            print("vrode norm")
                            return redirect('detail_plan',slug=profile.user.username,year=request.POST['year'])
                        else:
                            return redirect('log')


                        # count+=1



    # dlya doc faylov vseh
    # kafedri=Kafedra.objects.all()
    # count=0
    # for kaf in kafedri:
    #     # try:
    #         dir="/home/andrey/Desktop/sorplans/"+kaf.fullname
    #         list=os.listdir(dir)
    #         profiles=Profile.objects.filter(kafedra=kaf)
    #         for profile in profiles:
    #             for i in range(len(list)):
    #                 #запонить дату
    #                 if profile.fullname.split(' ', 1)[0] in list[i]:
    #                     # print(profile.fullname.split(' ', 1)[0])
    #                     if profile.fullname.split(' ', 1)[0]=="Хаминский":
    #                         data=takeTable('/home/andrey//Desktop/sorplans/прав человека и междун.права/Индивидуальный план Хаминский 2019-2020.docx')
    #                         # print (data)
    #
    #                         fields=UMR._meta.get_fields()
    #                         for table in range(len(data)):
    #                             if table==0:
    #                                 for row in range(len(data[table])):
    #                                     print(data[table])
    #
    #                                     count=0
    #                                     umr=UMR()
    #                                     umr.vid=data[table][row][1]
    #                                     umr.srok=data[table][row][2]
    #                                     umr.otmetka=data[table][row][3]
    #                                     umr.prepodavatel=profile
    #
    #
    #                                     umr.year="2019"
    #                                     umr.polugodie='1'
    #                                     # umr.save()
    #                                     print("sohraninen")
    #                             if table==2:
    #                                 for row in range(len(data[table])):
    #                                     print(data[table])
    #
    #                                     count=0
    #                                     umr=UMR()
    #                                     for field in fields:
    #                                         count+=1
    #                                         umr.vid=data[table][row][1]
    #                                         umr.srok=data[table][row][2]
    #                                         umr.otmetka=data[table][row][3]
    #                                         umr.prepodavatel=profile
    #                                         umr.year="2019"
    #                                         umr.polugodie='2'
    #                                         # umr.save()
    #
    #                         print("vrode norm")
    #
    #
    #                     count+=1

        # except:
        #     print("1")

    #analize doc file
    # data=[]
    # #
    # profile=get_object_or_404(Profile,_сделать выборку по имени из базы в цикле_)
    # for in in range(len(rucovodstvo_adunctami[0])):
    #     for #
    #
    #         fields=Umr._meta.get_fields()
    #         for table in range(len(data)):
    #             if table==0:
    #                 for row in range(len(data[table])):
    #                     count=0
    #                     umr=Umr()
    #                     for field in fields:
    #                         count+=1
    #                     umr.prepodavatel=profile
    #                     umr.year="2019"
    #                     umr.polugodie='1'
    #                     umr.save()
    #
    #
    # print(count)









    # return redirect('index')


def saveDB(request):
    saveallnagr()
    return redirect('index')

    #zapoln doc nagrq all
    # obr=0
    # all_profile=Profile.objects.all()
    #
    # for profile in all_profile:
    #     if profile.role==1:
    #         if profile.user.username=="admin" or profile.user.username=="user" or profile.user.username=="user145":
    #             continue
    #         nagruzkadoc=get_object_or_404(Nagruzka,year=2019,kafedra=profile.kafedra)
    #         plan=get_object_or_404(Plan,prepod=profile,year=2019)
    #         predmetsdel=Predmet.objects.filter(prepodavatel=profile,status=False)
    #         predmetsdel.delete()
    #         # print(nagruzkadoc.document.path)
    #         # print(plan.name)
    #         try:
    #
    #             data=takeXls(nagruzkadoc.document.path,plan.name)
    #             fields=Predmet._meta.get_fields()
    #             for table in range(len(data)):
    #                 if table==0:
    #                     for row in range(len(data[table])):
    #                         count=0
    #                         predmet=Predmet()
    #                         # print(data)
    #                         # print(len(data[table]))
    #                         # print(data[table])
    #
    #                         if data[table][row][0]=="0":
    #                             continue
    #                         for field in fields:
    #                             if field.name=="id":
    #                                 continue
    #                             if row==(len(data[table])-1) and field.name=="name":
    #                                 setattr(predmet,field.name, "Итого за 1 полугодие:")
    #                                 continue
    #                             if row==(len(data[table])-1) and field.name=="auditor_nagruzka":
    #                                 setattr(predmet,field.name, data[table][row][count])
    #                                 break
    #                             # print("suka")
    #                             setattr(predmet,field.name, data[table][row][count])
    #
    #                             if count==25:
    #                                 break
    #                             count+=1
    #                         predmet.kafedra=profile.kafedra
    #                         # print(predmet.__dict__)
    #                         predmet.prepodavatel=profile
    #                         predmet.year="2019"
    #                         predmet.polugodie='1'
    #                         predmet.status=False
    #                         #tru если выполена false если план
    #                         # print(data)
    #                         predmet.save()
    #
    #                 if table==1:
    #                     for row in range(len(data[table])):
    #                         count=0
    #                         predmet=Predmet()
    #                         # print(len(data[table]))
    #                         # print(data[table])
    #                         # print( data[table][row][0])
    #                         if data[table][row][0]=="0":
    #
    #                             continue
    #                         for field in fields:
    #                             if field.name=="id":
    #                                 continue
    #                             if row==(len(data[table])-2) and field.name=="name":
    #                                 setattr(predmet,field.name, "Итого за 2 полугодие:")
    #                                 continue
    #                             if row==(len(data[table])-1) and field.name=="name":
    #                                 setattr(predmet,field.name, "Итого за учебный год:")
    #                                 continue
    #
    #                             if row==(len(data[table])-2) and field.name=="auditor_nagruzka":
    #                                 setattr(predmet,field.name, data[table][row][count])
    #                                 break
    #                             if row==(len(data[table])-1) and field.name=="auditor_nagruzka":
    #                                 setattr(predmet,field.name, data[table][row][count])
    #                                 break
    #                             # print("suka2")
    #                             setattr(predmet,field.name, data[table][row][count])
    #                             # print(count)
    #                             if count==25:
    #                                 break
    #                             count+=1
    #
    #                         predmet.kafedra=profile.kafedra
    #                         # print(predmet.__dict__)
    #                         predmet.prepodavatel=profile
    #                         predmet.year="2019"
    #                         predmet.polugodie='2'
    #                         predmet.status=False#tru если выполена false если план
    #                         # print(predmet.all_values())
    #                         predmet.save()
    #
    #
    #             print("успешно обработан план "+profile.fullname)
    #             obr+=1
    #             print(obr)
    #         except:
    #             print("неудалось в профиле "+ profile.fullname)
    #             continue
    #
    #



#zapoln nagr doc all

    # all_profile=Profile.objects.all()
    # for profile in all_profile:
    #             #print(1)
    #             #print(profile.fullname)
    #             data=[]
    #             predmets=Predmet.objects.filter(prepodavatel=profile,polugodie=1,status=False,year=2019)
    #             for p in predmets:
    #                arr=p.all_values()
    #                for a in arr:
    #                    if a=='0':
    #                        data.append(" ")
    #                    else:
    #                        data.append(a)
    #             b1=int(len(data)/26)
    #             # data+=[" "]*(363-(predmets.count()*26))
    #
    #             predmets=Predmet.objects.filter(prepodavatel=profile,polugodie=2,status=False,year=2019)
    #             for p in predmets:
    #                arr=p.all_values()
    #                for a in arr:
    #                    if a=='0':
    #                        data.append(" ")
    #                    else:
    #                        data.append(a)
    #             # data+=[" "]*(362-(predmets.count()*26))
    #             b2=int((len(data)/26)-b1)
    #             # print(data)
    #             # print(str(b1)+" "+str(b2))
    #             print( profile.fullname,' ', data, ' ', b1, ' ', b2)
    #             name=profile.kafedra.fullname+profile.fullname
    #             createDoc2(name,data,b1,b2)


    #zapoln doc nagrq nach

    # all_profile=Profile.objects.filter(role=2)
    # for profile in all_profile:
    #             #print(1)
    #             #print(profile.fullname)
    #             data=[]
    #             predmets=Predmet.objects.filter(prepodavatel=profile,polugodie=1,status=False,year=2019)
    #             for p in predmets:
    #                arr=p.all_values()
    #                for a in arr:
    #                    if a=='0':
    #                        data.append(" ")
    #                    else:
    #                        data.append(a)
    #             b1=int(len(data)/26)
    #             # data+=[" "]*(363-(predmets.count()*26))
    #
    #             predmets=Predmet.objects.filter(prepodavatel=profile,polugodie=2,status=False,year=2019)
    #             for p in predmets:
    #                arr=p.all_values()
    #                for a in arr:
    #                    if a=='0':
    #                        data.append(" ")
    #                    else:
    #                        data.append(a)
    #             # data+=[" "]*(362-(predmets.count()*26))
    #             b2=int((len(data)/26)-b1)
    #             # print(data)
    #             # print(str(b1)+" "+str(b2))
    #             print( profile.fullname,' ', data, ' ', b1, ' ', b2)
    #             createDoc2(profile.fullname,data,b1,b2)


























  # #gruzka DLYA NACHKAF
  #   if request.user.is_authenticated:
  #       all_profile=Profile.objects.all()
  #
  #       for profile in all_profile:
  #           if profile.role==2:
  #               if profile.user.username=="admin" or profile.user.username=="user" or profile.user.username=="user145":
  #                   continue
  #               nagruzkadoc=get_object_or_404(Nagruzka,year=2019,kafedra=profile.kafedra)
  #               plan=get_object_or_404(Plan,prepod=profile,year=2019)
  #               predmetsdel=Predmet.objects.filter(prepodavatel=profile,status=False)
  #               predmetsdel.delete()
  #               print(nagruzkadoc.document.path)
  #               print(plan.name)
  #               try:
  #
  #                   data=takeXls(nagruzkadoc.document.path,plan.name)
  #                   fields=Predmet._meta.get_fields()
  #                   for table in range(len(data)):
  #                       if table==0:
  #                           for row in range(len(data[table])):
  #                               count=0
  #                               predmet=Predmet()
  #                               # print(data)
  #                               # print(len(data[table]))
  #                               # print(data[table])
  #
  #                               if data[table][row][0]=="0":
  #                                   continue
  #                               for field in fields:
  #                                   if field.name=="id":
  #                                       continue
  #                                   if row==(len(data[table])-1) and field.name=="name":
  #                                       setattr(predmet,field.name, "Итого за 1 полугодие:")
  #                                       continue
  #                                   if row==(len(data[table])-1) and field.name=="auditor_nagruzka":
  #                                       setattr(predmet,field.name, data[table][row][count])
  #                                       break
  #                                   # print("suka")
  #                                   setattr(predmet,field.name, data[table][row][count])
  #
  #                                   if count==25:
  #                                       break
  #                                   count+=1
  #                               predmet.kafedra=profile.kafedra
  #                               # print(predmet.__dict__)
  #                               predmet.prepodavatel=profile
  #                               predmet.year="2019"
  #                               predmet.polugodie='1'
  #                               predmet.status=False
  #                               #tru если выполена false если план
  #                               # print(data)
  #                               predmet.save()
  #
  #                       if table==1:
  #                           for row in range(len(data[table])):
  #                               count=0
  #                               predmet=Predmet()
  #                               # print(len(data[table]))
  #                               print(data[table])
  #                               # print( data[table][row][0])
  #                               if data[table][row][0]=="0":
  #
  #                                   continue
  #                               for field in fields:
  #                                   if field.name=="id":
  #                                       continue
  #                                   if row==(len(data[table])-2) and field.name=="name":
  #                                       setattr(predmet,field.name, "Итого за 2 полугодие:")
  #                                       continue
  #                                   if row==(len(data[table])-1) and field.name=="name":
  #                                       setattr(predmet,field.name, "Итого за учебный год:")
  #                                       continue
  #
  #                                   if row==(len(data[table])-2) and field.name=="auditor_nagruzka":
  #                                       setattr(predmet,field.name, data[table][row][count])
  #                                       break
  #                                   if row==(len(data[table])-1) and field.name=="auditor_nagruzka":
  #                                       setattr(predmet,field.name, data[table][row][count])
  #                                       break
  #                                   # print("suka2")
  #                                   setattr(predmet,field.name, data[table][row][count])
  #                                   # print(count)
  #                                   if count==25:
  #                                       break
  #                                   count+=1
  #
  #                               predmet.kafedra=profile.kafedra
  #                               # print(predmet.__dict__)
  #                               predmet.prepodavatel=profile
  #                               predmet.year="2019"
  #                               predmet.polugodie='2'
  #                               predmet.status=False#tru если выполена false если план
  #                               # print(predmet.all_values())
  #                               predmet.save()
  #
  #
  #                   print("успешно обработан план "+profile.fullname)
  #               except:
  #                   print("неудалось в профиле "+ profile.fullname)
  #                   continue
  #
  #
  #
  #
  #
  #       return redirect('detail_plan',slug=profile.user.username,year=2019)
  #   else:
  #       return redirect('log')
  #

#nagruzka for all
    # if request.user.is_authenticated:
    #     all_profile=Profile.objects.all()
    #
    #     for profile in all_profile:
    #         if profile.user.username=="admin" or profile.user.username=="user":
    #             continue
    #         nagruzkadoc=get_object_or_404(Nagruzka,year=2019,kafedra=profile.kafedra)
    #         plan=get_object_or_404(Plan,prepod=profile,year=2019)
    #         predmetsdel=Predmet.objects.filter(prepodavatel=profile,status=False)
    #         predmetsdel.delete()
    #         print(nagruzkadoc.document.path)
    #         print(plan.name)
    #         try:
    #
    #             data=takeXls(nagruzkadoc.document.path,plan.name)
    #
    #             fields=Predmet._meta.get_fields()
    #             for table in range(len(data)):
    #                 if table==0:
    #                     for row in range(len(data[table])):
    #                         count=0
    #                         predmet=Predmet()
    #                         if data[table][row][0]=="0" and row!=13:
    #                             continue
    #                         for field in fields:
    #                             if field.name=="id":
    #                                 continue
    #                             if row==13 and field.name=="name":
    #                                 setattr(predmet,field.name, "Итого за 1 полугодие:")
    #                                 continue
    #                             if row==13 and field.name=="auditor_nagruzka":
    #                                 setattr(predmet,field.name, data[table][row][count])
    #                                 break
    #                             setattr(predmet,field.name, data[table][row][count])
    #
    #                             if count==25:
    #                                 break
    #                             count+=1
    #                         predmet.kafedra=profile.kafedra
    #                         # print(predmet.__dict__)
    #                         predmet.prepodavatel=profile
    #                         predmet.year="2019"
    #                         predmet.polugodie='1'
    #                         predmet.status=False
    #                         #tru если выполена false если план
    #                         # print(data)
    #                         predmet.save()
    #
    #                 if table==1:
    #                     for row in range(len(data[table])):
    #                         count=0
    #                         predmet=Predmet()
    #                         if data[table][row][0]=="0" and row!=12 and row!=13:
    #                             continue
    #                         for field in fields:
    #                             if field.name=="id":
    #                                 continue
    #                             if row==12 and field.name=="name":
    #                                 setattr(predmet,field.name, "Итого за 2 полугодие:")
    #                                 continue
    #                             if row==13 and field.name=="name":
    #                                 setattr(predmet,field.name, "Итого за учебный год:")
    #                                 continue
    #
    #                             if row==12 and field.name=="auditor_nagruzka":
    #                                 setattr(predmet,field.name, data[table][row][count])
    #                                 break
    #                             if row==13 and field.name=="auditor_nagruzka":
    #                                 setattr(predmet,field.name, data[table][row][count])
    #                                 break
    #                             setattr(predmet,field.name, data[table][row][count])
    #
    #                             if count==25:
    #                                 break
    #                             count+=1
    #                         predmet.kafedra=profile.kafedra
    #                         # print(predmet.__dict__)
    #                         predmet.prepodavatel=profile
    #                         predmet.year="2019"
    #                         predmet.polugodie='2'
    #                         predmet.status=False#tru если выполена false если план
    #                         # print(predmet.all_values())
    #                         predmet.save()
    #             print("успешно обработан план"+profile.fullname)
    #         except:
    #             print("неудалось в профиле "+ profile.fullname)
    #             continue
    #
    #
    #
    #
    #
    #     return redirect('detail_plan',slug=profile.user.username,year=2019)
    # else:
    #     return redirect('log')








    # profiles=Profile.objects.all()
    # plans=Plan.objects.all()
    # for plan in plans:
    #     fullName = plan.name
    #     name=""
    #
    #     lenName = len(fullName)
    #     x = 0
    #     while x < lenName:
    #         if fullName[x] == ' ':
    #             x+=1
    #             break
    #         x+=1
    #     f=x
    #     while x < lenName:
    #         if fullName[x] == ' ':
    #             name = fullName[f:x+1]
    #             name += fullName[x+1] + '.'
    #             break
    #         x+=1
    #     x+=1
    #     while x < lenName:
    #         if fullName[x] == ' ':
    #             name += fullName[x+1] + '.'
    #             break
    #         x+=1
    #     print(name)
    #     plan.name=name
    #     plan.save()
    # for plan in plans:
    #     docinf=DocInfo()
    #     docinf.plan=plan
    #     docinf.save()
    # for profile in profiles:
    #     if profile.dolzhnost=="нач.кафедры":
    #         profile.role=2
    #         print(profile.fullname)
    #         profile.save()
    # a=xlsPrepod('/home/andrey/Desktop/shtatka.xlsx')
    #создание планов для всех
    # profiles=Profile.objects.all()
    # print(profiles.count())
    # for profile in profiles:
    #     plan=Plan()
    #     plan.name="План "+profile.fullname
    #     plan.prepod=profile
    #     plan.year=2019
    #     plan.save()
    #сохраняем кафедры
    # for i in range(len(a)):
    #     profile=Profile()
    #     passw=random.randint(10000000,99999999)
    #     user=User.objects.create_user('user'+str(i),str(passw),passw)
    #     profile.user=user
    #     profile.kafedra=get_object_or_404(Kafedra,fullname=a[i][0])
    #     profile.dolzhnost=a[i][1]
    #     profile.fullname=a[i][2]
    #     profile.stepen=a[i][3]
    #     profile.save()
    #     print(profile.user,profile.kafedra.fullname,profile.dolzhnost,profile.stepen)
        # for j in range(len(a[i])):
        #
            # if j==0:
            #     try:
            #         alkaf=Kafedra.objects.get(fullname=a[i][j])
            #     except Kafedra.DoesNotExist:
            #         kaf=Kafedra()
            #         kaf.name="kaf"+str(i)+str(j)
            #         kaf.fullname=a[i][j]
            #         kaf.save()






    # return redirect('index')






def index(request):
    if request.user.is_authenticated:
        profile=get_object_or_404(Profile,user=request.user)
        plans=Plan.objects.filter(prepod=profile)
        kafedri=Kafedra.objects.all()
        sotr=''
        if profile.role==2:
            kafedri=Kafedra.objects.filter(name=profile.kafedra.name)
            sotr=Profile.objects.filter(kafedra=profile.kafedra)
        nagruzkadocs=Nagruzka.objects.filter(kafedra=profile.kafedra)
        nagruzka=NagruzkaForm()
        useraddform=UserAddForm()
        articles=Article.objects.all()
        return render(request, 'plan.html',{
        'profile':profile,
        'kafedri':kafedri,
        'plans':plans,
        'nagruzka':nagruzka,
        'nagruzkadocs':nagruzkadocs,
        'useraddform':useraddform,
        'sotr':sotr,
        'articles':articles
        })
    else:
        return redirect('log')
def nagruzkaSave(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            profile=get_object_or_404(Profile,user=request.user)
            form=NagruzkaForm(request.POST,request.FILES)
            if form.is_valid():
                try:
                    nagruzka=form.save(commit=False)
                    my_object =Nagruzka.objects.get(kafedra=profile.kafedra,year=nagruzka.year,status=nagruzka.status)
                    my_object.delete()
                    nagruzka.kafedra=profile.kafedra
                    nagruzka.save()
                except Nagruzka.DoesNotExist:

                    nagruzka=form.save(commit=False)
                    nagruzka.kafedra=profile.kafedra
                    nagruzka.save()
            else:
                    print('blen')
        return redirect('index')
    else:
        return redirect('log')

def deleteNgruzka(request,year):
    if request.user.is_authenticated:
        profile=get_object_or_404(Profile,user=request.user)
        print("1")
        if profile.role==2:
            nagruzka=get_object_or_404(Nagruzka,year=year,kafedra=profile.kafedra)
            nagruzka.delete()
            return redirect('index')
    else:
        return redirect('log')
# анализ нагрузки
def nagruzka(request,year,slug):
    if request.user.is_authenticated:
        user=User.objects.get(username=slug)
        profile=get_object_or_404(Profile,user=user)
        plan=get_object_or_404(Plan,prepod=profile,year=year)
        nagruzkadoc=get_object_or_404(Nagruzka.objects.filter(year=year,kafedra=profile.kafedra).exclude(status='Фактическая'))
        predmetsdel=Predmet.objects.filter(prepodavatel=profile,status=False)
        predmetsdel.delete()


        try:
            plans=Plan.objects.filter(prepod__kafedra=profile.kafedra)
            count=0
            for p in plans:
                if p.name[0:-4]==plan.name[0:-4]:
                    count+=1
                # print(p)
                # print(p)
            if count==2:
                data=takeXls(nagruzkadoc.document.path,plan.name,True)
            else:
                data=takeXls(nagruzkadoc.document.path,plan.name[0:-4],True)
        except :
            return render(request,'error.html',{'content':"Произошла ошибка при заполнении плана из загруженного XLSX учебной нагрузки файла, пожалуйста проверьте формат документа(см.справку)"})


        # for i in range(len(data)):
        #     for j in range(len(data[i])):
        #         print(data[i][j])
        # # print('')
        # print(data)

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
                    predmet.save1()

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

                        setattr(predmet,field.name, data[table][row][count])
                        # print(count)
                        if count==25:
                            break
                        count+=1
                        # print(field.name+str(data[table][row][count]))
                    predmet.kafedra=profile.kafedra
                    # print(predmet.__dict__)
                    predmet.prepodavatel=profile
                    predmet.year="2019"
                    predmet.polugodie='2'
                    predmet.status=False#tru если выполена false если план
                    # print(predmet.all_values())
                    predmet.save1()



        return redirect('detail_plan',slug=profile.user.username,year=year)
    else:
        return redirect('log')

def nagruzkafact(request,year,slug):
    if request.user.is_authenticated:
        user=User.objects.get(username=slug)
        profile=get_object_or_404(Profile,user=user)
        plan=get_object_or_404(Plan,prepod=profile,year=year)
        try:

            nagruzkadoc=get_object_or_404(Nagruzka,year=year,kafedra=profile.kafedra,status='Фактическая')
            print(nagruzkadoc)
        except:
            return render(request,'error.html',{'content':"Произошла ошибка при заполнении плана из загруженного XLSX учебной нагрузки файла, пожалуйста проверьте формат документа(см.справку)"})

        predmetsdel=Predmet.objects.filter(prepodavatel=profile,status=True)
        predmetsdel.delete()
        print(nagruzkadoc.document.path)
        print(plan.name[0:-4])
        print('')
        try:
            plans=Plan.objects.filter(prepod__kafedra=profile.kafedra)
            count=0
            for p in plans:
                if p.name[0:-4]==plan.name[0:-4]:
                    count+=1
                # print(p)
                # print(p)
            if count==2:
                data=takeXls(nagruzkadoc.document.path,plan.name,False)
            else:
                data=takeXls(nagruzkadoc.document.path,plan.name[0:-4],False)
        except:
            return render(request,'error.html',{'content':"Произошла ошибка при заполнении плана из загруженного XLSX учебной нагрузки файла, пожалуйста проверьте формат документа(см.справку), возможно орфографическая ошибка в слове "+ data})
        if type(data) != list:
            if data == 'лекции':
                return render(request,'error.html',{'content':"Произошла ошибка при заполнении плана из загруженного XLSX учебной нагрузки файла, пожалуйста проверьте формат документа(см.справку), возможно орфографическая ошибка в слове "+ data+", либо строчка в exel документе с наименованием видов учебной работы(лекции, практики и т.д) находится не в соответствии с образцом, должна быть на 8 строчке"})

            return render(request,'error.html',{'content':"Произошла ошибка при заполнении плана из загруженного XLSX учебной нагрузки файла, пожалуйста проверьте формат документа(см.справку), возможно орфографическая ошибка в слове "+ data})


        # for i in range(len(data)):
        #     for j in range(len(data[i])):
        #         print(data[i][j])
        # # print('')
        # print(data)

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

                        setattr(predmet,field.name, data[table][row][count])

                        if count==25:
                            break
                        count+=1
                    predmet.kafedra=profile.kafedra
                    # print(predmet.__dict__)
                    predmet.prepodavatel=profile
                    predmet.year="2019"
                    predmet.polugodie='1'
                    predmet.status=True
                    #tru если выполена false если план

                    # print(data)
                    predmet.save1()

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

                        setattr(predmet,field.name, data[table][row][count])
                        # print(count)
                        if count==25:
                            break
                        count+=1
                        # print(field.name+str(data[table][row][count]))
                    predmet.kafedra=profile.kafedra
                    # print(predmet.__dict__)
                    predmet.prepodavatel=profile
                    predmet.year="2019"
                    predmet.polugodie='2'
                    predmet.status=True#tru если выполена false если план
                    print(predmet.all_values())
                    predmet.save1()



        return redirect('detail_plan',slug=profile.user.username,year=year)
    else:
        return redirect('log')
def kafedra_view(request,kafedra,year):
    if request.user.is_authenticated:
        profile=get_object_or_404(Profile,user=request.user)
        plans=Plan.objects.filter(prepod__kafedra__name=kafedra,year=year)
        kafedri=Kafedra.objects.all()
        if profile.role==2:
            kafedri=Kafedra.objects.filter(name=profile.kafedra.name)
        arr=[]
        # for kaf in kafedri:
        #     arr.append(kaf.fullname)
        # print(arr)
        return render(request, 'strprepod.html',{
        'profile':profile,
        'kafedri':kafedri,
        'plans':plans
        })
    else:
        return redirect('log')
        #выгружаем данные в документ
#формируем список из всех данных и отправляем в скрипт


def documentSave(request,year,slug):

    if request.user.is_authenticated:
            user=User.objects.get(username=slug)
            profile=get_object_or_404(Profile,user=user)
            plan=get_object_or_404(Plan,prepod=profile,year=year)
            data=[]
            #count row for every table
            indexRow=[]

            predmets=Predmet.objects.filter(prepodavatel=profile,polugodie=1,status=False,year=year)
            for p in predmets:
               arr=p.all_values()
               for a in arr:
                   if a=='0':
                       data.append(" ")
                   else:
                       data.append(a)

            indexRow.append(predmets.count())

            # data+=[" "]*(122-(predmets.count()*12))
            ##не забыть впихнуть 11 клеток итогов ра полугодие
            ##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            predmets=Predmet.objects.filter(prepodavatel=profile,polugodie=2,status=False,year=year)
            for p in predmets:
               arr=p.all_values()
               for a in arr:
                   if a=='0':
                       data.append(" ")
                   else:
                       data.append(a)
            indexRow.append(predmets.count())

            predmets=Predmet.objects.filter(prepodavatel=profile,polugodie=1,status=True,year=year)
            itog1=()
            itog2=()
            itogall=()
            for p in predmets:

                arr=p.all_values()
                if arr[0]=='Итого за 1 полугодие:':
                    itog1=arr
                    continue
                for a in arr:
                    if a=='0':
                       data.append(" ")
                    else:
                       data.append(a)
            if itog1:
                for a in itog1:
                    if a=='0':
                       data.append(" ")
                    else:
                       data.append(a)

            indexRow.append(predmets.count())


            ##не забыть впихнуть 11 клеток итогов ра полугодие
            ##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            predmets=Predmet.objects.filter(prepodavatel=profile,polugodie=2,status=True,year=year)
            for p in predmets:
                arr=p.all_values()
                if arr[0]=='Итого за 2 полугодие:':
                    itog2=arr
                    continue
                if arr[0]=='Итого за учебный год:':
                     itogall=arr
                     continue
                for a in arr:
                   if a=='0':
                       data.append(" ")
                   else:
                       data.append(a)
            indexRow.append(predmets.count())
            if itog2:
                for a in itog2:
                    if a=='0':
                       data.append(" ")
                    else:
                       data.append(a)
            if itogall:
                for a in itogall:
                    if a=='0':
                       data.append(" ")
                    else:
                       data.append(a)
            #по месяцам!!
            # data+=[" "]*(375)
            ##normalno po mesyacam
            #u admina dolzhna bit tablisa zapolnena
            mesyac=Mesyac.objects.filter(prepodavatel=profile,year=year)
            for m in mesyac:
                arr=m.all_values()
                for a in arr:
                   if a=='0':
                       data.append(" ")
                   else:
                       data.append(a)




            #учебно метадоч работа
            umr=UMR.objects.filter(prepodavatel=profile,polugodie=1,year=year)
            count=1
            for u in umr:
               arr=u.all_values()
               data.append(str(count))
               for a in arr:
                   if a=='0':
                       data.append(" ")
                   else:
                       data.append(a)
               count+=1
            indexRow.append(umr.count())


            umr=UMR.objects.filter(prepodavatel=profile,polugodie=2,year=year)
            count=1
            for u in umr:
               arr=u.all_values()
               data.append(str(count))
               for a in arr:
                   if a=='0':
                       data.append(" ")
                   else:
                       data.append(a)
               count+=1
            indexRow.append(umr.count())
        #таблица научно исслеовтельских работа
            nir=NIR.objects.filter(prepodavatel=profile,polugodie=1,year=year)
            count=1
            for u in nir:
               arr=u.all_values()
               data.append(str(count))
               for a in arr:
                   if a=='0':
                       data.append(" ")
                   else:
                       data.append(a)
               count+=1
            indexRow.append(nir.count())
            nir=NIR.objects.filter(prepodavatel=profile,polugodie=2,year=year)
            count=1
            for u in nir:
               arr=u.all_values()
               data.append(str(count))
               for a in arr:
                   if a=='0':
                       data.append(" ")
                   else:
                       data.append(a)
               count+=1
            indexRow.append(nir.count())
            #для воспитаттльной работы
            vr=VR.objects.filter(prepodavatel=profile,polugodie=1,year=year)
            count=1
            for u in vr:
               arr=u.all_values()
               data.append(str(count))
               for a in arr:
                   if a=='0':
                       data.append(" ")
                   else:
                       data.append(a)
               count+=1
            indexRow.append(vr.count())

            vr=VR.objects.filter(prepodavatel=profile,polugodie=2,year=year)
            count=1
            for u in vr:
               arr=u.all_values()
               data.append(str(count))
               for a in arr:
                   if a=='0':
                       data.append(" ")
                   else:
                       data.append(a)
               count+=1
            indexRow.append(vr.count())
            #работа ин спец
            inr=INR.objects.filter(prepodavatel=profile,polugodie=1,year=year)
            count=1
            for u in inr:
               arr=u.all_values()
               data.append(str(count))
               for a in arr:
                   if a=='0':
                       data.append(" ")
                   else:
                       data.append(a)
               count+=1
            indexRow.append(inr.count())

            inr=INR.objects.filter(prepodavatel=profile,polugodie=2,year=year)
            count=1
            for u in inr:
               arr=u.all_values()
               data.append(str(count))
               for a in arr:
                   if a=='0':
                       data.append(" ")
                   else:
                       data.append(a)
               count+=1
            indexRow.append(inr.count())
            #для другой работы
            dr=DR.objects.filter(prepodavatel=profile,polugodie=1,year=year)
            count=1
            for u in dr:
               arr=u.all_values()
               data.append(str(count))
               for a in arr:
                   if a=='0':
                       data.append(" ")
                   else:
                       data.append(a)
               count+=1
            indexRow.append(dr.count())

            dr=DR.objects.filter(prepodavatel=profile,polugodie=2,year=year)
            count=1
            for u in dr:
               arr=u.all_values()
               data.append(str(count))
               for a in arr:
                   if a=='0':
                       data.append(" ")
                   else:
                       data.append(a)
               count+=1
            indexRow.append(dr.count())
            #главная таблица
            data+=plan.all_values()


            #shapka
            try:
                docinf=DocInfo.objects.get(plan=plan)
            except:
                docinf=DocInfo(plan=plan)
            listInfo=docinf.all_values()
            # print(indexRow)
            # print(data)
            #

            doc=writeInfoDoc(listInfo,data,indexRow)
            # doc=createDoc('testforsave',data)
            # plan.document.save("testsave",f,save=True)
            file_path=plan.document.path
            f =BytesIO()
            doc.save(f)
            response = HttpResponse(f.getvalue(), content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
            response['Content-Disposition'] = 'inline; filename=plan.docx'
            return response

            # print(data)
            # response = HttpResponse(doc,content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
            # return response
            return redirect('detail_plan',slug=profile.user.username,year=plan.year)

    else:
        return redirect('log')


# выгружаем данные с дока в базу
#пока тест на 1 запись

# listAllTable=takeTable('/home/andrey/Documents/Vazhno_sho_pizdec/mvdproject/mvd/plan/kavesh.docx')
# print(listAllTable[1][0][0])
# form2=Table1Form()
# predmet2=form2.save(commit=False)
# predmet2.kafedra=profile.kafedra
# predmet2.prepodavatel=profile
# predmet2.prepodavatel=profile
# predmet2.leccii=listAllTable[1][0][1]
# predmet2.name=listAllTable[1][0][0]
# if predmet2.name!='':
# predmet2.save()
#закидываем даные с базы в документ
# data=[]
# predmets=list(Predmet.objects.filter(prepodavatel=profile))
# for p in predmets:
#     a=p.all_values()
#     data+=a
#     print(data)
# createDoc('out.docx', data)
#подсчет вcей нагррузки
def mainTableCount(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            profile=get_object_or_404(Profile,user=request.user)
            plan=get_object_or_404(Plan,prepod=profile)
        #заполняем
            umr=UMR.objects.filter(prepodavatel=profile)
            nir=NIR.objects.filter(prepodavatel=profile)
            vr=VR.objects.filter(prepodavatel=profile)
            dr=DR.objects.filter(prepodavatel=profile)
            predmets=Predmet.objects.filter(prepodavatel=profile)
            ucheb_r_1_p=0
            ucheb_r_2_p=0
            ucheb_r_god_p=0
            ucheb_med_r_1_p=0
            ucheb_med_r_2_p=0
            ucheb_med_r_god_p=0
            nir_1_p=0
            nir_2_p=0
            nir_god_p=0
            vr_1_p=0
            vr_2_p=0
            vr_god_p=0
            dr_1_p=0
            dr_2_p=0
            dr_god_p=0
            ucheb_r_1_f=0
            ucheb_r_2_f=0
            ucheb_r_god_f=0
            ucheb_med_r_1_f=0
            ucheb_med_r_2_f=0
            ucheb_med_r_god_f=0
            nir_1_f=0
            nir_2_f=0
            nir_god_f=0
            vr_1_f=0
            vr_2_f=0
            vr_god_f=0
            dr_1_f=0
            dr_2_f=0
            dr_god_f=0
            summ_1_p=0
            summ_2_p=0
            summ_god_p=0
            summ_1_f=0
            summ_2_f=0
            summ_god_f=0
            def __str__(self):
                return self.name
            for p in predmets:
                if p.polugodie==1 and p.status==False:
                    ucheb_r_1_p+=int(p.get_obshaya_nagruzka())
                if p.polugodie==2 and p.status==False:
                    ucheb_r_2_p+=int(p.get_obshaya_nagruzka())
                if p.polugodie==1 and p.status==True:
                    ucheb_r_1_f+=int(p.get_obshaya_nagruzka())
                if p.polugodie==2 and p.status==True:
                    ucheb_r_2_f+=int(p.get_obshaya_nagruzka())

            for u in umr:
                if u.polugodie==1 :
                    ucheb_med_r_1_p+=u.plan
                    ucheb_med_r_1_f+=u.fact
                if u.polugodie==2 :
                    ucheb_med_r_2_p+=u.plan
                    ucheb_med_r_2_f+=u.fact
            for n in nir:
                if n.polugodie==1 :
                    nir_1_p+=n.plan
                    nir_1_f+=n.fact
                if n.polugodie==2 :
                    nir_2_p+=n.plan
                    nir_2_f+=n.fact
            for v in vr:
                if v.polugodie==1 :
                    vr_1_p+=v.plan
                    vr_1_f+=v.fact
                if n.polugodie==2 :
                    vr_2_p+=v.plan
                    vr_2_f+=v.fact
            for d in dr:
                if d.polugodie==1 :
                    dr_1_p+=d.plan
                    dr_1_f+=d.fact
                if n.polugodie==2 :
                    dr_2_p+=d.plan
                    dr_2_f+=d.fact



            plan.ucheb_r_1_p=ucheb_r_1_p
            plan.ucheb_r_2_p=ucheb_r_2_p
            plan.ucheb_r_1_f=ucheb_r_1_f
            plan.ucheb_r_2_f=ucheb_r_2_f
            plan.ucheb_r_god_p=ucheb_r_1_p+ucheb_r_2_p
            plan.ucheb_r_god_f=ucheb_r_1_f+ucheb_r_2_f

            plan.ucheb_med_r_1_p=ucheb_med_r_1_p
            plan.ucheb_med_r_2_p=ucheb_med_r_2_p
            plan.ucheb_med_r_1_f=ucheb_med_r_1_f
            plan.ucheb_med_r_2_f=ucheb_med_r_2_f
            plan.ucheb_med_r_god_p=ucheb_med_r_1_p+ucheb_med_r_2_p
            plan.ucheb_med_r_god_f=ucheb_med_r_1_f+ucheb_med_r_2_f

            plan.nir_1_p=nir_1_p
            plan.nir_1_f=nir_1_f
            plan.nir_2_p=nir_2_p
            plan.nir_2_f=nir_2_f
            plan.nir_god_p=nir_1_p+nir_2_p
            plan.nir_god_f=nir_2_f+nir_2_f

            plan.vr_1_p=vr_1_p
            plan.vr_1_f=vr_1_f
            plan.vr_2_p=vr_2_p
            plan.vr_2_f=vr_2_f
            plan.vr_god_p=vr_1_p+vr_2_p
            plan.vr_god_f=vr_2_f+vr_2_f

            plan.dr_1_p=dr_1_p
            plan.dr_1_f=dr_1_f
            plan.dr_2_p=dr_2_p
            plan.dr_2_f=dr_2_f
            plan.dr_god_p=dr_1_p+dr_2_p
            plan.dr_god_f=dr_2_f+dr_2_f

            plan.summ_1_p=(plan.ucheb_r_1_p+plan.ucheb_med_r_1_p+plan.nir_1_p+
            plan.vr_1_p+plan.dr_1_p)

            plan.summ_2_p=(plan.ucheb_r_2_p+plan.ucheb_med_r_2_p+plan.nir_2_p+
            plan.vr_2_p+plan.dr_2_p)
            plan.summ_god_p=plan.summ_2_p+plan.summ_1_p
            plan.summ_1_f=(plan.ucheb_r_1_f+plan.ucheb_med_r_1_f+plan.nir_1_f+
            plan.vr_1_f+plan.dr_1_f)
            plan.summ_2_f=(plan.ucheb_r_2_f+plan.ucheb_med_r_2_f+plan.nir_2_f+
            plan.vr_2_f+plan.dr_2_f)
            plan.summ_god_f=plan.summ_1_f+plan.summ_2_f
            plan.save()
            return redirect('detail_plan',slug=profile.user.username,year=request.POST['year'])
    else:
        return redirect('log')

#форма основной таблицы
def mainTableSave(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            profile=get_object_or_404(Profile,user=request.user)
            if profile.role==3 or profile.role==2:
                profile=get_object_or_404(Profile,user__username=request.POST['profile'])
            plan=get_object_or_404(Plan,prepod=profile,year=request.POST['year'])
        #заполняем
            # try:
            #
            #     form=MAinTableForm(request.POST,instance=plan)
            #     print(form.errors)
            #     if form.is_valid():
            #         newplan=form.save(commit=False)
            #         predmets=Predmet.objects.filter(prepodavatel=profile)
            #         for p in predmets:
            #             if p.name=="Итого за 1 полугодие:":
            #                 newplan.ucheb_med_r_1_p=p.ucheb_nagruzka
            #             if p.name=="Итого за 2 полугодие:":
            #                 newplan.ucheb_med_r_2_p=p.ucheb_nagruzka
            #         newplan.year=request.POST['year']
            #         newplan.name=plan.name
            #         newplan.save()
            #
            #     else:
            #         print('blen')
            # except:
            #     return render(request,'error.html',{'content':""})

            form=MAinTableForm(request.POST)
            print(form.errors)
            if form.is_valid():

                    newplan=form.save(commit=False)
                    predmets=Predmet.objects.filter(prepodavatel=profile,status=True)
                    for p in predmets:
                        if p.name=="Итого за 1 полугодие:":
                            newplan.ucheb_med_r_1_p=p.ucheb_nagruzka
                            print(newplan.ucheb_med_r_1_p)
                        if p.name=="Итого за 2 полугодие:":
                            newplan.ucheb_med_r_2_p=p.ucheb_nagruzka
                            print(newplan.ucheb_med_r_2_p)
                    newplan.year=request.POST['year']
                    newplan.name=plan.name
                    newplan.prepod=profile
                    print(newplan.name)

                    newplan.save()
                    plan.delete()


            else:
                    print('blen')


        return redirect('detail_plan',slug=profile.user.username,year=request.POST['year'])
    else:
        return redirect('log')
#сохранение первой  таблицы

def saveT1(request):
    if request.user.is_authenticated:
        profile=get_object_or_404(Profile,user=request.user)
        plan=get_object_or_404(Plan,prepod=profile,year=year)
        if request.method=="POST":
            profile=get_object_or_404(Profile,user=request.user)
            Table1FormSet = modelformset_factory(Predmet,form=Table1Form,extra=5)
            formset=Table1FormSet(request.POST,queryset=Predmet.objects.filter(prepodavatel=profile,polugodie=1,status=False))
            # predmets=formset.save()
            #формсет для первого полугодия

            for form in formset:
                if form.is_valid():
                    predmet=form.save(commit=False)
                    predmet.kafedra=profile.kafedra
                    predmet.polugodie=1
                    predmet.status=False
                    print(predmet.get_obshaya_nagruzka())
                    predmet.prepodavatel=profile
                    if predmet.name!='':
                        predmet.save()
                else:
                    print('blen')
        return redirect('detail_plan',slug=profile.user.username,year=plan.year)
    else:
        return redirect('log')
#сохранение 2  таблицы
def saveT2(request):
    if request.user.is_authenticated:
        profile=get_object_or_404(Profile,user=request.user)
        if request.method=="POST":
            profile=get_object_or_404(Profile,user=request.user)
            Table1FormSet = modelformset_factory(Predmet,form=Table1Form,extra=5)
            formset2=Table1FormSet(request.POST,queryset=Predmet.objects.filter(prepodavatel=profile,polugodie=2,status=False))
            # predmets=formset.save()
            #формсет для первого полугодия

            if formset2.is_valid():
                for form in formset2:
                    predmet=form.save(commit=False)
                    predmet.kafedra=profile.kafedra
                    predmet.polugodie=2
                    predmet.status=False
                    print(predmet.get_obshaya_nagruzka())
                    predmet.prepodavatel=profile
                    if predmet.name!='':
                            predmet.save()
            else:
                    print('blen')
        return redirect('detail_plan',slug=profile.user.username,year=request.POST['year'])
    else:
        return redirect('log')

#сохранение 3  таблицы
def saveT3(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            # print(request.POST)

            profile=get_object_or_404(Profile,user=request.user)
            if profile.role==3 or profile.role==2:
                profile=get_object_or_404(Profile,user__username=request.POST['profile'])

            Table1FormSet = modelformset_factory(Predmet,form=Table1Form,extra=5,can_delete=True)
            formset3=Table1FormSet(request.POST,queryset=Predmet.objects.filter(prepodavatel=profile,polugodie=1,status=True))
            # predmets=formset.save()
            #формсет для первого полугодия

            if formset3.is_valid():
                pdel=Predmet.objects.filter(prepodavatel=profile,polugodie=1,status=True)
                for p in pdel:
                    p.delete()
                for form in formset3:
                    predmet=form.save(commit=False)
                    predmet.kafedra=profile.kafedra
                    predmet.polugodie=1
                    predmet.status=True
                    # print(predmet.get_obshaya_nagruzka())
                    predmet.prepodavatel=profile
                    predmet.year=request.POST['year']
                    if predmet.name!='' and predmet.name!='Итого за 1 полугодие:':
                            predmet.save()
                itog=Predmet()
                predmets=Predmet.objects.filter(prepodavatel=profile,polugodie=1,status=True)
                fields=Predmet._meta.get_fields()
                setattr(itog,'status',True)
                setattr(itog,'polugodie',1)
                setattr(itog,'kafedra',profile.kafedra)
                setattr(itog,'year',request.POST['year'])
                setattr(itog,'prepodavatel',profile)


                for field in fields:
                    buff=0
                    if field.name=="id" or field.name=="kafedra" or field.name=="polugodie" or field.name=="status" or field.name=="prepodavatel" or field.name=="year":
                        continue

                    if field.name=="name":
                        setattr(itog,field.name,'Итого за 1 полугодие:')
                        continue
                    for p in predmets:
                        buff+=getattr(p,field.name)
                        # print(getattr(p,field.name))

                    setattr(itog,field.name,buff)
                    # print(str(buff)+field.name)
                itog.save()

            else:
                    print('blen')


        return redirect('detail_plan',slug=profile.user.username,year=request.POST['year'])
    else:
        return redirect('log')



def saveT4(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            profile=get_object_or_404(Profile,user=request.user)
            if profile.role==3 or profile.role==2:
                profile=get_object_or_404(Profile,user__username=request.POST['profile'])
            Table1FormSet = modelformset_factory(Predmet,form=Table1Form,extra=5)
            formset4=Table1FormSet(request.POST,queryset=Predmet.objects.filter(prepodavatel=profile,polugodie=2,status=True))
            # predmets=formset.save()
            #формсет для первого полугодия

            if formset4.is_valid():
                pdel=Predmet.objects.filter(prepodavatel=profile,polugodie=2,status=True)
                for p in pdel:
                    p.delete()
                for form in formset4:
                    predmet=form.save(commit=False)
                    predmet.kafedra=profile.kafedra
                    predmet.polugodie=2
                    predmet.status=True
                    print(predmet.get_obshaya_nagruzka())
                    predmet.prepodavatel=profile
                    predmet.year=request.POST['year']
                    if predmet.name!='' and predmet.name!='Итого за 2 полугодие:' and predmet.name!='Итого за учебный год:':
                        predmet.save()
                itog=Predmet()
                predmets=Predmet.objects.filter(prepodavatel=profile,polugodie=2,status=True)
                fields=Predmet._meta.get_fields()
                setattr(itog,'status',True)
                setattr(itog,'polugodie',2)
                setattr(itog,'kafedra',profile.kafedra)
                setattr(itog,'year',request.POST['year'])
                setattr(itog,'prepodavatel',profile)


                for field in fields:
                    buff=0
                    if field.name=="id" or field.name=="kafedra" or field.name=="polugodie" or field.name=="status" or field.name=="prepodavatel" or field.name=="year":
                        continue

                    if field.name=="name":
                        setattr(itog,field.name,'Итого за 2 полугодие:')
                        print('Итого за 2 полугодие:')
                        continue
                    for p in predmets:
                        buff+=getattr(p,field.name)
                        # print(getattr(p,field.name))

                    setattr(itog,field.name,buff)
                    print(str(buff)+field.name)
                itog.save()
                itogall=Predmet()
                try:
                    itog1=Predmet.objects.get(name="Итого за 1 полугодие:",prepodavatel=profile,polugodie=1,status=True)
                    setattr(itogall,'status',True)
                    setattr(itogall,'polugodie',2)
                    setattr(itogall,'kafedra',profile.kafedra)
                    setattr(itogall,'year',request.POST['year'])
                    setattr(itogall,'prepodavatel',profile)
                    for field in fields:
                        buff=0
                        if field.name=="id" or field.name=="kafedra" or field.name=="polugodie" or field.name=="status" or field.name=="prepodavatel" or field.name=="year":
                            continue

                        if field.name=="name":
                            setattr(itogall,field.name,'Итого за учебный год:')
                            continue
                        setattr(itogall,field.name,(getattr(itog,field.name)+getattr(itog1,field.name)))
                    itogall.save()
                except:
                    setattr(itogall,'status',True)
                    setattr(itogall,'polugodie',2)
                    setattr(itogall,'kafedra',profile.kafedra)
                    setattr(itogall,'year',request.POST['year'])
                    setattr(itogall,'prepodavatel',profile)
                    for field in fields:
                        buff=0
                        if field.name=="id" or field.name=="kafedra" or field.name=="polugodie" or field.name=="status" or field.name=="prepodavatel" or field.name=="year":
                            continue

                        if field.name=="name":
                            setattr(itogall,field.name,'Итого за учебный год:')
                            continue
                        setattr(itogall,field.name,(getattr(itog,field.name)))
                    itogall.save()





            else:

                    print('blen')

        return redirect('detail_plan',slug=profile.user.username,year=request.POST['year'])
    else:
        return redirect('log')
#
#table for umr
def saveT5(request):
    if request.user.is_authenticated:
        profile=get_object_or_404(Profile,user=request.user)
        if request.method=="POST":
            profile=get_object_or_404(Profile,user=request.user)
            if profile.role==3 or profile.role==2:
                profile=get_object_or_404(Profile,user__username=request.POST['profile'])
            Table1FormSet = modelformset_factory(UMR,form=Table2Form,extra=5)
            formset4=Table1FormSet(request.POST,queryset=UMR.objects.filter(prepodavatel=profile,polugodie=1))
            # predmets=formset.save()
            #формсет для первого полугодия

            if formset4.is_valid():
                udel=UMR.objects.filter(prepodavatel=profile,polugodie=1)
                for u in udel:
                    u.delete()
                for form in formset4:
                    umr=form.save(commit=False)
                    umr.polugodie=1
                    umr.prepodavatel=profile
                    umr.year=request.POST['year']
                    if umr.vid!='':
                            umr.save()
            else:
                    print('blen')
        return redirect('detail_plan',slug=profile.user.username,year=request.POST['year'])
    else:
        return redirect('log')


def saveT6(request):
    if request.user.is_authenticated:
        profile=get_object_or_404(Profile,user=request.user)
        if request.method=="POST":
            profile=get_object_or_404(Profile,user=request.user)
            if profile.role==3 or profile.role==2:
                profile=get_object_or_404(Profile,user__username=request.POST['profile'])
            Table1FormSet = modelformset_factory(UMR,form=Table2Form,extra=5)
            formset4=Table1FormSet(request.POST,queryset=UMR.objects.filter(prepodavatel=profile,polugodie=2))
            # predmets=formset.save()
            #формсет для первого полугодия

            if formset4.is_valid():
                udel=UMR.objects.filter(prepodavatel=profile,polugodie=2)
                for u in udel:
                    u.delete()
                for form in formset4:
                    umr=form.save(commit=False)
                    umr.polugodie=2
                    umr.prepodavatel=profile
                    umr.year=request.POST['year']
                    if umr.vid!='':
                            umr.save()
            else:
                    print('blen')
        return redirect('detail_plan',slug=profile.user.username,year=request.POST['year'])
    else:
        return redirect('log')





#tabler foe NIR
def saveT7(request):
    if request.user.is_authenticated:
        profile=get_object_or_404(Profile,user=request.user)
        if request.method=="POST":
            profile=get_object_or_404(Profile,user=request.user)
            if profile.role==3 or profile.role==2:
                profile=get_object_or_404(Profile,user__username=request.POST['profile'])
            Table1FormSet = modelformset_factory(NIR,form=Table3Form,extra=5)
            formset4=Table1FormSet(request.POST,queryset=NIR.objects.filter(prepodavatel=profile,polugodie=1))
            # predmets=formset.save()
            #формсет для первого полугодия

            if formset4.is_valid():
                udel=NIR.objects.filter(prepodavatel=profile,polugodie=1)
                for u in udel:
                    u.delete()
                for form in formset4:
                    umr=form.save(commit=False)
                    umr.polugodie=1
                    umr.prepodavatel=profile
                    umr.year=request.POST['year']
                    if umr.vid!='':
                            umr.save()
            else:
                    print('blen')
        return redirect('detail_plan',slug=profile.user.username,year=request.POST['year'])
    else:
        return redirect('log')

def saveT8(request):
    if request.user.is_authenticated:
        profile=get_object_or_404(Profile,user=request.user)
        if request.method=="POST":
            profile=get_object_or_404(Profile,user=request.user)
            if profile.role==3 or profile.role==2:
                profile=get_object_or_404(Profile,user__username=request.POST['profile'])
            Table1FormSet = modelformset_factory(NIR,form=Table3Form,extra=5)
            formset4=Table1FormSet(request.POST,queryset=NIR.objects.filter(prepodavatel=profile,polugodie=2))
            # predmets=formset.save()
            #формсет для первого полугодия

            if formset4.is_valid():
                udel=NIR.objects.filter(prepodavatel=profile,polugodie=2)
                for u in udel:
                    u.delete()
                for form in formset4:
                    umr=form.save(commit=False)
                    umr.polugodie=2
                    umr.prepodavatel=profile
                    umr.year=request.POST['year']
                    if umr.vid!='':
                            umr.save()
            else:
                    print('blen')
        return redirect('detail_plan',slug=profile.user.username,year=request.POST['year'])
    else:
        return redirect('log')



#table for vr
def saveT9(request):
    if request.user.is_authenticated:
        profile=get_object_or_404(Profile,user=request.user)
        if request.method=="POST":
            profile=get_object_or_404(Profile,user=request.user)
            if profile.role==3 or profile.role==2:
                profile=get_object_or_404(Profile,user__username=request.POST['profile'])
            Table1FormSet = modelformset_factory(VR,form=Table4Form,extra=5)
            formset4=Table1FormSet(request.POST,queryset=VR.objects.filter(prepodavatel=profile,polugodie=1))
            # predmets=formset.save()
            #формсет для первого полугодия

            if formset4.is_valid():
                udel=VR.objects.filter(prepodavatel=profile,polugodie=1)
                for u in udel:
                    u.delete()
                for form in formset4:
                    umr=form.save(commit=False)
                    umr.polugodie=1
                    umr.prepodavatel=profile
                    umr.year=request.POST['year']
                    if umr.vid!='':
                            umr.save()
            else:
                    print('blen')
        return redirect('detail_plan',slug=profile.user.username,year=request.POST['year'])
    else:
        return redirect('log')
def saveT10(request):
    if request.user.is_authenticated:
        profile=get_object_or_404(Profile,user=request.user)
        if request.method=="POST":
            profile=get_object_or_404(Profile,user=request.user)
            if profile.role==3 or profile.role==2:
                profile=get_object_or_404(Profile,user__username=request.POST['profile'])
            Table1FormSet = modelformset_factory(VR,form=Table4Form,extra=5)
            formset4=Table1FormSet(request.POST,queryset=VR.objects.filter(prepodavatel=profile,polugodie=2))
            # predmets=formset.save()
            #формсет для первого полугодия

            if formset4.is_valid():
                udel=VR.objects.filter(prepodavatel=profile,polugodie=2)
                for u in udel:
                    u.delete()
                for form in formset4:
                    umr=form.save(commit=False)
                    umr.polugodie=2
                    umr.prepodavatel=profile
                    umr.year=request.POST['year']
                    if umr.vid!='':
                            umr.save()
            else:
                    print('blen')
        return redirect('detail_plan',slug=profile.user.username,year=request.POST['year'])
    else:
        return redirect('log')


#table for DR

def saveT11(request):
    if request.user.is_authenticated:
        profile=get_object_or_404(Profile,user=request.user)
        if request.method=="POST":
            profile=get_object_or_404(Profile,user=request.user)
            if profile.role==3 or profile.role==2:
                profile=get_object_or_404(Profile,user__username=request.POST['profile'])
            Table1FormSet = modelformset_factory(DR,form=Table5Form,extra=5)
            formset4=Table1FormSet(request.POST,queryset=DR.objects.filter(prepodavatel=profile,polugodie=1))
            # predmets=formset.save()
            #формсет для первого полугодия
            print(formset4.errors)
            if formset4.is_valid():
                udel=DR.objects.filter(prepodavatel=profile,polugodie=1)
                for u in udel:
                    u.delete()
                for form in formset4:
                    umr=form.save(commit=False)
                    umr.polugodie=1
                    umr.prepodavatel=profile
                    umr.year=request.POST['year']
                    if umr.vid!='':
                            umr.save()
            else:
                    print('blen')
        return redirect('detail_plan',slug=profile.user.username,year=request.POST['year'])
    else:
        return redirect('log')

def saveT12(request):
    if request.user.is_authenticated:
        profile=get_object_or_404(Profile,user=request.user)
        if request.method=="POST":
            profile=get_object_or_404(Profile,user=request.user)
            if profile.role==3 or profile.role==2:
                profile=get_object_or_404(Profile,user__username=request.POST['profile'])
            Table1FormSet = modelformset_factory(DR,form=Table5Form,extra=5)
            formset4=Table1FormSet(request.POST,queryset=DR.objects.filter(prepodavatel=profile,polugodie=2))
            # predmets=formset.save()
            #формсет для первого полугодия
            print(request.POST['year'])
            print(formset4.errors)
            if formset4.is_valid():
                udel=DR.objects.filter(prepodavatel=profile,polugodie=2)
                for u in udel:
                    u.delete()
                for form in formset4:
                    umr=form.save(commit=False)
                    umr.polugodie=2
                    umr.prepodavatel=profile
                    umr.year=request.POST['year']
                    if umr.vid!='':
                            umr.save()
            else:
                    print('blen')
        return redirect('detail_plan',slug=profile.user.username,year=request.POST['year'])
    else:
        return redirect('log')
        #иностранные слушателями
def saveT13(request):
    if request.user.is_authenticated:
        profile=get_object_or_404(Profile,user=request.user)
        if request.method=="POST":
            profile=get_object_or_404(Profile,user=request.user)
            if profile.role==3 or profile.role==2:
                profile=get_object_or_404(Profile,user__username=request.POST['profile'])
            Table1FormSet = modelformset_factory(INR,form=Table6Form,extra=5)
            formset4=Table1FormSet(request.POST,queryset=INR.objects.filter(prepodavatel=profile,polugodie=1))
            # predmets=formset.save()
            #формсет для первого полугодия
            print(request.POST['year'])
            print(formset4.errors)
            if formset4.is_valid():
                udel=INR.objects.filter(prepodavatel=profile,polugodie=1)
                for u in udel:
                    u.delete()
                for form in formset4:
                    umr=form.save(commit=False)
                    umr.polugodie=1
                    umr.prepodavatel=profile
                    umr.year=request.POST['year']
                    if umr.vid!='':
                            umr.save()
            else:
                    print('blen')
        return redirect('detail_plan',slug=profile.user.username,year=request.POST['year'])
    else:
        return redirect('log')

def saveT14(request):
    if request.user.is_authenticated:
        profile=get_object_or_404(Profile,user=request.user)
        if request.method=="POST":
            profile=get_object_or_404(Profile,user=request.user)
            if profile.role==3 or profile.role==2:
                profile=get_object_or_404(Profile,user__username=request.POST['profile'])
            Table1FormSet = modelformset_factory(INR,form=Table6Form,extra=5)
            formset4=Table1FormSet(request.POST,queryset=INR.objects.filter(prepodavatel=profile,polugodie=2))
            # predmets=formset.save()
            #формсет для первого полугодия
            print(request.POST['year'])
            print(formset4.errors)
            if formset4.is_valid():
                udel=INR.objects.filter(prepodavatel=profile,polugodie=2)
                for u in udel:
                    u.delete()
                for form in formset4:
                    umr=form.save(commit=False)
                    umr.polugodie=2
                    umr.prepodavatel=profile
                    umr.year=request.POST['year']
                    if umr.vid!='':
                            umr.save()
            else:
                    print('blen')
        return redirect('detail_plan',slug=profile.user.username,year=request.POST['year'])
    else:
        return redirect('log')



def deltable(request):
    if request.user.is_authenticated and request.method=='POST':
        print(request.POST)
    return JsonResponse("1",safe=False)
def spravka(request):
    if request.user.is_authenticated:

        return render( request,'spravka.html')
    else:
        return redirect('log')

#сохранение шапки
def shapka(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            profile=get_object_or_404(Profile,user=request.user)
            if profile.role==3 or profile.role==2:
                profile=get_object_or_404(Profile,user__username=request.POST['profile'])
            plan=get_object_or_404(Plan,prepod=profile,year=request.POST['year'])
            form=ShapkaForm(request.POST)
            print(request.POST)

            if form.is_valid():
                try:
                    shpkdel=get_object_or_404(DocInfo,plan=plan)
                    shpkdel.delete()
                except:
                    print("ne")

                shpk=form.save(commit=False)
                shpk.plan=plan
                shpk.save()
                kolvomes=request.POST['kolvomes']
                try:
                    rating =Rating.objects.get(year=request.POST['year'],profile=profile)
                    rating.kolvomes=kolvomes
                    rating.save()
                except:
                    rating = Rating()
                    rating.profile=profile
                    rating.kolvomes = kolvomes
                    rating.year = request.POST['year']
                    rating.save()

            else:
                    print('blen')
        return redirect('detail_plan',slug=profile.user.username,year=request.POST['year'])
    else:
        return redirect('log')

def saveMesyac(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            profile=get_object_or_404(Profile,user=request.user)
            if profile.role==3 or profile.role==2:
                profile=get_object_or_404(Profile,user__username=request.POST['profile'])
            plan=get_object_or_404(Plan,prepod=profile,year=request.POST['year'])
            MesyacFormSet = modelformset_factory(Mesyac,form=MesyacForm)
            formset4=MesyacFormSet(request.POST,queryset=Mesyac.objects.filter(prepodavatel=profile,polugodie=1))
            if formset4.is_valid():
                try:
                    mesyacdel=Mesyac.objects.filter(prepodavatel=profile,polugodie=1)
                    for m in mesyacdel:
                        m.delete()

                except:
                    print("ne")

                for form in formset4:
                    umr=form.save(commit=False)
                    umr.prepodavatel=profile
                    umr.kafedra=profile.kafedra
                    umr.year=request.POST['year']
                    umr.save()
            else:
                    print('blen')
        return redirect('detail_plan',slug=profile.user.username,year=request.POST['year'])
    else:
        return redirect('log')


def detail_plan(request,slug,year):
    if request.user.is_authenticated:
        profile=get_object_or_404(Profile,user=request.user)
        profile1=get_object_or_404(Profile,user__username=slug)
        Table0FormSet = modelformset_factory(Predmet,form=Table1Form,extra=0)
        Table1FormSet = modelformset_factory(Predmet,form=Table1Form,extra=5)
        Table2FormSet = modelformset_factory(UMR,form=Table2Form,extra=5)
        Table3FormSet = modelformset_factory(NIR,form=Table3Form,extra=5)
        Table4FormSet = modelformset_factory(VR,form=Table4Form,extra=5)
        Table5FormSet = modelformset_factory(DR,form=Table5Form,extra=5)
        Table6FormSet = modelformset_factory(INR,form=Table6Form,extra=5)
        MesyacFormSet= modelformset_factory(Mesyac,form=MesyacForm)
        plan=get_object_or_404(Plan,prepod=profile1,year=year)
        try:
            querymes=Mesyac.objects.filter(prepodavatel=profile1,year=2019,polugodie=1,status=False)

            if not querymes:
                mesyacprofile=get_object_or_404(Profile,user__username='admin')
                mesyac=MesyacFormSet(queryset=Mesyac.objects.filter(prepodavatel=mesyacprofile,year=2019,polugodie=1,status=False))
            else:
                mesyac=MesyacFormSet(queryset=Mesyac.objects.filter(prepodavatel=profile1,year=year,polugodie=1,status=False))
        except:
            mesyac=MesyacFormSet()
        mainForm=MAinTableForm(instance=plan)
        docForm=docUploadForm()
        formset=Table0FormSet(queryset=Predmet.objects.filter(prepodavatel=profile1,year=year,polugodie=1,status=False))
        formset2=Table0FormSet(queryset=Predmet.objects.filter(prepodavatel=profile1,year=year,polugodie=2,status=False))
        formset3=Table1FormSet(queryset=Predmet.objects.filter(prepodavatel=profile1,year=year,polugodie=1,status=True))
        formset4=Table1FormSet(queryset=Predmet.objects.filter(prepodavatel=profile1,year=year,polugodie=2,status=True))
        formset5=Table2FormSet(queryset=UMR.objects.filter(prepodavatel=profile1,year=year,polugodie=1))
        formset6=Table2FormSet(queryset=UMR.objects.filter(prepodavatel=profile1,year=year,polugodie=2))
        formset7=Table3FormSet(queryset=NIR.objects.filter(prepodavatel=profile1,year=year,polugodie=1))
        formset8=Table3FormSet(queryset=NIR.objects.filter(prepodavatel=profile1,year=year,polugodie=2))
        formset9=Table4FormSet(queryset=VR.objects.filter(prepodavatel=profile1,year=year,polugodie=1))
        formset10=Table4FormSet(queryset=VR.objects.filter(prepodavatel=profile1,year=year,polugodie=2))
        formset11=Table5FormSet(queryset=DR.objects.filter(prepodavatel=profile1,year=year,polugodie=1))
        formset12=Table5FormSet(queryset=DR.objects.filter(prepodavatel=profile1,year=year,polugodie=2))
        formset13=Table6FormSet(queryset=INR.objects.filter(prepodavatel=profile1,year=year,polugodie=1))
        formset14=Table6FormSet(queryset=INR.objects.filter(prepodavatel=profile1,year=year,polugodie=2))
        kafedri=Kafedra.objects.all()
        if profile.role==2:
            kafedri=Kafedra.objects.filter(name=profile.kafedra.name)
        try:
            docinf=DocInfo.objects.get(plan=plan)
            shapka=ShapkaForm(instance=docinf)
        except DocInfo.DoesNotExist:
            shapka=ShapkaForm()
        return render(request, 'detail_plan.html',{
        'mainForm':mainForm,
        'formset': formset,
        'formset2': formset2,
        'formset3': formset3,
        'formset4': formset4,
        'formset5': formset5,
        'formset6': formset6,
        'formset7': formset7,
        'formset8': formset8,
        'formset9': formset9,
        'formset10': formset10,
        'formset11': formset11,
        'formset12': formset12,
        'formset13': formset13,
        'formset14': formset14,
        'kafedri':kafedri,
        'plan':plan,
        'profile':profile,
        'profile1':profile1,
        'shapka':shapka,
        'docForm':docForm,
        'mesyac':mesyac


        })
    else:
        return redirect('log')
