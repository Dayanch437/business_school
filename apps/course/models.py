from django.db import models
from util.compressedFields import AdvanceThumbnailField
from util.utils import CompressedImageField

import os

class Course(models.Model):
    name = models.CharField(max_length=200)
    image = AdvanceThumbnailField(upload_to='course/', null=True, blank=True)
    description = models.TextField()
    duration = models.CharField(max_length=200)
    price = models.FloatField()
    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'

    def __str__(self):
        return self.name

