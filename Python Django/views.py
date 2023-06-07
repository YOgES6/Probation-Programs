from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render  
from .models import Book
from .forms import MyForm
from .models import Book


def my_form(request):
    data=request.GET['name']
    p=Book(Name=name,Mobile=mob,Address=ad,Checkin=che,Checkout=che1)
    return render(request,'index.html',{'data':data})
