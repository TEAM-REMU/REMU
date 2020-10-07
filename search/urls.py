
from django.contrib import admin
from django.urls import path
import search.views

app_name = 'search_app'

urlpatterns = [
    path('', search.views.result, name="result"),
]
