from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Seller

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)


    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)

    # Email Validation
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already in use")
        return email
    


class SellerForm(forms.ModelForm):

    class Meta:
        model = Seller
        fields = ['phone_number', 'direction', 'avatar']
        widgets = {
            'phone_number': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Phone number',
                'name':'phone_number',}
            ),
            'direction': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Direction',
                'name':'direction',}
            ),
            'avatar': forms.FileInput(attrs={
                'class':'form-control',
                'name':'avatar'}
            ),
        }