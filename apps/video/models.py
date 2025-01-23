from django.db import models
from util.compressedFields import AdvanceThumbnailField
from util.validator import validate_video_extension

class Videos(models.Model):
    title = models.CharField(max_length=200)
    video = models.FileField(
        upload_to="videos/",
        validators=[validate_video_extension],
    )

    image = AdvanceThumbnailField(upload_to='videos/image/')
    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'
    def __str__(self):
        return self.title
