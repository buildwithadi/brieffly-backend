from rest_framework import serializers
from .models import Project, Question
# Import the Response serializer (fetch it from the responses app)
# Note: Ensure the 'responses' app exists and has a serializers.py
from responses.serializers import ResponseSerializer 

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'project', 'question_text', 'input_type', 'is_required', 'options', 'order_position']

class ProjectSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    # Fetch related responses using the serializer from the other app
    responses = ResponseSerializer(many=True, read_only=True)
    
    class Meta:
        model = Project
        # The 'uuid' field is now correctly separated by a comma
        fields = ['id', 'uuid', 'title', 'description', 'unique_link', 'status', 'created_at', 'questions', 'responses']
        read_only_fields = ['id', 'unique_link', 'created_at', 'questions', 'responses']