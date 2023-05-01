from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'author', 'post', 'created_date']
    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

admin.site.register(Comment, CommentAdmin)
