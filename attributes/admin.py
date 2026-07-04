from django.contrib import admin
from .models import Attribute, AttributeValue


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "data_type",
    )

    search_fields = (
        "name",
    )


@admin.register(AttributeValue)
class AttributeValueAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "event",
        "attribute",
        "value",
    )

    list_filter = (
        "attribute",
    )