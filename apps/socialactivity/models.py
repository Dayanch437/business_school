from django.db import models

from util.compressedFields import AdvanceThumbnailField


class SocialActivity(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'social activity'
        verbose_name_plural = 'social activities'
    def __str__(self):
        return self.title





class Image(models.Model):
    image = AdvanceThumbnailField(upload_to="images/",null=True, blank=True)
    social_activity = models.ForeignKey(SocialActivity,on_delete=models.CASCADE,related_name='images')

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'