from rest_framework import routers
from backend.account.viewsets import UserViewSet

app_name = "account"

router = routers.DefaultRouter()

router.register('info', UserViewSet, basename='info')

urlpatterns = router.urls
