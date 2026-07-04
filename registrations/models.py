from django.db import models
from django.conf import settings

from events.models import Event


class Registration(models.Model):

    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        APPROVED = "approved", "Approved"
        REJECTED = "rejected", "Rejected"

    participant = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="registrations"
    )

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="registrations"
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )

    registered_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        unique_together = ("participant", "event")
        ordering = ["-registered_at"]

    def __str__(self):
        return f"{self.participant.email} - {self.event.title}"