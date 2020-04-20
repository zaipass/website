from rest_framework import viewsets

from django_filters.rest_framework import DjangoFilterBackend

from apps.article.models import Articles, EnArticles
from apps.article.serializers import ArticleSerializer

from apps.article.filters import ArticleTypeFilter, EnArticleTypeFilter


class EnArticleView(viewsets.ModelViewSet):
    """
    En: For NEWS API
    """
    queryset = EnArticles.objects.filter(is_published=True).order_by('-createtime')
    serializer_class = ArticleSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = EnArticleTypeFilter


class ArticleView(viewsets.ModelViewSet):
    """
    For NEWS API
    """
    queryset = Articles.objects.filter(is_published=True).order_by('-createtime')
    serializer_class = ArticleSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = ArticleTypeFilter
