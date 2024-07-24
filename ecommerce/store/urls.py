from django.urls import path
from .views import ProductListView, ProductDetailView


urlpatterns = [
    path('', ProductListView.as_view(), name="store"),   
    path('product-detail/<int:pk>/<slug:slug>', ProductDetailView.as_view(), name="product_detail"),
]