
from django.contrib import admin
from django.urls import path
import director.views

urlpatterns = [
    path('directorList', director.views.directorList, name="directorList"),
    path('directorProfile/<int:id>', director.views.directorProfile, name="directorProfile"),
]
