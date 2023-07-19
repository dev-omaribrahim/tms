# Generated by Django 3.2 on 2023-07-15 12:39

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("new", "new"),
                            ("in progress", "in progress"),
                            ("completed", "completed"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "priority",
                    models.CharField(
                        choices=[
                            ("low", "low"),
                            ("medium", "medium"),
                            ("high", "high"),
                        ],
                        max_length=100,
                    ),
                ),
                ("due_date", models.DateField()),
                ("created_at", models.DateField(auto_now=True)),
            ],
            options={
                "ordering": ("-created_at",),
            },
        ),
    ]