from django import forms
from .models import Profile, HomeAddress, ShippingAddress, Credit_Card
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .validators import validate_cc_number, validate_cc_exp, validate_cc_security,validate_address_line, validate_string, validate_zip

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
    first_name = forms.CharField(max_length=100, validators=[validate_string])
    last_name = forms.CharField(max_length=100, validators=[validate_string])
    cc_number = forms.CharField(validators=[validate_cc_number])
    cc_expiration = forms.CharField(validators=[validate_cc_exp])
    cc_security_code = forms.CharField(validators=[validate_cc_security] )
    class Meta:
        model = Credit_Card
        fields = ['first_name', 'last_name','cc_number', 'cc_expiration', 'cc_security_code']

class HomeAddressForm(forms.ModelForm):
    address_line = forms.CharField(max_length = 100,validators=[validate_address_line])
    state = forms.CharField(max_length=50, validators=[validate_string])
    city = forms.CharField(max_length=50, validators=[validate_string])
    zip_code = forms.CharField(validators=[validate_zip])

    class Meta:
        model = HomeAddress
        fields = ['address_line', 'state', 'city', 'zip_code']

class ShippingAddressForm(forms.ModelForm):

    address_line = forms.CharField(max_length = 100,validators=[validate_address_line])
    state = forms.CharField(max_length=50, validators=[validate_string])
    city = forms.CharField(max_length=50, validators=[validate_string])
    zip_code = forms.CharField(validators=[validate_zip])
    
    class Meta:
        model = ShippingAddress
        fields = ['address_line', 'state', 'city', 'zip_code']

