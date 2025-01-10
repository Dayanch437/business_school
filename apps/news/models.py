from django.db import models
from util.utils import CompressedImageField
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
import os

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    image = CompressedImageField(upload_to='news/')
    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'

    def __str__(self):
        return self.title

@receiver(pre_delete,sender=News)
def auto_delete_file_on_change_activity_image(sender,instance,*args,**kwargs):
    if instance.image:
        image_path = instance.image.path
        if os.path.exists(image_path):
            os.remove(image_path)
        else:
            print ("no path fount")


@receiver(pre_save,sender=News)
def update_image_on_change_banner(sender,instance,*args,**kwargs):
    if not instance.pk:
        return False
    try:
        old_image = News.objects.get(pk=instance.pk).image
    except News.DoesNotExist:
        return False
    new_image = instance.image
    if not old_image == new_image:
        if os.path.isfile(old_image.path):
            os.remove(old_image.path)
