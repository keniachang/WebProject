from django.shortcuts import render
from .models import Book
from cart.views import add_to_cart
from comment.views import comment_view
from django.http import HttpResponseRedirect


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
        request.session['id'] = comment_id
        #comment_id = str(comment_id)
        #redirect_url = "/books/bookdetail/?id=" + str(comment_id)
        #comment_view(request, comment_id)
        redirect_url = "/comment"


        return HttpResponseRedirect(redirect_url)

    return render(request, 'bookdetail.html', book_context)
