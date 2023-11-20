# yourappname/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, HttpResponseRedirect,redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .utils import *
from django.core.management.utils import get_random_secret_key
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect


# def my_view(request):
#     print("ojassss")
#     return HttpResponse("Hello, this is my view!")


# def user_info(request):
#     print("i am user info view")
#     context={'name':'Rahul'}
#     return TemplateResponse(request,'user.html',context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # print(username,"views..............")
           
        else:
            # Form is not valid, handle accordingly
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def log(request):
    return render(request,"logout.html")


def home_views(request):
    return render(request,'home.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/') 

