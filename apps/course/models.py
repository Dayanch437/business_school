from django.db import models
from util.utils import CompressedImageField
from django.db.models.signals import pre_save,pre_delete
from django.dispatch import receiver
import os

class Course(models.Model):
    name = models.CharField(max_length=200)
    image = CompressedImageField(upload_to='courses/')
    description = models.TextField()
    duration = models.CharField(max_length=200)
    price = models.FloatField()
    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'
    def __str__(self):
        return self.name
@receiver(pre_delete,sender=Course)
def auto_delete_file_on_change_activity_image(sender,instance,*args,**kwargs):
    if instance.image:
        image_path = instance.image.path
        if os.path.exists(image_path):
            os.remove(image_path)
        else:
            print ("no path fount")


@receiver(pre_save,sender=Course)
def update_image_on_change_banner(sender,instance,*args,**kwargs):
    if not instance.pk:
        return False
    try:
        old_image = Course.objects.get(pk=instance.pk).image
    except Course.DoesNotExist:
        return False
    new_image = instance.image
    if not old_image == new_image:
        if os.path.isfile(old_image.path):
            os.remove(old_image.path)
