from django.contrib.auth.models import User
from products.models import Product
from django.db import models


# Create your models here.


class Reviews(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.content
