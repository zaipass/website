from django.conf import settings

from rest_framework import serializers

from apps.user.models import Position


class IndexSerializer(serializers.ModelSerializer):
    pass


class PositionSerializer(serializers.ModelSerializer):

    create_time = serializers.DateTimeField(format=settings.DATETIME_FORMAT)

    class Meta:
        model = Position
        fields = '__all__'


class PositionIndexSerializer(serializers.ModelSerializer):

    create_time = serializers.DateTimeField(format=settings.DATETIME_FORMAT)

    class Meta:
        model = Position
        fields = ('id', 'position_title', 'work_experience', 'create_time')
