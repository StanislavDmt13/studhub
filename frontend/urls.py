from django.urls import path
from django.urls import re_path
from .views import base

urlpatterns = [
    re_path('^', base),
]
