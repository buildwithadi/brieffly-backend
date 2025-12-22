from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model # <--- CHANGE THIS
from .serializers import RegisterSerializer

User = get_user_model() # <--- GET THE CORRECT USER MODEL

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer