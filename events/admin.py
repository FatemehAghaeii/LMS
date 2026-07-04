from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "title",
        "organizer",
        "capacity",
        "status",
        "start_date",
    )

    list_filter = (
        "status",
        "start_date",
    )

    search_fields = (
        "title",
        "description",
        "location",
    )