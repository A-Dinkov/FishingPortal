from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify

from FishingPortal.auth_app.validators import ValidateIsOnlyAlpha
from FishingPortal.business.validators import ValidateIsAlAlphaNumHypAndUnderscore
from django.core.validators import MaxLengthValidator, MinLengthValidator

UserModel = get_user_model()


class Adventure(models.Model):
    NAME_MAX_LENGTH = 50
    NAME_MIN_LENGTH = 2
    PLACE_MAX_LENGTH = 50
    DESCRIPTION_MAX_LENGTH = 1000

    objects = models.Manager()

    name = models.CharField(
        blank=False,
        null=False,
        validators=(
            MaxLengthValidator(NAME_MAX_LENGTH),
            MinLengthValidator(NAME_MIN_LENGTH),
            ValidateIsOnlyAlpha()
        )

    )

    place = models.CharField(
        blank=True,
        null=True,
        validators=(
            ValidateIsAlAlphaNumHypAndUnderscore(),
            MaxLengthValidator(PLACE_MAX_LENGTH),
        )
    )
    date = models.DateField(
        blank=True,
        null=True,
    )
    description = models.TextField(
        blank=True,
        validators=(
            MaxLengthValidator(DESCRIPTION_MAX_LENGTH),
        )
    )
    adventurer = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    slug = models.SlugField(
        unique=True,
        null=True
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            split_name = self.name.split()
            split_name_lower = [x.lower() for x in split_name]
            joined_name = '-'.join(split_name_lower)
            self.slug = slugify(f'{self.pk}-{joined_name}')

        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'
