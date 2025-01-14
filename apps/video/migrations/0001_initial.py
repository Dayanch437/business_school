# Generated by Django 5.1.1 on 2025-01-10 17:33

import util.utils
import util.validator
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Videos",
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
                ("title", models.CharField(max_length=200)),
                (
                    "video",
                    models.FileField(
                        null=True,
                        upload_to="videos/webm/",
                        validators=[util.validator.validate_video_extension],
                    ),
                ),
                ("image", util.utils.CompressedImageField(upload_to="videos/")),
            ],
            options={
                "verbose_name": "video",
                "verbose_name_plural": "videos",
                "db_table": "videos",
            },
        ),
    ]
