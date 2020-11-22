from backend.account.models import User
from backend.serializers import BaseModelSerializer


class UserSerializer(BaseModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'phone', 'first_name', 'last_name', 'photo']

