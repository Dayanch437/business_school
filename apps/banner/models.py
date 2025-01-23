import os

from django.db import models
from util.compressedFields import AdvanceThumbnailField
from util.utils import CompressedImageField
# Create your models here.



class Banner(models.Model):
    title = models.CharField(max_length=255)
    image = AdvanceThumbnailField(upload_to="banner/", null=True, blank=True)
    description = models.TextField()
    class Meta:
        verbose_name = 'banner'
        verbose_name_plural = 'banners'
        db_table = 'banner_01'

    def __str__(self):
        return self.title

