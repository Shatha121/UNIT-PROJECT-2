from django.contrib import admin
from .models import Job , JobAnalysis
# Register your models here.

admin.register(Job)
admin.register(JobAnalysis)

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'rating', 'category', 'created_at')
    list_filter = ('rating', 'category', 'created_at')


class JobAnalysisAdmin(admin.ModelAdmin):
    list_display = ('job', 'summary', 'score')