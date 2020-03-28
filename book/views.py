from django.shortcuts import render
from .models import Book
from cart.views import add_to_cart
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from wishlist.views import wishlist_view


# Create your views here.
def book_detail_view(request):
    books = Book.objects.all()[:20]
    books_context = {
        'books': books
    }
    return render(request, "books.html", books_context)


def bookdetail_view(request):
    book_id = request.get_full_path().split("=")[-1]
    book = Book.objects.get(pk=book_id)
    user = User.objects.get(id=request.user.id)
    book_context = {
        'book': book
    }

    # button for add to cart
    book_id = request.GET.get('addToCart')
    if book_id:
        redirect_url = "/books/bookdetail/?id=" + str(book_id)
        add_to_cart(request, book_id, redirect_url)
        return HttpResponseRedirect(redirect_url)

    # button for add comment
    comment_id = request.GET.get('addComment')
    if comment_id:
        books = user.profile.books_owned
        if books:
            books = books.split(",")
            book_num = str(comment_id)
            if book_num in books:
                request.session['id'] = comment_id
                redirect_url = "/comment"
                return HttpResponseRedirect(redirect_url)

    # options for add to wishlist
    book_id = request.GET.get('addwl1')
    if book_id:
        wishlist_view(request)
        return HttpResponseRedirect("/books/bookdetail/?id=" + str(book_id))

    book_id = request.GET.get('addwl2')
    if book_id:
        wishlist_view(request)
        return HttpResponseRedirect("/books/bookdetail/?id=" + str(book_id))

    book_id = request.GET.get('addwl3')
    if book_id:
        wishlist_view(request)
        return HttpResponseRedirect("/books/bookdetail/?id=" + str(book_id))

    return render(request, 'bookdetail.html', book_context)


def authorbook_view(request, author):
    books = Book.objects.all()
    author_context = {
        'author': author,
        'books': books
    }
    return render(request, 'authorbook.html', author_context)
