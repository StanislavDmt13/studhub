from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from backend.models import AbstractCreatedUpdatedModel


class User(AbstractUser):
    phone = models.CharField(max_length=20, unique=True)
    photo = models.ImageField()
    lang = models.CharField(max_length=10, null=False, default=settings.LANGUAGE_CODE)


class UserRate(AbstractCreatedUpdatedModel):

    evaluator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='evaluator_rates')
    evaluated = models.ForeignKey(User, on_delete=models.CASCADE, related_name='evaluated_rates')
    score = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = (("evaluator", "evaluated"),)
