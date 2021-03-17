from django import forms
from django.forms import ModelForm
from .models import person,FileUpload
class ProductForm(forms.Form):
    name= forms.CharField(max_length=200)
    price= forms.IntegerField()
class personform(ModelForm):

    class Meta:
        model=person
        fields="__all__"

class FileForm(ModelForm):
    class Meta:
        model=FileUpload
        fields='__all__'
