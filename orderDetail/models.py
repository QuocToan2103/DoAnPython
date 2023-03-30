from django.db import models

# Create your models here.
class OrderDetail(models.Model):
    order_code = models.CharField(max_length=150)
    product_id = models.IntegerField(max_length=150)
    status = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "OrderDetails"
        verbose_name_plural ="OrderDetails"
        
    def __str__(self):
        return self.code
    

