from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from events.models import Event
from registrations.models import Registration

class DashboardAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        # ۱. داشبورد اختصاصی برگزارکننده (Organizer)
        if user.role == "organizer":
            my_events = Event.objects.filter(organizer=user)
            total_events = my_events.count()
            active_events = my_events.filter(status="published").count()
            total_registrations = Registration.objects.filter(event__organizer=user).count()

            return Response({
                "role": user.role,
                "stats": {
                    "total_events": total_events,
                    "active_events": active_events,
                    "total_registrations_received": total_registrations
                }
            }, status=status.HTTP_200_OK)

        # ۲. داشبورد اختصاصی شرکت‌کننده (Participant)
        elif user.role == "participant":
            my_registrations = Registration.objects.filter(participant=user)
            total_enrolled = my_registrations.count()
            approved = my_registrations.filter(status="approved").count()
            pending = my_registrations.filter(status="pending").count()

            return Response({
                "role": user.role,
                "stats": {
                    "total_enrolled_events": total_enrolled,
                    "approved_registrations": approved,
                    "pending_registrations": pending
                }
            }, status=status.HTTP_200_OK)

        return Response({"error": "Role not recognized"}, status=status.HTTP_400_BAD_REQUEST)