from rest_framework import routers
from backend.account import viewsets

app_name = "account"

router = routers.DefaultRouter()

router.register('detail', viewsets.UserViewSet, basename='detail')

urlpatterns = router.urls
