import os
from django.shortcuts import render,redirect
from django.template import RequestContext
from django.core.files.storage import FileSystemStorage
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from .models import Doc

# Create your views here.


def goHome(request):
    
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return redirect('login')

def home(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            files = os.listdir(path="./media/docs")
            count = len(files)
            return render(request, 'home/home.html', {
                'count': count 

            })   
        return render(request,'home/home.html')
    else:
        return redirect('login')
    
   

def upload(request):
    if request.method == 'POST' and request.FILES:
        # получаем загруженный файл
        file = request.FILES['myfile']
        fs = FileSystemStorage()
        Doc.objects.create(title='some title', doc=request.FILES['myfile'])
        # сохраняем на файловой системе
        #filename = fs.save(file.name, file)
        # получение адреса по которому лежит файл
        #file_url = fs.url(filename)
        
        return render(request, 'home/upload.html') 
        #{
         #   'file_url': file_url
        #})

    return render(request,'home/upload.html')

def view_docs(request):
    return render(request,'home/view_docs.html')

def settings(request):
    return render(request,'home/settings.html')

def err404(request,exaptions,template_name='errs/404-page.html'):
    response = render(request, template_name)
    response.status_code = 404
    return response  