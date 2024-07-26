from django import forms
from .models import Product, STATUS_CHOICES
from django.contrib.auth.models import User

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'state', 'image']
        state = forms.ChoiceField(choices=STATUS_CHOICES)
        widgets = {
            'title': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Title'}
            ),
            'description': forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':'Description',
                'id':'exampleFormControlTextarea1',
                'rows':3}
            ),
            'image': forms.ClearableFileInput(attrs={
                'class':'form-control-file',}
            ),
            'price': forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Price'}
            ),
            'state': forms.Select(attrs={
                'class':'form-control'
            }),
        }