from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from book.models import Book
from .models import Comment
from .forms import CommentForm




# Create your views here.
def comment_view(request):
    comment_id = request.session['id']
    obj = Book.objects.get(pk=comment_id)
    obj2 = Comment()
    user = request.user
    form = CommentForm(request.POST or None, instance=obj)
    context = {
        'object': obj,
        'form': form,
        'user': user
    }


    if form.is_valid():

        comment = form.cleaned_data['comments']
        obj2.rating = form.cleaned_data['rating']
        nickname = form.cleaned_data['nickname']
        anonymous = form.cleaned_data['anonymous']
        obj2.title = obj.title

        if anonymous:
            obj2.comments = comment
        else:
            if nickname:
                obj2.comments = comment + " - " + user.username
            else:
                obj2.comments = comment + " - " + user.first_name
        obj2.save()
        redirect_url = "/books/bookdetail/?id=" + str(comment_id)
        return HttpResponseRedirect(redirect_url)

    return render(request, "comment.html", context)

