from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, FileExtensionValidator, MaxLengthValidator
from django.db import models
from django.template.defaultfilters import slugify
from FishingPortal.auth_app.validators import ValidateImageSize, ValidateIsOnlyAlpha
from FishingPortal.business.validators import ValidateIsAlAlphaNumHypAndUnderscore


UserModel = get_user_model()


class Business(models.Model):
    MAX_LENGTH_NAME = 100
    MIN_LENGTH_NAME = 2
    MAX_LENGTH_CITY = 80
    MIN_LENGTH_CITY = 2
    MAX_LENGTH_LOCATION = 500
    MAX_LENGTH_DESCRIPTION = 1000

    lake_name = models.CharField(
        unique=True,
        blank=False,
        null=False,
        default='default_name',
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

    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE, blank=True, null=True)

    slug = models.SlugField(
        unique=True,
        blank=False,
        null=False,
        default='default-slug'
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            lake_name = '-'.join(self.lake_name.split())
            self.slug = slugify(f'{self.pk}-{lake_name}')


