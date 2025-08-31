from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request," Registration successful. You can now log in.")
            return render('/')

        else:
            messages.error(request,"Registration failed. Please correct the errors below.")
            return render(request,'register.html',{'form':form})
    else:
        form = UserCreationForm()
        return render(request,'register.html',{'form':form})

