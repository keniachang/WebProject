from django.shortcuts import render


# Create your views here.
def comment_view(request):
    #books = Book.objects.all()[:20]
    #comment_context = {
    #    'books': books
    #}
    return render(request, "comment.html", )
