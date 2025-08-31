from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.

# User Registration
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request," Registration successful. You can now log in.")
            return redirect('/')

        else:
            messages.error(request,"Registration failed. Please correct the errors below.")
            
    else:
        form = UserCreationForm()
        return render(request,'register.html',{'form':form})

# Login View 
def login_view(request):
    if request.method =="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"Login Successful")
                return redirect('/')
            else:
                messages.error(request,"Invalid username or password")
    else:
        form = LoginForm()
        return render(request,'login.html',{'form':form})
