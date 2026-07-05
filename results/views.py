from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from .models import Result
from .serializers import ResultSerializer

class ResultViewSet(viewsets.ModelViewSet):
    serializer_class = ResultSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        
        # اگر کاربر برگزارکننده (Organizer) است، نتایج رویدادهای خودش را می‌بیند
        if user.role == "organizer":
            return Result.objects.filter(registration__event__organizer=user)
            
        # اگر شرکت‌کننده است، فقط نتیجه ثبت‌نام‌های خودش را می‌بیند
        return Result.objects.filter(registration__participant=user)

    def perform_create(self, serializer):
        registration = serializer.validated_data.get("registration")
        
        # بررسی اینکه آیا کاربر فعلی واقعاً برگزارکننده این رویداد هست یا خیر
        if registration.event.organizer != self.request.user:
            raise PermissionDenied("شما برگزارکننده این رویداد نیستید و دسترسی ثبت نمره ندارید!")
            
        serializer.save()