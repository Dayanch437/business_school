from django.db import models
from django.db.models import ForeignKey
from util.utils import BaseImageModel
from util.validator import validate_video_extension,validate_email

class Banner(BaseImageModel):
    image = models.ImageField(upload_to='banners/')
    title = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        verbose_name = 'banner'
        verbose_name_plural = 'banners'
        db_table = 'banner'




class Teacher(BaseImageModel):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    image = models.ImageField(upload_to='teachers/')
    class Meta:
        verbose_name = 'teacher'
        verbose_name_plural = 'teachers'
        db_table = 'teacher'

    def __str__(self):
        return f"{self.name} - {self.surname}"



class Course(BaseImageModel):
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



class Videos(BaseImageModel):
    title = models.CharField(max_length=200)
    video = models.FileField(upload_to='videos/',validators=[validate_video_extension])
    image = models.ImageField(upload_to='videos/')
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



class ActivityImage(BaseImageModel):
    social_activity = models.ForeignKey(SocialActivity, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='social_activity_images/')


    def __str__(self):
        return f"Image for {self.social_activity.name}"



class DiscountItem(BaseImageModel):
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='discounts/')
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



class Main(BaseImageModel):
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


class Advise(BaseImageModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='advise_images/')
    leftside =  ForeignKey('MainText', on_delete=models.SET_NULL, null=True,related_name='leftside')
    rightside = ForeignKey('MainText', on_delete=models.SET_NULL, null=True,related_name='rightside')
    class Meta:
        verbose_name = 'advise'
        verbose_name_plural = 'advises'
        db_table = 'advise'

    def __str__(self):
       return self.title


class News(BaseImageModel):
    title = models.CharField(max_length=400)
    description = models.TextField()
    date = models.DateField()

    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'
        db_table = 'news'

    def __str__(self):
        return self.title
