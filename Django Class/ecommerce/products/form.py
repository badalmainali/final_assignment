from django import forms
from django.forms import ModelForm
from .models import person,FileUpload,Reporter,Article
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

class ReporterForm(ModelForm):
    class Meta:
        model=Reporter
        fields='__all__'

class ArticleForm(ModelForm):
    class Meta:
        model=Article
        fields='__all__'
