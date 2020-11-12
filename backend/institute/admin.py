from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from . import models


@admin.register(models.City)
class CityModelAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(models.Institute)
class InstituteModelAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("city",)


@admin.register(models.Faculty)
class FacultyModelAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("institute",)


@admin.register(models.Category)
class CategoryMPTTModelAdmin(MPTTModelAdmin):
    search_fields = ("name",)


@admin.register(models.Subject)
class SubjectModelAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("category", "faculty", "faculty__institute")
