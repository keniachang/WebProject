
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, PaymentInfoForm, AddressForm
from .models import Profile

def register(request):

    if request.method == 'POST':

        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('profile')
    else:
        form = UserRegisterForm()

    return render(request, 'user/register.html', {'form': form})

@login_required
def profile(request):

    if request.method == 'POST':

        user_form = UserUpdateForm(request.POST,instance=request.user)

        if user_form.is_valid():
            user_form.save()

            messages.success(request, f'Account Updated!')
            return redirect('profile') 
    
    else: 
        user_form = UserUpdateForm(instance=request.user)
      
    
    context = {
        'user_form' : user_form,
     }
    
    return render(request,'user/profile.html', context)

@login_required
def payment(request):

    if request.method == 'POST':

        pay_form = PaymentInfoForm(request.POST)
        pay_address_form = AddressForm(request.POST)

        if pay_form.is_valid() and pay_address_form.is_valid():
            pay_form.save()
            pay_address_form.save()

            messages.success(request, f'Payment Info Added!')
            return redirect('profile') 
    
    else: 
        pay_form = PaymentInfoForm()
        pay_address_form = AddressForm()

      
    
    context = {
        'pay_form' : pay_form,
        'pay_address_form' : pay_address_form
     }
    
    return render(request,'user/payment.html', context)

