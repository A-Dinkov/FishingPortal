from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
import re


@deconstructible
class ValidateIsAlAlphaNumHypAndUnderscore:

    def __call__(self, value):
        first_pattern = r'^[\w\d_\- ]'
        second_pattern = r'^[\w\d_\-]'
        if not re.match(first_pattern, value):
            raise ValidationError(
                "Name can only contain letters, numbers, underscores, hyphens")

        elif not re.match(second_pattern, value):
            raise ValidationError(
                "Name can't be white spaces"
            )

    def __eq__(self, other):
        return True
