from django.contrib import admin
from .models import Stage


@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "title",
        "event",
        "order",
        "start_time",
    )

    list_filter = (
        "event",
    )

    search_fields = (
        "title",
    )