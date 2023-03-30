from django.db import models

from order.models import Order
from product.models import Product

# Create your models here.
class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,null=True,blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(null=True,default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    class Meta:
        db_table = "ordersDetail"
        verbose_name_plural ="ordersDetail"
        
    def get_product_price(self):
        price = [self.product.price * self.quantity]
        return sum(price)
    

