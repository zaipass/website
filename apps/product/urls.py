from django.urls import path

from apps.product.views import ProductView

urlpatterns = [
    path('list/', ProductView.as_view({'get': 'list'}), name='product-list'),
]
