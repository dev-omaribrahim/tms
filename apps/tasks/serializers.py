from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for the Task model.
    """

    class Meta:
        model = Task
        fields = (
            "id",
            "title",
            "description",
            "due_date",
            "status",
            "priority",
            "created_at",
        )
        read_only_fields = ("id", "created_at")
