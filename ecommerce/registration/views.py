from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from .models import Seller
from django.forms import BaseModelForm
from django.views.generic import CreateView, DetailView
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