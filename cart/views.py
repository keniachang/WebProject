from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Cart
from .models import has_cart


# TODO: change the login_url to the normal user login page
@login_required(login_url='/admin/')
def cart_view(request):
    user = request.user
    create_cart = has_cart(user)
    if create_cart is True:
        cart = Cart.objects.get(user=user)
    else:
        cart = Cart.create(user)

    try:
        items = cart.items.all()
    except:
        items = []

    items_context = {
        'items': items
    }

    return render(request, "cart.html", items_context)
