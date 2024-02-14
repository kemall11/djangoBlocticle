from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
def register(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            newUser=User()
            newUser.username=username
            newUser.set_password(password)
            newUser.save()
            login(request,newUser)
            messages.success(request,"başarıyla kayıt oldunuz")
            return redirect("index")
        messages.info(request,"Hatalı giriş")
        return render(request,"register.html",{"form":form})
    else:
        form=RegisterForm()
        return render(request,"register.html",{"form":form})                        
def login1(request):
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
           username=form.cleaned_data.get("username")
           password=form.cleaned_data.get("password") 
           user=authenticate(username=username,password=password)               
           if user is None:
               messages.info(request,"Bilgilerizi doğru girdiğinizden emin olunuz.")
           else:
               login(request,user)
               messages.success(request,"Başarıyla giriş yapıldı.")
               return redirect("index")
        return render(request,"login.html",{"form":form})    
    else:
       form=LoginForm()                          
       return render(request,"login.html",{"form":form})       
def logout1(request):    
    logout(request)
    messages.success(request,"başarıyla çıkış yapıldı")
    return redirect("index")
def changeAccount(request):
    logout(request)
    messages.success(request,"Değiştirmek istediğiniz hesabın bilgilerini giriniz.")
    return redirect("user:login")