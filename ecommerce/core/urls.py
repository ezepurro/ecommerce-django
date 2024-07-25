from django.urls import path
from .views import home, seller_profile, sign_in

urlpatterns = [
    path('', home, name="home"),  
    path('seller-profile/', seller_profile, name="seller_profile"),       
    path('sign-in/', sign_in, name="sign_in"),   
]