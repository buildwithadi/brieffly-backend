from django.contrib import admin
from .models import Project, Question

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'status', 'created_at')
    inlines = [QuestionInline] # Allows adding questions directly inside the Project screen

admin.site.register(Question)