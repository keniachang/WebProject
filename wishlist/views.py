from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import bigWishlist
from cart.views import add_to_cart


@login_required(login_url='/admin/')
def wishlist_view(request):
    user = request.user
    wishlist = bigWishlist.objects.get(user=user)
    wishlist_context = {
        'wishlist': wishlist
    }

    # button for add to cart
    book_id = request.GET.get('addToCart')
    if book_id:
        add_to_cart(request, book_id, "/wishlist")

    return render(request, "wishlist.html", wishlist_context)
