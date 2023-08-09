from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth.mixins import LoginRequiredMixin
from FishingPortal.adventure.forms import AdventureCreationForm, AdventureEditForm
from FishingPortal.adventure.models import Adventure


class CreateAdventureView(LoginRequiredMixin, views.CreateView):
    model = Adventure
    template_name = 'adventure/create.html'
    form_class = AdventureCreationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        adventure = form.save(commit=False)
        adventure.adventurer = self.request.user
        adventure.save()
        return super().form_valid(form)


class AdventureDetailView(LoginRequiredMixin, views.DetailView):
    model = Adventure
    template_name = 'adventure/details.html'


class EditAdventureView(LoginRequiredMixin, views.UpdateView):
    model = Adventure
    template_name = 'adventure/edit.html'
    success_url = reverse_lazy('adventure_details')
    form_class = AdventureEditForm


class DeleteAdventureView(LoginRequiredMixin, views.DeleteView):
    model = Adventure
    template_name = 'adventure/delete.html'
    success_url = reverse_lazy('home')
