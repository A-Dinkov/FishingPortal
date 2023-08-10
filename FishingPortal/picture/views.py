from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic as views
from django.shortcuts import reverse
from FishingPortal.picture.forms import UploadPictureForm
from FishingPortal.picture.models import Picture

UserModel = get_user_model()


class UploadPictureView(LoginRequiredMixin, views.CreateView):
    model = Picture
    template_name = 'picture/upload.html'
    form_class = UploadPictureForm

    def get_success_url(self):
        user = self.request.user

        if user.is_owner:
            return reverse('private_owner')
        elif user.is_regular_user:
            return reverse('private_regular')

        else:
            return reverse('home')

    def get_form_kwargs(self):
        kwargs = super(UploadPictureView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        picture = form.save(commit=False)
        picture.uploader = self.request.user
        picture.save()
        return super().form_valid(form)



