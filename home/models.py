from django.db import models

from product.models import Product
from django.contrib.auth.models import User

# Create your models here.
class VariationManager(models.Manager):
    def colors(self):
        # Trả về tất các bản ghi có loại là color
        return super(VariationManager, self).filter(variation_category='color', is_active=True)

    def sizes(self):
        # Trả về tất các bản ghi có loại là size
        return super(VariationManager, self).filter(variation_category='size', is_active=True)

variation_category_choice = (
    ('color', 'color'),
    ('size', 'size'),
)

