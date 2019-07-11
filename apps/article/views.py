from rest_framework import viewsets

from django_filters.rest_framework import DjangoFilterBackend

from apps.article.models import Articles
from apps.article.serializers import ArticleSerializer

from apps.article.filters import ArticleTypeFilter


class ArticleView(viewsets.ModelViewSet):
    """
    For NEWS API
    """
    queryset = Articles.objects.filter(is_published=True).order_by('-create_time')
    serializer_class = ArticleSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = ArticleTypeFilter
