from sre_parse import CATEGORIES
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import CreateUserForm
from .forms import ProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.views.decorators.csrf import csrf_protect
from .models import Category, Product
from django.shortcuts import get_object_or_404
from .models import Profile
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.urls import reverse

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
            return redirect("login")

    context = {"form": form}
    return render(request, "register.html", context)


@csrf_protect
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            request.session["username"] = username
            return redirect("AccountSetting")
        else:
            messages.error(request, "Username OR password is incorrect")

    context = {}
    return render(request, "login.html", context)


def logoutuser(request):
    logout(request)
    messages.success(request, "You Were Succesfully Logged Out")
    return redirect("login")


def homepage(request):
    categories = Category.objects.all()
    return render(request, "homepage.html", {"categories": categories})


def showproducts(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    categories = Category.objects.all()
    return render(
        request, "categoryproducts.html", {"category": categories, "products": products}
    )


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    template_name = "single.html"
    context = {
        "product": product,
        "template_name": template_name,
    }
    return render(request, "single.html", {"product": product})


@login_required(login_url="/login")
def AccountSetting(request):
    username = request.session.get("username")

    context = {"username": username}

    return render(request, "AccountSetting.html", context)


@login_required(login_url="/login")
def edit_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            new_username = form.cleaned_data["username"]
            if User.objects.filter(username=new_username).exists():
                messages.error(
                    request,
                    "Username already exists. Please choose a different username.",
                )
                return redirect("edit_profile")
            else:
                user = request.user
                user.username = new_username
                user.save()

                return redirect("profile")
    else:
        form = ProfileForm(instance=request.user)

    context = {"form": form}
    return render(request, "edit_profile.html", context)


@login_required(login_url="/login")
def favorites(request):
    return render(request, 'favorites.html')


def add_to_favorites(request, product_id):
    product = Product.objects.get(id=product_id)
    request.user.favorite_products.add(product)
    return redirect('account_settings')



@login_required(login_url="/login")
def FAQ(request):
    return render(request, "FAQ.html")


def productlistajax(request):
    productz = Product.objects.filter(is_active=True).values_list('title', flat = True)   
    productList = list(productz)
    return JsonResponse(productList, safe=False)


def search_product(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query')

        if search_query:
            products = Product.objects.filter(title__icontains=search_query, is_active=True)

            if products.exists():
                if products.count() == 1:
                    product_slug = products.first().slug
                    return redirect(reverse('product_detail', kwargs={'slug': product_slug}))
                else:                    
                    messages.info(request, 'Multiple items match your search query. Please refine your search.')
                    return redirect('homepage')
            else:                
                messages.info(request, 'No items match your search query.')
                return redirect('homepage')
        else:
            messages.info(request, 'Please enter a search query.')
            return redirect('homepage')

    return render(request, 'single.html')