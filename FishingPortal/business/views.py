from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic as views

from FishingPortal.business.forms import BusinessCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .models import Business

UserModel = get_user_model()


class BusinessCreateView(LoginRequiredMixin, CreateView):
    model = Business
    form_class = BusinessCreationForm
    template_name = 'business/create.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        business = form.save(commit=False)
        business.owner = self.request.user
        business.save()
        return super().form_valid(form)


# @login_required
# def business_details(request, slug):
#     business = Business.objects.filter(slug=slug).get()
#
#     context = {
#         'business': business,
#     }
#
#     return render(request, 'business/details.html', context)


class BusinessDetailView(LoginRequiredMixin, views.DetailView):
    model = Business
    template_name = 'business/details.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class BusinessOwnerView(LoginRequiredMixin, views.ListView):
    template_name = 'business/private.html'
    model = Business


class DeleteBusinessView(LoginRequiredMixin, views.DeleteView):
    template_name = 'business/delete.html'
    context_object_name = 'business'
    success_url = 'home'

    def form_valid(self, form):
        messages.success(self.request, "The business was deleted successfully.")
        return super(DeleteBusinessView, self).form_valid(form)

