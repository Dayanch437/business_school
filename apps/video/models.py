from django.db import models
from util.validator import validate_video_extension
from util.utils import CompressedImageField
import os
from django.core.files.base import ContentFile
import subprocess
from django.db.models.signals import pre_save,pre_delete
from django.dispatch import receiver
# Create your models here.


class Videos(models.Model):
    title = models.CharField(max_length=200)
    video = models.FileField(upload_to='videos/webm/',null=True,blank=False,validators=[validate_video_extension])
    image = CompressedImageField(upload_to='videos/')
    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'

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
    except Videos.DoesNotExist:
        return False
    new_image = instance.video
    if not old_image == new_image:
        if os.path.isfile(old_image.path):
            os.remove(old_image.path)