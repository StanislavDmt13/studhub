from rest_framework import fields

from backend.account.models import User
from backend.serializers import BaseModelSerializer, BaseSerializer


class UserSerializer(BaseModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'phone', 'first_name', 'last_name', 'photo']
