from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import bigWishlist
from .models import smallWishlist
from .models import WishlistItem

# Create your views here.


@login_required(login_url='/admin/')
def wishlist_view(request):
    user = request.user


    if bigWishlist.objects.filter(user=user).exists():

        # works if testing on user with bWL object

        bigwishlist = bigWishlist.objects.get(user=user)
    else:

        #does not work
        bigwishlist = bigWishlist.add_wishlist(user,swishlist)


    wishlist_context = {
        'bigwishlist': bigwishlist
    }


    if 'remove' in request.POST:
        wishlist_book = request.POST.get('remove')
        print(wishlist_book)

        WishlistItem.objects.filter(id=wishlist_book).delete()

        return HttpResponseRedirect("/wishlist")

    elif 'move1' in request.POST:
        wishlist_book = request.POST.get('move1')
        print(wishlist_book)

        book = WishlistItem.objects.filter(id=wishlist_book)
        print(book)

        sWL = smallWishlist.objects.get(num=1)

        print(sWL)
        book.update(wishlist=sWL)

        return HttpResponseRedirect("/wishlist")

    elif 'move2' in request.POST:
        wishlist_book = request.POST.get('move2')
        print(wishlist_book)

        book = WishlistItem.objects.filter(id=wishlist_book)
        print(book)

        sWL = smallWishlist.objects.get(num=2)

        print(sWL)
        book.update(wishlist=sWL)

        return HttpResponseRedirect("/wishlist")

    elif 'move3' in request.POST:
        wishlist_book = request.POST.get('move3')
        print(wishlist_book)

        book = WishlistItem.objects.filter(id=wishlist_book)
        print(book)

        sWL = smallWishlist.objects.get(num=3)

        print(sWL)
        book.update(wishlist=sWL)

        return HttpResponseRedirect("/wishlist")

    elif 'cart' in request.POST:



        return HttpResponseRedirect("/wishlist")

    return render(request, "wishlist.html", wishlist_context)
