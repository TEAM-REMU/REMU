
from django.contrib import admin
from django.urls import path
import accounts.views

urlpatterns = [
    path('signIn', accounts.views.signIn, name="signIn"),
    path('signUp', accounts.views.signUp, name="signUp"),
    path('myPage', accounts.views.myPage, name="myPage")
]
