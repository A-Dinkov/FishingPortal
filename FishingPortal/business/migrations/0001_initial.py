# Generated by Django 4.2.3 on 2023-08-07 16:29

import FishingPortal.auth_app.validators
import FishingPortal.business.validators
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lake_name', models.CharField(blank=True, null=True, unique=True, validators=[FishingPortal.business.validators.ValidateIsAlAlphaNumHypAndUnderscore(), django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(100)])),
                ('city', models.CharField(blank=True, null=True, validators=[django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(80), FishingPortal.auth_app.validators.ValidateIsOnlyAlpha()])),
                ('coordinates', models.CharField(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(50)])),
                ('location', models.TextField(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(500)])),
                ('description', models.TextField(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(1000)])),
                ('business_images', models.ImageField(blank=True, null=True, upload_to='business_images/', validators=[FishingPortal.auth_app.validators.ValidateImageSize(), django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'svg', 'webp'])])),
                ('phone_number', models.PositiveIntegerField(blank=True, null=True, unique=True, validators=[FishingPortal.business.validators.ValidateNuberOfDigits()])),
                ('slug', models.SlugField(unique=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_businesses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
