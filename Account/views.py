from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import User
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required




# Create your views here.


def REGISTER(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        if request.method == 'POST':
            first_name = request.POST.get('first-name')
            last_name = request.POST.get('last-name')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm-password')
            email = request.POST.get('email')
            # print(first_name)
            # print(last_name)
            # print(password)
            # print(confirm_password)
            # print(email)
            if password != confirm_password:
                messages.error(request, "Password is not matching")
                return redirect('register')
            
            email_exist = User.objects.filter(email=email)

            if not email_exist:
                user = User.objects.create_user(first_name=first_name, last_name=last_name,password=password, email=email)
                user.is_active = True
                user.save()
                return redirect('login')

            else:
                messages.error(request, "This e-mail is already taken")
                return redirect('register')

    return render(request, 'Account/reg.html')


def LOGIN(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    
    else:
        if request.method=='POST':
            email= request.POST.get('email')
            password = request.POST.get('password')
            print(password)
            print(email)
            user = authenticate(request, email=email, password=password)
            print(user)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful")
                return redirect('homepage')
            
            else:
                messages.error(request, "Account not found! Incorrect e-mail or password")
                return redirect('login')
            
    return render(request, 'Account/login.html')

@login_required
def LOGOUT(request):
    logout(request)
    return redirect('homepage')