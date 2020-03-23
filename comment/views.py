from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from book.models import Book
from .forms import CommentForm, RawCommentForm
from django import template



# Create your views here.
def comment_view(request):
    comment_id = request.session['id']
    obj = Book.objects.get(pk=comment_id)
    user = request.user
    form = CommentForm(request.POST or None, instance=obj)
    context = {
        'object': obj,
        'form': form,
        'user': user
    }


    if form.is_valid():
        comment = form.cleaned_data['comments']
        obj.rating = form.cleaned_data['rating']
        nickname = form.cleaned_data['nickname']

        if nickname == True:
            obj.comments = comment + " - " + user.username
        else:
           obj.comments = comment
        form = CommentForm()
        obj.save()
        redirect_url = "/books/bookdetail/?id=" + str(comment_id)
        return HttpResponseRedirect(redirect_url)




    return render(request, "comment.html", context)

