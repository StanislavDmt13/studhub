from django.db import models
from .. import models as backend_models
from ..account import models as account_models


class Tag(backend_models.AbstractNameModel):
    user = models.ForeignKey(account_models.User, on_delete=models.CASCADE, related_name="tags")


class Product(backend_models.AbstractNameModel, backend_models.AbstractCreatedUpdatedModel):
    owner = models.ForeignKey(account_models.User, on_delete=models.PROTECT, related_name="products")
    tags = models.ManyToManyField(Tag, related_name="products")
    description = models.TextField(blank=True)


class ProductFile(backend_models.AbstractCreatedModel):

    file_name = models.FileField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='files')


class ProductRate(backend_models.AbstractCreatedModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="rates")
    user = models.ForeignKey(account_models.User, on_delete=models.CASCADE, related_name="rates")
    score = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = (("product", "user"),)


class Comment(backend_models.AbstractCreatedUpdatedModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(account_models.User, on_delete=models.CASCADE, related_name="comments")

    text = models.TextField(blank=True)
