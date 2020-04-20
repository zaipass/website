from django.contrib import admin
from apps.product.models import Product, ProductType, EnProduct, EnProductType


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'main', 'time_long', 'types')


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('typename', 'create_time')


@admin.register(EnProduct)
class EnProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'main', 'time_long', 'types')


@admin.register(EnProductType)
class EnProductTypeAdmin(admin.ModelAdmin):
    list_display = ('typename', 'create_time')
