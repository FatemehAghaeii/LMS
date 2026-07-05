from rest_framework import serializers
from .models import Feedback

class FeedbackSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')  # ایمیل کاربر لاگین شده را نشان می‌دهد

    class Meta:
        model = Feedback
        fields = ['id', 'user', 'event', 'rating', 'comment', 'created_at', 'updated_at']

    def validate(self, data):
        request = self.context.get('request')
        user = request.user
        event = data.get('event')

        # بررسی اینکه آیا کاربر قبلاً برای این رویداد نظری ثبت کرده یا خیر
        if Feedback.objects.filter(user=user, event=event).exists():
            raise serializers.ValidationError("شما قبلاً نظر خود را برای این رویداد ثبت کرده‌اید!")
        return data