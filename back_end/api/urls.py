from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import UserViewSet, ShopList 
from . import views


router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('shop/', ShopList.as_view(), name='shop'),
    path('details/<str:pk>/',views.details, name='details'),
    path('create/',views.create, name='create'),
    path('update/<str:pk>/',views.update, name='update'),
    path('delete/<str:pk>/',views.delete, name='delete'),
]
