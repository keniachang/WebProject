from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class HomeAddress(models.Model):
    address_line = models.CharField(max_length=100)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=5)


class ShippingAddress(models.Model):
    address_line = models.CharField(max_length=100)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=5)

    def get_absolute_url(self):
        return reverse('shipping_edit', kwargs={'pk': self.pk})


class Credit_Card(models.Model):
    first_name = models.CharField(max_length=100, default=None)
    last_name = models.CharField(max_length=100, default=None)
    cc_number = models.CharField(max_length=30)
    cc_expiration = models.CharField(max_length=10)
    cc_security_code = models.CharField(max_length=10)

    def get_absolute_url(self):
        return reverse('payment_edit', kwargs={'pk': self.pk})


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    home_address = models.OneToOneField(HomeAddress, default=None, null=True, on_delete=models.CASCADE)
    shipping_address = models.ManyToManyField(ShippingAddress, blank=True, default=None)
    payment_info = models.ManyToManyField(Credit_Card, blank=True, default=None)
    books_owned = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
