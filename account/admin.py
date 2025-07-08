from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("phone",)}),
    )
