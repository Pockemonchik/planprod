#from background_task import background
from django.shortcuts import render, redirect, get_object_or_404
from plan.models import Profile,Kafedra,Plan,Predmet,NIR,VR,DR,UMR,INR,Nagruzka,DocInfo
from plan.forms import ShapkaForm,Table1Form,Table2Form,Table3Form,Table4Form,Table6Form,Table5Form,MainTableForm,Table1UploadForm,NagruzkaForm
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
from plan.Parser_and_overview import createDoc2,createDoc,takeTable,takeXls,writeInfoDoc,xlsPrepod
from django.core.files.base import ContentFile
from django.core.files import File
from django.contrib.auth.models import User
from django.conf import settings
from django.http import HttpResponse
import random
from docx import Document
import os

#exec(open('plan/tasks.py', encoding='utf-8').read())

"""Функции для заполнения бд из нагрузок"""
def zapolnenie_bd():
    print('Введите название папки в с файлами в plan/, ./dir например (paht to dir with files)')
    path_input = str(input())
    path = "./plan/"+ path_input
    file_list = os.listdir(path)
    print(file_list)
    print('Введите тип нагрузки 0=планируемая,1=фактическая(type of nagtuzka)')
    type = int(input())
    print('Введите год нагрузки, 2019 например (year of nagtuzka)')
    year = int(input())
    data = None
    for file_name in file_list:
        print(file_name)
        kafedra = None
        try:
            if "АП" in file_name:
                kafedra = Kafedra.objects.get(fullname="администр.права")
            if "АД" in file_name:
                kafedra = Kafedra.objects.get(fullname="администрат.деят.ОВД")
            if "ГиТП" in file_name:
                kafedra = Kafedra.objects.get(fullname="граж.и труд.права,гражд.процесса")
            if "ДОУ" in file_name:
                kafedra = Kafedra.objects.get(fullname="деят. ОВД в ОУ")
            if "ИД" in file_name:
                kafedra = Kafedra.objects.get(fullname="исслед. докум.")
            if "Ин яз" in file_name:
                kafedra = Kafedra.objects.get(fullname="иностр. языков")
            if "ИиМ" in file_name:
                kafedra = Kafedra.objects.get(fullname="инф. и мат.")
            if "ИБ" in file_name:
                kafedra = Kafedra.objects.get(fullname="информац. без-ти")
            if "ИГиП" in file_name:
                kafedra = Kafedra.objects.get(fullname="истории гос.и пр.")
            if "КиМП" in file_name:
                kafedra = Kafedra.objects.get(fullname="конст.и муниц.пр.")
            if "Криминалистика" in file_name:
                kafedra = Kafedra.objects.get(fullname="криминалистики")
            if "Криминология" in file_name:
                kafedra = Kafedra.objects.get(fullname="криминологии")
            if "ОП" in file_name:
                kafedra = Kafedra.objects.get(fullname="огневой подгот.")
            if "ОРД" in file_name:
                kafedra = Kafedra.objects.get(fullname="ОРД и спец.техники")
            if "ОиТ" in file_name:
                kafedra = Kafedra.objects.get(fullname="оружиевед.и трасологии")
            if "Педагогики" in file_name or "Педагогика" in file_name:
                kafedra = Kafedra.objects.get(fullname="педагогики")
            if "ПЧиМП" in file_name:
                kafedra = Kafedra.objects.get(fullname="прав человека и междун.права")
            if "ПР" in file_name:
                kafedra = Kafedra.objects.get(fullname="предв. расслед.")
            if "психология" in file_name:
                kafedra = Kafedra.objects.get(fullname="психологии")
            if "Русск.яз" in file_name:
                kafedra = Kafedra.objects.get(fullname="русского языка")
            if "СиП" in file_name:
                kafedra = Kafedra.objects.get(fullname="социол.и полит.")
            if "СТ" in file_name:
                kafedra = Kafedra.objects.get(fullname="специальной тактики")
            if "СИТ" in file_name:
                kafedra = Kafedra.objects.get(fullname="спец.инф.технол.")
            if "ТГП" in file_name:
                kafedra = Kafedra.objects.get(fullname="теории гос.и права")
            if "ТКОЭИ" in file_name:
                kafedra = Kafedra.objects.get(fullname="ТКОЭИ")
            if "УП" in file_name:
                kafedra = Kafedra.objects.get(fullname="уголовного права")
            if "Упр" in file_name:
                kafedra = Kafedra.objects.get(fullname="уголовного процесса")
            if "ФП" in file_name:
                kafedra = Kafedra.objects.get(fullname="физ. подготовки")
            if "Философии" in file_name:
                kafedra = Kafedra.objects.get(fullname="философии")
            if "ЭиБУ" in file_name:
                kafedra = Kafedra.objects.get(fullname="экономики и бух.учета")
            if "КЭБФиЭА" in file_name:
                kafedra = Kafedra.objects.get(fullname="эконом.безоп.,финансов и эконом.анализа")
            if "ЭКД" in file_name:
                kafedra = Kafedra.objects.get(fullname="эксп.крим.деят-ти")
            if "Юр псих" in file_name:
                kafedra = Kafedra.objects.get(fullname="юридической психологии")
        except Exception as e:
            print(file_name)

        full_path = os.path.abspath(os.curdir)+'/plan/'+path_input
        # print(full_path)
        profiles = Profile.objects.filter(kafedra=kafedra)
        logs = open("logs.txt",'a')
        status = None
        data = ""
        if type == 0:
            status = False
        else:
            status = True
        for p in profiles:
            if Predmet.objects.filter(prepodavatel=p,year=int(year),status=status).count()>0:
                print('пропускаем '+ p.fullname+' уже есть предметы'+str(Predmet.objects.filter(prepodavatel=p,year=int(year),status=status).count()))
                continue

            try:
                if type == 0:
                    data = takeXls(full_path+'/'+file_name, p.fullname.split(' ',1)[0],True)
                else:
                    data = takeXls(full_path+'/'+file_name, p.fullname.split(' ',1)[0],False)
                if not isinstance(data, list):
                    try:
                       print(p.kafedra.fullname+"  "+p.fullname)
                       print(data)
                       logs.write(p.kafedra.fullname+"  "+p.fullname+ " "+ data+'\n')
                       continue
                    except Exception as e:
                       logs.write(str(e)+" \n")
                try:
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
                                predmet.kafedra=p.kafedra
                                # print(predmet.__dict__)
                                predmet.prepodavatel=p
                                predmet.year=year
                                predmet.polugodie='1'
                                if type == 0:
                                    predmet.status = False
                                else:
                                    predmet.status = True
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
                                    # print("suka2")
                                    setattr(predmet,field.name, data[table][row][count])
                                    # print(count)
                                    if count==25:
                                        break
                                    count+=1

                                predmet.kafedra=p.kafedra
                                # print(predmet.__dict__)
                                predmet.prepodavatel=p
                                predmet.year=year
                                predmet.polugodie='2'
                                if type == 0:
                                    predmet.status = False
                                else:
                                    predmet.status = True
                                #tru если выполена false если план
                                # print(predmet.all_values())
                                predmet.save1()


                    print("успешно обработан план "+p.fullname)
                except Exception as e:
                    logs.write("неудалось в профиле "+ p.fullname + " "+str(e)+'\n')


                    continue

            except Exception as e:

                logs.write(kafedra.fullname +" не прошел документ "+ str(e)+'\n')
                logs.write(full_path + '\\' + file_name + " " + p.fullname.split(' ', 1)[0] + '\n')
                continue
        continue






    # all_profile=Profile.objects.all()
    # all_profile=Profile.objects.filter(kafedra__name='kaf4370')

    # for profile in all_profile:
    #     if profile.role==2:
    #         # if (profile.user.username=="admin" or profile.user.username=="user" or profile.kafedra.fullname=="инф. и мат.":
    #         if profile.kafedra.fullname!="инф. и мат.":
    #             continue
    #         nagruzkadoc=get_object_or_404(Nagruzka,year=2019,kafedra=profile.kafedra)
    #         plan=get_object_or_404(Plan,prepod=profile,year=2019)
    #         predmetsdel=Predmet.objects.filter(prepodavatel=profile,status=False)
    #         predmetsdel.delete()
    #         # print(nagruzkadoc.document.path)
    #         # print(plan.name)
    #


    return 0
def create_plans():
    print("enter year for new plans")
    year = int(input())
    profiles = Profile.objects.all()
    count = 0
    for p in profiles:
        if not Plan.objects.get(prepod=p,year=year):
            newplan = Plan()
            newplan.user = p.user
            newplan.prepod = p
            newplan.year = year

            newplan.name = "".join([p.fullname.split(' ')[0], ' ', p.fullname.split(' ')[1][0], '.',p.fullname.split(' ')[2][0]])
            print("sozadanie plana ")
            count +=1
            #newplan.save()
    print("sozdano "+count+" planov iz " +profiles.count()+"profiley")
zapolnenie_bd()
#create_plans()
print('konets')





