from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import UploadForm
from .models import Doc
 
def index(request):
    return render(request, "index.html")

def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        namefile = request.POST.get('name')
        fs = FileSystemStorage()
        filename = fs.save(namefile, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'upload.html')