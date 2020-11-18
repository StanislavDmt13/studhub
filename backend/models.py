from django.db import models

NAME_MAX_LENGTH = 200


class BaseModel(models.Model):
    class Meta:
        abstract = True


class AbstractNameModel(BaseModel):
    name = models.CharField(max_length=NAME_MAX_LENGTH)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class AbstractCreatedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class AbstractCreatedUpdatedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
