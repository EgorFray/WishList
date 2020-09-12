from rest_framework import serializers
from .models import Goods, WishList


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ['id', 'title', 'body', 'slug']


class ItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ['title', 'body']


class WishListSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = WishList
        fields = '__all__'
