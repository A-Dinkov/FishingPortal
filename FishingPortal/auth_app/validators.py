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
