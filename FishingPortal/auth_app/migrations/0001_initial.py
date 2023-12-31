# Generated by Django 4.2.3 on 2023-08-07 16:28

import FishingPortal.auth_app.managers
import FishingPortal.auth_app.validators
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegularUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('consent', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_owner', models.BooleanField(default=False)),
                ('is_regular_user', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ['pk'],
            },
            managers=[
                ('objects', FishingPortal.auth_app.managers.RegularUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(validators=[django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(50), FishingPortal.auth_app.validators.ValidateIsOnlyAlpha()])),
                ('last_name', models.CharField(validators=[django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(50), FishingPortal.auth_app.validators.ValidateIsOnlyAlpha()])),
                ('age', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(16)])),
                ('city', models.CharField(blank=True, max_length=80, null=True)),
                ('bio', models.TextField(blank=True, max_length=1000, null=True)),
                ('image_profile', models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics/', validators=[FishingPortal.auth_app.validators.ValidateImageSize(), django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'svg', 'webp'])])),
            ],
        ),
    ]
