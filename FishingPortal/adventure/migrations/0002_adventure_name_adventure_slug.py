# Generated by Django 4.2.3 on 2023-08-09 16:29

import FishingPortal.auth_app.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adventure',
            name='name',
            field=models.CharField(default='1', validators=[django.core.validators.MaxLengthValidator(50), django.core.validators.MinLengthValidator(2), FishingPortal.auth_app.validators.ValidateIsOnlyAlpha()]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adventure',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
