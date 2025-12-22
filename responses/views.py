from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response as APIResponse
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from .models import Response
from projects.models import Project, Question

class SubmitResponseView(APIView):
    permission_classes = [AllowAny] # Clients don't need to log in

    def post(self, request):
        data = request.data
        
        # 1. Validate inputs
        project_id = data.get('project_id')
        question_id = data.get('question_id')
        response_data = data.get('response_data')

        if not all([project_id, question_id]):
            return APIResponse({"error": "Missing project_id or question_id"}, status=status.HTTP_400_BAD_REQUEST)

        # 2. Check if Project is Active
        project = get_object_or_404(Project, id=project_id)
        if project.status != 'Active':
             return APIResponse({"error": "This project is closed."}, status=status.HTTP_403_FORBIDDEN)

        # 3. Save or Update (The Magic "Upsert")
        # This looks for a response with matching project & question.
        # If found, it updates 'response_data'. If not, it creates a new one.
        response_obj, created = Response.objects.update_or_create(
            project_id=project_id,
            question_id=question_id,
            defaults={'response_data': response_data}
        )

        return APIResponse({
            "status": "success", 
            "action": "created" if created else "updated",
            "id": response_obj.id
        }, status=status.HTTP_200_OK)