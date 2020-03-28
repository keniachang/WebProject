from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem, has_cart, total
from book.models import Book
from django.shortcuts import get_object_or_404


@login_required(login_url="/login/")
def cart_view(request):
    user = request.user
    create_cart = not (has_cart(user))
    if create_cart is True:
        cart = Cart(user=user)
        cart.save()
    else:
        cart = Cart.objects.get(user=user)

    try:
        items = cart.cartitem_set.all()
        is_saved_empty = cart.is_saved_empty()
    except:
        items = []
        is_saved_empty = True

    is_empty_cart = cart.is_cart_empty()

    subtotal = total(items)

    items_context = {
        'items': items,
        'is_saved_empty': is_saved_empty,
        'is_empty_cart': is_empty_cart,
        'subtotal': subtotal
    }

    if request.method == 'POST':
        cart_item_ids = request.POST.getlist('saves')
        if cart_item_ids:
            for item_id in cart_item_ids:
                # print(item_id)
                cart_item = CartItem.objects.get(pk=item_id)
                cart_item.save_for_later = True
                cart_item.save(update_fields=['save_for_later'])

        quantities = request.POST.getlist('quantity')
        # print(quantities)
        if quantities:
            i = 0
            for cart_item in items:
                if cart_item.save_for_later is False:
                    cart_item.quantity = quantities[i]
                    cart_item.save(update_fields=['quantity'])
                    i += 1

        cart_item_ids = request.POST.getlist('remove')
        if cart_item_ids:
            for item_id in cart_item_ids:
                cart_item = CartItem.objects.get(pk=item_id)
                cart_item.delete()

        cart_item_ids = request.POST.getlist('unsaved')
        if cart_item_ids:
            for item_id in cart_item_ids:
                cart_item = CartItem.objects.get(pk=item_id)
                cart_item.save_for_later = False
                cart_item.save(update_fields=['save_for_later'])
        return HttpResponseRedirect("/cart")

    # Add book to cart by book name
    # book_name = request.GET.get('addToCart')
    # if book_name:
    #     book = get_object_or_404(Book, title=book_name)
    #     cart_item = cart.cartitem_set.filter(item=book)
    #     if cart_item:
    #         cart_item = cart_item[0]
    #         cart_item.quantity += 1
    #         cart_item.save(update_fields=['quantity'])
    #     else:
    #         CartItem.objects.create(item=book, cart=cart)
    #     return HttpResponseRedirect("/cart")

    return render(request, "cart.html", items_context)


@login_required(login_url="/login/")
def add_to_cart(request, book_id, current_page="/cart"):
    user = request.user
    create_cart = not (has_cart(user))
    if create_cart is True:
        cart = Cart(user=user)
        cart.save()
    else:
        cart = Cart.objects.get(user=user)

    book = Book.objects.get(pk=book_id)
    cart_item = cart.cartitem_set.filter(item=book)
    if cart_item:
        cart_item = cart_item[0]
        cart_item.quantity += 1
        cart_item.save(update_fields=['quantity'])
    else:
        CartItem.objects.create(item=book, cart=cart)

    return HttpResponseRedirect(current_page)
