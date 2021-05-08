import os
import datetime
from django.shortcuts import render,redirect
from django.template import RequestContext
from django.core.files.storage import FileSystemStorage
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from .models import add_Doc
#from django.conf import settings

# Create your views here.

def auth(request):
    if not request.user.is_authenticated:
        return redirect('login')
        #return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        return redirect('home')

def home(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            files = os.listdir(path="./media/")
            count = len(files)
            return render(request, 'home/home.html', {
                'count': count 

            })   
        return render(request,'home/home.html')
    else:
        return redirect('login')
    
   

def upload(request): # страница загрузки
    if request.method == 'POST' and request.FILES:
        # получаем загруженный файл
        username = request.user.username
        file = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        file_url = fs.url(filename)
        d = datetime.datetime.now()
        add_Doc.objects.create(title=filename, user_upload = username)
        Actions_user.objects.create(action_name="Загрузка файла", time=d,)
        return render(request, 'home/upload.html' ,
        {
            'file_url': file_url
        })

    return render(request,'home/upload.html')

def all_docs(request):
    return render(request,'home/all_docs.html')

def view_docs(request):
    return render(request,'home/view_docs.html')

def get_history(request):
    actions = Actions_user.objects.all()
    return render(request,'home/history.html', {'actions': actions})

def history(request):
    history_add_doc = add_Doc.objects.all()
    return render(request,'home/history.html', {'history_add_doc': history_add_doc})

def settings(request):
    return render(request,'home/settings.html')

def err404(request,exaptions,template_name='errs/404-page.html'):
    response = render(request, template_name)
    response.status_code = 404
    return response  