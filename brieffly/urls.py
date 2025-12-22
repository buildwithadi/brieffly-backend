from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from users.views import RegisterView
from projects.views import ProjectViewSet, QuestionViewSet, PublicProjectView
from responses.views import SubmitResponseView

# Create a router for our ViewSets
router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'questions', QuestionViewSet, basename='question')

urlpatterns = [
    # Admin Panel
    path('admin/', admin.site.urls),

    # Authentication Endpoints
    path('api/auth/register/', RegisterView.as_view(), name='register'),
    path('api/auth/login/', obtain_auth_token, name='login'), # Built-in DRF token login

    # Public Client Endpoint (The magic link)
    # CRITICAL FIX: Changed <uuid:unique_link> to <uuid:uuid> to match lookup_field='uuid' in views.py
    path('api/public/projects/<uuid:uuid>/', PublicProjectView.as_view(), name='public-project'),

    # Dashboard Endpoints (Projects & Questions)
    path('api/', include(router.urls)),

    path('api/public/responses/', SubmitResponseView.as_view(), name='submit-response'),
]