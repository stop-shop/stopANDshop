from rest_framework.generics import ListCreateAPIView
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User 
from .serializers import UserSerializer, ShopSerializer
from .models import Shop
from rest_framework.generics import ListCreateAPIView

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ShopList(ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer




@api_view(['GET'])
def apiOverview(request):####################
    api_urls={
    'List':'/list/',
    'Detail View':'/detail/<str:pk>/',
    'Create':'/create/',
    'Update':'/updat/<str:pk>/',
    'Delete':'/delete/<str:pk>/',}
    return Response(api_urls)
@api_view(['GET'])
def pagelist(request):
     items=Shop.objects.all()
     serializer=ShopSerializer(items,many=True)
     return Response(serializer.data)
@api_view(['GET'])
def details(request,pk):
     items=Shop.objects.get(id=pk)
     serializer=ShopSerializer(items,many=False)
     return Response(serializer.data)
@api_view(['POST'])
def create(request):
     serializer=ShopSerializer(data=request.data)
     if serializer.is_valid():
        serializer.save()
     return Response(serializer.data)
@api_view(['POST'])
def update(request,pk):
     items=Shop.objects.get(id=pk)
     serializer=ShopSerializer(instance=items,data=request.data)
     if serializer.is_valid():
        serializer.save()
     return Response(serializer.data)
@api_view(['DELETE'])
def delete(request,pk):
     items=Shop.objects.get(id=pk)
     items.delete()
     return Response('item successfully deleted ')