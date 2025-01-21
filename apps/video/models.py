from django.db import models
from util.compressedFields import AdvanceThumbnailField
from util.compressedFields import CompressedVideoField




class Videos(models.Model):
    title = models.CharField(max_length=200)
    video = CompressedVideoField(
        upload_to='videos/',
        allowed_formats=['mp4', 'mov', 'avi'],
        output_format='mp4',
        codec='libx264'
    )

    image = AdvanceThumbnailField(upload_to='videos/image/')
    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'
