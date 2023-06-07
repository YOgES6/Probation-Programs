from  django import forms
from .models import Book 

class MyForm(forms.ModelForm):
      name=forms.CharField(max_length=20)
      mob=forms.CharField(max_length=20)
      ad=forms.CharField(max_length=20)
      che=forms.CharField(max_length=20)
      che1=forms.CharField(max_length=20)

