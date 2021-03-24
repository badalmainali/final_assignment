from django.db import models
from ckeditor.fields import RichTextField
from django.contrib import messages
from django.core import validators
from django.core.validators import *



# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    image_url = models.CharField(max_length=2000)

    def __str__(self):
        return self.name


class person(models.Model):
    firstname = models.CharField(max_length=200, null=True, validators=[validators.MinLengthValidator(2)])
    lastname = models.CharField(max_length=200, null=True, validators=[validators.MinLengthValidator(2)])
    email = models.EmailField(null=True, validators=[validate_email])
    phone = models.CharField(null=True, max_length=10, validators=[validators.MinLengthValidator(9)])


class Student(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    batch = models.CharField(max_length=20)
    category = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)


class FileUpload(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='static/uploads')

class Reporter(models.Model):
    first_name=models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email=models.EmailField()

    def __str__(self):
        return self.first_name+''+self.last_name

class Article(models.Model):
    headline=models.CharField(max_length=100)
    pub_date=models.DateField(auto_now_add=True)
    reporter=models.ForeignKey(Reporter,on_delete=models.CASCADE)