from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import Product
from .forms import ProductForm
from registration.models import Seller


# Create your views here.

class ProductListView(ListView):
    model = Product
    paginate_by = 24
    template_name = 'store/store.html'



class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product_detail.html'




class ProductCreateView(CreateView):
    model = Product
    success_url = reverse_lazy("store")
    form_class = ProductForm    


    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.seller = User.objects.get(pk=self.kwargs['pk']).seller
        form.save()
        return super(ProductCreateView, self).form_valid(form)
    


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm    
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("store")


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("store")