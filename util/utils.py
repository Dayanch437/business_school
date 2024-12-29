from django.db import models
from PIL import Image
import io,os
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from django.core.files.base import ContentFile
from util.validator import validate_image

class BaseImageModel(models.Model):
    image = models.ImageField(validators=[validate_image], blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.image:
            image_file = self.image
            image = Image.open(image_file)
            webp_image = io.BytesIO()
            image.save(webp_image, format='WebP')
            webp_image.seek(0)

            webp_filename = f'{self.image.name.rsplit(".", 1)[0]}.webp'
            self.image.save(webp_filename, ContentFile(webp_image.read()), save=False)

        super().save(*args, **kwargs)


@receiver(pre_delete)
def auto_delete_file_on_change(sender, instance, *args, **kwargs):
    if issubclass(sender, BaseImageModel) and instance.image:
        image_path = instance.image.path
        if os.path.exists(image_path):
            os.remove(image_path)


@receiver(pre_save)
def update_image_on_change(sender, instance, *args, **kwargs):
    if issubclass(sender, BaseImageModel) and instance.pk:
        try:
            old_image = sender.objects.get(pk=instance.pk).image
        except sender.DoesNotExist:
            return
        new_image = instance.image
        if old_image and old_image != new_image and os.path.isfile(old_image.path):
            os.remove(old_image.path)
