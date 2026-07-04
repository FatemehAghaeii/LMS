from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):

    organizer = serializers.StringRelatedField()
    remaining_capacity = serializers.ReadOnlyField()

    class Meta:
        model = Event

        fields = (
            "id",
            "title",
            "description",
            "location",
            "banner",
            "capacity",
            "remaining_capacity",
            "status",
            "start_date",
            "end_date",
            "organizer",
            "created_at",
        )

    def validate(self, attrs):

        if attrs["start_date"] >= attrs["end_date"]:
            raise serializers.ValidationError(
                "End date must be after start date."
            )

        return attrs