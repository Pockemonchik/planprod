
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



]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL,
    document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
