from django.contrib import admin
from .models import  Incident, Comment
# Register your models here.

admin.site.register(Incident)
admin.site.register(Comment)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('incident', 'author', 'content', 'created_at')


class IncidentAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'category', 'reporter', 'date_reported')
    list_filter = ('status', 'category')
    search_fields = ('title', 'location', 'description')