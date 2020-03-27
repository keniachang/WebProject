from django import forms
from .models import Profile, Address, Credit_Card
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=150)


    class Meta:
        model = User    
        fields = ['username', 'first_name', 'last_name','email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=150)
    

    class Meta:
        model = User    
        fields = ['username', 'email', 'first_name', 'last_name']

class PaymentInfoForm(forms.ModelForm):
    class Meta:
        model = Credit_Card
        fields = ['cc_number', 'cc_expiration', 'cc_security_code']

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['address_line', 'country', 'state', 'city', 'zip_code']

