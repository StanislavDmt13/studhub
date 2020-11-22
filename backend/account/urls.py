from rest_framework import routers
from backend.account import viewsets

app_name = "account"

router = routers.DefaultRouter()

router.register('info', viewsets.UserViewSet, basename='info')
router.register('rate', viewsets.UserRateViewSet, basename='rate')

urlpatterns = router.urls
