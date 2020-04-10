from django.urls import path
from apps.user.views import (
    IndexView, ProductNameView, ArticleTypesView, PositionView, SearchProductView
)
from apps.user.views_en import (
    EnIndexView, EnProductNameView, EnArticleTypesView,
    EnPositionView,
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

urlpatterns.extend([
    path('en/', EnIndexView.as_view({'get': 'list'}), name='en-index'),

    path('en/center/', EnIndexView.as_view({'get': 'center'}), name='en-center'),
    path('en/center_famous/', EnIndexView.as_view({'get': 'center_famous'}), name='en-center-famous'),
    path('en/center_hospital/', EnIndexView.as_view({'get': 'center_hospital'}), name='en-center-hospital'),
    path('en/center_class/', EnIndexView.as_view({'get': 'center_class'}), name='en-center-class'),

    path('en/product/', EnProductNameView.as_view({'get': 'product'}), name='en-product'),
    path('en/product/class_product/', EnProductNameView.as_view({'get': 'class_product'}), name='en-product-class'),
    path('en/product/new_product/', EnProductNameView.as_view({'get': 'new_product'}), name='en-product-new'),
    path('en/product/<int:pk>/', EnProductNameView.as_view({'get': 'list'}), name='en-product-all'),

    path('en/news/', EnArticleTypesView.as_view({'get': 'list'}), name='en-news'),
    path('en/news/<int:pk>/', EnArticleTypesView.as_view({'get': 'news'}), name='en-news-detail'),
    path('en/news_list/', EnArticleTypesView.as_view({'get': 'news_list'}), name='en-news-list'),

    path('en/recruitment/', EnPositionView.as_view({'get': 'recruitment'}), name='en-recruitment'),
    path('en/position/<int:pk>/', EnPositionView.as_view({'get': 'list'}), name='en-recruitment-position'),

    path('en/contact/', EnIndexView.as_view({'get': 'contact'}), name='en-contact'),

    path('en/index_hd/', EnIndexView.as_view({'get': 'index_hd'}), name='en-index-hd'),
    path('en/index_cy/', EnIndexView.as_view({'get': 'index_cy'}), name='en-index-cy'),
    path('en/index_zy/', EnIndexView.as_view({'get': 'index_zy'}), name='en-index-zy'),


])
