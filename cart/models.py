from django.db import models
from django.conf import settings

from book.models import Book


# Create your models here.
class CartItem(models.Model):
    item = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    save_for_later = models.BooleanField(default=False, null=False)


class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem, blank=True)

    @classmethod
    def create(cls, user):
        cart = cls(user=user)
        return cart


def has_cart(user):
    carts = Cart.objects.all()
    for cart in carts:
        if user == cart.user:
            return True
    return False
