from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from apps.product.models import Product
from apps.product.filters import ProductNameFilter
from apps.product.serializers import ProductSerializer

from django_filters.rest_framework import DjangoFilterBackend


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-create_time')
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)
    filter_class = ProductNameFilter
    search_fields = ['=types__typename', ]
