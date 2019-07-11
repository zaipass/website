from rest_framework import serializers

from django.conf import settings

from apps.article.models import Articles, Certificate


class ArticleSerializer(serializers.ModelSerializer):
    # 序列化返回对应形式的时间格式
    create_time = serializers.DateTimeField(format=settings.DATETIME_FORMAT)

    class Meta:
        model = Articles
        fields = '__all__'


class CertificateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Certificate
        fields = '__all__'
