import django_filters

from apps.article.models import Articles, EnArticles


class EnArticleTypeFilter(django_filters.FilterSet):

    types = django_filters.CharFilter(field_name='types__typename')
    pk = django_filters.CharFilter(field_name='id')

    class Meta:
        model = EnArticles
        fields = ['types', 'pk']


class ArticleTypeFilter(django_filters.FilterSet):

    types = django_filters.CharFilter(field_name='types__typename')
    pk = django_filters.CharFilter(field_name='id')

    class Meta:
        model = Articles
        fields = ['types', 'pk']
