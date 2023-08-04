from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model


@receiver(post_save, sender=get_user_model())
def set_regular_user(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:
        instance.is_regular_user = True
        instance.save()


@receiver(pre_save, sender=get_user_model())
def update_is_regular_user(sender, instance, **kwargs):
    if instance.is_staff:
        instance.is_regular_user = False
