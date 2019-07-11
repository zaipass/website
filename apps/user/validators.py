from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _, ngettext


@deconstructible
class CodeUsernameValidator(validators.RegexValidator):
    """
    Validate username and exclude '@'
    """
    regex = r"^[\w.+-]+$"
    message = _(
        "请输入有效用户名称,包含'字母','数字',或者特殊字符'./+/-/_'"
    )
    flags = 0


class MaxmumLengthValidator:
    """
    Validate whether the password is of a max length.
    """

    def __init__(self, max_length=16):
        self.max_length = max_length

    def validate(self, password, user=None):
        if len(password) > self.max_length:
            raise ValidationError(
                ngettext(
                    "密码长度不可超过 %(max_length)d 字符.",
                    "密码长度不可超过 %(max_length)d 字符.",
                    self.max_length
                ),
                code='password_too_long',
                params={'max_length': self.max_length},
            )

    def get_help_text(self):
        return ngettext(
            "密码长度不可超过 %(max_length)d 字符.",
            "密码长度不可超过 %(max_length)d 字符.",
            self.max_length
        ) % {'max_length': self.max_length}
