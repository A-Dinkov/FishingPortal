import re

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


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


@deconstructible
class ValidateNuberOfDigits:

    def __call__(self, value):
        count = 0
        while value > 0:
            count += 1

            value = value // 10

        if count != 9:
            raise ValidationError('Phone number must be 9 digits')

    def __eq__(self, other):
        return True
