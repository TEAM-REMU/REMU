from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('404', views.errorPage, name="404"),
    path('mv/', include('mv.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('director.urls')),
    path('search/', include('search.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
