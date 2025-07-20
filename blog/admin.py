from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group, Permission
from mptt.admin import DraggableMPTTAdmin

from blog.models import Blog, Comment, Like

# admin.site.register(Comment, DraggableMPTTAdmin)
admin.site.register(Like)


class ReadOnlyPermission:
    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if not request.user.is_superuser:
            return True
        return False

    def has_view_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


@admin.register(Blog)
class BlogAdmin(ReadOnlyPermission, admin.ModelAdmin):
    list_display = ['title']


@admin.register(Comment)
class CommentAdmin(DraggableMPTTAdmin):
    list_display = ['indented_title', 'message']

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False
