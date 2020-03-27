from django.db import models
from django.contrib.auth.models import User




class Address(models.Model):

    address_line = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=5)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length = 12)


class Credit_Card(models.Model):
    cc_number = models.CharField(max_length=30)
    cc_expiration = models.CharField(max_length=10)
    cc_security_code = models.CharField(max_length=10)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    home_address = models.ManyToManyField(Address, related_name='home_address', blank=True ,default=None)
    shipping_address = models.ManyToManyField(Address, related_name='shipping_address', blank=True ,default=None)
    payment_info = models.ManyToManyField(Credit_Card, blank=True, default=None)
    books_owned = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'


