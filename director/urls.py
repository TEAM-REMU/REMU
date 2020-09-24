
from django.contrib import admin
from django.urls import path
import director.views

urlpatterns = [
    #path('', director.views.director_list, name="director_list"),
    path('director/<int:id>', director.views.director_profile, name="director_profile"),
    path('production/<int:id>', director.views.production_profile, name="production_profile"), 
    
]
