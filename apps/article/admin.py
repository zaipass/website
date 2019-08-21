from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.article.models import Articles, ArticleType, Certificate


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('summarize', 'title', 'user', 'create_time')
    fieldsets = (
        (None, {'fields': (
            'img_header', 'title',
            'sub_title', 'summarize', 'createtime', 'content'
        )}),
        (_('重要信息'), {'fields': ('types', 'is_published', 'is_top')}),
    )
    search_fields = ('user', 'types', 'title', 'content')

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


@admin.register(ArticleType)
class ArticleTypeAdmin(admin.ModelAdmin):
    list_display = ('typename', 'create_time')


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'cert_type')
