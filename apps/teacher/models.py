from django.db import models
from django.db.models.signals import pre_save,pre_delete
from django.dispatch import receiver
from util.utils import CompressedImageField
import os



# Create your models here.



class Teacher(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    description = models.TextField()
    image = CompressedImageField(upload_to='teachers/')
    major = models.CharField(max_length=200)
    class Meta:
        verbose_name = 'teacher'
        verbose_name_plural = 'teachers'
        db_table = 'teacher'

    def __str__(self):
        return f"{self.name} - {self.surname}"

@receiver(pre_delete,sender=Teacher)
def auto_delete_file_on_change_activity_image(sender,instance,*args,**kwargs):
    if instance.image:
        image_path = instance.image.path
        if os.path.exists(image_path):
            os.remove(image_path)
        else:
            print ("no path fount")


@receiver(pre_save,sender=Teacher)
def update_image_on_change_banner(sender,instance,*args,**kwargs):
    if not instance.pk:
        return False
    try:
        old_image = Teacher.objects.get(pk=instance.pk).image
    except Teacher.DoesNotExist:
        return False
    new_image = instance.image
    if not old_image == new_image:
        if os.path.isfile(old_image.path):
            os.remove(old_image.path)
