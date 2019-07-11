from django.urls import path

from apps.article.views import ArticleView


urlpatterns = [
    path('', ArticleView.as_view({'get': 'list'}), name='article')
]
