from django.shortcuts import render, redirect
from .models import Product
from .models import person, Student
from .models import person
from .models import Student
from .models import Article
from .models import Reporter

from .models import FileUpload
from .form import ProductForm
from .form import personform
from .form import FileForm
from .form import ArticleForm
from .form import ReporterForm
from django.http import HttpResponse, request
import os
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .filters import PersonFilter
from accounts.auth import user_only


# Create your views here.
@login_required
@user_only
def indexs(request):
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'products/index.html', context)

@login_required
@user_only
def get_product_form(request):
    form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'products/getproduct.html', context)

@login_required
@user_only
def get_person_form(request):
    form = personform()
    context = {
        'form': form
    }
    return render(request, 'products/getpersonform.html', context)

@login_required
@user_only
def post_student(request):
    if request.method == 'POST':
        data = request.POST
        firstname = data['firstname']
        lastname = data['lastname']
        batch = data['batch']
        category = data['category']
        image_url = data['image_url']
        student = Student.objects.create(firstname=firstname,
                                         lastname=lastname,
                                         batch=batch,
                                         category=category,
                                         image_url=image_url
                                         )
        if student:
            return redirect('/products/getstudents')
        else:
            return HttpResponse("Failed to add student")
    return render(request, 'products/addstudent.html')

@login_required
@user_only
def get_students(request):
    students = Student.objects.all()
    context = {
        'students': students,
        'activate_student': 'active'
    }

    return render(request, 'products/getstudents.html', context)

@login_required
@user_only
def deleteStudent(request, student_id):
    students = Student.objects.get(id=student_id)
    students.delete()
    return redirect('/products/getstudents')

@login_required
def updateStudent(request, student_id):
    students = Student.objects.get(id=student_id)
    if request.method == "POST":
        data = request.POST
        students.firstname = data['firstname']
        students.lastname = data['lastname']
        students.batch = data['batch']
        students.category = data['category']
        students.image_url = data['image_url']
        students.save()
        return redirect('/products/getstudents')
    context = {
        'students': students,
        'activate_student': 'active'
    }
    return render(request, 'products/updateStudents.html', context)

@login_required
@user_only
def get_person_mf(request):
    persons = person.objects.all()
    person_filter=PersonFilter(request.GET,queryset=persons)
    person_final=person_filter.qs
    context = {
        'persons': person_final,
        'activate_personMF': 'active',
        'person_filter':person_filter
    }
    return render(request, 'products/getPersonMF.html', context)

@login_required
def post_person_mf(request):
    if request.method == "POST":
        form = personform(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'person added successfully')
            return redirect('/products/getPersonMF')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to add person')
            return render(request, 'products/postPersonMF.html', {'form': form})
    context = {
        'form': personform,
        'activate_personMF': 'active'

    }
    return render(request, 'products/postPersonMF.html', context)

@login_required
def deletePersonMF(request, person_id):
    persons = person.objects.get(id=person_id)
    persons.delete()
    return redirect('/products/getPersonMF')

@login_required
def updatePersonMF(request, person_id):
    persons = person.objects.get(id=person_id)
    if request.method == 'POST':
        form = personform(request.POST, instance=persons)
        if form.is_valid():
            form.save()
            return redirect('/products/getPersonMF')

    context = {
        'form': personform(instance=persons),
        'activate_personMF': 'active'
    }
    return render(request, 'products/updatePersonMF.html', context)

@login_required
def post_file(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        file = request.FILES.get('file')
        file_obj = FileUpload(title=title, file=file)
        file_obj.save()
        if file_obj:
            return redirect('/products/getFile')
        else:
            return HttpResponse("Files cannot be added")
    context = {
        'activate_file': 'active'
    }
    return render(request, 'products/addFile.html', context)

@login_required
def get_file(request):
    files = FileUpload.objects.all()
    context = {
        'files': files,
        'activate_file': 'active'
    }
    return render(request, 'products/showFile.html', context)

@login_required
def delete_file(request, file_id):
    file = FileUpload.objects.get(id=file_id)
    file.delete()
    return redirect('/products/getFile')

@login_required
def update_file(request, file_id):
    file = FileUpload.objects.get(id=file_id)
    if request.method == "POST":
        if request.FILES.get('file'):
            file.title = request.POST.get('title')
            file.file = request.FILES.get('file')
            file.save()
        else:
            file.title = request.POST.get('title')
            file.save()
        return redirect('/products/getFile')
    context = {
        'file': file,
        'activate_file': 'active'
    }
    return render(request, 'products/updateFile.html', context)

@login_required
def get_file_mf(request):
    files = FileUpload.objects.all()
    context = {
        'files': files,
        'activate_fileMF': 'active'
    }
    return render(request, 'products/showFileMF.html', context)

@login_required
def post_file_mf(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/products/getFileMF')
    context = {
        'form': FileForm,
        'activate_fileMF': 'active'
    }
    return render(request, 'products/addFileMF.html', context)

@login_required
def deleteFileMF(request, file_id):
    file = FileUpload.objects.get(id=file_id)
    os.remove(file.file.path)
    file.delete()
    return redirect('/products/getFileMF')

@login_required
def updateFileMF(request, file_id):
    file = FileUpload.objects.get(id=file_id)
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES, instance=file)
        if form.is_valid():
            form.save()
            return redirect('/products/getFileMF')
    context = {
        'form': FileForm(instance=file),
        'activate_fileMF': 'active'

    }
    return render(request, 'products/updateFileMF.html', context)

def show_reporter_mf(request):
    reporters = Reporter.objects.all()
    context = {
        'reporters':reporters,
        'activate_reporterMF':'active'
    }
    return render(request, 'products/getReporterMF.html', context)

def post_reporter_mf(request):
    if request.method == 'POST':
        form = ReporterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Reporter Added Successfully')
            return redirect('/products/getReporterMF')
        else:
            messages.add_message(request, messages.ERROR, 'Error in adding reporter')
            return render(request,'products/postReporterMF.html', {'form':form})
    context = {
        'form' :ReporterForm
    }
    return render(request, 'products/postReporterMF.html',context)

def show_article_mf(request):
    articles = Article.objects.all()
    context = {
        'articles':articles,
        'activate_articleMF':'active'
    }
    return render(request, 'products/getArticleMF.html', context)

def post_article_mf(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Article Added Successfully')
            return redirect('/products/getArticleMF')
        else:
            messages.add_message(request, messages.ERROR, 'Error in adding article')
            return render(request,'products/postArticleMF.html', {'form':form})
    context = {
        'form' :ArticleForm,
    }
    return render(request, 'products/postArticleMF.html',context)