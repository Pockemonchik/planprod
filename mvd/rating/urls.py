
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.conf import settings
from . import views
# Import static if not imported
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

urlpatterns = [
    url(r'^rate_otsenka/(?P<slug>[\w-]+)/(?P<year>\d{4})/$', views.rate_otsenka,name='rate_otsenka'),
    url('profilesfilter', views.ProfileFilterView.as_view()),
    url(r'^nach_kaf', views.nach_kaf,name='nach_kaf'),
    url(r'^sotr_umr', views.sotr_umr,name='sotr_umr'),
    url(r'^documentSaveRating/(?P<year>\d{4})/(?P<slug>[\w-]+)/$', views.documentSave,name='documentSaveRating'),
    url('kafedras', views.KafedraAllView.as_view()),
    url('profiles', views.ProfileAllView.as_view()),
    url('profilerating', views.ProfileRatingView.as_view()),
    url('profileplace', views.ProfilePlaceView.as_view()),
    url('saveURR', views.SaveURRView.as_view(),name='saveURR'),
    url('saveORMR', views.SaveORMRView.as_view(),name='saveORMR'),
    url('savePCR', views.SavePCRView.as_view(),name='savePCR'),
    url('saveMRR', views.SaveMRRView.as_view(),name='saveMRR'),
    url('years', views.YearView.as_view()),
    url('graph', views.GraphView.as_view()),
    url('ratingTable', views.RatingTableView.as_view()),
    url('refresh_rating',views.RefreshRatingView.as_view())

]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL,
    document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
