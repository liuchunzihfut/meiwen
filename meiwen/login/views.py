from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib import auth
import time


def index(request):
    return HttpResponse("Hello, world. You're at the login index.")

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
