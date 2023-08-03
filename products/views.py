from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def index(request):#main page of the app
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def login(request):
    context = {}
    return render(request, 'login.html', context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'register.html', context)