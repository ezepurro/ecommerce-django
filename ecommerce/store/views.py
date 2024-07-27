from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import Product
from .forms import ProductForm


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




class ProductCreateView(CreateView):
    model = Product
    success_url = reverse_lazy("store")
    form_class = ProductForm    


    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.seller = User.objects.get(pk=self.kwargs['pk']).seller
        form.save()
        return super(ProductCreateView, self).form_valid(form)