
from django.contrib import admin
from django.urls import path
import mv.views

urlpatterns = [
    path('mvList', mv.views.mvList, name="mvList"),
    path('mvDetail/<int:id>', mv.views.mvDetail, name="mvDetail"),
]
