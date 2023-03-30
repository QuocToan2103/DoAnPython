from django.db import models

from product.models import Product

# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    note = models.TextField(null=False, max_length=1208)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    approved_comment = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return self.name