from django.contrib import admin
from .models import Profile, HomeAddress, ShippingAddress, Credit_Card



admin.site.register(Profile)
admin.site.register(HomeAddress)
admin.site.register(ShippingAddress)
admin.site.register(Credit_Card)

