import django_filters
from apps.product.models import Product


class ProductNameFilter(django_filters.FilterSet):
    """
    search a product of the name
    """
    name = django_filters.CharFilter(field_name='name', )
    types = django_filters.CharFilter(field_name='types__typename',)

    class Meta:
        model = Product
        fields = ['name', 'types', ]


class SearchProductFilter(django_filters.FilterSet):
    """
    search a product of the name
    """
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    types = django_filters.CharFilter(field_name='types__typename', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['name', 'types', ]
