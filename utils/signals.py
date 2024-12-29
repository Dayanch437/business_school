from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
import os

from school.models import Banner


@receiver(pre_delete,sender=Banner)
def auto_delete_file_on_change(sender,instance,*args,**kwargs):
    if instance.image:
        image_path = instance.image.path
        if os.path.exists(image_path):
            os.remove(image_path)
        else:
            print ("no path fount")


@receiver(pre_save,sender=Banner)
def update_image_on_change(sender,instance,*args,**kwargs):
    if not instance.pk:
        return False
    try:
        old_image = Banner.objects.get(pk=instance.pk).image
    except Banner.DoesNotExist:
        return False
    new_image = instance.image
    if not old_image == new_image:
        if os.path.isfile(old_image.path):
            os.remove(old_image.path)
