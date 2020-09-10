from django.contrib import admin
from django.urls import path
import accounts.views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login', accounts.views.login, name="login"),
    path('signup', accounts.views.signup, name="signup"),
    path('my_page/<int:id>', accounts.views.my_page, name="my_page")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
