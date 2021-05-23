from django.urls import path
from . import views



urlpatterns = [
    #path('', views.auth,name='home'),
    path('', views.home,name='home'),
    path('upload/', views.upload,name='upload'),
    path('all_docs/', views.all_docs,name='all_docs'),
    #path('all_docs/view_docs', views.view_docs,name='list_docs'),
    path('settings/', views.settings,name='settings'),
    path('history/', views.history,name='history'),

]