from django.shortcuts import render
from .forms import DownloadStartForm
from .utils import checkLink
import youtube_dl
from django.conf import settings
from django.core import serializers
from django.http import JsonResponse
from django.contrib.staticfiles.storage import staticfiles_storage
import os, shutil
import random

# Create your views here.

def downloading(request):
    if request.is_ajax and request.method == "POST":
        form = DownloadStartForm(request.POST)
        if form.is_valid():
            ser_instance = serializers.serialize('json', [ instance, ])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
    return JsonResponse({"error": ""}, status=400)

def downloader(request):
    form = DownloadStartForm()
    context = {
    "form":form,
    "title":"Download",
    "downloadLink":"none",
    "error":"none"
}
    if request.POST:
        ydl_opts = {
            "format":"bestaudio/best",
            'noplaylist' : True,
            "postprocessors":[{
                "key":"FFmpegExtractAudio",
                "preferredcodec":"mp3",
                "preferredquality":"192",
            }],
        }
        try:
            if request.POST["link"] != "":
                print("downloading"+request.POST["link"])
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([request.POST["link"]])
                print("Finished Downloading")
                print("Moving")
                fileName = "song"+str(random.randint(0,100000))+".mp3"
                for file in os.listdir("./"):
                    if file.endswith(".mp3"):
                        os.rename(file,fileName)
                        shutil.move(fileName,"static/downloader/")
                        context["downloadLink"] = "/static/downloader/" + fileName
        except:
            context["error"] = "Yeah, I programmed this poorly, please try again or another link :)"
    return render(request, "downloader/download_start.html",context=context)