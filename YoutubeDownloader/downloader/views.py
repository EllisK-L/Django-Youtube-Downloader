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
    filename = ""
    if request.is_ajax and request.method == "POST":
        form = DownloadStartForm(request.POST)
        if form.is_valid():
            error = ""
            url = request.POST["link"]
            ydl_opts = {
                    "format":"bestaudio/best",
                    'noplaylist' : True,
                    "postprocessors":[{
                        "key":"FFmpegExtractAudio",
                        "preferredcodec":"mp3",
                        "preferredquality":"192",
                    }],
                }
            if url != "":
                try:
                    print("downloading "+url)
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([url])
                    print("Finished Downloading")
                    print("Moving")
                    fileName = "song"+str(random.randint(0,100000))+".mp3"
                    for file in os.listdir("./"):
                        if file.endswith(".mp3"):
                            os.rename(file,fileName)
                            shutil.move(fileName,"media/downloader/")
                            filename = "/media/downloader/" + fileName
                except:
                    error = "There was a problem, sorry :/"
            else:
                error = "Did you really try and download nothing -_-"

            # ser_instance = serializers.serialize('json', [ request.POST, ])
            # send to client side.
            if(error != ""):
                return JsonResponse({"error": error}, status=400)
    return JsonResponse({"instance": filename,"error":error}, status=200)





def downloader(request):
    form = DownloadStartForm()
    context = {
    "form":form,
    "title":"Download",
    "downloadLink":"none",
    "error":"none"
}
        
    return render(request, "downloader/download_start.html",context=context)