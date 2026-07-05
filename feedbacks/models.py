from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from events.models import Event  # امپورت کردن مدل رویداد از اپلیکیشن events

User = get_user_model()

class Feedback(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='feedbacks',
        verbose_name="کاربر"
    )
    event = models.ForeignKey(
        Event, 
        on_delete=models.CASCADE, 
        related_name='feedbacks',
        verbose_name="رویداد"
    )
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="امتیاز"
    )
    comment = models.TextField(
        blank=True, 
        null=True,
        verbose_name="متن نظر"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        # جلوگیری از اینکه یک کاربر بتواند برای یک رویداد چند بار نظر ثبت کند
        unique_together = ('user', 'event')

    def __str__(self):
        return f"Feedback by {self.user.email} on {self.event.title}"