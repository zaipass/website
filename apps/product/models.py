# ProductType Product
from django.db import models


class ProductType(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)

    typename = models.CharField(max_length=50,
                                unique=True,
                                verbose_name='类别名称',
                                help_text='类别名称')

    def __str__(self):
        return self.typename

    class Meta:
        verbose_name = '药品种类'
        verbose_name_plural = verbose_name


class Product(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)

    product_num = models.IntegerField(verbose_name='药品排序',
                                      default=1,
                                      help_text='药品排序')

    name = models.CharField(max_length=50,
                            unique=True,
                            verbose_name='药品名称',
                            help_text='药品名称')
    composition = models.CharField(max_length=255,
                                   verbose_name='药品成分',
                                   help_text='药品成分')
    properties = models.CharField(max_length=255,
                                  verbose_name='性状',
                                  help_text='性状')
    standard = models.CharField(max_length=255,
                                verbose_name='规格',
                                help_text='规格')
    main = models.CharField(max_length=255,
                            verbose_name='主要功效',
                            help_text='主要功效')
    dosage = models.CharField(max_length=255,
                              verbose_name='用法用量',
                              help_text='用法用量')
    save_way = models.CharField(max_length=255,
                                verbose_name='贮藏',
                                help_text='贮藏')
    info_detail = models.TextField(max_length=500,
                                   verbose_name='药品详细描述',
                                   help_text='药品详细描述')
    time_long = models.CharField(max_length=100,
                                 verbose_name='有效期',
                                 help_text='有效期')
    img = models.ImageField(upload_to='./upload_img/product/',
                            verbose_name='药品图片',
                            help_text='药品图片')
    types = models.ForeignKey(ProductType,
                              related_name='tps',
                              on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '药品'
        verbose_name_plural = verbose_name
