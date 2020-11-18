from django.db import models
from mptt import models as mptt_models
from .. import models as backend_models


class City(backend_models.AbstractNameModel):
    pass


class Institute(backend_models.AbstractNameModel):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="institutes")


class Faculty(backend_models.AbstractNameModel):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name="faculties")


class Category(mptt_models.MPTTModel, backend_models.AbstractNameModel, backend_models.AbstractCreatedUpdatedModel):
    parent = mptt_models.TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )


class Subject(backend_models.AbstractNameModel, backend_models.AbstractCreatedUpdatedModel):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name="subjects")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subjects")
