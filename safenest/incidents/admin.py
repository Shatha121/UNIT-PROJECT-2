from django.contrib import admin
from .models import  Incident
# Register your models here.

admin.site.register(Incident)

class IncidentAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'category', 'reporter', 'date_reported')
    list_filter = ('status', 'category')
    search_fields = ('title', 'location', 'description')