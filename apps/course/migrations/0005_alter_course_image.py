# Generated by Django 5.1.1 on 2025-01-20 08:37

import util.utils
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0004_alter_course_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="image",
            field=util.utils.CompressedImageField(
                blank=True, max_size_mb=20, null=True, upload_to="course/"
            ),
        ),
    ]
