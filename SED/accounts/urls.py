from django.urls import path
from . import views


urlpatterns = [	
	#path('', views.accounts, name="accounts"),	
	path('login/', views.loginPage, name="login"),  
	path('accounts/logout/', views.logoutUser, name="logout"),
    
   

]