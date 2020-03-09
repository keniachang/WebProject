from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import bigWishlist
from .models import WishlistItem

# Create your views here.

@login_required(login_url='/admin/')
def wishlist_view(request):
    user = request.user

    wishlist = bigWishlist.objects.get(user=user)


    wishlist_context = {
        'wishlist': wishlist
    }

    if request.method == 'POST':
        wishlist_book = request.POST.get('remove')
        print(wishlist_book)

        WishlistItem.objects.filter(id=wishlist_book).delete()

        return HttpResponseRedirect("/wishlist")

    return render(request, "wishlist.html", wishlist_context)
