from django.urls import path, include
from . import views
from rest_framework import routers

wishlist_router = routers.DefaultRouter()
wishlist_router.register('goods', views.UltraGoodsView, basename='goods')
wishlist_router.register('wishlist', views.WishListView, basename='wishlist')
app_name = 'wishapp'

urlpatterns = [
    path('', include(wishlist_router.urls))
]