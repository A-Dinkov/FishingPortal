from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group


@receiver(post_save, sender=get_user_model())
def set_regular_user(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:
        instance.is_regular_user = True
        group = Group.objects.get(name='RegularUsers')
        group.user_set.add(instance)
        instance.save()


@receiver(pre_save, sender=get_user_model())
def update_is_regular_user(sender, instance, **kwargs):
    if instance.is_staff:
        instance.is_regular_user = False



