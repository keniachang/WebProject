from django import forms
from book.models import Book


class CommentForm(forms.ModelForm):


    nickname = forms.BooleanField(required=False, label='Leave Nickname?')

    class Meta:
        model = Book
        fields = [
            'comments',
            'rating'
        ]

class RawCommentForm(forms.Form):
    model = Book

    comments = forms.CharField(widget=forms.Textarea)


