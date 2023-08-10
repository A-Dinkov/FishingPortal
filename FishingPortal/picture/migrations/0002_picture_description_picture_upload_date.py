# Generated by Django 4.2.3 on 2023-08-10 06:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='description',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='picture',
            name='upload_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
