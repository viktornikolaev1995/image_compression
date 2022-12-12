import os
from typing import Any

from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver

from products import models


@receiver(post_save, sender=models.Image, dispatch_uid="convert_image_to_webp_format")
def convert_image(sender, instance, created: bool, **kwargs: Any) -> None:
    if created:
        formats = []
        file_path = instance.image.path
        request_format = file_path.rsplit(".", 1)[1]
        image = Image.open(file_path)
        formats.append(request_format)
        required_format = "webp"
        image = image.convert('RGB')

        if request_format != required_format:
            new_file_path = file_path.replace(request_format, required_format)
            image.save(new_file_path, "WEBP")
            instance.image = instance.image.name.replace(request_format, required_format)
            formats.append(required_format)
            os.remove(file_path)

        instance.formats = formats
        instance.save()
