from django.urls import path
from . import views



urlpatterns = [
    path('', views.goHome),#,name='gohome'),
    path('home/', views.home,name='home'),
    path('home/upload/', views.upload,name='upload'),
    path('home/view_docs/', views.view_docs,name='view_docs'),
    path('home/settings/', views.settings,name='settings'),

]