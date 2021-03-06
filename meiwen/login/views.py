from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from reader.models import Reader, ReaderAdditional

import time


def index(request):
    return HttpResponse("Hello, world. please login before")

def userLogin(request):  
    curtime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime());  
          
    if request.method=='POST':  
        print("POST")  
        username=request.POST.get('name','')
        password=request.POST.get('password','')
        user= auth.authenticate(username=username,password=password)
        if user and user.is_active:  
            auth.login(request, user)
            return HttpResponse("Hello, world. You're login success.")
                
    return HttpResponse("Hello, world. You're login failed.")

def signUp(request):
    username = request.POST.get('name', '')
    password = request.POST.get('password', '')
    email = request.POST.get('email', '')
    if username and password and email:
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        user_new = User.objects.get(username=username)
        reader = Reader(
            reader_id = user_new.id,
            nickname = user_new.username,
            name =user_new.username,
        )
        reader_add = ReaderAdditional(
            reader_id = user_new.id,
        )
        reader.save()
        reader_add.save()
        return HttpResponse("sign up success")
    else:
        return HttpResponse("please write password or email or name")

@login_required(login_url='/login/index/')
def changePassword(request):
    username = request.POST.get('name', '')
    password = request.POST.get('password', '')
    newPassword = request.POST.get('newPassword', '')
    user = auth.authenticate(username=username,password=password)
    if user and user.is_active:
        user = User.objects.get(username=username)
        user.set_password(newPassword) 
        user.save()
        return HttpResponse("change password success")
    return HttpResponse("user not active")

@login_required(login_url='/login/login/')
def logout(request):
    auth.logout(request)
    return HttpResponse("logout success")

@login_required(login_url='/login/login/')
def test(request):
    return HttpResponse('test success')
