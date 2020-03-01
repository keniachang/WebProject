from django.db import models
from django.conf import settings

# Create your models here.
from book.models import Book


# Create your models here.

class bigWishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def add_wishlist(self, swishlist):

        if self.smallwishlist_set.count() >= 3:

            raise Exception("Too many wishlists.")

        self.smallwishlist_set.add(swishlist)


class smallWishlist(models.Model):
    name = models.CharField(max_length=30, null=False, default='Wishlist')
    list = models.ForeignKey(bigWishlist, on_delete=models.CASCADE)


class WishlistItem(models.Model):
    item = models.ForeignKey(Book, on_delete=models.CASCADE)
    wishlist = models.ForeignKey(smallWishlist, on_delete=models.CASCADE)
