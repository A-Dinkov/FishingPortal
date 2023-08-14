# Django imports
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.views import generic as gen_views

# Application imports
from FishingPortal.business.models import Like
from FishingPortal.picture.filters import PictureFilterPrivate, PictureFilter
from FishingPortal.picture.forms import PhotoEditForm, UploadPictureForm
from FishingPortal.picture.models import Picture


UserModel = get_user_model()


class UploadPictureView(LoginRequiredMixin, gen_views.CreateView):
    model = Picture
    template_name = 'picture/upload.html'
    form_class = UploadPictureForm

    def get_success_url(self):
        user = self.request.user

        if user.is_owner:
            return reverse('private_owner', args=[user.pk])
        elif user.is_regular_user:
            return reverse('private_regular', args=[user.pk])

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


class PhotoListView(LoginRequiredMixin, gen_views.ListView):
    model = Picture
    template_name = 'picture/list-photos.html'
    context_object_name = 'photos'
    paginate_by = 10

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filter = None

    def get_queryset(self):
        queryset = super().get_queryset().all()
        self.filter = PictureFilter(self.request.GET, queryset=queryset)
        return self.filter.qs

    def get_context_data(self, **kwargs):
        userprofile = self.request.user.userprofile
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filter
        context['show_filter'] = 'all_photos'
        context['user_profile'] = userprofile
        return context


class PrivatePhotoView(PhotoListView):

    def get_queryset(self):
        queryset = super().get_queryset().filter(uploader=self.request.user)
        self.filter = PictureFilterPrivate(self.request.GET, queryset=queryset, user=self.request.user)
        return self.filter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filter
        context['show_filter'] = 'user_photos'
        return context


class BusinessPhotoListView(PhotoListView):
    template_name = 'picture/list-photos.html'
    paginate_by = 10

    def get_queryset(self):
        if 'pk' in self.kwargs:
            pk = self.kwargs['pk']
            return Picture.objects.filter(pk=pk)
        return Picture.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'pk' in self.kwargs:
            context['business_pk'] = self.kwargs['pk']
        return context


class PhotoDetailView(LoginRequiredMixin, gen_views.DetailView):
    model = Picture
    template_name = 'picture/details.html'
    context_object_name = 'photo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get the content type for Business objects
        content_type = ContentType.objects.get_for_model(self.object)

        # Query the Like model directly to get the count of likes for this Business object
        likes_count = Like.objects.filter(content_type=content_type, object_id=self.object.id).count()

        context['likes_count'] = likes_count

        return context


class PhotoEditView(LoginRequiredMixin, gen_views.UpdateView):
    model = Picture
    form_class = PhotoEditForm
    template_name = 'picture/edit.html'
    context_object_name = 'photo'

    def get_success_url(self):
        return reverse('photo_details', kwargs={'slug': self.object.slug})


class PhotoDeleteView(LoginRequiredMixin, gen_views.DeleteView):
    model = Picture
    template_name = 'picture/delete.html'
    context_object_name = 'photo'

    def get_success_url(self):
        user = self.request.user

        if user.is_owner:
            return reverse('private_owner', args=[user.pk])
        elif user.is_regular_user:
            return reverse('private_regular', args=[user.pk])

        else:
            return reverse('home')




