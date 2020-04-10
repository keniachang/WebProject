
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.models import User
from .forms import(
    UserRegisterForm, UserUpdateForm, 
    PaymentInfoForm, ShippingAddressForm,
    HomeAddressForm
    )
from .models import Profile, HomeAddress, Credit_Card, ShippingAddress

def register(request):

    if request.method == 'POST':

        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'user/register.html', {'form': form})

@login_required
def profile(request):

    if request.method == 'POST':

        user_form = UserUpdateForm(request.POST, instance=request.user, prefix='user_form')
        home_form = HomeAddressForm(request.POST,instance=request.user.profile.home_address,prefix='home_form')
        print(request.POST)

        if user_form.is_valid() and home_form.is_valid():

            user_form.save()
            home_address = home_form.save()

            profile = request.user.profile
            profile.home_address = home_address
            profile.save(update_fields=['home_address'])


            messages.success(request, f'Account Updated!')
            return redirect('profile') 
    
    else: 
        user_form = UserUpdateForm(instance=request.user,prefix='user_form')
        home_form = HomeAddressForm(instance=request.user.profile.home_address,prefix='home_form')

    
    context = {
        'user_form' : user_form,
        'home_form' : home_form
     }
    
    return render(request,'user/profile.html', context)

@login_required
def payment_list(request):
    logged_in_profile = Profile.objects.get(user=request.user)
    credit_cards = logged_in_profile.payment_info.all()
    
    
    context = {
        'credit_cards' : credit_cards,
        'profile': logged_in_profile

    }

    return render(request,'user/payment/home.html', context)

@login_required
def shipping_list(request):
    logged_in_profile = Profile.objects.get(user=request.user)
    shipping_addresses = logged_in_profile.shipping_address.all()
    
    
    context = {
        'shipping_addresses' : shipping_addresses,
        'profile': logged_in_profile
    }

    return render(request,'user/shipping/home.html', context)



class PaymentEditView(LoginRequiredMixin, SuccessMessageMixin , UpdateView):
    model = Credit_Card
    form_class = PaymentInfoForm
    template_name = 'user/payment/edit.html'

    success_message = 'Payment Info Updated!'

class ShippingEditView(LoginRequiredMixin, SuccessMessageMixin , UpdateView):
    model = ShippingAddress
    form_class = ShippingAddressForm
    template_name = 'user/shipping/edit.html'

    success_message = 'Shipping Address Updated!'




@login_required
def add_shipping(request):

    if request.method == 'POST':

        shipping_address_form = ShippingAddressForm(request.POST)

        if shipping_address_form.is_valid():
            shipping_address = shipping_address_form.save()

            profile = request.user.profile
            
            profile.shipping_address.add(shipping_address)

            messages.success(request, f'Shipping Address Added!')
            return redirect('shipping_home') 
    
    else: 
        shipping_address_form = ShippingAddressForm()

      
    
    context = {
        'shipping_address_form' : shipping_address_form
     }
    
    return render(request,'user/shipping/new.html', context)





@login_required
def add_payment(request):

    if request.method == 'POST':

        pay_form = PaymentInfoForm(request.POST)

        if pay_form.is_valid():
            payment_info = pay_form.save()

            profile = request.user.profile
            
            profile.payment_info.add(payment_info)

            messages.success(request, f'Payment Info Added!')
            return redirect('payment_home') 
    
    else: 
        pay_form = PaymentInfoForm()

      
    
    context = {
        'pay_form' : pay_form,
     }
    
    return render(request,'user/payment/new.html', context)

class PaymentDeleteView(LoginRequiredMixin,DeleteView):
    model = Credit_Card
    template_name = 'user/payment/delete.html'

    success_url ='/profile/payment'

class ShippingDeleteView(LoginRequiredMixin,DeleteView):
    model = ShippingAddress
    template_name = 'user/shipping/delete.html'

    success_url ='/profile/shipping'




