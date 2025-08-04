from django.contrib import admin
from .models import  Incident, Comment
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ('incident', 'content', 'created_at')


class IncidentAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'category', 'date_reported')
    list_filter = ('status', 'category')
    search_fields = ('title', 'location', 'description')

admin.site.register(Incident, IncidentAdmin)
admin.site.register(Comment, CommentAdmin)

