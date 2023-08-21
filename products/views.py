from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.views.decorators.csrf import csrf_protect

# Create your views here.


def index(request):#main page of the app
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account was created for " + user)
            return redirect('login')
        

            

    context = {'form':form}
    return render(request, 'register.html', context)

@csrf_protect
def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password )
        
        if user is not None:
            auth_login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, 'Username OR password is incorrect')
    

    context = {}
    return render(request, 'login.html', context)

def homepage(request):
    context = {}
    return render(request, 'homepage.html', context)

