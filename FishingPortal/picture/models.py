# Django imports
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator, MinLengthValidator, MaxLengthValidator
from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone

# Application imports
from FishingPortal.adventure.models import Adventure
from FishingPortal.auth_app.validators import ValidateImageSize, ValidateIsOnlyAlpha
from FishingPortal.business.models import Business
from FishingPortal.competition.models import Competition


class Picture(models.Model):

    TITLE_MAX_LENGTH = 30
    TITLE_MIN_LENGTH = 2

    objects = models.Manager()
    UserModel = get_user_model()

    title = models.CharField(
        blank=False,
        null=False,
        validators=(
            MinLengthValidator(TITLE_MIN_LENGTH),
            MaxLengthValidator(TITLE_MAX_LENGTH),
            ValidateIsOnlyAlpha()
        )
    )

    image = models.ImageField(
        upload_to='picture/',
        validators=(
            ValidateImageSize(),
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'svg', 'webp']),
        )
    )

    uploader = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

    related_adventure = models.ForeignKey(
        Adventure,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    related_business = models.ForeignKey(
        Business,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    related_competition = models.ForeignKey(
        Competition,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    description = models.TextField(
        blank=True,
        null=True,
        max_length=200
    )

    upload_date = models.DateTimeField(default=timezone.now)

    slug = models.SlugField(
        unique=True,
        null=True
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            split_title = self.title.split()
            lowered_title = [x.lower() for x in split_title]
            title = '-'.join(lowered_title)
            self.slug = slugify(f'{self.pk}-{title}')

        return super().save(*args, **kwargs)

    def __str__(self):
        return f'Uploaded by {self.uploader.userprofile.first_name} {self.uploader.userprofile.last_name}'


