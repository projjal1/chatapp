from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

def base(request):
    return render(request,"home.html")
    

def login(request): 
    if request.method=="POST":
        user=auth.authenticate(username=request.POST['username'],password=request.POST['pass1'])
        if (user!=None):
            auth.login(request,user)
            return render(request,"home.html")
        else:
            return render(request,"log.html",{'error':'User does not exist or password is wrong.'})
    else:
        return render(request,"log.html")

def logout(request):
    if request.method=="POST":
        auth.logout(request)
        return render(request,"home.html")


def signup(request):
    if request.method=="POST":
        if request.POST['pass1']==request.POST['pass2']:
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request,'sign.html',{'error':'Sorry, Username already taken.'})
            except User.DoesNotExist:
                user=User.objects.create_user(request.POST['username'],password=request.POST['pass1'])
                auth.login(request,user)
                return render(request,"home.html")

        else:
            return render(request,'sign.html',{'error':'Sorry, Passwords do not match.'}) 
    else:
        return render(request,'sign.html')


