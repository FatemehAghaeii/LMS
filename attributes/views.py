from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Attribute, AttributeValue
from .serializers import (
    AttributeSerializer,
    AttributeValueSerializer
)


class AttributeViewSet(viewsets.ModelViewSet):

    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class AttributeValueViewSet(viewsets.ModelViewSet):

    queryset = AttributeValue.objects.all()
    serializer_class = AttributeValueSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]