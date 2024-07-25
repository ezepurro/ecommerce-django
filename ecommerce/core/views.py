from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "core/home.html")



def seller_profile(request):
    return render(request, "core/seller_profile.html")


def sign_in(request):
    return render(request, "core/sign_in.html")

