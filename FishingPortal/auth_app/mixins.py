from django.shortcuts import redirect
from django.contrib import messages


class AnonymousUserOnlyMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.warning(request, "You are already registered!")
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
