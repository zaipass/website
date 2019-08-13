from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.product.models import Product, ProductType
from apps.user.constants import product_type

from utils.generate import (
    generate_product_type_static_html,
    update_all_product_detail, update_two_types_list
)
from utils.remove import remove_static_html, remove_queryset_html


# 添加自定义的 action 操作
def generate_html(modeladmin, request, queryset):
    update_all_product_detail()

    update_two_types_list(queryset)


generate_html.short_description = _('生成所选药品的静态文件')


def remove_html(modeladmin, request, queryset):
    update_all_product_detail()

    update_two_types_list(queryset)

    remove_queryset_html(queryset)


remove_html.short_description = _('删除所选药品的静态文件')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    delete_model(): 删除对象进行的操作
    1. 移除商品详情页面
    2. 更新此商品类型的分类静态页
    3. 更新所有商品的商品列表

    delete_queryset(): 删除所选的对象
    1. 移除所选择的商品静态页
    2. 更新所选择的商品类型的分类静态页
    3. 更新所有商品的商品列表
    """
    list_display = ('name', 'main', 'time_long', 'types')
    actions = [generate_html]

    # def save_model(self, request, obj, form, change):
    #     """
    #     Given a model instance save it to the database.
    #     Generate the static html
    #     """
    #     obj.save()

    #     update_all_product_detail()

    #     tps_name = obj.types.typename
    #     for k, v in product_type.items():
    #         if v == tps_name:
    #             generate_product_type_static_html(tps=k)

    def delete_model(self, request, obj):
        """
        Given a model instance delete it from the database.
        Delete the static html
        """
        # before delete
        remove_static_html(obj.id)

        tps_name = obj.types.typename

        obj.delete()

        for k, v in product_type.items():
            if v == tps_name:
                generate_product_type_static_html(tps=k)

        update_all_product_detail()

    def delete_queryset(self, request, queryset):
        """Given a queryset, delete it from the database."""

        tps_list = {obj.types.typename for obj in queryset}

        remove_queryset_html(queryset)

        queryset.delete()

        for k, v in product_type.items():
            if v in tps_list:
                generate_product_type_static_html(tps=k)

        update_all_product_detail()


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('typename', 'create_time')
