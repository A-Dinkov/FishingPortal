# Generated by Django 4.2.3 on 2023-08-22 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0004_alter_picture_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='picture',
            options={'ordering': ['upload_date']},
        ),
    ]
