from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.auth import admin_only
from products.models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

@login_required
@admin_only
def admin_dashboard(request):
    student = Student.objects.all()
    student_count = student.count()
    files = FileUpload.objects.all()
    files_count = files.count()
    users = User.objects.all()
    user_count = users.filter(is_staff=0).count()
    admin_count = users.filter(is_staff=1).count()
    context = {
        'student': student_count,
        'file': files_count,
        'user': user_count,
        'admins': admin_count
    }
    return render(request, 'admins/adminDashboard.html', context)


@login_required
@admin_only
def get_user(request):
    user_all = User.objects.all()
    users = user_all.filter(is_staff=0)
    context = {
        'users': users,
    }
    return render(request, 'admins/showUser.html', context)


@login_required
@admin_only
def update_user_to_admin(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_staff = True
    user.save()
    messages.add_message(request, messages.SUCCESS, 'User has been updated to Admin')
    return redirect('/admin-dashboard')

@login_required
@admin_only
def register_user_admin(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'User Registered Successfully')
            return redirect('/admin-dashboard')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Please provide correct details')
            return render(request, "admins/register-user-admin.html", {'form': form})
    context = {
        'form': UserCreationForm
    }
    return render(request, 'admins/register-user-admin.html', context)