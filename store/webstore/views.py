from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html',{'data':1})

def login(request):
    return render(request,'login.html',{'data':1})

def register(request):
    return render(request,'register.html',{'data':1})