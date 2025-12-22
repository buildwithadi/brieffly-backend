from rest_framework import serializers
from .models import Response

class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = ['id', 'project', 'question', 'response_data', 'submitted_at']
        read_only_fields = ['id', 'submitted_at']