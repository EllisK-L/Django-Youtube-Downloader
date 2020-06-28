from django.contrib import admin
from django.urls import path, include
from .views import downloader

urlpatterns = [
    path('', downloader,name="downloader-start"),
]