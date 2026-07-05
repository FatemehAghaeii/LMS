from rest_framework import serializers
from .models import Result

class ResultSerializer(serializers.ModelSerializer):
    participant_email = serializers.CharField(source="registration.participant.email", read_only=True)
    event_title = serializers.CharField(source="registration.event.title", read_only=True)

    class Meta:
        model = Result
        fields = [
            "id",
            "registration",
            "participant_email",
            "event_title",
            "score",
            "status",
            "remarks",
            "created_at",
            "updated_at",
        ]

    def validate(self, data):
        registration = data.get("registration")
        
        # بررسی اینکه آیا ثبت‌نام کاربر قبلاً توسط برگزارکننده تأیید شده است یا خیر
        if registration.status != "approved":
            raise serializers.ValidationError(
                "امکان ثبت نتیجه برای کاربری که ثبت‌نامش تأیید نشده است وجود ندارد!"
            )
            
        return data