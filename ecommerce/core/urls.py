from django.urls import path
from .views import home, seller_profile, log_in, sign_in

urlpatterns = [
    path('', home, name="home"),  
    path('seller-profile/', seller_profile, name="seller_profile"),
    path('log-in/', log_in, name="log_in"),         
    path('sign-in/', sign_in, name="sign_in"),   
]