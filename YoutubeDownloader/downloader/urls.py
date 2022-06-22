from django.contrib import admin
from django.urls import path, include
from .views import downloader, downloadInfo

urlpatterns = [
    path('', downloader,name="downloader-start"),
    path('info',downloadInfo, name="downloader-info"),
    path('info/<str:url>',downloadInfo, name="downloader-info")
]