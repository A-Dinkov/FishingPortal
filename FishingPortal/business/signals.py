from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Business
from django.contrib.auth.models import Group


@receiver(post_save, sender=Business)
def update_user_is_owner_on_create(sender, instance, created, **kwargs):
    if created:
        instance.owner.groups.clear()
        new_group = Group.objects.get(name='Owners')
        instance.owner.is_regular_user = False
        new_group.user_set.add(instance.owner)
        instance.owner.is_owner = True
        instance.owner.save()




