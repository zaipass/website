from django.conf import settings
from django.template import loader
from django.core.paginator import Paginator

from apps.user.utils import get_all_navbar
from apps.user.models import Position
from apps.user.constants import product_type, news_type, position_type
from apps.user.utils import get_next_news_not_position, get_pre_news_not_position
from apps.user.serializers import PositionIndexSerializer, PositionSerializer

from apps.product.models import Product
from apps.product.serializers import ProductSerializer

from apps.article.models import Certificate, Articles
from apps.article.serializers import CertificateSerializer, ArticleSerializer

from .constants import center_static_type

import os


def generate_base(data, pagename, to_pagename):
    """
    :data: 需要渲染的数据
    :pagename: 模板文件的名称
    :to_pagename: 生成文件的名称
    :tps: 生成产品列表详情
    """
    context = get_all_navbar()
    data.update(context)

    try:
        temp = loader.get_template(pagename)
    except loader.TemplateDoesNotExist:
        raise ValueError('模板不存在')

    static_html = temp.render(data)

    save_path = os.path.join(settings.BASE_DIR, 'static/{}'.format(to_pagename))

    with open(save_path, 'w') as f:
        f.write(static_html)


def generate_static_html(pk):
    # 动态页面静态化-商品详情
    product_object = Product.objects.get(pk=pk)
    product_object_list = Product.objects.order_by('product_num', '-create_time')

    product_serializer = ProductSerializer(product_object)

    data = {
        'product': product_serializer.data,
        'product_name_list': product_object_list,
        'productnav': True,
    }

    to_pagename = 'product/product-{}.html'.format(pk)

    generate_base(data, 'product-detail.html', to_pagename)

    # 首页重新生成
    generate_navbar_static_html('index.html')


def generate_product_type_static_html(tps):
    if not tps:
        # 选择更新全部
        raise ValueError('参数不可为none')

    if tps == 'new_product':
        # 更新新品
        product_types_list = Product.objects.filter(types__typename=product_type.get(tps)).order_by('product_num', '-create_time')
        webname = 'product-new.html'

    elif tps == 'classical_product':
        # 更新经典
        product_types_list = Product.objects.filter(types__typename=product_type.get(tps)).order_by('product_num', '-create_time')
        webname = 'product-classical.html'

    product_serializer = ProductSerializer(product_types_list, many=True)

    pg = Paginator(product_serializer.data, 6)
    pg_objects = pg.get_page(1)

    data = {
        'product_data': {
            'results': pg_objects if pg_objects else None,
            'total_pages': pg.num_pages,
            'range_pages': [num for num in range(1, pg.num_pages + 1)],
            'next': pg_objects.has_next(),
            'previous': pg_objects.has_previous(),
            'previous_page_number': pg_objects.previous_page_number() if pg_objects.has_previous() else None,
            'next_page_number': pg_objects.next_page_number() if pg_objects.has_next() else None,
        },
        'current_page': 1,
        'module_name': 'product.html',
    }
    generate_base(data, webname, webname)

    # 首页重新生成
    generate_navbar_static_html('index.html')


# 更新所有商品信息页面
def update_all_product_detail():
    product_list = Product.objects.all()

    for pro in product_list:
        generate_static_html(pro.id)


# 更新两种商品类型的页面
def update_two_types_list(queryset):
    if queryset:
        tps_list = {obj.types.typename for obj in queryset}
    else:
        tps_list = product_type.values()

    for k, v in product_type.items():
        if v in tps_list:
            generate_product_type_static_html(tps=k)


# 静态化导航页
# 固定模块; 如需增加模块需要重新添加
def generate_navbar_static_html(pageurl):

    if not isinstance(pageurl, str):
        raise ValueError('导航页面参数非字符串')

    split_list = pageurl.split('.')

    name = split_list[0]

    if not name:
        name = 'index'

    data = {
        'module_name': pageurl,
    }

    if name == 'index':
        # 首页 ==>返回所有的产品
        product_object_list = Product.objects.order_by('product_num', '-create_time')

        products_serializer = ProductSerializer(product_object_list, many=True)

        data.update({'data_list': products_serializer.data})

    elif name == 'about':
        # 走进汉典 ==> 荣誉

        certificates = Certificate.objects.all().order_by('-create_time')

        certificate_serializer = CertificateSerializer(certificates, many=True)

        data.update({'certs': certificate_serializer.data})

    elif name == 'center':
        for html_name, name_zh in center_static_type.items():
            data.update({'current_name': name_zh})
            generate_base(data, html_name, html_name)

        data['current_name'] = '国家专利技术'

    elif name == 'product':
        update_two_types_list(None)

    elif name == 'news':
        articles_queryset = Articles.objects.filter(is_published=True).order_by('-create_time')

        # 汉典新闻
        articles_news = articles_queryset.filter(types__typename=news_type.get('handian_news'))[:4]
        news_serializer = ArticleSerializer(articles_news, many=True)

        # 行业动态
        articles_action = articles_queryset.filter(types__typename=news_type.get('same_action'))[:4]
        action_serializer = ArticleSerializer(articles_action, many=True)

        data.update({
            'handian_news': news_serializer.data if news_serializer.data else None,
            'action_news': action_serializer.data if action_serializer.data else None
        })

    elif name == 'recruitment':
        # 招聘信息
        pose_info = Articles.objects.filter(is_published=True).order_by('-create_time').filter(types__typename=position_type)
        post_serializer = ArticleSerializer(pose_info, many=True)

        position_queryset = Position.objects.filter(is_published=True).order_by('-create_time')

        # 校招
        student_position = position_queryset.filter(types='student')
        student_serializer = PositionIndexSerializer(student_position, many=True)

        # 社招
        society_position = position_queryset.filter(types='society')
        society_serializer = PositionIndexSerializer(society_position, many=True)

        data.update({
            'position_info': post_serializer.data,
            'position_society': society_serializer.data,
            'position_student': student_serializer.data
        })

    generate_base(data, pageurl, pageurl)


# 生成新闻详情静态页
def generate_news_detail_static_html(pk):

    article_object = Articles.objects.get(pk=pk)

    article_serializer = ArticleSerializer(article_object)

    try:
        news_obj = article_object.get_next_by_create_time()
        next_news = get_next_news_not_position(news_obj)
    except Articles.DoesNotExist:
        next_news = None

    try:
        news_obj = article_object.get_previous_by_create_time()
        previous_news = get_pre_news_not_position(news_obj)
    except Articles.DoesNotExist:
        previous_news = None

    data = {
        'news': article_serializer.data,
        'newsOnenav': True,
        'next': next_news,
        'previous': previous_news
    }

    generate_base(data, 'news-detail.html', 'news/news-{}.html'.format(pk))


# 生成职位详情静态页
def generate_position_static_html(pk):
    position_object = Position.objects.get(pk=pk)
    position_serializer = PositionSerializer(position_object)

    data = {
        'single': True,
        'recruitmentnav': True
    }

    data.update(position_serializer.data)

    generate_base(data, 'recruitment-position.html', 'position/position-{}.html'.format(pk))
