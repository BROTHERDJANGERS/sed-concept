from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import HttpResponseRedirect



def accounts(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		return redirect('login')


def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				auth.login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Логин или Пароль введен неверно.')

		context = {}
		return render(request, 'registration/login.html', context)	


def logoutUser(request):
	logout(request)
	return redirect('login')




