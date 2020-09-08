"""mvd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.conf import settings
from . import views
# Import static if not imported
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^supertable', views.supertable,name='supertable'),
    url(r'^createratinghome/$', views.createratinghome,name='createratinghome'),
    url(r'^createrating/(?P<slug>[\w-]+)/(?P<year>\d{4})/$', views.createrating, name='createrating'),
    url(r'^createplan/$', views.createplan,name='createplan'),

    url(r'^profileinfo/$', views.profileinfo,name='profileinfo'),
    url(r'^saveMesyac/$', views.saveMesyac,name='saveMesyac'),

    url(r'^deluser/$', views.deluser,name='deluser'),
    url(r'^createUser/$', views.adduser,name='adduser'),
    url(r'^editUser/$', views.changepass, name='changepass'),



    url(r'^spravka/$', views.spravka,name='spravka'),
    url(r'^docxobr/$', views.docxobr,name='docxobr'),
    url(r'^exelobr/$', views.exelobr,name='exelobr'),
    url(r'^exelobrfact/$', views.exelobrfact,name='exelobrfact'),
    url(r'^deleteNgruzka/(?P<year>\d{4})/$', views.deleteNgruzka,name='deleteNgruzka'),
    url(r'^saveDB/$', views.saveDB,name='saveDB'),
    url(r'^nagruzkafact/(?P<slug>[\w-]+)/(?P<year>\d{4})/$', views.nagruzkafact,name='nagruzkafact'),
    url(r'^nagruzka/(?P<slug>[\w-]+)/(?P<year>\d{4})/$', views.nagruzka,name='nagruzka'),
    url(r'^documentSave/(?P<slug>[\w-]+)/(?P<year>\d{4})/$', views.documentSave,name='documentSave'),
    url(r'^plan/(?P<slug>[\w-]+)/(?P<year>\d{4})/$', views.detail_plan,name='detail_plan'),
    url(r'^(?P<kafedra>[\w-]+)/(?P<year>\d{4})/$', views.kafedra_view,name='kafedra_view'),
    url(r'^saveMain/$', views.mainTableSave,name='mainTableSave'),
    url(r'^mainTableCount/$', views.mainTableCount,name='mainTableCount'),
    url(r'^saveT1/$', views.saveT1,name='saveT1'),
    url(r'^saveT2/$', views.saveT2,name='saveT2'),
    url(r'^saveT3/$', views.saveT3,name='saveT3'),
    url(r'^saveT4/$', views.saveT4,name='saveT4'),
    url(r'^saveT5/$', views.saveT5,name='saveT5'),
    url(r'^saveT6/$', views.saveT6,name='saveT6'),
    url(r'^saveT7/$', views.saveT7,name='saveT7'),
    url(r'^saveT8/$', views.saveT8,name='saveT8'),
    url(r'^saveT9/$', views.saveT9,name='saveT9'),
    url(r'^saveT10/$', views.saveT10,name='saveT10'),
    url(r'^saveT11/$', views.saveT11,name='saveT11'),
    url(r'^saveT12/$', views.saveT12,name='saveT12'),
    url(r'^saveT13/$', views.saveT13,name='saveT13'),
    url(r'^saveT14/$', views.saveT14,name='saveT14'),
    url(r'^documentAnalize/$', views.documentAnalize,name='documentAnalize'),

    url(r'^nagruzkaSave/$', views.nagruzkaSave,name='nagruzkaSave'),
    url(r'^shapka/$', views.shapka,name='shapka'),
    url(r'^update_plan_summ/(?P<slug>[\w-]+)/(?P<year>\d{4})$', views.update_plan_summ,name='update_plan_summ'),

    url(r'^deltable/$', views.deltable,name='deltable'),



]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL,
    document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
