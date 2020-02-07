from django.db import models
from django.conf import settings

from book.models import Book


# Create your models here.
class CartItem(models.Model):
    item = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    save_for_later = models.BooleanField(default=False, null=False)


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
