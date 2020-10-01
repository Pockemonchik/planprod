# from django.test import TestCase


from django.shortcuts import render, redirect, get_object_or_404
from models import Profile,Kafedra,Plan,Predmet,NIR,VR,DR,UMR,INR,Nagruzka,DocInfo
from forms import ShapkaForm,Table1Form,Table2Form,Table3Form,Table4Form,Table6Form,Table5Form,MAinTableForm,Table1UploadForm,NagruzkaForm
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
from Parser_and_overview import createDoc2,createDoc,takeTable,takeXls,writeInfoDoc,xlsPrepod
from django.core.files.base import ContentFile
from django.core.files import File
from django.contrib.auth.models import User
from django.http import JsonResponse
# from .tasks import saveallnagr

from django.http import HttpResponse
import random
from docx import Document
import os

"""Функции для заполнения бд из нагрузок"""
def zapolnenie_bd():
    print('Введите тип нагрузки 0=планируемая,1=фактическая(type of nagtuzka)')

    while type !=1 or type !=0:
        type = input()
        if type == 0:
            type = False
        elif type == 1:
            type = True
    print('Введите год нагрузки, 2019 например (year of nagtuzka)')
    year = int(input())
    print('Введите путь до папки с файлами, ./dir например (paht to dir with files)')
    path = input()
    file_list = os.listdir(path)
    print(file_list)
    for file in file_list:
        print(file)
    return 0
























# Create your tests here.
# def nepustNagr():
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
    #nepustNagr

    # profiles=Profile.objects.all()
    # count=0
    # for p in profiles:
    #         plan=get_object_or_404(Plan,prepod=p,year=2019)
    #         allpred=p.predmets.all()
    #         if not allpred.exists():
    #             print(p.fullname)
    #             print(p.kafedra.fullname)
    #             count+=1
    # print(count)
    # f = open("users.txt", "w")
    # pr=Profile.objects.all()
    # for p in pr:
    #     f.write(str(p))
    #     f.write('\n')
    # f.close()
    # inf=DocInfo.objects.all()
    # for i in inf:
        # if i.plan.pk=='':
        #     print(i.plan.name)
        # print(str(i.plan.pk)+" "+i.plan.name)

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
