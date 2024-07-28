from django.urls import path
from .views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView


urlpatterns = [
    path('', ProductListView.as_view(), name="store"),   
    path('product-detail/<int:pk>/<slug:slug>', ProductDetailView.as_view(), name="product_detail"),
    path('sell/<int:pk>', ProductCreateView.as_view(), name="sell"),   
    path('update/<int:pk>/<slug:slug>', ProductUpdateView.as_view(), name="update_product"),  
    path('delete/<int:pk>/<slug:slug>', ProductDeleteView.as_view(), name="delete_product"),  
]