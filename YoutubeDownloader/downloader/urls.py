from django.contrib import admin
from django.urls import path, include
from .views import downloader
from .views import downloading

urlpatterns = [
    path('', downloader,name="downloader-start"),
    path('ajax/', downloading, name="downloading")
]