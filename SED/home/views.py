import os
import datetime
from django.shortcuts import render,redirect
from django.template import RequestContext
from django.core.files.storage import FileSystemStorage
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from .models import add_Doc
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views import  generic
from django.contrib.auth.models import Group



#users_in_group = Group.objects.get(name="group name").user_set.all()
#from django.conf import settings

# Create your views here.

def signature(request):
   title = request.POST["title"]

class viewDoc(PermissionRequiredMixin,generic.DetailView):     
    permission_required = 'home.add_add_doc'
    permission_denied_message = 'У вас нет доступа для загрузки документов'
    model = add_Doc
    


""" def auth(request):
    if not request.user.is_authenticated:
        return redirect('login')
        #return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        return redirect('home') """

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
    if request.user.has_perm('home.add_add_doc'):
        if request.method == 'POST' and request.FILES:
            # получаем загруженный файл
            username = request.user.username
            file = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(file.name, file)
            file_path = fs.url(filename)
            d = datetime.datetime.now()
            #Отправляем данные в базу
            add_Doc.objects.create(action_name="Загрузка файла",title=filename, user_upload = username,create_datetime=d,file_url=file_path)
            #Actions_user.objects.create(action_name="Загрузка файла", time=d,)
            return render(request, 'home/upload.html' ,{'file_path': file_path  })

        return render(request,'home/upload.html')
    else:
        return render(request,'home/error_403.html')

""" def get_file_path(request):
    return render(request{'file_path':file_path}) """



""" def get_history(request):
    actions = Actions_user.objects.all()
    return render(request,'home/history.html', {'actions': actions}) """

def is_member(user):
    return user.groups.filter(name='Metod').exists()

#Вызов объектов class add_Doc / вызов формы
def history(request):
    if request.user.has_perm('home.view_add_doc'):
        history_add_doc = add_Doc.objects.all()
        return render(request,'home/history.html', {'history_add_doc': history_add_doc})
    else:
        return render(request,'home/error_403.html')


    

def all_docs(request):
    if request.user.has_perm('home.view_add_doc'):
        all_add_doc = add_Doc.objects.all()
        return render(request,'home/all_docs.html', {'all_add_doc': all_add_doc})
    else:
        return render(request,'home/error_403.html')

def settings(request):
    return render(request,'home/settings.html')

def err404(request,exaptions,template_name='errs/404-page.html'):
    response = render(request, template_name)
    response.status_code = 404
    return response  


