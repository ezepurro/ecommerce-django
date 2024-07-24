from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product

# Create your views here.

class ProductListView(ListView):
    model = Product
    paginate_by = 24
    template_name = 'store/store.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["now"] = timezone.now()
    #     return context



class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product_detail.html'