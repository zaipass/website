# from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action

from apps.user.models import Position
from apps.user.decorators import decorator_template
from apps.user.pagination import NewsListPagination
from apps.user.serializers import IndexSerializer, PositionSerializer, PositionIndexSerializer
from apps.user.utils import get_next_news_not_position, get_pre_news_not_position, serializer_function

from apps.product.views import ProductView
from apps.product.models import Product
from apps.product.serializers import ProductSerializer, ProductSearchSerializer

from apps.article.views import ArticleView
from apps.article.models import Certificate, Articles
from apps.article.serializers import CertificateSerializer

from apps.user.constants import product_type, news_type, position_type

import math


class PositionView(viewsets.ModelViewSet):
    queryset = Position.objects.all().order_by('-create_time')

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
            'position_info': serializer_function(ArticleView, position_articles, is_many=True),
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
    def center_remote(self, request, *args, **kwargs):

        response_data = {
            'centernav': True,
            'current_name': '远程医疗'
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
            'current_name': '云课堂'
        }
        return response_data

    @decorator_template(pagename='index.html')
    def list(self, request, *args, **kwargs):
        all_products = Product.objects.all()

        list_products = ProductSerializer(all_products, many=True)

        data = {
            'data_list': list_products.data
        }

        return data

    @action(detail=False)
    @decorator_template(pagename='about.html')
    def about(self, request, *args, **kwargs):
        certificates = Certificate.objects.all().order_by('-create_time')

        certificate_serializer = CertificateSerializer(certificates, many=True)

        data = {
            'certs': certificate_serializer.data,
        }

        return data

    @action(detail=False)
    @decorator_template(pagename='famous.html')
    def famous(self, request, *args, **kwargs):
        return dict()

    @action(detail=False)
    @decorator_template(pagename='center.html')
    def center(self, request, *args, **kwargs):
        certificates = Certificate.objects.all().order_by('-create_time')

        certificate_serializer = CertificateSerializer(certificates, many=True)

        data = {
            'certs': certificate_serializer.data,
            'current_name': '国家专利技术'
        }

        return data


class ProductNameView(ProductView):
    zh_new = product_type.get('new_product')
    zh_class = product_type.get('classical_product')

    def get_queryset(self):
        tps = self.request.query_params.get('types')

        if tps == self.zh_class:
            return super().get_queryset().filter(types__typename=self.zh_class)
        elif tps == self.zh_new:
            return super().get_queryset().filter(types__typename=self.zh_new)

        return super().get_queryset()

    # def get_serializer(self, *args, **kwargs):
    #     """
    #     get_serializer and serializer of difference: override GeneriView get_serializer()
    #     """
    #     serializer_class = self.get_serializer_class()
    #     return serializer_class(*args, **kwargs)

    @action(detail=False)
    @decorator_template(pagename='product.html')
    def product(self, request, *args, **kwargs):

        class_products = self.get_queryset().filter(types__typename=self.zh_class)

        # class_serializer = self.serializer_class(class_products, many=True)
        class_list_product = serializer_function(self, class_products, is_many=True)

        # new products
        new_products = self.get_queryset().filter(types__typename=self.zh_new)
        # new_serializer = self.serializer_class(new_products, many=True)
        new_list_product = serializer_function(self, new_products, is_many=True)

        rows = math.ceil(len(new_list_product) / 2)

        new_list = []
        index = 0

        for row in range(rows):
            data = new_list_product[index:index + 2]
            index += 2
            new_list.append(data)

        data = {
            'class_products': class_list_product,
            'new_products': new_list,
        }

        return data

    @decorator_template(pagename='one-product.html')
    def list(self, request, *args, **kwargs):
        data = {}

        # if no params 'types': return '/product/' page
        current_types = request.query_params.get('types')
        # if not current_types:
        #     data['error'] = True
        #     data['render_url'] = '/product/'
        #     return data
        try:
            # ?name=
            view_response = super().list(self, request, *args, **kwargs)

            if len(view_response.data) != 1:
                data['error'] = True
                data['render_url'] = '/product/'
                return data

        except Exception as e:
            print(e, '=w==')
            data['error'] = True
            data['render_url'] = '/product/'
            return data
        # all classical products
        class_products = self.get_queryset()

        data.update({
            'product': view_response.data[0],
            'productnav': True,
            'current_types': current_types,
            'classical_name_list': class_products,
        })

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
            news_list = self.get_queryset().filter(
                types__typename=news_type.get('handian_news'))[:4]
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
