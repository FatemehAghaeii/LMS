from rest_framework import serializers
from events.models import Event
from registrations.models import Registration

class OrganizerDashboardSerializer(serializers.Serializer):
    total_events = serializers.IntegerField()
    active_events = serializers.IntegerField()
    total_registrations_received = serializers.IntegerField()

class ParticipantDashboardSerializer(serializers.Serializer):
    total_enrolled_events = serializers.IntegerField()
    approved_registrations = serializers.IntegerField()
    pending_registrations = serializers.IntegerField()