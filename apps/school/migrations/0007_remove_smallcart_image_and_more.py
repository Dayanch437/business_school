# Generated by Django 5.1.1 on 2025-01-10 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("school", "0006_delete_teacher_delete_videos"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="smallcart",
            name="image",
        ),
        migrations.RemoveField(
            model_name="smallcart",
            name="social_activity",
        ),
        migrations.DeleteModel(
            name="CartImage",
        ),
        migrations.DeleteModel(
            name="SmallCart",
        ),
        migrations.DeleteModel(
            name="SocialActivity",
        ),
    ]