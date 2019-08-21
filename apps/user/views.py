# from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.exceptions import NotFound
from rest_framework.decorators import action

from apps.user.models import Position
from apps.user.decorators import decorator_template
from apps.user.pagination import NewsListPagination, GoodsListPagination
from apps.user.serializers import (
    IndexSerializer, PositionSerializer, PositionIndexSerializer
)
from apps.user.utils import (
    get_next_news_not_position, get_pre_news_not_position, serializer_function
)

from apps.product.views import ProductView
from apps.product.serializers import ProductSearchSerializer

from apps.article.views import ArticleView
from apps.article.models import Certificate, Articles
from apps.article.serializers import CertificateSerializer

from apps.user.constants import product_type, news_type, position_type


class PositionView(viewsets.ModelViewSet):
    queryset = Position.objects.filter(is_published=True).order_by('-create_time')

    def get_serializer_class(self):
        if self.action == 'recruitment':
            return PositionIndexSerializer
        return PositionSerializer

    @decorator_template(pagename='recruitment-position.html')
    def list(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        response_data = {}

        if pk:
            try:
                obj = self.get_object()
            except Exception:
                obj = None
            if obj:
                serializer = self.get_serializer(obj)
                response_data.update(serializer.data)
                response_data.update({
                    'single': True,
                    'recruitmentnav': True
                })
                return response_data

        response_data['error'] = True
        response_data['render_url'] = '/recruitment/'
        return response_data

    @action(detail=False)
    @decorator_template(pagename='recruitment.html')
    def recruitment(self, request, *args, **kwargs):
        position_articles = ArticleView.queryset.filter(types__typename=position_type)

        # serializer_info = ArticleView.serializer_class(position_articles, many=True)
        serializer_position_society = self.get_serializer(
            self.get_queryset().filter(types='society'),
            many=True
        )
        serializer_position_student = self.get_serializer(
            self.get_queryset().filter(types='student'),
            many=True
        )

        return {
            'position_info': serializer_function(
                ArticleView, position_articles, is_many=True
            ),
            'position_society': serializer_position_society.data,
            'position_student': serializer_position_student.data
        }


class IndexView(viewsets.ModelViewSet):
    serializer_class = IndexSerializer
    permission_classes = []
    authentication_classes = []

    @action(detail=False)
    @decorator_template(pagename='contact.html')
    def contact(self, request, *args, **kwargs):
        return {}

    @action(detail=False)
    @decorator_template(pagename='center-1.html')
    def center_famous(self, request, *args, **kwargs):

        response_data = {
            'centernav': True,
            'current_name': '名医咨询'
        }
        return response_data

    @action(detail=False)
    @decorator_template(pagename='center-2.html')
    def center_hospital(self, request, *args, **kwargs):

        response_data = {
            'centernav': True,
            'current_name': '医学中心'
        }
        return response_data

    @action(detail=False)
    @decorator_template(pagename='center-3.html')
    def center_class(self, request, *args, **kwargs):

        response_data = {
            'centernav': True,
            'current_name': '空中课堂'
        }
        return response_data

    @decorator_template(pagename='index.html')
    def list(self, request, *args, **kwargs):
        certificates = Certificate.objects.filter(cert_type='荣誉').order_by('-create_time')

        certificate_serializer = CertificateSerializer(certificates, many=True)

        data = {
            'certs': certificate_serializer.data,
        }

        return data

    @decorator_template(pagename='index-1.html')
    def index_hd(self, request, *args, **kwargs):
        return {'abouthd': True}

    @decorator_template(pagename='index-2.html')
    def index_cy(self, request, *args, **kwargs):
        return {'abouthd': True}

    @decorator_template(pagename='index-3.html')
    def index_zy(self, request, *args, **kwargs):
        return {'abouthd': True}

    @action(detail=False)
    @decorator_template(pagename='famous.html')
    def famous(self, request, *args, **kwargs):
        return dict()

    @action(detail=False)
    @decorator_template(pagename='center.html')
    def center(self, request, *args, **kwargs):
        certificates = Certificate.objects.filter(cert_type='专利').order_by('-create_time')

        certificate_serializer = CertificateSerializer(certificates, many=True)

        data = {
            'certs': certificate_serializer.data,
            'current_name': '国家专利技术'
        }

        return data


class ProductNameView(ProductView):
    pagination_class = GoodsListPagination

    zh_new = product_type.get('new_product')
    zh_class = product_type.get('classical_product')

    def get_queryset(self):
        if self.action == 'class_product':
            return super().queryset.filter(types__typename=self.zh_class)
        elif self.action == 'new_product':
            return super().queryset.filter(types__typename=self.zh_new)
        return super().queryset

    def get_product(self, req, *args, **kwargs):
        current_page = req.query_params.get('page', 1)

        try:
            response = super().list(req, *args, **kwargs)
        except NotFound:
            return {
                'error': True,
                'render_url': '/product/'
            }
        else:
            data = {
                'product_data': response.data if response.data else None,
                'current_page': current_page if current_page else 1,
                'productnav': True,
            }
            return data

    @action(detail=False)
    @decorator_template(pagename='product.html')
    def product(self, request, *args, **kwargs):
        return dict()

    @action(detail=False)
    @decorator_template(pagename='product-1.html')
    def class_product(self, request, *args, **kwargs):
        return self.get_product(request, *args, **kwargs)

    @action(detail=False)
    @decorator_template(pagename='product-2.html')
    def new_product(self, request, *args, **kwargs):
        return self.get_product(request, *args, **kwargs)

    @decorator_template(pagename='product-detail.html')
    def list(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        serializer = ProductSearchSerializer(self.get_queryset(), many=True)

        data = {
            'product': response.data,
            'product_name_list': serializer.data,
            'productnav': True,
        }

        return data


class ArticleTypesView(ArticleView):

    pagination_class = NewsListPagination

    def get_queryset(self):
        tps = self.request.query_params.get('types')

        if tps:
            return super().get_queryset().filter(types__typename=tps)

        return super().get_queryset()

    @decorator_template(pagename='news.html')
    def list(self, request, *args, **kwargs):
        try:
            object_list = self.get_queryset().filter(types__typename=news_type.get('handian_news'))

            news_list = object_list.order_by('-is_top', '-createtime')

            # news_list = self.get_queryset().filter(types__typename=news_type.get('handian_news'))[:4]

        except Exception:
            news_list = None

        try:
            action_list = self.get_queryset().filter(
                types__typename=news_type.get('same_action'))[:4]
        except Exception:
            action_list = None

        # article_serializer = self.serializer_class(news_list, many=True)

        handian_news = serializer_function(self, news_list, is_many=True)

        # news_serializer = self.serializer_class(action_list, many=True)
        action_news = serializer_function(self, action_list, is_many=True)

        data = {
            'handian_news': handian_news if handian_news else None,
            'action_news': action_news if action_news else None
        }
        return data

    @action(detail=False)
    @decorator_template(pagename='news-detail.html')
    def news(self, request, pk, *args, **kwargs):

        try:
            pk_obj = self.get_object()
        except Exception:
            pk_obj = None
        # serializer = self.serializer_class(pk_obj)
        try:
            news_obj = pk_obj.get_next_by_create_time()
            next_news = get_next_news_not_position(news_obj)
        except Articles.DoesNotExist:
            next_news = None

        try:
            news_obj = pk_obj.get_previous_by_create_time()
            previous_news = get_pre_news_not_position(news_obj)
        except Articles.DoesNotExist:
            previous_news = None

        data = {
            'news': serializer_function(self, pk_obj),
            'newsOnenav': True,
            'next': next_news,
            'previous': previous_news
        }
        return data

    @action(detail=False)
    @decorator_template(pagename='news-list.html')
    def news_list(self, request, *args, **kwargs):
        response_data = {}
        types = request.query_params.get('types')

        page = request.query_params.get('page')

        if not types or types == position_type:
            response_data['error'] = True
            response_data['render_url'] = '/news/'
            return response_data

        try:
            response_list = super().list(request, *args, **kwargs)
        except Exception:
            response_list = None

        response_data = {
            'tps': types,
            'page': page if page else 1,
            'newsListnav': True,
        }
        if response_list:
            response_data.update(response_list.data)
        else:
            response_data.update({'results': None})

        return response_data


class SearchProductView(ProductView):
    serializer_class = ProductSearchSerializer
    search_fields = [
        'types__typename', 'name', 'composition', 'properties', 'main', 'info_detail',
    ]

    @decorator_template(pagename='search.html')
    def list(self, request, *args, **kwargs):
        data = {}
        obj_products = self.filter_queryset(self.get_queryset())
        # serializer = self.serializer_class(obj_products, many=True)
        data.update({
            'productnav': True,
            'objects': serializer_function(self, obj_products, is_many=True),
        })
        return data
