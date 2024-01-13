from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from apps.forms import RegisterForm
from apps.models import Blog

def shop_list_page(request):
    context = {
        'shop-list'
    }
    return  render(request, 'apps/blogs/shop-list.html', context)

def blog_list_page(request):
    context = {
        'blogs': Blog.objects.all()
    }
    return render(request, 'apps/blogs/blog-list.html', context)


def blog_detail_page(request):
    context = {
        'blogs': []
    }
    return render(request, 'apps/blogs/blog-detail.html', context)


def index_page(request):
    return render(request, 'apps/index.html')


def logout_page(request):
    logout(request)
    return redirect('index_page')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if User.objects.filter(username=username).exists():
            login(request, user)
            return redirect('index_page')

    return render(request, 'apps/login.html')


def register_page(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index_page')
    context = {
        'form': form
    }
    return render(request, 'apps/login.html', context)
