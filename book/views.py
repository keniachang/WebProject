from django.shortcuts import render
from .models import Book


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


    return render(request, 'bookdetail.html', book_context)





def authorbook(request, author):
    books = Book.objects.all()[:20]
    author_context = {
        'author' : author,
        'books': books
    }
    return render(request, 'authorbook.html', author_context)

