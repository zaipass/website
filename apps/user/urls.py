from django.urls import path
from apps.user.views import (
    IndexView, ProductNameView, ArticleTypesView, PositionView, SearchProductView
)

urlpatterns = [
    # path('', IndexView.as_view({'get': 'list'}), name='index'),
    path('', IndexView.as_view({'get': 'list'}), name='index'),
    path('index_hd/', IndexView.as_view({'get': 'index_hd'}), name='index-hd'),
    path('index_cy/', IndexView.as_view({'get': 'index_cy'}), name='index-cy'),
    path('index_zy/', IndexView.as_view({'get': 'index_zy'}), name='index-zy'),

    path('famous/', IndexView.as_view({'get': 'famous'}), name='famous'),
    path('center/', IndexView.as_view({'get': 'center'}), name='center'),
    path('contact/', IndexView.as_view({'get': 'contact'}), name='contact'),
    path('center_famous/', IndexView.as_view({'get': 'center_famous'}), name='center-famous'),
    path('center_hospital/', IndexView.as_view({'get': 'center_hospital'}), name='center-hospital'),
    path('center_class/', IndexView.as_view({'get': 'center_class'}), name='center-class'),

    # the product
    path('product/class_product/', ProductNameView.as_view({'get': 'class_product'}), name='product-class'),
    path('product/new_product/', ProductNameView.as_view({'get': 'new_product'}), name='product-new'),
    path('product/<int:pk>/', ProductNameView.as_view({'get': 'list'}), name='product-all'),
    path('product/', ProductNameView.as_view({'get': 'product'}), name='product'),

    path('news/', ArticleTypesView.as_view({'get': 'list'}), name='news'),
    path('news/<int:pk>/',
         ArticleTypesView.as_view({'get': 'news'}), name='news-detail'),
    path('news_list/', ArticleTypesView.as_view({'get': 'news_list'}), name='news-list'),
    path('recruitment/', PositionView.as_view({'get': 'recruitment'}), name='recruitment'),
    path('position/<int:pk>/',
         PositionView.as_view({'get': 'list'}), name='recruitment-position'),
    path('position/',
         PositionView.as_view({'get': 'list'}), name='position'),

    path('search/', SearchProductView.as_view({'get': 'list'}), name='search'),

]
