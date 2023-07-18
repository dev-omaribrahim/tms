from django.db import models

from . import choices


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=100, choices=choices.STATUS_CHOICES)
    priority = models.CharField(max_length=100, choices=choices.PPRIORITY_CHOICES)
    due_date = models.DateField()
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.title
