from django.db import models
import uuid
from django.conf import settings  # To refer to your custom user model

class Project(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Completed', 'Completed'),
        ('Archived', 'Archived'),
    ]

    # Restored User Association
    # null=True allowed temporarily to prevent migration conflicts with existing anonymous data
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='projects', null=True, blank=True)
    
    # Core Fields
    # This UUID is the primary public identifier now (matches your Serializer's 'uuid' field)
    # UPDATED: Temporarily removed unique=True and added null=True to resolve migration conflict
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, null=True, db_index=True)
    
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    
    # Kept as CharField to satisfy Serializer if it expects 'unique_link' separate from 'uuid'
    # In practice, you can probably deprecate this and just use 'uuid'
    unique_link = models.CharField(max_length=255, blank=True, null=True)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    INPUT_TYPES = [
        ('text', 'Short Text'),
        ('textarea', 'Long Text'),
        ('file', 'File Upload'),
        ('multiple_choice', 'Multiple Choice'),
        ('checkbox', 'Checkbox'),
        ('date', 'Date'),
    ]

    project = models.ForeignKey(Project, related_name='questions', on_delete=models.CASCADE)
    
    question_text = models.TextField() # Changed back to TextField for flexibility
    input_type = models.CharField(max_length=20, choices=INPUT_TYPES, default='text')
    
    is_required = models.BooleanField(default=False)
    # JSONField for options (e.g., ["Red", "Blue"])
    options = models.JSONField(blank=True, null=True, default=list) 
    order_position = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order_position'] # Automatically sort by order

    def __str__(self):
        return f"{self.project.title} - {self.question_text[:30]}"