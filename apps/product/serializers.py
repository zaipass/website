from rest_framework import serializers

from apps.product.models import Product, EnProduct


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class EnProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = EnProduct
        fields = '__all__'


class ProductSearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'main')


class EnProductSearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'main')
