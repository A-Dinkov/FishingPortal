from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, get_list_or_404, render, redirect
from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from django.views import generic as views
from FishingPortal.business.forms import BusinessCreationForm, BusinessEditForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .models import Business
from ..competition.models import Competition

UserModel = get_user_model()


class BusinessCreateView(LoginRequiredMixin, CreateView):
    model = Business
    form_class = BusinessCreationForm
    template_name = 'business/create.html'
    success_url = reverse_lazy('private_page')

    def form_valid(self, form):
        business = form.save(commit=False)
        business.owner = self.request.user
        business.save()
        return super().form_valid(form)


class BusinessDetailView(LoginRequiredMixin, views.DetailView):
    model = Business
    template_name = 'business/details.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class BusinessOwnerView(LoginRequiredMixin, views.ListView):
    template_name = 'business/private.html'
    model = Business

    def get_queryset(self):
        # This ensures that only the businesses owned by the user are fetched.
        return get_list_or_404(Business, owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get the list of businesses owned by the user.
        user_businesses = self.get_queryset()

        # Fetch related competitions for those businesses.
        # This step is optional and depends on how you want to structure your data in the template.
        # This creates a dictionary where the key is a business and the value is a list of its competitions.
        business_competitions = {business: business.competitions.all() for business in user_businesses}

        context['business_competitions'] = business_competitions
        return context


class EditBusinessView(LoginRequiredMixin, views.UpdateView):
    model = Business
    form_class = BusinessEditForm
    template_name = 'business/edit.html'
    success_url = reverse_lazy('private_page')


class DeleteBusinessView(LoginRequiredMixin, views.DeleteView):
    model = Business
    template_name = 'business/delete.html'
    context_object_name = 'business'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('home')

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
    template_name = 'business/lakes_list.html'
    context_object_name = 'businesses'
    paginate_by = 5



