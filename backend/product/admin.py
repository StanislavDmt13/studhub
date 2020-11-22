from django.contrib import admin
from . import models


@admin.register(models.Tag)
class TagModelAdmin(admin.ModelAdmin):
    search_fields = ("name",)


# @admin.register(models.ProductFile)
# class ProductFileAdmin(admin.TabularInline):
#     fields = '__all__'


@admin.register(models.Product)
class ProductModelAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(models.ProductRate)
class RateModelAdmin(admin.ModelAdmin):
    search_fields = ("product__name",)


@admin.register(models.Comment)
class CommentModelAdmin(admin.ModelAdmin):
    search_fields = ("product__name",)
