
from django.contrib import admin
from django.urls import path
import mv.views

urlpatterns = [
    path('', mv.views.mvList, name="mvList"),
    path('<int:id>', mv.views.mvDetail, name="mvDetail"),
]
