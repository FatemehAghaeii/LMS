from rest_framework import serializers

from .models import Registration


class RegistrationSerializer(serializers.ModelSerializer):

    participant = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Registration
        fields = "__all__"