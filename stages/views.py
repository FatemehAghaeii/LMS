from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Stage
from .serializers import StageSerializer


class StageViewSet(viewsets.ModelViewSet):

    queryset = Stage.objects.all()

    serializer_class = StageSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]