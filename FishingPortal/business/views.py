# Django imports
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic as views

# Application imports
from FishingPortal.business.forms import BusinessCreationForm, BusinessEditForm
from FishingPortal.business.models import Business, Like
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView


UserModel = get_user_model()


class BusinessCreateView(LoginRequiredMixin, CreateView):
    model = Business
    form_class = BusinessCreationForm
    template_name = 'business/create.html'

    def get_success_url(self):
        user = self.request.user
        return reverse('private_owner', args=[user.pk])

    def form_valid(self, form):
        business = form.save(commit=False)
        business.owner = self.request.user
        business.save()
        return super().form_valid(form)


class BusinessDetailView(LoginRequiredMixin, views.DetailView):
    model = Business
    template_name = 'business/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get the content type for Business objects
        content_type = ContentType.objects.get_for_model(self.object)

        # Query the Like model directly to get the count of likes for this Business object
        likes_count = Like.objects.filter(content_type=content_type, object_id=self.object.id).count()

        context['likes_count'] = likes_count

        return context


class EditBusinessView(LoginRequiredMixin, views.UpdateView):
    model = Business
    form_class = BusinessEditForm
    template_name = 'business/edit.html'

    def get_success_url(self):
        user = self.request.user
        return reverse('private_owner', args=[user.pk])


class DeleteBusinessView(LoginRequiredMixin, views.DeleteView):
    model = Business
    template_name = 'business/delete.html'
    context_object_name = 'business'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_success_url(self):
        user = self.request.user
        return reverse('private_owner', args=[user.pk])

    def get_queryset(self):
        return self.request.user.owned_businesses.all()

    def form_valid(self, form):
        messages.success(self.request, "The business was deleted successfully.")
        return super(DeleteBusinessView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        # Call the DeleteView's post method and delete the object
        response = super().post(request, *args, **kwargs)

        user = request.user

        # Check if the user has no more businesses
        if not Business.objects.filter(owner=user).exists():

            # Remove the user from the "owners" group
            owners_group = get_object_or_404(Group, name='Owners')
            user.groups.remove(owners_group)

            # Add the user to the "regular users" group
            regular_users_group = get_object_or_404(Group, name='RegularUsers')
            user.groups.add(regular_users_group)

            user.is_owner = False
            user.is_regular_user = True

            user.save()

        return response


class LakesListDisplayView(LoginRequiredMixin, views.ListView):
    model = Business
    template_name = 'business/lakes-list.html'
    context_object_name = 'businesses'
    paginate_by = 5




