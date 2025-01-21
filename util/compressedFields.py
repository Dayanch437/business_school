from django.db.models import FileField
from django.core.exceptions import ValidationError
import subprocess

import io
import os

from django.core.files import File
from django.db import models
from PIL import Image, ImageOps



class CompressedVideoField(FileField):
    """
    Custom Video Field for handling compressed and progressive video uploads.
    """

    def __init__(self, *args, **kwargs):
        # Add any specific parameters if needed, like allowed formats
        self.allowed_formats = kwargs.pop('allowed_formats', ['mp4'])
        self.output_format = kwargs.pop('output_format', 'mp4')
        self.codec = kwargs.pop('codec', 'libx264')
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        file = super().pre_save(model_instance, add)
        if file and file.name:
            file_path = file.path
            if not self._is_allowed_format(file_path):
                raise ValidationError(f"Unsupported file format. Allowed formats: {self.allowed_formats}")
            return self._convert_to_progressive(file_path)
        return file

    def _is_allowed_format(self, file_path):
        """
        Validate if the uploaded file is in an allowed format.
        """
        ext = os.path.splitext(file_path)[-1].lower()[1:]
        return ext in self.allowed_formats

    def _convert_to_progressive(self, file_path):
        """
        Convert video to a progressive format (MP4 with H.264 codec).
        """
        output_path = f"{os.path.splitext(file_path)[0]}_progressive.{self.output_format}"
        try:
            # Use ffmpeg for video conversion
            subprocess.run(
                [
                    "ffmpeg",
                    "-i", file_path,
                    "-vcodec", self.codec,
                    "-acodec", "aac",
                    "-movflags", "faststart",
                    output_path
                ],
                check=True
            )
            os.remove(file_path)  # Remove the original file
            return output_path
        except subprocess.CalledProcessError as e:
            raise ValidationError(f"Video compression failed: {e}")
#


class AdvanceThumbnailField(models.ImageField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def contribute_to_class(self, cls, name, **kwargs):
        super().contribute_to_class(cls, name, **kwargs)
        models.signals.post_save.connect(self.convert_to_webp, sender=cls)
        models.signals.pre_delete.connect(self.delete_image, sender=cls)
        models.signals.pre_save.connect(self.auto_delete_file_on_change, sender=cls)

    def pre_save(self, model_instance, add):
        file = super().pre_save(model_instance, add)
        if not file:
            file.delete(save=False)
        return file

    def convert_to_webp(self, instance, **kwargs):
        image_field = getattr(instance, self.name)
        if not image_field or not image_field.name:
            return

        # Disconnect the signal before converting and saving the image
        models.signals.post_save.disconnect(
            self.convert_to_webp, sender=instance.__class__
        )

        try:
            with image_field.open() as source_file:
                img = Image.open(source_file)

                # Handle orientation from EXIF data
                img = ImageOps.exif_transpose(img)

                webp_io = io.BytesIO()

                img.save(webp_io, format="WEBP")
                webp_io.seek(0)

                base_name = os.path.basename(image_field.name)  # Get the file name without path
                name, _ = os.path.splitext(base_name)  # Remove the original extension
                name = f'{name}.webp'

                image_field.delete(save=False)
                webp_file = File(webp_io, name=name)
                setattr(instance, self.name, webp_file)
                instance.save(update_fields=[self.name])

        finally:
            # Reconnect the signal after saving
            models.signals.post_save.connect(
                self.convert_to_webp, sender=instance.__class__
            )

    def delete_image(self, instance, **kwargs):
        if instance.image:
            image_path = instance.image.path
            if os.path.exists(image_path):
                os.remove(image_path)
            else:
                print("error accured")
    def auto_delete_file_on_change(self, instance, **kwargs):
        if not instance.pk:
            return False

        try:
            old_instance = instance.__class__.objects.get(pk=instance.pk)
            old_file = getattr(old_instance, self.name)
        except instance.__class__.DoesNotExist:
            return False
        new_file = getattr(instance, self.name)
        print(old_file.path, new_file.path)
        if old_file and new_file and old_file != new_file:
            old_file_path = old_file.path if old_file else None
            new_file_path = new_file.path if new_file else None

            if old_file_path and old_file_path != new_file_path and os.path.isfile(old_file_path):
                os.remove(old_file_path)
                print(f"Deleted old file: {old_file_path}")

        return False

