from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.core.validators import MaxLengthValidator, MinLengthValidator
from FishingPortal.business.models import Business
from FishingPortal.business.validators import ValidateIsAlAlphaNumHypAndUnderscore


UserModel = get_user_model()


class Competition(models.Model):
    NAME_MAX_LENGTH = 50
    NAME_MIN_LENGTH = 2
    PLACE_MAX_LENGTH = 50
    PLACE_MIN_LENGTH = 2
    DESCRIPTION_MAX_LENGTH = 500

    name = models.CharField(
        validators=(
            MinLengthValidator(NAME_MIN_LENGTH),
            MaxLengthValidator(NAME_MAX_LENGTH),
            ValidateIsAlAlphaNumHypAndUnderscore()
        ),
    )

    place = models.CharField(
        validators=(
            MinLengthValidator(PLACE_MIN_LENGTH),
            MaxLengthValidator(PLACE_MAX_LENGTH)
        )
    )

    date = models.DateTimeField()

    description = models.TextField(
        blank=True,
        null=True,
        validators=(
            MaxLengthValidator(DESCRIPTION_MAX_LENGTH),
        )
    )

    business = models.ForeignKey(
        Business,
        on_delete=models.CASCADE,
        related_name='competitions'
    )
    participants = models.ManyToManyField(
        UserModel,
        related_name='competitions',
        blank=True
    )

    active = models.BooleanField(
        default=True,
    )

    slug = models.SlugField(
        unique=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            split_name = self.name.split()
            lower_case_name = [x.lower() for x in split_name]
            name = '-'.join(lower_case_name)
            self.slug = slugify(f'{self.pk}-{name}')
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
