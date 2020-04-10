from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.user.models import MyUser, NavBar, Position, EnNavBar

from django.utils.translation import gettext_lazy as _


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('position_title', 'work_salary', 'work_time', 'work_need_person', 'create_time')
    search_fields = ('position_title', 'work_salary', 'work_time', 'create_time')


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


@admin.register(NavBar)
class NavBar(admin.ModelAdmin):
    list_display = ('zh_name', 'nav_num', 'nav_url', 'is_published')


@admin.register(EnNavBar)
class EnNavBar(admin.ModelAdmin):
    list_display = ('en_name', 'nav_num', 'nav_url', 'is_published')


admin.site.site_header = '汉典制药官网后台管理'
admin.site.site_title = '汉典制药官网后台管理'
