from django.db import models
from util.compressedFields import AdvanceThumbnailField
from util.utils import CompressedImageField
# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    image = AdvanceThumbnailField(upload_to="news/", null=True, blank=True)
    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'

    def __str__(self):
        return self.title
