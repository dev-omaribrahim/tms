# Generated by Django 3.2 on 2023-07-15 12:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="created_at",
            field=models.DateField(auto_now_add=True),
        ),
    ]
