from django.contrib import admin
from .models import Response

@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('project', 'question', 'updated_at')
    list_filter = ('project',)