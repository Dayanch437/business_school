from django.db import models
from util.compressedFields import AdvanceThumbnailField
from util.utils import CompressedImageField


# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=300)
    surname = models.CharField(max_length=300)
    description = models.TextField()
    image = AdvanceThumbnailField(upload_to="teacher", null=True, blank=True)
    major = models.CharField(max_length=400)
    class Meta:
        verbose_name = 'teacher'
        verbose_name_plural = 'teachers'
        db_table = 'teacher'

    def __str__(self):
        return f"{self.name} - {self.surname}"

