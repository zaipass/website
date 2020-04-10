# MyUser NavBar Position
from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    UserManager
)

from apps.user.validators import CodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.core.mail import send_mail
from django.utils import timezone

from datetime import date

from ckeditor.fields import RichTextField


class EnNavBar(models.Model):
    """ english nav model """
    create_time = models.DateTimeField(auto_now_add=True)

    is_published = models.BooleanField(verbose_name='是否发布',
                                       default=False,
                                       help_text='是否发布')
    en_name = models.CharField(verbose_name='导航名称',
                               help_text='导航名称',
                               max_length=20)
    nav_url = models.CharField(verbose_name='导航路径',
                               help_text='导航路径',
                               null=True,
                               max_length=100,
                               validators=[RegexValidator(
                                   regex=r'^/en/(?:[0-9a-zA-Z]*[-]*[0-9a-zA-Z]*/?)$',
                                   message='例如: "/en/" 或者 "/en/index/", "/en/index-1/", 字符应为字母/数字/-',
                                   code='url-error'),
                               ])
    nav_num = models.IntegerField(verbose_name='排列顺序',
                                  help_text='排列顺序',
                                  unique=True)

    def __str__(self):
        return self.en_name

    class Meta:
        verbose_name = _('英文版导航')
        verbose_name_plural = verbose_name


class MyUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model
    """
    username_validator = CodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=100,
        unique=True,
        help_text=_('要求: 少于100位字符. 仅仅支持"数字, 字母 和 ./+/-/_"'),
        validators=[username_validator],
        error_messages={
            'unique': _("该用户名已存在."),
        },
    )
    email = models.EmailField(_('邮箱地址'),
                              unique=True,
                              blank=True)
    phone = models.CharField(max_length=11,
                             unique=True,
                             null=True,
                             blank=True,
                             verbose_name='用户号码',
                             help_text='用户号码')
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('user')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return self.username


class NavBar(models.Model):
    """ nav model """
    create_time = models.DateTimeField(auto_now_add=True)

    is_published = models.BooleanField(verbose_name='是否发布',
                                       default=False,
                                       help_text='是否发布')
    zh_name = models.CharField(verbose_name='导航名称',
                               help_text='导航名称',
                               max_length=20)
    nav_url = models.CharField(verbose_name='导航路径',
                               help_text='导航路径',
                               null=True,
                               max_length=100,
                               validators=[RegexValidator(
                                   regex=r'^/(?:[0-9a-zA-Z]*[-]*[0-9a-zA-Z]*/?)$',
                                   message='例如: "/" 或者 "/index/", "/index-1/", 字符应为字母/数字/-',
                                   code='url-error'),
                               ])
    nav_num = models.IntegerField(verbose_name='排列顺序',
                                  help_text='排列顺序',
                                  unique=True)

    def __str__(self):
        return self.zh_name

    class Meta:
        verbose_name = _('导航')
        verbose_name_plural = verbose_name


class Position(models.Model):
    create_time = models.DateTimeField(auto_now_add=True,
                                       verbose_name='创建时间',
                                       help_text='创建时间')
    createtime = models.DateField(null=True,
                                  blank=True,
                                  verbose_name='发布时间',
                                  help_text='发布时间')
    position_title = models.CharField(max_length=100,
                                      verbose_name='职位头衔',
                                      help_text='职位头衔')
    work_experience = models.CharField(max_length=100,
                                       verbose_name='工作经验',
                                       help_text='工作经验')
    work_place = models.CharField(max_length=100,
                                  verbose_name='工作地点',
                                  help_text='工作地点')
    work_salary = models.CharField(max_length=20,
                                   verbose_name='薪资待遇',
                                   help_text='薪资待遇')
    work_time = models.CharField(max_length=20,
                                 verbose_name='工作性质',
                                 help_text='工作性质')
    work_need_person = models.CharField(max_length=20,
                                        verbose_name='招聘人数',
                                        help_text='招聘人数')
    work_need = RichTextField(verbose_name='专业要求',
                              help_text='专业要求',
                              config_name='position')
    work_for = RichTextField(verbose_name='工作职责',
                             help_text='工作职责',
                             config_name='position')
    contact = models.TextField(max_length=200,
                               verbose_name='联系方式',
                               help_text='联系方式')

    POSITION_TYPE = (
        ('society', '社会招聘'),
        ('student', '校园招聘')
    )
    types = models.CharField(max_length=10,
                             choices=POSITION_TYPE,
                             verbose_name='招聘类型',
                             help_text='招聘类型')

    is_published = models.BooleanField(default=True, verbose_name='职位是否发布', help_text='职位是否发布')

    def __str__(self):
        return self.position_title

    class Meta:
        verbose_name = _('职位招聘')
        verbose_name_plural = verbose_name
