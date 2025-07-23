from django.contrib import admin
# Register your models here.
from .models import Contact

admin.site.register(Contact)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email','message')
    search_fields = ('text',)