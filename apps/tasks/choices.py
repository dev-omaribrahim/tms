from django.db import models

class StatusChoices(models.TextChoices):
    NEW = "new", "new"
    IN_PROGRESS = "in progress", "in progress"
    COMPLETED = "completed", "completed"


class PriorityChoices(models.TextChoices):
    LOW = "low", "low"
    MEDIUM = "medium", "medium"
    HIGH = "high", "high"

# choices of status field
# NEW = "new"
# IN_PROGRESS = "in progress"
# COMPELETED = "completed"

# STATUS_CHOICES = ((NEW, "new"), (IN_PROGRESS, "in progress"), (COMPELETED, "completed"))


# # choices of priority field
# LOW = "low"
# MEDIUM = "medium"
# HIGH = "high"

# PPRIORITY_CHOICES = ((LOW, "low"), (MEDIUM, "medium"), (HIGH, "high"))
