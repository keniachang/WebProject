from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from book.models import Book
from .forms import CommentForm, RawCommentForm
from django import template

#register = template.Library()

#@register.filter
#def addstr(arg1, arg2):
#    return str(arg1) + str(arg2)

# Create your views here.
def comment_view(request):
    obj = Book.objects.get(id=10)
    user = request.user
    form = CommentForm(request.POST or None, instance=obj)
    context = {
        'object': obj,
        'form': form,
        'user': user
    }


    if form.is_valid():
        #obj.comment = form.cleaned_data['comments']
        comment = form.cleaned_data['comments']
        obj.rating = form.cleaned_data['rating']
        nickname = form.cleaned_data['nickname']

        if nickname == True:
            obj.comments = comment + " - nicknamehere"
        else:
           obj.comments = comment
        form = CommentForm()
        obj.save()
        return HttpResponseRedirect("/comment")
        #return HttpResponse('/thanks/')



    return render(request, "comment.html", context)


    #user = Profile.objects.get(id=1)
    #'title': obj.title,
        #'cover': obj.cover,
        #'rating': obj.rating,
        #'comment': obj.comments,
        #'nickname': user.username,