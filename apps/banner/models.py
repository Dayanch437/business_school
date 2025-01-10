from django.db import models
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from util.utils import CompressedImageField
import os
# Create your models here.



class Banner(models.Model):
    image =CompressedImageField(upload_to="banner/", null=True,blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        verbose_name = 'banner'
        verbose_name_plural = 'banners'
        db_table = 'banner_01'

@receiver(pre_delete,sender=Banner)
def auto_delete_file_on_change_activity_image(sender,instance,*args,**kwargs):
    if instance.image:
        image_path = instance.image.path
        if os.path.exists(image_path):
            os.remove(image_path)
        else:
            print ("no path fount")


@receiver(pre_save,sender=Banner)
def update_image_on_change_banner(sender,instance,*args,**kwargs):
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
