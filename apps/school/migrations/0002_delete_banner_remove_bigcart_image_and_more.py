# Generated by Django 5.1.1 on 2025-01-10 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("school", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Banner",
        ),
        migrations.RemoveField(
            model_name="bigcart",
            name="image",
        ),
        migrations.RemoveField(
            model_name="bigcart",
            name="social_activity",
        ),
        migrations.DeleteModel(
            name="News",
        ),
        migrations.AlterModelOptions(
            name="smallcart",
            options={
                "verbose_name": "small cart",
                "verbose_name_plural": "small carts",
            },
        ),
        migrations.AlterModelTable(
            name="smallcart",
            table="smallCart",
        ),
        migrations.DeleteModel(
            name="BigCart",
        ),
    ]
