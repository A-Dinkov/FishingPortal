from django.core.validators import MinLengthValidator
from django.db import models
from FishingPortal.business.validators import ValidateIsAlAlphaNumHypAndUnderscore


class Business(models.Model):
    business_name = models.CharField(
        blank=False,
        null=False,
        max_length=250,
        validators=(
            ValidateIsAlAlphaNumHypAndUnderscore(),
            MinLengthValidator(2)
        )


    )

