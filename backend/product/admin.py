from django.contrib import admin
from . import models


@admin.register(models.Tag)
class TagModelAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(models.File)
class FileModelAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(models.Product)
class ProductModelAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(models.Rate)
class RateModelAdmin(admin.ModelAdmin):
    search_fields = ("product__name",)


@admin.register(models.Comment)
class CommentModelAdmin(admin.ModelAdmin):
    search_fields = ("product__name",)
