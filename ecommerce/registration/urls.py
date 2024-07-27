from django.urls import path
from .views import SignUpView, SellerProfile, SellerCreateView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('seller/<int:pk>/<slug:slug>/', SellerProfile.as_view(), name="seller_profile"),
    path('seller/create-profile/<int:pk>/<slug:slug>/', SellerCreateView.as_view(), name="seller_create"),
]