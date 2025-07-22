from django.contrib import admin
from .models import Comment
# Register your models here.

admin.site.register(Comment)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('incident', 'author', 'created_at')
    search_fields = ('text',)