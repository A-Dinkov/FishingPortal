# Django imports
from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver

# Application imports
from .models import Business


@receiver(post_save, sender=Business)
def update_user_is_owner_on_create(sender, instance, created, **kwargs):
    if created:
        instance.owner.groups.clear()
        new_group = Group.objects.get(name='Owners')
        instance.owner.is_regular_user = False
        new_group.user_set.add(instance.owner)
        instance.owner.is_owner = True
        instance.owner.save()




