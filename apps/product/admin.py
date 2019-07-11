from django.contrib import admin
from apps.product.models import Product, ProductType


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'main', 'time_long', 'types')


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('typename', 'create_time')
