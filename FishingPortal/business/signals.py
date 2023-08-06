from django.db.models.signals import post_save
from django.dispatch import receiver
from FishingPortal.business.models import Business


@receiver(post_save, sender=Business)
def set_is_owner(sender, instance, **kwargs):
    instance.is_regular_user = False
    instance.is_owner = True
    instance.save()
