from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework import viewsets
from .models import Goods, WishList
from .serializers import ItemSerializer, ItemCreateSerializer, WishListSerializer
from rest_framework.response import Response
from rest_framework import status


class UltraGoodsView(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def list(self, request):
        queryset = Goods.objects.all()
        serializer = ItemSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        queryset = Goods.objects.create()
        serializer = ItemCreateSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, slug=None):
        queryset = Goods.objects.get(slug=slug)
        serializer = ItemSerializer(queryset)
        return Response(serializer.data)

    def update(self, request, slug=None):
        queryset = Goods.objects.get(slug=slug)
        serializer = ItemSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def destroy(self, request, slug=None):
        queryset = Goods.objects.get(slug=slug)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WishListView(viewsets.ModelViewSet):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer
    permission_classes = [AllowAny]




