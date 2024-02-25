from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display=['name','owner','price']
    list_filter=['owner']
    search_fields=['owner__username__icontains','name']
    readonly_fields=['owner','id','created_at']



admin.site.register(Product,ProductAdmin)
admin.site.register(Category)
admin.site.register(SubCategory)




# Register your models here.
