from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone = models.CharField(max_length=20, unique=True)
    photo = models.ImageField()
    lang = models.CharField(max_length=10, null=False, default=settings.LANGUAGE_CODE)


