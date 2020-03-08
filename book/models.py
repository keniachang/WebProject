from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255, null=False)
    cover = models.URLField(max_length=300, null=False)
    author = models.CharField(max_length=50, null=False)
    bio = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    genre = models.CharField(max_length=50, null=False)
    publisher = models.CharField(max_length=100, null=False)
    release_date = models.CharField(max_length=20, null=False)
    rating = models.DecimalField(min_value=0.0, max_value=5.0, max_digits=2, decimal_places=1, null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    price = models.DecimalField(null=False, max_digits=5, decimal_places=2)
