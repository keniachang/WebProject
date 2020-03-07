from django import forms
from book.models import Book


class CommentForm(forms.Modelform):
    class Meta:
        model = Book
        fields = [
            'comment',
            'title',
            'cover',
            'rating'
        ]

    #comment = forms.CharField(label='comment', max_length=100)
    #rating = forms.range(label='rating', min="0", max="5")
    #nickname = forms.radio(label='Leave Nickname?', value="Yes", value="No")
