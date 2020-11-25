from rest_framework import fields

from backend.account import models as account_models
from backend.product import serializers as product_serializer
from backend.serializers import BaseModelSerializer


class UserSerializer(BaseModelSerializer):

    class Meta:
        model = account_models.User
        fields = ['username', 'phone', 'first_name', 'last_name']


class UserDetailSerializer(BaseModelSerializer):

    rate = fields.FloatField()

    class Meta:
        model = account_models.User
        fields = ['username', 'phone', 'first_name', 'last_name', 'photo', 'rate']
