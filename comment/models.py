from django.db import models
from django.conf import settings
from book.models import Book


class Comment(models.Model):
    book_comment = models.ForeignKey(Book, on_delete=models.CASCADE)

# Create your models here.
