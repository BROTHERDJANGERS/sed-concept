from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

# Create your views here.

def home(request):
    return render(request,'home/home.html')


def upload(request):
    if request.method == 'POST' and request.FILES:
        # получаем загруженный файл
        file = request.FILES['myfile']
        fs = FileSystemStorage()
        # сохраняем на файловой системе
        filename = fs.save(file.name, file)
        # получение адреса по которому лежит файл
        file_url = fs.url(filename)
        return render(request, 'home/home.html', {
            'file_url': file_url
        })
    return render(request,'home/upload.html')