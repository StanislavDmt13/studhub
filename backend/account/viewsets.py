from backend.account.models import User
from backend.viewsets import BaseModelViewSet, BaseManagerViewSet

from backend.account import serializers as account_serializer
from backend.account import managers as account_manager


class UserViewSet(BaseModelViewSet):

    queryset = User.objects.all()

    serializer_class = account_serializer.UserSerializer


class UserRateViewSet(BaseManagerViewSet):

    manager_classes = {
        'list': account_manager.UserRatesManager,
        'retrieve': account_manager.UserRateManager
    }
