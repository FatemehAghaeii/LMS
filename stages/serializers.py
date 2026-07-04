from rest_framework import serializers
from .models import Stage


class StageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stage

        fields = "__all__"

    def validate(self, attrs):

        if attrs["start_time"] >= attrs["end_time"]:
            raise serializers.ValidationError(
                "End time must be after start time."
            )

        return attrs