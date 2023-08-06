import re

from PIL import Image
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class ValidateImageSize:

    def __call__(self, image):
        max_width = 2000
        max_height = 2000

        img = Image.open(image)
        img_width, img_height = img.size

        if img_width > max_width or img_height > max_height:
            raise ValidationError(
                f"Image dimensions should not exceed {max_width}x{max_height} pixels."
            )

    def __eq__(self, other):
        return True


@deconstructible
class ValidateIsOnlyAlpha:
    def __call__(self, value):
        pattern1 = r'^[a-zA-Z\s]+$'
        pattern2 = r'^[\s]+$'
        if not re.match(pattern1, value):
            raise ValidationError('Name should contain only letters and space between')

        elif re.match(pattern2, value):
            raise ValidationError('Name can not be only from white space')

    def __eq__(self, other):
        return True
