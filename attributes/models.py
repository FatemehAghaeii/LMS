from django.db import models
from events.models import Event


class Attribute(models.Model):

    class DataType(models.TextChoices):
        TEXT = "text", "Text"
        INTEGER = "integer", "Integer"
        BOOLEAN = "boolean", "Boolean"
        FLOAT = "float", "Float"

    name = models.CharField(
        max_length=100,
        unique=True
    )

    data_type = models.CharField(
        max_length=20,
        choices=DataType.choices,
        default=DataType.TEXT
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class AttributeValue(models.Model):

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="attribute_values"
    )

    attribute = models.ForeignKey(
        Attribute,
        on_delete=models.CASCADE,
        related_name="values"
    )

    value = models.CharField(
        max_length=255
    )

    class Meta:
        unique_together = ("event", "attribute")

    def __str__(self):
        return f"{self.event.title} - {self.attribute.name}"