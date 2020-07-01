from django.shortcuts import render
from .forms import DownloadStartForm
from .utils import checkLink

# Create your views here.

def downloader(request):
    if request.method == "POST":
        form = DownloadStartForm(request.POST)
        context = {
        "form":form,
        "title":"Download"
        }
        print("RE")
        if form.is_valid():
            print("VALIUD")
        else:
            return render(request, "downloader/download_start.html",context=context)


    context = {
        "form":DownloadStartForm(),
        "title":"Download"
    }
    return render(request, "downloader/download_start.html",context=context)