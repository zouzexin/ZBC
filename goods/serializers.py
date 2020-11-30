from rest_framework import serializers
from .models import GoodsInfo

class GoodsInfoSeriazlizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GoodsInfo
        fields = '__all__'