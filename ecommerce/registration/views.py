from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from .models import Seller
from store.models import Product
from django.views.generic import CreateView, DetailView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django import forms


# Create your views here.

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'
    
    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()
        form.fields['username'].widget = forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Username',
        })
        form.fields['password1'].widget = forms.PasswordInput(attrs={
            'class':'form-control',
            'placeholder':'Password',
        })
        form.fields['password2'].widget = forms.PasswordInput(attrs={
            'class':'form-control',
            'placeholder':'Repeat the password',
        })
        form.fields['email'].widget = forms.EmailInput(attrs={
            'class':'form-control',
            'placeholder':'Email',
        })
        form.fields['first_name'].widget = forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'First Name',
        })
        form.fields['last_name'].widget = forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Last Name',
        })
        return form


class SellerProfile(DetailView):
    model = Seller
    template_name = 'registration/seller_profile.html'

    def get_context_data(self, **kwargs):
        context = super(SellerProfile, self).get_context_data(**kwargs)
        context.update({
            'product_list': Product.objects.order_by('title'),            
        })
        return context
    
    def get_queryset(self):
        return Seller.objects.order_by('user')    
    


class SellerCreateView(CreateView):
    model = Seller
    template_name = 'registration/create_seller_profile.html'
    fields = ['phone_number', 'direction', 'avatar']
    success_url = reverse_lazy('store')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user= User.objects.get(pk=self.kwargs['pk'])
        form.save()
        return super(SellerCreateView, self).form_valid(form)