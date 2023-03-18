from django.contrib import admin
from django.urls import path
from .views import hero, base

urlpatterns = [
    path("", hero, name='hero'),
    path("base/", base, name='base')
]