from django.shortcuts import render
from .forms import DownloadStartForm

# Create your views here.

def downloader(request):
    if request.POST:
        pass
    form = DownloadStartForm()
    context = {
        "form":form,
        "title":"Download"
    }
    return render(request, "downloader/download_start.html",context=context)