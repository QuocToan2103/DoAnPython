from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=100,null=False)
    subject = models.CharField(max_length=1208,null=False)
    email = models.EmailField(max_length=50,null=True,blank=True)
    message = models.TextField(null=False, max_length=1208)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    def __str__(self):
        return self.email