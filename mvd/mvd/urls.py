
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.conf import settings
# Import static if not imported
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView


# import debug_toolbar
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^', include('plan.urls')),
    url(r'^rating/', include('rating.urls')),


]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL,
    document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
