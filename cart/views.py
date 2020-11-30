from django.shortcuts import render
from rest_framework import viewsets
from .models import CartInfo
from .serializers import CartInfoSeriazlizer

# Create your views here.
class CartInfoViewSet(viewsets.ModelViewSet):
    queryset = CartInfo.objects.all()
    serializer_class = CartInfoSeriazlizer