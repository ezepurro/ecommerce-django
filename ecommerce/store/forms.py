from django import forms
from .models import Product, STATUS_CHOICES
from django.contrib.auth.models import User


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'state', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Title',
                'name':'title',
                'required':True}
            ),
            'description': forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':'Description',
                'id':'exampleFormControlTextarea1',
                'rows':3,
                'name':'description',
                'required':True}
            ),
            'image': forms.FileInput(attrs={
                'class':'form-control',
                'name':'image'}
            ),
            'price': forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Price',
                'name':'price',
                'required':True,
                'step':'.01',
                'min':'0',}
            ),
            'state': forms.Select(attrs={
                'class':'form-control',
                'name':'state',
                'required':True
            }),
        }