# Generated by Django 5.1.1 on 2025-01-10 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("school", "0005_delete_contact"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Teacher",
        ),
        migrations.DeleteModel(
            name="Videos",
        ),
    ]