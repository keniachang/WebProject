from django.db import models
from django.conf import settings


class Comment(models.Model):
    title = models.CharField(max_length=255, null=False)
    comments = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)

