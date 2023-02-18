from rest_framework.viewsets import ModelViewSet

from backend.models import Project
from backend.serializers import ProjectSerializer


class ProjectModelViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
