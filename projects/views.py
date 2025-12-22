from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Project, Question
from .serializers import ProjectSerializer, QuestionSerializer

# 1. Protected ViewSet (For your Dashboard)
# This handles GET, POST, PUT, DELETE for Projects automatically
class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only show projects belonging to the logged-in user
        return Project.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        # Automatically set the user to the currently logged-in user
        serializer.save(user=self.request.user)

# 2. Public View (For Clients)
# This looks up a project by its 'unique_link' UUID
class PublicProjectView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny] # No login required
    lookup_field = 'uuid' # We look up by UUID, not ID

# 3. Question ViewSet (To add questions to projects)
class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Ensure user can only see questions for their own projects
        return Question.objects.filter(project__user=self.request.user)