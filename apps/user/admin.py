from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.utils.translation import gettext_lazy as _

from apps.user.models import MyUser, NavBar, Position

from utils.generate import generate_navbar_static_html, generate_position_static_html
from utils.remove import remove_position_static_html


def create_position_static_html(modeladmin, request, queryset):
    # 更新页面
    generate_navbar_static_html('recruitment.html')

    for i in queryset:
        generate_position_static_html(i.id)


create_position_static_html.short_description = '生成所选职位静态文件'


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    """
    delete_queryset(): 删除选择的对象
    1. 删除职位的详情静态文件
    2. 更新招贤纳士的页面
    """
    list_display = ('position_title', 'work_salary', 'work_time', 'work_need_person', 'create_time')
    search_fields = ('position_title', 'work_salary', 'work_time', 'create_time')

    actions = [create_position_static_html]

    def delete_queryset(self, request, queryset):

        id_list = [obj.id for obj in queryset]

        queryset.delete()

        for i in id_list:
            remove_position_static_html(i)

        generate_navbar_static_html('recruitment.html')


@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('phone', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'phone', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'email', 'phone', 'is_staff')
    search_fields = ('username', 'phone', 'email')


# 静态化 navbar 页面
def generate_navbar_html(modeladmin, request, queryset):
    for qs in queryset:
        generate_navbar_static_html('{}'.format(qs.nav_html))


generate_navbar_html.short_description = '生成所选导航模块的静态页面'


@admin.register(NavBar)
class NavBar(admin.ModelAdmin):
    list_display = ('zh_name', 'nav_num', 'nav_url', 'nav_html', 'is_published')
    list_editable = ('is_published',)

    actions = [generate_navbar_html]

    def save_model(self, request, obj, form, change):
        """
        Given a model instance save it to the database.
        Generate the static html
        """
        obj.save()
        # after save
        generate_navbar_static_html('{}'.format(obj.nav_html))


admin.site.site_header = '汉典制药官网后台管理'
admin.site.site_title = '汉典制药官网后台管理'
