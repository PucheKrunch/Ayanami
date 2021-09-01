from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'home.html',context)

def login(request):
    return render(request,'login.html',{'data':1})

def register(request):
    return render(request,'register.html',{'data':1})