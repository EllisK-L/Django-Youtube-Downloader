from django.shortcuts import render
from .forms import DownloadStartForm
from .utils import checkLink

# Create your views here.

def downloader(request):
    if request.POST:
        form = reu
        print("RE")
    form = DownloadStartForm()
    context = {
        "form":form,
        "title":"Download"
    }
    return render(request, "downloader/download_start.html",context=context)