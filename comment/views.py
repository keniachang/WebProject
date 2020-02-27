from django.shortcuts import render
from .models import Book


# Create your views here.
def comment_view(request):
    books = Book.objects.all()[:20]
    books_context = {
        'books': books
    }
    return render(request, "books.html", books_context)
