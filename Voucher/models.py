from datetime import timezone
from django.db import models

# Create your models here.
class Voucher(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount_percent = models.FloatField(default=0.0)
    valid_from = models.DateField()
    valid_to = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return self.code

    def is_valid(self):
        now = timezone.now().date()
        return self.valid_from <= now and self.valid_to >= now
        
    def save(self, *args, **kwargs):
        if not self.is_valid():
            self.is_active = False
        super(Voucher, self).save(*args, **kwargs)