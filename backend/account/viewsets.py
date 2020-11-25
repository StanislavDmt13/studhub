from django.db.models import Avg

from backend.account import models as account_models
from backend.viewsets import BaseModelViewSet

from backend.account import serializers as account_serializer


class UserViewSet(BaseModelViewSet):

    queryset = account_models.User.objects.all()

    serializer_class = account_serializer.UserSerializer

    serializer_classes = {
        'list': account_serializer.UserDetailSerializer,
        'retrieve': account_serializer.UserDetailSerializer
    }
    
    def get_queryset(self):

        annotate = {
            'rate': Avg('evaluated_rates__score')
        }

        queryset = self.queryset.annotate(**annotate)

        return queryset
