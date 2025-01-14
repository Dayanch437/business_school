# Generated by Django 5.1.1 on 2025-01-10 08:35

import util.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Banner",
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
                (
                    "image",
                    util.utils.CompressedImageField(
                        blank=True, null=True, upload_to="banner/"
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
            ],
            options={
                "verbose_name": "banner",
                "verbose_name_plural": "banners",
                "db_table": "banner",
            },
        ),
    ]
