from django.db import models

# Create your models here.
class Order(models.Model):
    code = models.CharField(max_length=150)
    description = models.TextField()
    status = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "Orders"
        verbose_name_plural ="Orders"
        
    def __str__(self):
        return self.code
