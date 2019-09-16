# Articles ArticleType Certificate
from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField

from apps.user.models import MyUser


class ArticleType(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)

    typename = models.CharField(max_length=20,
                                verbose_name='类别名称',
                                help_text='类别名称')

    def __str__(self):
        return self.typename

    class Meta:
        verbose_name = '新闻/文章类别'
        verbose_name_plural = verbose_name


class Articles(models.Model):

    ART_TYPE = (
        ('normal', '无'),
        ('famous', '名医咨询'),
        ('center', '医学中心'),
        ('product', '服务与产品'),
    )

    create_time = models.DateTimeField(auto_now_add=True)

    createtime = models.DateField(verbose_name='发布时间',
                                  help_text='发布时间',
                                  null=True,
                                  blank=True,)

    img_header = models.ImageField(upload_to='./upload_img/news-header/',
                                   null=True,
                                   verbose_name='新闻封面图片',
                                   help_text='新闻封面图片')

    title = models.CharField(max_length=200,
                             verbose_name='文章标题',
                             help_text='文章标题')
    sub_title = models.CharField(max_length=100,
                                 verbose_name='文章副标题',
                                 help_text='文章副标题')

    summarize = models.CharField(max_length=300,
                                 verbose_name='文章概述',
                                 null=True,
                                 blank=True,
                                 help_text='文章概述')

    content = RichTextUploadingField(config_name='wo')

    types = models.ForeignKey(ArticleType,
                              related_name='article',
                              on_delete=models.CASCADE)

    is_published = models.BooleanField(verbose_name='是否发布',
                                       default=False,
                                       help_text='是否发布')
    is_top = models.BooleanField(verbose_name='是否置顶', default=False, help_text='是否置顶')

    user = models.ForeignKey(MyUser, related_name='article', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '新闻/文章'
        verbose_name_plural = verbose_name


class Certificate(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)

    img = models.ImageField(upload_to='./upload_img/cert/',
                            verbose_name='证书图片',
                            help_text='证书图片')

    title = models.CharField(max_length=200,
                             verbose_name='证书描述',
                             help_text='证书描述')
    content = models.TextField(max_length=800,
                               verbose_name='证书详情',
                               help_text='证书详情')
    CERT_TYPE_CHOICE = (
        ('专利', '专利'),
        ('荣誉', '荣誉')
    )
    cert_type = models.CharField(max_length=4, choices=CERT_TYPE_CHOICE, verbose_name='证书类型', help_text='证书类型')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '技术/荣誉证书'
        verbose_name_plural = verbose_name
