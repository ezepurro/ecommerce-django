from django.urls import path
from .views import home, store, seller_profile, product_detail, log_in, sign_in

# path('dashboard/', Dashboard.as_view(), name="dashboard"),
urlpatterns = [
    path('', home, name="home"),
    path('store/', store, name="store"),     
    path('seller-profile/', seller_profile, name="seller_profile"),
    path('product-detail/', product_detail, name="product_detail"),
    path('log-in/', log_in, name="log_in"),         
    path('sign-in/', sign_in, name="sign_in"),   
]