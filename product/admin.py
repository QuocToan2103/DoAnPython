from django.contrib import admin
from product.models import Product
from django.utils.html import format_html
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name']
    def image_tag(self, obj): 
        return format_html('<img src="{}" style="max-width:80px; max-height:80px"/>'.format(obj.image.url))
    list_display = ['name','quantity','price','image_tag','categoryId'] 
admin.site.register(Product ,ProductAdmin)