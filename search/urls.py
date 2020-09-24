
from django.contrib import admin
from django.urls import path
import search.views

urlpatterns = [
    path('', search.views.result, name="result"),
]
