from rest_framework import serializers
from backend.account.models import User


class BaseSerializer(serializers.Serializer):

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    @property
    def user(self) -> User:
        return self.context["request"].user

    @property
    def request(self):
        return self.context.get("request")


class BaseModelSerializer(serializers.ModelSerializer, serializers.BaseSerializer):

    pass
