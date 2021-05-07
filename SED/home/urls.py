from django.urls import path
from . import views



urlpatterns = [
    path('', views.auth),#,name='gohome'),
    path('home/', views.home,name='home'),
    path('home/upload/', views.upload,name='upload'),
  
]