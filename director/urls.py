
from django.contrib import admin
from django.urls import path
import director.views

urlpatterns = [
<<<<<<< HEAD
    path('directorList', director.views.directorList, name="directorList"),
    path('directorProfile', director.views.directorProfile, name="directorProfile"),
=======
    path('director', director.views.director_list, name="director_list"),
    path('director/<int:id>', director.views.director_profile, name="director_profile"),
>>>>>>> 5070472aade9d541d55f1a4f25bd1d1e9ccd619f
]
