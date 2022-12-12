from django.contrib import admin
from products.models import Product, Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    exclude = ["formats", ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
