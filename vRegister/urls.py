from django.contrib import admin
from django.urls import path
from .views import login, base

urlpatterns = [
    path("", login, name='login'),
    path("base/", base, name='base')
]