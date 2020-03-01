from django.contrib import admin

from .models import bigWishlist, smallWishlist, WishlistItem
# Register your models here.
admin.site.register(bigWishlist)
admin.site.register(smallWishlist)
admin.site.register(WishlistItem)


