from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import loginform
from .auth import unauthenticated_user


# Create your views here.
@unauthenticated_user
def register_user(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'User Registered Successfully')
            return redirect('/')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to register user')
            return render(request, 'accounts/register.html')
    context = {
        'form': UserCreationForm

    }
    return render(request, 'accounts/register.html', context)

@unauthenticated_user
def login_user(request):
    if request.method == 'POST':

        form = loginform(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])

            if user is not None:
                if not user.is_staff:

                    login(request, user)
                    return redirect('/products')
                elif user.is_staff:
                    login(request,user)
                    return redirect('/admin-dashboard')
            else:
                messages.add_message(request, messages.ERROR, 'Username or password is invalid')
                return render(request, 'accounts/login.html')

    context = {

        'form': loginform
    }

    return render(request, 'accounts/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('/')
