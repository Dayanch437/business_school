from django.db import models
from util.utils import CompressedImageField
from util.validator import validate_video_extension,validate_email
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
import os
from django.core.files.base import ContentFile
import subprocess
from tempfile import NamedTemporaryFile


class Banner(models.Model):
    image =CompressedImageField(upload_to="banner/", null=True,blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        verbose_name = 'banner'
        verbose_name_plural = 'banners'
        db_table = 'banner'

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



class Content(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    class Meta:
        verbose_name = 'content'
        verbose_name_plural = 'contents'
        db_table = 'content'
    def __str__(self):
        return self.title


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



class Course(models.Model):
    name = models.CharField(max_length=200)
    image = CompressedImageField(upload_to='courses/')
    description = models.TextField()
    duration = models.CharField(max_length=200)
    price = models.FloatField()
    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'
        db_table = 'courses'
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


class Videos(models.Model):
    title = models.CharField(max_length=200)
    video = models.FileField(upload_to='videos/webm/',null=True,blank=True,validators=[validate_video_extension])
    image = CompressedImageField(upload_to='videos/')
    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'
        db_table = 'videos'

    def save(self, *args, **kwargs):
        # Call the original save method first
        super().save(*args, **kwargs)

        # If a video file is uploaded, convert it to WebM
        if self.video:
            input_video_path = self.video.path
            if not input_video_path.endswith('.webm'):
                output_video_path = os.path.splitext(input_video_path)[0] + '.webm'

                # Convert the video to WebM using ffmpeg
                try:
                    subprocess.run(
                        ['ffmpeg', '-i', input_video_path, '-c:v', 'libvpx-vp9', '-b:v', '1M', '-c:a', 'libopus',
                         output_video_path],
                        check=True
                    )
                    # Replace the original file with the WebM version
                    with open(output_video_path, 'rb') as f:
                        self.video.save(os.path.basename(output_video_path), ContentFile(f.read()), save=False)

                    # Delete the original non-WebM video file
                    os.remove(input_video_path)
                    os.remove(output_video_path)

                except subprocess.CalledProcessError as e:
                    print(f"Error during video conversion: {e}")

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


@receiver(pre_delete,sender=Videos)
def auto_delete_file_on_change_activity_image(sender,instance,*args,**kwargs):
    if instance.video:
        image_path = instance.video.path
        if os.path.exists(image_path):
            os.remove(image_path)
        else:
            print ("no path fount")


@receiver(pre_save,sender=Videos)
def update_image_on_change_banner(sender,instance,*args,**kwargs):
    if not instance.pk:
        return False
    try:
        old_image = Videos.objects.get(pk=instance.pk).video
    except Course.DoesNotExist:
        return False
    new_image = instance.video
    if not old_image == new_image:
        if os.path.isfile(old_image.path):
            os.remove(old_image.path)


class CartImage(models.Model):
    image = CompressedImageField(upload_to='cartImages/',null=True,blank=True)
    def __str__(self):
        return self.image.name


class SocialActivity(models.Model):

    class Meta:
        verbose_name = 'social activity'
        verbose_name_plural = 'social activities'
        db_table = 'socialActivity'

#
# class BigCart(models.Model):
#     social_activity = models.ForeignKey(SocialActivity, on_delete=models.CASCADE)
#     image = models.ManyToManyField(to=CartImage,related_name='bigCart')
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     date = models.DateTimeField(auto_now_add=True)
#     class Meta:
#         verbose_name = 'Big cart'
#         verbose_name_plural = 'Big carts'
#         db_table = 'bigCart'
#     def __str__(self):
#         return self.title
#
# class SmallCart(models.Model):
#     social_activity = models.ForeignKey(SocialActivity, on_delete=models.CASCADE)
#     image = models.ManyToManyField(to=CartImage,related_name='smallCart')
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     date = models.DateTimeField(auto_now_add=True)
#     class Meta:
#         verbose_name = 'Small cart'
#         verbose_name_plural = 'Small carts'
#         db_table = 'smallCart'
#     def __str__(self):
#         return self.title

class BigCart(models.Model):
    social_activity = models.ForeignKey(SocialActivity, on_delete=models.CASCADE, related_name='big_carts')
    image = models.ManyToManyField(CartImage, related_name='big_cart')
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class SmallCart(models.Model):
    social_activity = models.ForeignKey(SocialActivity, on_delete=models.CASCADE, related_name='small_carts')
    image = models.ManyToManyField(CartImage, related_name='small_cart')
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class DiscountItem(models.Model):
    description = models.CharField(max_length=255)
    percentage = models.CharField(max_length=50)
    class Meta:
        verbose_name = 'discount item'
        verbose_name_plural = 'discount items'
        db_table = 'discount_item'

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


class Image(models.Model):
    image = CompressedImageField(upload_to='images/')

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'

    def __str__(self):
        return self.image.name

@receiver(pre_delete,sender=Image)
def auto_delete_file_on_change_activity_image(sender,instance,*args,**kwargs):
    if instance.image:
        image_path = instance.image.path
        if os.path.exists(image_path):
            os.remove(image_path)
        else:
            print ("no path fount")


@receiver(pre_save,sender=Image)
def update_image_on_change_banner(sender,instance,*args,**kwargs):
    if not instance.pk:
        return False
    try:
        old_image = Image.objects.get(pk=instance.pk).image
    except Image.DoesNotExist:
        return False
    new_image = instance.image
    if not old_image == new_image:
        if os.path.isfile(old_image.path):
            os.remove(old_image.path)


class Main(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    images =models.ManyToManyField(to=Image, related_name='images')
    class Meta:
        verbose_name = 'main'
        verbose_name_plural = 'main'
        db_table = 'main'
    def __str__(self):
        return self.title



class News(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    image = CompressedImageField(upload_to='news/')
    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'
        db_table = 'news'

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

