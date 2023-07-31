from django import template
from FishingPortal.auth_app.models import UserProfile

register = template.Library()


@register.simple_tag(takes_context=True)
def get_profile(context):
    request = context['request']
    if request.user.is_authenticated:
        try:
            return UserProfile.objects.get(user=request.user)

        except UserProfile.DoesNotExist:
            return None


