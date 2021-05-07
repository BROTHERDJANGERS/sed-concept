from django.urls import path
from . import views



urlpatterns = [
    path('', views.goHome),#,name='gohome'),
    path('home/', views.home,name='home'),
    path('upload/', views.upload,name='upload'),

]