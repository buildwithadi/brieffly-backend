from django.db import models
from projects.models import Project, Question

class Response(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='responses')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='responses')
    # We store text answers OR file URLs here as a string
    response_data = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # Ensures one response per question per project submission
        # (For MVP, we assume one "client" per project link)
        unique_together = ('project', 'question') 

    def __str__(self):
        return f"Response to {self.question.id} in {self.project.title}"