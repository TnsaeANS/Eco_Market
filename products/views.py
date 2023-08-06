from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
# from .forms import OrderForm
# Create your views here.


def index(request):#main page of the app
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def login(request):
    context = {}
    return render(request, 'login.html', context)

def homepage(request):
    context = {}
    return render(request, 'homepage.html', context)

def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'register.html', context)