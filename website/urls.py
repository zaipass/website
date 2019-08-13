"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('', include(('apps.user.urls', 'user'), namespace='user')),
    path('hd/', include(('apps.user.urls', 'user'), namespace='user-hd')),
    path('goods/', include(('apps.product.urls', 'goods'), namespace='goods')),
    path('articles/', include(('apps.article.urls', 'articles'), namespace='articles')),

    path('api/', include_docs_urls(
        title='官网API',
        authentication_classes=[],
        permission_classes=[])),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
