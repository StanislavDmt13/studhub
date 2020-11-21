from rest_framework.views import APIView


class BaseAPIView(APIView):

    @property
    def user(self):
        return self.request.user
