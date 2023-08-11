# Generated by Django 4.2.3 on 2023-08-10 10:43

import FishingPortal.auth_app.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0003_picture_slug_picture_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='title',
            field=models.CharField(validators=[django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(30), FishingPortal.auth_app.validators.ValidateIsOnlyAlpha()]),
        ),
    ]
