# from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.exceptions import NotFound
from rest_framework.decorators import action

from django.shortcuts import render

from apps.user.models import EnPosition
from apps.user.decorators import en_decorator_template
from apps.user.pagination import NewsListPagination, GoodsListPagination
from apps.user.serializers import (
    IndexSerializer, PositionSerializer, PositionIndexSerializer
)
from apps.user.utils import (
    get_next_news_not_position, get_pre_news_not_position, serializer_function
)

from apps.product.views import EnProductView
from apps.product.models import EnProduct
from apps.product.serializers import EnProductSearchSerializer

from apps.article.views import EnArticleView
from apps.article.models import EnCertificate, EnArticles
from apps.article.serializers import CertificateSerializer

from apps.user.constants import en_product_type, en_news_type, en_position_type

from django.utils.translation import gettext_lazy as _


class EnPositionView(viewsets.ModelViewSet):
    queryset = EnPosition.objects.filter(is_published=True).order_by('-create_time')

    def get_serializer_class(self):
        if self.action == 'recruitment':
            return PositionIndexSerializer
        return PositionSerializer

    @en_decorator_template(pagename='en/recruitment-position.html')
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
        response_data['render_url'] = '/en/recruitment/'
        return response_data

    @action(detail=False)
    @en_decorator_template(pagename='en/recruitment.html')
    def recruitment(self, request, *args, **kwargs):
        position_articles = EnArticleView.queryset.filter(types__typename=en_position_type)

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
                EnArticleView, position_articles, is_many=True
            ),
            'position_society': serializer_position_society.data,
            'position_student': serializer_position_student.data
        }


class EnIndexView(viewsets.ModelViewSet):
    serializer_class = IndexSerializer
    permission_classes = []
    authentication_classes = []

    @en_decorator_template(pagename='en/index-1.html')
    def index_hd(self, request, *args, **kwargs):
        return {'abouthd': True}

    @en_decorator_template(pagename='en/index-2.html')
    def index_cy(self, request, *args, **kwargs):
        return {'abouthd': True}

    @en_decorator_template(pagename='en/index-3.html')
    def index_zy(self, request, *args, **kwargs):
        return {'abouthd': True}

    @action(detail=False)
    @en_decorator_template(pagename='en/contact.html')
    def contact(self, request, *args, **kwargs):
        return {}

    @action(detail=False)
    @en_decorator_template(pagename='en/center-1.html')
    def center_famous(self, request, *args, **kwargs):

        response_data = {
            'centernav': True,
            'current_name': _('咨询')
        }
        return response_data

    @action(detail=False)
    @en_decorator_template(pagename='en/center-2.html')
    def center_hospital(self, request, *args, **kwargs):

        response_data = {
            'centernav': True,
            'current_name': _('医学')
        }
        return response_data

    @action(detail=False)
    @en_decorator_template(pagename='en/center-3.html')
    def center_class(self, request, *args, **kwargs):

        response_data = {
            'centernav': True,
            'current_name': _('课堂')
        }
        return response_data

    @en_decorator_template(pagename='en/index.html')
    def list(self, request, *args, **kwargs):
        certificates = EnCertificate.objects.filter(cert_type='Honorary').order_by('-create_time')

        certificate_serializer = CertificateSerializer(certificates, many=True)

        data = {
            'certs': certificate_serializer.data,
        }

        return data

    @action(detail=False)
    @en_decorator_template(pagename='en/center.html')
    def center(self, request, *args, **kwargs):
        certificates = EnCertificate.objects.filter(cert_type='Patent').order_by('-create_time')

        certificate_serializer = CertificateSerializer(certificates, many=True)

        data = {
            'certs': certificate_serializer.data,
            'current_name': _('专利')
        }

        return data


class EnProductNameView(EnProductView):
    pagination_class = GoodsListPagination

    zh_new = en_product_type.get('new_product')
    zh_class = en_product_type.get('classical_product')

    def get_queryset(self):
        if self.action == 'class_product':
            return EnProduct.objects.order_by('product_num', '-create_time').filter(types__typename=self.zh_class)
        elif self.action == 'new_product':
            return EnProduct.objects.order_by('product_num', '-create_time').filter(types__typename=self.zh_new)
        return EnProduct.objects.order_by('product_num', '-create_time')

    def get_product(self, req, *args, **kwargs):
        current_page = req.query_params.get('page', 1)

        try:
            response = super().list(req, *args, **kwargs)
        except NotFound:
            return {
                'error': True,
                'render_url': 'en/product/'
            }
        else:
            data = {
                'product_data': response.data if response.data else None,
                'current_page': current_page if current_page else 1,
                'productnav': True,
            }
            return data

    @action(detail=False)
    @en_decorator_template(pagename='en/product.html')
    def product(self, request, *args, **kwargs):
        return dict()

    @action(detail=False)
    @en_decorator_template(pagename='en/product-1.html')
    def class_product(self, request, *args, **kwargs):
        return self.get_product(request, *args, **kwargs)

    @action(detail=False)
    @en_decorator_template(pagename='en/product-2.html')
    def new_product(self, request, *args, **kwargs):
        return self.get_product(request, *args, **kwargs)

    @en_decorator_template(pagename='en/product-detail.html')
    def list(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            pro = EnProduct.objects.get(pk=pk)   # noqa
        except EnProduct.DoesNotExist:
            return {
                'error': True,
                'render_url': 'en/product/'
            }

        response = super().retrieve(request, *args, **kwargs)
        serializer = EnProductSearchSerializer(self.get_queryset(), many=True)

        data = {
            'product': response.data,
            'product_name_list': serializer.data,
            'productnav': True,
        }

        return data


class EnArticleTypesView(EnArticleView):

    pagination_class = NewsListPagination

    def get_queryset(self):
        tps = self.request.query_params.get('types')

        if tps:
            return super().get_queryset().filter(types__typename=tps)

        return super().get_queryset()

    @en_decorator_template(pagename='en/news.html')
    def list(self, request, *args, **kwargs):
        try:
            object_list = self.get_queryset().filter(types__typename=en_news_type.get('handian_news'))

            news_list = object_list.order_by('-is_top', '-createtime')

            # news_list = self.get_queryset().filter(types__typename=news_type.get('handian_news'))[:4]

        except Exception:
            news_list = None

        try:
            action_list = self.get_queryset().filter(
                types__typename=en_news_type.get('same_action'))[:4]
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
    @en_decorator_template(pagename='en/news-detail.html')
    def news(self, request, pk, *args, **kwargs):

        try:
            pk_obj = self.get_object()
        except Exception:
            pk_obj = None
        # serializer = self.serializer_class(pk_obj)
        try:
            news_obj = pk_obj.get_next_by_create_time()
            next_news = get_next_news_not_position(news_obj)
        except EnArticles.DoesNotExist:
            next_news = None

        try:
            news_obj = pk_obj.get_previous_by_create_time()
            previous_news = get_pre_news_not_position(news_obj)
        except EnArticles.DoesNotExist:
            previous_news = None

        data = {
            'news': serializer_function(self, pk_obj),
            'newsOnenav': True,
            'next': next_news,
            'previous': previous_news
        }
        return data

    @action(detail=False)
    @en_decorator_template(pagename='en/news-list.html')
    def news_list(self, request, *args, **kwargs):
        response_data = {}
        types = request.query_params.get('types')

        page = request.query_params.get('page')

        if not types or types == en_position_type:
            response_data['error'] = True
            response_data['render_url'] = '/en/news/'
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
