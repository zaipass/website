from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.article.models import Articles, ArticleType, Certificate

from apps.user.constants import position_type

from utils.generate import generate_navbar_static_html, generate_news_detail_static_html
from utils.remove import remove_news_queryset_html, remove_news_static_html


def update_news_html(modeladmin, request, queryset):
    generate_navbar_static_html('news.html')


def generate_static_html(modeladmin, request, queryset):
    """
    :生成选择新闻的静态页面
    1. 更新新闻首页
    2. 选项中有新闻类型为"招聘信息", 则更新招贤纳士页面
    3. 生成所选的所有新闻详情
    """
    # 更新首页
    generate_navbar_static_html('news.html')

    tps = {i.types.typename for i in queryset}

    if position_type in tps:
        generate_navbar_static_html('recruitment.html')

    # 更新详情
    for i in queryset:
        if i.types.typename == position_type:
            continue
        generate_news_detail_static_html(i.id)

    # TODO ==> 更新整个新闻列表


generate_static_html.short_description = '生成所选择的静态页面'


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    """
    save_model(): 保存对象/更新对象
    1. 更新新闻页面
    2. 更新前后类型包括"招聘信息" => 更新招贤纳士页面
    delete_queryset(): 删除所选项
    1. 删除对应新闻详情页面
    2. 更新新闻页面
    3. 选项中存在类型为"招聘信息" => 更新招贤纳士页面
    """
    list_display = ('summarize', 'title', 'user', 'create_time')
    fieldsets = (
        (None, {'fields': (
            'img_header', 'title',
            'sub_title', 'summarize', 'content'
        )}),
        (_('重要信息'), {'fields': ('types', 'is_published')}),
    )
    search_fields = ('user', 'types', 'title', 'content')

    actions = [generate_static_html]

    def save_model(self, request, obj, form, change):
        tps_list = set()

        new_tps_name = obj.types.typename
        tps_list.add(new_tps_name)

        obj.user = request.user

        if change:
            object_art = Articles.objects.get(pk=obj.id)
            old_tps_name = object_art.types.typename
            tps_list.add(old_tps_name)

            if new_tps_name != old_tps_name and old_tps_name == position_type:
                remove_news_static_html(obj.id)

        obj.save()

        # 更新首页
        if position_type in tps_list:
            generate_navbar_static_html('recruitment.html')

        generate_navbar_static_html('news.html')

    def delete_queryset(self, request, queryset):

        remove_news_queryset_html(queryset)

        tps = {obj.types.typename for obj in queryset}

        queryset.delete()

        # 更新首页
        generate_navbar_static_html('news.html')

        if position_type in tps:
            generate_navbar_static_html('recruitment.html')


@admin.register(ArticleType)
class ArticleTypeAdmin(admin.ModelAdmin):
    list_display = ('typename', 'create_time')


# 添加证书 => 更新 "关于汉典" navbar页面
def update_about_html(modeladmin, request, queryset):
    generate_navbar_static_html('about.html')


update_about_html.short_description = '更新静态页面(和所选证书无关)'


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')

    actions = [update_about_html]

    def delete_queryset(self, request, queryset):
        queryset.delete()

        generate_navbar_static_html('about.html')
