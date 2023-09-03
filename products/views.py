from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.views.decorators.csrf import csrf_protect
from .models import Category, Product
from django.shortcuts import get_object_or_404
# Create your views here.


def index(request):  # main page of the app
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})

def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, "Account was created for " + user)
            return redirect('login')
        

    context = {"form": form}
    return render(request, "register.html", context)

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
            return redirect('AccountSetting')
        else:
            messages.error(request, 'Username OR password is incorrect')
    

    context = {}
    return render(request, 'login.html', context)

def logoutuser(request):
    logout(request)
    messages.success(request, 'You Were Succesfully Logged Out')
    return redirect('login')


def homepage(request):
    context = {}
    return render(request, 'homepage.html', context)


def product_all(request):
    products = Product.products.all()
    return render(request, 'templates/index.html', {'products': products})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.products.filter(category=category)
    return render(request, 'templates/category.html', {'category': category, 'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    template_name = 'single.html'
    context ={
        'product': product,
        'template_name': template_name,
    }
    return render(request, 'single.html', {'product': product})


@login_required(login_url='/login')
def AccountSetting(request):
    return render(request,'AccountSetting.html')

@login_required(login_url='/login')
def editprofile(request):
    return render(request, 'edit_profile.html')

@login_required(login_url='/login')
def favorites(request):
    return render(request, 'favorites.html')