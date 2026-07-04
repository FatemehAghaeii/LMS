from django.db import models
from events.models import Event


class Stage(models.Model):

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="stages"
    )

    title = models.CharField(
        max_length=255
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    order = models.PositiveIntegerField()

    start_time = models.DateTimeField()

    end_time = models.DateTimeField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["order"]
        unique_together = ("event", "order")

    def __str__(self):
        return f"{self.event.title} - {self.title}"