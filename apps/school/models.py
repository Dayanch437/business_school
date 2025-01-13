from django.db import models
from util.utils import CompressedImageField
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
import os





class Main(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    class Meta:
        verbose_name = 'main'
        verbose_name_plural = 'main'
        db_table = 'main'
    def __str__(self):
        return self.title



