from rest_framework import serializers
from .models import CartInfo

class CartInfoSeriazlizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CartInfo
        fields = '__all__' # 增加一个url