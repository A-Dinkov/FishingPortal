from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, FileExtensionValidator, MaxLengthValidator
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

from FishingPortal.auth_app.validators import ValidateImageSize, ValidateIsOnlyAlpha
from FishingPortal.business.validators import ValidateIsAlAlphaNumHypAndUnderscore, ValidateNuberOfDigits

UserModel = get_user_model()


class Business(models.Model):
    MAX_LENGTH_NAME = 100
    MIN_LENGTH_NAME = 2
    MAX_LENGTH_CITY = 80
    MIN_LENGTH_CITY = 2
    MAX_LENGTH_COORDINATES = 50
    MAX_LENGTH_LOCATION = 500
    MAX_LENGTH_DESCRIPTION = 1000

    objects = models.Manager()

    lake_name = models.CharField(
        unique=True,
        blank=True,
        null=True,
        validators=(
            ValidateIsAlAlphaNumHypAndUnderscore(),
            MinLengthValidator(MIN_LENGTH_NAME),
            MaxLengthValidator(MAX_LENGTH_NAME)
        )
    )

    city = models.CharField(
        blank=True,
        null=True,
        validators=(
            MinLengthValidator(MIN_LENGTH_CITY),
            MaxLengthValidator(MAX_LENGTH_CITY),
            ValidateIsOnlyAlpha()
        )
    )

    coordinates = models.CharField(
        blank=True,
        null=True,
        validators=(
            MaxLengthValidator(MAX_LENGTH_COORDINATES),
        )
    )

    location = models.TextField(
        blank=True,
        null=True,
        validators=(
            MaxLengthValidator(MAX_LENGTH_LOCATION),
        )
    )

    description = models.TextField(
        blank=True,
        null=True,
        validators=(
            MaxLengthValidator(MAX_LENGTH_DESCRIPTION),
        )
    )

    business_images = models.ImageField(
        blank=True,
        null=True,
        upload_to='business_images/',
        validators=(
            ValidateImageSize(),
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'svg', 'webp']),
        )
    )

    phone_number = models.PositiveIntegerField(
        unique=True,
        blank=True,
        null=True,
        validators=(
            ValidateNuberOfDigits(),
        )
    )

    owner = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='owned_businesses'
    )

    slug = models.SlugField(
        unique=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            split_lake_name = self.lake_name.split()
            lower_case_lake_name = [x.lower() for x in split_lake_name]
            lake_name = '-'.join(lower_case_lake_name)
            self.slug = slugify(f'{self.pk}-{lake_name}')
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.lake_name}'

