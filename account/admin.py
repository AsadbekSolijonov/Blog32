from django.contrib import admin
from django.contrib.admin import StackedInline, TabularInline
from django.contrib.auth.admin import UserAdmin

from account.models import CustomUser, Profile


# class ProfileAdmin(TabularInline):
#     model = Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['__str__']


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # inlines = [ProfileAdmin, ]
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("phone",)}),
    )
