from django.shortcuts import render

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout,authenticate
from django.db.models import Q
from django.contrib import messages

from .forms import RegistrationForm,LoginForm


def signup_page(request):
    if request.method=='POST':
        print(request.POST)
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.filter(
                Q(username=form.cleaned_data['username']) | Q(username=form.cleaned_data['email'])
            )
            if user.exists():
                messages.add_message(request, messages.ERROR, 'User with such email or username already exists')
                return redirect('register')
            new_user = User.objects.create(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                # first_name=form.cleaned_data['first_name'],
                # last_name=form.cleaned_data['last_name']
            )
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            messages.add_message(request, messages.SUCCESS, 'Successfully registered')
            login(request,new_user)
    form = RegistrationForm()
    context = {
        'form':form
    }
    return render(request, 'auth_custom/register.html', context)

def login_page(request):
    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if not user:
                return redirect('login')
                messages.add_message(request, messages.ERROR, 'Wrong credentials!')
            login(request,user)
            return redirect('home')     
            messages.add_message(request, messages.SUCCESS, 'Successfully logged in')
                 
    form = LoginForm()
    context = {
        'form':form
    }
    return render(request,'auth_custom/login.html',context)


def logout_page(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'Successfully logged out')
    return redirect('login')


def profile(request):
    if request.user.is_authenticated:
        return render(request,'main/index.html')
    else:
        return render(request,'auth_custom/login.html')