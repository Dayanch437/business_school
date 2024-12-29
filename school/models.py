import io
from PIL import Image
from django.db import models
from django.db.models import ForeignKey
from utils.validator import validate_video_extension,validate_image,validate_email
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
import os


class Banner(models.Model):
    image = models.ImageField(upload_to='banners/',validators=[validate_image],blank=True)
    title = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'banner'
        verbose_name_plural = 'banners'
        db_table = 'banner'

    def save(self, *args, **kwargs):
        if self.image:
            image_file = self.image
            image = Image.open(image_file)
            webp_image = io.BytesIO()
            image.save(webp_image, format='WebP')
            webp_image.seek(0)

            webp_filename = f'{self.image.name.rsplit(".", 1)[0]}.webp'
            self.image.save(webp_filename, io.BytesIO(webp_image.read()), save=False)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


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




class Teacher(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    image = models.ImageField(upload_to='teachers/')
    class Meta:
        verbose_name = 'teacher'
        verbose_name_plural = 'teachers'
        db_table = 'teacher'


    def save(self, *args, **kwargs):
        if self.image:
            # Convert image to WebP format
            image_file = self.image
            image = Image.open(image_file)
            webp_image = io.BytesIO()
            image.save(webp_image, format='WebP')
            webp_image.seek(0)

            webp_filename = f'{self.image.name.rsplit(".", 1)[0]}.webp'
            self.image.save(webp_filename, io.BytesIO(webp_image.read()), save=False)

        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.name} - {self.surname}"



class Course(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='courses/')
    description = models.TextField()
    duration = models.CharField(max_length=200)
    price = models.FloatField()
    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'
        db_table = 'courses'
    def __str__(self):
        return self.name



class Videos(models.Model):
    title = models.CharField(max_length=200)
    video = models.FileField(upload_to='videos/',validators=[validate_video_extension])
    image = models.ImageField(upload_to='videos/',validators=[validate_image])
    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'
        db_table = 'videos'
    def __str__(self):
        return self.title


class SocialActivity(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    id = models.AutoField(primary_key=True)
    def __str__(self):
        return self.name



class ActivityImage(models.Model):
    social_activity = models.ForeignKey(SocialActivity, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='social_activity_images/')

    def save(self, *args, **kwargs):
        if self.image:
            # Convert image to WebP format
            image_file = self.image
            image = Image.open(image_file)
            webp_image = io.BytesIO()
            image.save(webp_image, format='WebP')
            webp_image.seek(0)

            webp_filename = f'{self.image.name.rsplit(".", 1)[0]}.webp'
            self.image.save(webp_filename, io.BytesIO(webp_image.read()), save=False)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Image for {self.social_activity.name}"



class DiscountItem(models.Model):
    description = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='discounts/',validators=[validate_image],blank=True)
    percentage = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'discount item'
        verbose_name_plural = 'discount items'
        db_table = 'discount_item'

    def save(self, *args, **kwargs):
        if self.icon:
            # Convert image to WebP format
            image_file = self.icon
            image = Image.open(image_file)
            webp_image = io.BytesIO()
            image.save(webp_image, format='WebP')
            webp_image.seek(0)

            webp_filename = f'{self.icon.name.rsplit(".", 1)[0]}.webp'
            self.icon.save(webp_filename, io.BytesIO(webp_image.read()), save=False)

        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.description}"




class Contact(models.Model):
    username = models.CharField(max_length=255)
    gmail = models.EmailField(max_length=200, validators=[validate_email])
    comment = models.TextField()
    is_verified = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=6, blank=True, null=True)

    def __str__(self):
        return f"{self.username}: {self.comment}"

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'
        db_table = 'contact'



class Main(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='main_images/')
    description = models.TextField()
    class Meta:
        verbose_name = 'main'
        verbose_name_plural = 'main'
        db_table = 'main'


    def __str__(self):
        return self.title


class MainText(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    class Meta:
        db_table = 'text'
        verbose_name = 'text'
        verbose_name_plural = 'texts'


class Advise(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    imagecenter = models.ImageField(upload_to='advise_images/',validators=[validate_image],blank=True)
    leftside =  ForeignKey('MainText', on_delete=models.SET_NULL, null=True,related_name='leftside')
    rightside = ForeignKey('MainText', on_delete=models.SET_NULL, null=True,related_name='rightside')
    class Meta:
        verbose_name = 'advise'
        verbose_name_plural = 'advises'
        db_table = 'advise'

    def save(self, *args, **kwargs):
        if self.imagecenter:
            # Convert image to WebP format
            image_file = self.imagecenter
            image = Image.open(image_file)
            webp_image = io.BytesIO()
            image.save(webp_image, format='WebP')
            webp_image.seek(0)
            webp_filename = f'{self.imagecenter.name.rsplit(".", 1)[0]}.webp'
            self.imagecenter.save(webp_filename, io.BytesIO(webp_image.read()), save=False)