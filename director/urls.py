
from django.contrib import admin
from django.urls import path
import director.views

urlpatterns = [
    path('directorList', director.views.directorList, name="directorList"),
    path('directorProfile', director.views.directorProfile, name="directorProfile"),
]
