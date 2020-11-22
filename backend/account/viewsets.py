from backend.account.models import User
from backend.viewsets import BaseModelViewSet

from backend.account.serializers import UserSerializer


class UserViewSet(BaseModelViewSet):

    queryset = User.objects.all()

    serializer_class = UserSerializer
