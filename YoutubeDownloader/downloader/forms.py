from django import forms

class DownloadStartForm(forms.Form):
    link = forms.CharField(label="Youtube Link",max_length=1000,widget=forms.TextInput(attrs={
        "class":"form-control",
        "id":"download_link_input",
        "placeholder":"https://youtube.com/......"
    }))