# Generated by Django 5.1.1 on 2025-01-23 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("banner", "0008_alter_banner_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="banner",
            name="title_en",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="banner",
            name="title_ru",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="banner",
            name="title_tk",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
