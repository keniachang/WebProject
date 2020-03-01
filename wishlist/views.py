from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import bigWishlist

# Create your views here.

@login_required(login_url='/admin/')
def wishlist_view(request):
    user = request.user

    wishlist = bigWishlist.objects.get(user=user)


    wishlist_context = {
        'wishlist': wishlist
    }

    return render(request, "wishlist.html", wishlist_context)
