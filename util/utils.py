

import os
import uuid
from PIL import Image, UnidentifiedImageError
from django.db import models
from django.core.files.base import ContentFile


def upload_file(instance, filename: str) -> str:
    """Generate a unique file path for the uploaded file."""
    path = type(instance).__name__.lower()
    ext = filename.rsplit(".", 1)[-1]
    new_filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join(path, new_filename)


class CompressedImageFile(models.fields.files.FieldFile):
    def save(self, name, content, save=True):
        try:
            # Validate and process image
            content.seek(0)
            image = Image.open(content)

            if image.format != "WEBP":
                webp_image = ContentFile(b"")
                image = image.convert("RGB")  # Ensure compatibility with WebP
                image.save(webp_image, format="WEBP", quality=75)

                # Update the filename with .webp extension
                base_name, _ = os.path.splitext(name)
                name = f"{base_name}.webp"
                webp_image.seek(0)
                content = webp_image

            super().save(name, content, save)
        except UnidentifiedImageError:
            raise ValueError("The uploaded file is not a valid image.")
        except Exception as e:
            raise ValueError(f"Error processing image: {e}")

    def delete(self, save=True):
        """Delete the file from storage when the model instance is deleted."""
        storage, path = self.storage, self.path
        super().delete(save)
        if path and os.path.exists(path):
            try:
                os.remove(path)
            except OSError:
                pass


class CompressedImageField(models.ImageField):
    attr_class = CompressedImageFile

    def __init__(self, *args, upload_to=upload_file, max_size_mb=20, **kwargs):
        self.max_size_mb = max_size_mb
        super().__init__(upload_to=upload_to, *args, **kwargs)

    def clean(self, value, model_instance):
        """Validate file size before saving."""
        if value.size > self.max_size_mb * 1024 * 1024:
            raise ValueError(f"File size exceeds {self.max_size_mb} MB.")
        return super().clean(value, model_instance)

    def deconstruct(self):
        """Ensure field serialization for migrations."""
        name, path, args, kwargs = super().deconstruct()
        kwargs["max_size_mb"] = self.max_size_mb
        return name, path, args, kwargs












