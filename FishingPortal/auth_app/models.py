# Django imports
from django.contrib.auth import models as auth_models, get_user_model
from django.core.validators import FileExtensionValidator, MinValueValidator, MinLengthValidator, MaxLengthValidator
from django.db import models
from django.utils import timezone

# Application imports
from FishingPortal.auth_app.managers import RegularUserManager
from FishingPortal.auth_app.validators import ValidateImageSize, ValidateIsOnlyAlpha


class RegularUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    objects = RegularUserManager()

    EMAIL_MAX_LENGTH = 50

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    email = models.EmailField(
        null=False,
        blank=False,
        unique=True,
        validators=(
            MaxLengthValidator(EMAIL_MAX_LENGTH),
        )
    )

    consent = models.BooleanField(
        default=False,
        blank=False,
        null=False,
    )

    date_joined = models.DateTimeField(default=timezone.now)

    is_staff = models.BooleanField(
        default=False,
    )
    is_superuser = models.BooleanField(
        default=False
    )

    is_active = models.BooleanField(
        default=True
    )

    is_owner = models.BooleanField(
        default=False
    )

    is_regular_user = models.BooleanField(
        default=False
    )

    def __str__(self):
        return f"@{self.email.split('@')[0]}"

    class Meta:
        ordering = ['pk']


UserModel = get_user_model()


class UserProfile(models.Model):
    MIN_LENGTH_NAME = 2
    MAX_LENGTH_NAME = 50
    MIN_AGE = 16
    CITY_MAX_LENGTH = 30
    BIO_MAX_LENGTH = 1000

    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, primary_key=True)

    first_name = models.CharField(
        blank=False,
        null=False,
        validators=(
            MinLengthValidator(MIN_LENGTH_NAME),
            MaxLengthValidator(MAX_LENGTH_NAME),
            ValidateIsOnlyAlpha()
        )
    )

    last_name = models.CharField(
        blank=False,
        null=False,
        validators=(
            MinLengthValidator(MIN_LENGTH_NAME),
            MaxLengthValidator(MAX_LENGTH_NAME),
            ValidateIsOnlyAlpha()
        )

    )

    age = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=(
            MinValueValidator(MIN_AGE),
        )
    )

    city = models.CharField(
        blank=True,
        null=True,
        validators=(
            MaxLengthValidator(CITY_MAX_LENGTH),
        )
    )

    bio = models.TextField(
        blank=True,
        null=True,
        validators=(
            MaxLengthValidator(BIO_MAX_LENGTH),
        )
    )

    image_profile = models.ImageField(
        default='profile_pics/default.jpg',
        upload_to='profile_pics/',
        validators=(
            ValidateImageSize(),
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'svg', 'webp']),
        )
    )

    objects = models.Manager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
