from django.shortcuts import render, redirect
from .forms import DownloadStartForm
from .utils import checkLink, getVid

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
            print(form.cleaned_data)
            return redirect('downloader-info', url=form.cleaned_data)
        else:
            return render(request, "downloader/download_start.html",context=context)


    context = {
        "form":DownloadStartForm(),
        "title":"Download"
    }
    return render(request, "downloader/download_start.html",context=context)

def downloadInfo(request, url=None):
    print(url)
    context = {
        "title":"Download Info"
    }
    return render(request, "downloader/download_info.html", context=context)
