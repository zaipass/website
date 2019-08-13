import os

from django.conf import settings

from apps.user.constants import position_type


# 删除商品详情页
def remove_static_html(pk):
    path = os.path.join(settings.BASE_DIR, 'static')
    try:
        os.remove('{}/product/product-{}.html'.format(path, pk))
    except FileNotFoundError:
        pass


# 删除的商品列表的详情页
def remove_queryset_html(queryset):
    for i in queryset:
        remove_static_html(i.id)


# 删除职位详情页
def remove_position_static_html(pk):
    path = os.path.join(settings.BASE_DIR, 'static')
    try:
        os.remove('{}/position/position-{}.html'.format(path, pk))
    except FileNotFoundError:
        pass


# 删除多个职位详情页
def remove_position_queryset_html(queryset):
    for i in queryset:
        remove_position_static_html(i.id)


# 删除新闻详情页
def remove_news_static_html(pk):
    path = os.path.join(settings.BASE_DIR, 'static')
    try:
        os.remove('{}/news/news-{}.html'.format(path, pk))
    except FileNotFoundError:
        pass


# 删除多个新闻详情页
def remove_news_queryset_html(queryset):
    for i in queryset:
        if i.types.typename == position_type:
            continue
        remove_news_static_html(i.id)
