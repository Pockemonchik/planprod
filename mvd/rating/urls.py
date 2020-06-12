
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.conf import settings
from . import views
# Import static if not imported
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

urlpatterns = [
    url(r'^rate_otsenka', views.rate_otsenka),
    url(r'^nach_kaf', views.nach_kaf),
    url(r'^sotr_umr', views.sotr_umr),
    url('kafedras', views.KafedraAllView.as_view()),
    url('profiles', views.ProfileAllView.as_view()),
    url('profilerating', views.ProfileRatingView.as_view()),
    url('profileplace', views.ProfilePlaceView.as_view()),
    url('saveURR', views.SaveURRView.as_view()),
    url('saveORMR', views.SaveORMRView.as_view()),
    url('savePCR', views.SavePCRView.as_view()),
    url('saveMRR', views.SaveMRRView.as_view()),
    url('years', views.YearView.as_view()),

]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL,
    document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
