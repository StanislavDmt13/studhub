from .yasg import urlpatterns as yasg_urlpatterns
from django.urls import path, include

app_name = "api"

urlpatterns = [
    path("", include(yasg_urlpatterns), name="swagger"),
    path("account/", include('backend.account.urls'), name="account")
]
