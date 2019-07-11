from django.apps import AppConfig

from django.utils.translation import gettext_lazy as _

VERBOSE_APP_NAME = "user"


class UserConfig(AppConfig):
    name = 'apps.user'
    verbose_name = _(VERBOSE_APP_NAME)
