from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "core/home.html")


def store(request):
    return render(request, "core/store.html")


def seller_profile(request):
    return render(request, "core/seller_profile.html")


def product_detail(request):
    return render(request, "core/product_detail.html")


def sign_in(request):
    return render(request, "core/sign_in.html")


def log_in(request):
    return render(request, "core/log_in.html")