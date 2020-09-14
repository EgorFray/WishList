from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Goods, WishList


class GoodsTests(APITestCase):
    def setUp(self):
        Goods.objects.create(title="Samsung", body="s20", slug="samsung")

    def test_goods(self):
        response = self.client.get(reverse('api-wishlist:goods-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_wishlist(self):
        response = self.client.get(reverse('api-wishlist:wishlist-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

