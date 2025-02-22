# Generated by Django 5.1.1 on 2025-01-23 10:42

import util.compressedFields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("socialactivity", "0004_socialactivity_description_en_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="image",
            field=util.compressedFields.AdvanceThumbnailField(
                blank=True, null=True, upload_to="images/"
            ),
        ),
    ]
