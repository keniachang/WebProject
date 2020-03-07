from django.http import HttpResponse
from django.shortcuts import render
from book.models import Book
from user.models import Profile
from .forms import CommentForm

# Create your views here.
def comment_view(request):
   form = CommentForm(request.POST or None)
    context = {

        'form': form
    }

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data['comment']
            rating = form.cleaned_data['rating']

            if nickname:
                comment.append(nickname)

            return HttpResponse('/thanks/')
    else:
        form = CommentForm()


    return render(request, "comment.html", context)

 #obj = Book.objects.get(id=1)
    #user = Profile.objects.get(id=1)
    #'title': obj.title,
        #'cover': obj.cover,
        #'rating': obj.rating,
        #'comment': obj.comments,
        #'nickname': user.username,