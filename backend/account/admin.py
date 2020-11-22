from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class UserModelAdmin(UserAdmin):
    model = models.User
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'phone')}
         ),
    )


@admin.register(models.UserRate)
class UserRateAdmin(admin.ModelAdmin):

    model = models.UserRate
    fields = ('evaluator', 'evaluated', 'score')
    list_display = ('evaluator', 'evaluated', 'score')
