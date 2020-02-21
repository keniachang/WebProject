from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Cart
from .models import has_cart
from .models import CartItem


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
        is_saved_empty = cart.is_saved_empty()
    except:
        items = []
        is_saved_empty = True

    is_empty_cart = cart.is_cart_empty()

    items_context = {
        'items': items,
        'is_saved_empty': is_saved_empty,
        'is_empty_cart': is_empty_cart
    }

    if request.method == 'POST':
        cart_item_ids = request.POST.getlist('saves')
        for item_id in cart_item_ids:
            # print(item_id)
            cart_item = CartItem.objects.get(pk=item_id)
            cart_item.save_for_later = True
            cart_item.save(update_fields=['save_for_later'])
        return HttpResponseRedirect("/cart")

    return render(request, "cart.html", items_context)
