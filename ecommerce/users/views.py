from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from .auth import redirect_if_logged_in
from django.core.mail import send_mail
from django.conf import settings



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
@redirect_if_logged_in
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Login Successful")

                if user.is_staff:
                    return redirect('dashboard_product_lists')
                else:
                    next_url = request.GET.get('next', '/')
                    return redirect(next_url)
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid form submission")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

    
  
    
# logout view
def logout_view(request):
    logout(request)
    messages.success(request,"You have been logged out.")
    return redirect('login')

# contact us view
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        full_message = f"""
        You have received a new message from {name}.
        Email: {email}

        Message:
        {message}
        """

        send_mail(
            subject=f"Contact Us Message from {name}",
            message=full_message,
            from_email=settings.EMAIL_HOST_USER,   
            recipient_list=['ems78352@gmail.com'],  
            fail_silently=False
        )

        return render(request, 'contact.html', {'success': True})

    return render(request, 'contact.html')

