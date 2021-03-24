from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


from django.conf import settings
from django.conf.urls.static import static

def index(request):
    return HttpResponse('this is test .....')

def index1(request):
    return HttpResponse('this is test two hai ta.....')


urlpatterns = [



    path('',views.indexs),
    path('getproductform',views.get_product_form),
    path('getpersonform',views.get_person_form),
    path('addstudent',views.post_student),
    path('getstudents',views.get_students),
    path('deletestudent/<int:student_id>',views.deleteStudent),
    path('updateStudent/<int:student_id>',views.updateStudent),
    path('getPersonMF',views.get_person_mf),
    path('postPersonMF',views.post_person_mf),
    path('deletePersonMF/<int:person_id>',views.deletePersonMF),
    path('updatePersonMF/<int:person_id>',views.updatePersonMF),
    path('getFile',views.get_file),
    path('postFile',views.post_file),
    path('deleteFile/<int:file_id>',views.delete_file),
    path('updateFile/<int:file_id>',views.update_file),
    path('getFileMF',views.get_file_mf),
    path('postFileMF', views.post_file_mf),
    path('updateFileMF/<int:file_id>',views.updateFileMF),
    path('deleteFileMF/<int:file_id>',views.deleteFileMF),
    path('password_change', auth_views.PasswordChangeView.as_view(template_name='products/passwordChange.html')),
    path('password_change_done', auth_views.PasswordChangeView.as_view(template_name='products/passwordChangeDone.html'), name='password_change_done'),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_URL)