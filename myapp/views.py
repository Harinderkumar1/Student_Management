from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import *
from .forms import *
# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('show')
        else:
            messages.info(request,'Invalid Username/Password')
            return redirect('login')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']

        if password==password2:
            user=User.objects.create_user(username=username,email=email,password=password)
            user.save()
            return redirect('login')
        else:
            messages.info(request,'Try Matching Password')
            return redirect('signup')
    return render(request,'signup.html')

@login_required(login_url='login')
def std(request):
    form=studentform()
    if request.method=='POST':
        form=studentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
    return render(request,'index.html',{'form':form})

@login_required(login_url='login')
def show(request):
    data=student.objects.all()
    return render(request,'show.html',{'data':data})


def delete(request,id):
    data=student.objects.get(id=id)
    data.delete()
    return redirect('show')

@login_required(login_url='login')
def update(request,id):
    data=student.objects.get(id=id)
    if request.method=='GET':
        form=studentform(instance=data)
        return render(request,'index.html',{'form':form})
    else:
        form=studentform(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect('show')
        return redirect('show')
