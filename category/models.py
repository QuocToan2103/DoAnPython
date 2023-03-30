from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=1500)
    description = models.TextField()
    image = models.ImageField(upload_to='photos/categories' , null=True)
    class Meta:
        db_table = "Categories"
        verbose_name_plural ="Categories"
    def __str__(self):
        return self.name