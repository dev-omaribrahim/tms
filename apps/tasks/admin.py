from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Task model.
    """

    list_display = (
        "title",
        "description",
        "status",
        "priority",
        "due_date",
        "created_at",
    )
    list_filter = ("status", "priority", "due_date")
    search_fields = ("title", "description")


admin.site.register(Task, TaskAdmin)
