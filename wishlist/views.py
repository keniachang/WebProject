from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import bigWishlist
from .models import smallWishlist
from .models import WishlistItem
from cart.views import add_to_cart
from book.models import Book


# Create your views here.


@login_required(login_url='/login/')
def wishlist_view(request):
    user = request.user

    if bigWishlist.objects.filter(user=user).exists():

        bigwishlist = bigWishlist.objects.get(user=user)
    else:

        bigwishlist = bigWishlist(user=user)
        bigwishlist.save()

    wishlist_context = {
        'bigwishlist': bigwishlist
    }

    if 'remove' in request.POST:
        wishlist_book = request.POST.get('remove')

        WishlistItem.objects.filter(id=wishlist_book).delete()

        return HttpResponseRedirect("/wishlist")

    elif 'move1' in request.POST:
        wishlist_book = request.POST.get('move1')

        book = WishlistItem.objects.filter(id=wishlist_book)

        sWL = smallWishlist.objects.get(num=1)

        book.update(wishlist=sWL)

        return HttpResponseRedirect("/wishlist")

    elif 'move2' in request.POST:
        if bigwishlist.smallwishlist_set.count() > 1:
            wishlist_book = request.POST.get('move2')

            book = WishlistItem.objects.filter(id=wishlist_book)

            sWL = smallWishlist.objects.get(num=2)

            book.update(wishlist=sWL)

            return HttpResponseRedirect("/wishlist")

        else:
            return HttpResponseRedirect("/wishlist")

    elif 'move3' in request.POST:
        if bigwishlist.smallwishlist_set.count() > 2:
            wishlist_book = request.POST.get('move3')

            book = WishlistItem.objects.filter(id=wishlist_book)

            sWL = smallWishlist.objects.get(num=3)

            book.update(wishlist=sWL)

            return HttpResponseRedirect("/wishlist")
        else:
            return HttpResponseRedirect("/wishlist")

    # button for add to cart
    elif 'cart' in request.POST:
        book_id = request.POST.get('cart')
        if book_id:
            add_to_cart(request, book_id, "/wishlist")
            return HttpResponseRedirect("/wishlist")


    swishlist_name = request.GET.get('createWishlist')
    if swishlist_name:
        wishlist_count = bigwishlist.smallwishlist_set.count()
        wishlist_count += 1

        bwl = bigWishlist.objects.all()
        temp = bwl[0]

        a = smallWishlist.objects.create(name=swishlist_name, num=wishlist_count, list=temp)
        bigwishlist.add_wishlist(a)

        return HttpResponseRedirect("/wishlist")

    if 'addwl1' in request.GET:
        if bigwishlist.smallwishlist_set.count() > 0:

            sWL = smallWishlist.objects.get(num=1)
            book_id = request.GET.get('addwl1')

            book = Book.objects.get(pk=book_id)
            WishlistItem.objects.create(item=book, wishlist=sWL)

        else:
            bwl = bigWishlist.objects.all()
            temp = bwl[0]

            a = smallWishlist.objects.create(name="1", num=1, list=temp)
            bigwishlist.add_wishlist(a)

            book_id = request.GET.get('addwl1')

            book = Book.objects.get(pk=book_id)

            WishlistItem.objects.create(item=book, wishlist=a)

    if 'addwl2' in request.GET:
        if bigwishlist.smallwishlist_set.count() > 1:

            sWL = smallWishlist.objects.get(num=2)
            book_id = request.GET.get('addwl2')

            book = Book.objects.get(pk=book_id)
            WishlistItem.objects.create(item=book, wishlist=sWL)

        else:
            return HttpResponseRedirect("/wishlist")

    if 'addwl3' in request.GET:
        if bigwishlist.smallwishlist_set.count() > 2:

            sWL = smallWishlist.objects.get(num=3)
            book_id = request.GET.get('addwl3')

            book = Book.objects.get(pk=book_id)
            WishlistItem.objects.create(item=book, wishlist=sWL)

        else:
            return HttpResponseRedirect("/wishlist")


    new_wishlistname = request.GET.get('rename1')
    if new_wishlistname:

        sWL = smallWishlist.objects.get(num=1)
        sWL.name = new_wishlistname
        sWL.save()

        return HttpResponseRedirect("/wishlist")


    new_wishlistname = request.GET.get('rename2')
    if new_wishlistname:

        sWL = smallWishlist.objects.get(num=2)
        sWL.name = new_wishlistname
        sWL.save()

        return HttpResponseRedirect("/wishlist")

    new_wishlistname = request.GET.get('rename3')
    if new_wishlistname:


        sWL = smallWishlist.objects.get(num=3)
        sWL.name = new_wishlistname
        sWL.save()

        return HttpResponseRedirect("/wishlist")

    return render(request, "wishlist.html", wishlist_context)
