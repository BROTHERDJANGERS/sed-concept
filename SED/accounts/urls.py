from django.urls import path
from . import views


urlpatterns = [	
	#path('', views.auth, name="auth"),	
	path('login/', views.loginView, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
   # path('loged/', views.logedr, name="loged"),
   

]