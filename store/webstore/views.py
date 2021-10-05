from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'home.html',context)

def cart(request,pk):
    client = Client.objects.get(pk=pk)

    context = {'client':client}
    return render(request,'cart.html',context)

def user_login(request):
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

def register(request):
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