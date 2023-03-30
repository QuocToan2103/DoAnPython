from django.contrib import admin
from category.models import Category
from django.utils.html import format_html
# Register your models here.
class CategoryAdmin (admin.ModelAdmin):
    def image_tag(self, obj): 
        return format_html('<img src="{}" style="max-width:100px; max-height:80px"/>'.format(obj.image.url))
    list_display = ['name','image_tag', 'description'] 
admin.site.register(Category, CategoryAdmin)