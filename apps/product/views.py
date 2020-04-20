from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from apps.product.models import Product, EnProduct
from apps.product.filters import ProductNameFilter, EnProductNameFilter
from apps.product.serializers import ProductSerializer, EnProductSerializer

from django_filters.rest_framework import DjangoFilterBackend


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.order_by('product_num', '-create_time')
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)
    filter_class = ProductNameFilter
    search_fields = ['=types__typename', ]


class EnProductView(viewsets.ModelViewSet):
    queryset = EnProduct.objects.order_by('product_num', '-create_time')
    serializer_class = EnProductSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)
    filter_class = EnProductNameFilter
    search_fields = ['=types__typename', ]
