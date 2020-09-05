
from django.contrib import admin
from django.urls import path
import director.views

urlpatterns = [
    path('director', director.views.director_list, name="director_list"),
    path('director/<int:id>', director.views.director_profile, name="director_profile"),
]
