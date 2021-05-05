from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home/home.html')


def upload(request):
    return render(request,'home/upload.html')