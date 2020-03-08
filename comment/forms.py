from django import forms
from book.models import Book


class CommentForm(forms.ModelForm):
    #nickname_choice = [(Yes, 'Yes'), (No, 'No')]

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

    #rating  = forms.IntegerField(min="0", max="5")
    #nickname = forms.radio(label='Leave Nickname?', value="Yes")
    #comment = forms.CharField(label='comment', max_length=100)
    #rating = forms.range(label='rating', min="0", max="5")

