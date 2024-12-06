# Generated by Django 5.1.2 on 2024-12-01 12:35

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0002_review"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                ("name", models.CharField(max_length=200)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="project",
            name="vote_ratio",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name="project",
            name="vote_total",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name="project",
            name="tags",
            field=models.ManyToManyField(blank=True, to="projects.tag"),
        ),
    ]
