# Generated by Django 5.1.1 on 2025-01-09 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("school", "0005_remove_bigcart_image_remove_smallcart_image_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bigcart",
            name="image",
        ),
        migrations.RemoveField(
            model_name="smallcart",
            name="image",
        ),
        migrations.AddField(
            model_name="bigcart",
            name="image",
            field=models.ManyToManyField(related_name="bigCart", to="school.cartimage"),
        ),
        migrations.AddField(
            model_name="smallcart",
            name="image",
            field=models.ManyToManyField(
                related_name="smallCart", to="school.cartimage"
            ),
        ),
    ]