
from django.contrib import admin
from django.urls import path
import director.views

urlpatterns = [
<<<<<<< HEAD
    path('director', director.views.director_list, name="director_list"),
    path('director/<int:id>', director.views.director_profile, name="director_profile"),
=======
    #path('', director.views.director_list, name="director_list"),
    # path('director/<int:id>', director.views.director_profile, name="director_profile"),
    # path('production/<int:id>', director.views.production_profile, name="production_profile"), 
    # path('director/<int:id>/popular_ordered_mv', director.views.popular_ordered_mv_of_director, name="popular_ordered_mv_of_director"),
    # path('director/<int:id>/latest_ordered_mv', director.views.latest_ordered_mv_of_director, name="latest_ordered_mv_of_director"),
    # path('production/<int:id>/popular_ordered_mv', director.views.popular_ordered_mv_of_production, name="popular_ordered_mv_of_production"),
    # path('production/<int:id>/latest_ordered_mv', director.views.latest_ordered_mv_of_production, name="latest_ordered_mv_of_production"),
    path('director/<int:id>/popular_ordered_mv', director.views.director_profile, name="popular_ordered_mv_of_director"),
    path('director/<int:id>/latest_ordered_mv', director.views.director_profile, name="latest_ordered_mv_of_director"),
    path('production/<int:id>/popular_ordered_mv', director.views.production_profile, name="popular_ordered_mv_of_production"),
    path('production/<int:id>/latest_ordered_mv', director.views.production_profile, name="latest_ordered_mv_of_production"),
>>>>>>> d4d16c5cb78c5af8ee440b2499b449ac94455174
]
