from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='guest')
def home(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'home.html',context)

def guest(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'guest.html',context)

@login_required(login_url='login')
def cart(request,pk):
    client = User.objects.get(pk=pk)
    context = {'client':client}
    return render(request,'cart.html',context)

def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        context = {}
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username = username, password = password)
            if user is not None:
                try:
                    login(request, user)
                    return redirect('home')
                except:
                    messages.success(request,"Ha ocurrido un error, intenta de nuevo")
                    return render(request,'login.html',context)
            else:
                messages.success(request,"Usuario no registrado")
                return render(request,'login.html',context)

        return render(request,'login.html',context)

def user_logout(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,"Cuenta creada para exitosamente para " + user)
                return redirect('login')

        context = {'form':form}
        return render(request,'register.html',context)