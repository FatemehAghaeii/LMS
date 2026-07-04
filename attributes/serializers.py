from rest_framework import serializers
from .models import Attribute, AttributeValue


class AttributeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attribute
        fields = "__all__"


class AttributeValueSerializer(serializers.ModelSerializer):

    attribute_name = serializers.CharField(
        source="attribute.name",
        read_only=True
    )

    class Meta:
        model = AttributeValue
        fields = (
            "id",
            "event",
            "attribute",
            "attribute_name",
            "value",
        )