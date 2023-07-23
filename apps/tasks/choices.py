from django.db import models

class StatusChoices(models.TextChoices):
    """
    Choices for status field
    """
    NEW = "new", "new"
    IN_PROGRESS = "in progress", "in progress"
    COMPLETED = "completed", "completed"


class PriorityChoices(models.TextChoices):
    """
    Choices for priority field
    """
    LOW = "low", "low"
    MEDIUM = "medium", "medium"
    HIGH = "high", "high"

