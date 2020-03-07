from django.shortcuts import render
from book.models import Book

# Create your views here.
def comment_view(request):
    obj = Book.objects.get(id=1)
    context = {
        'title': obj.title,
        'cover': obj.cover,
        'rating': obj.rating,
        'comment': obj.comments
    }
    return render(request, "comment.html", context)
