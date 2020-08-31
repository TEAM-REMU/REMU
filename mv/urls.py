
from django.contrib import admin
from django.urls import path
import mv.views

urlpatterns = [
    path('', mv.views.mv_list, name="mvList"),
    path('<int:id>', mv.views.mv_detail, name="mvDetail"),
]
