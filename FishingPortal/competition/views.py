from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from FishingPortal.competition.forms import CompetitionCreationForm, CompetitionEditForm
from FishingPortal.competition.models import Competition


class CompetitionCreateView(LoginRequiredMixin, views.CreateView):
    model = Competition
    form_class = CompetitionCreationForm
    template_name = 'competition/create.html'
    success_url = reverse_lazy('private_page')

    def get_form_kwargs(self):
        kwargs = super(CompetitionCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        competition = form.save()
        return super().form_valid(form)


class CompetitionDetailsView(LoginRequiredMixin, views.DetailView):
    model = Competition
    template_name = 'competition/details.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class CompetitionEditView(LoginRequiredMixin, views.UpdateView):
    model = Competition
    form_class = CompetitionEditForm
    template_name = 'competition/edit.html'
    success_url = reverse_lazy('private_page')


class CompetitionDeleteView(LoginRequiredMixin, views.DeleteView):
    model = Competition
    template_name = 'competition/delete.html'
    context_object_name = 'competition'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('private_page')

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        return response

    def form_valid(self, form):
        messages.success(self.request, "The business was deleted successfully.")
        return super(CompetitionDeleteView, self).form_valid(form)


@login_required
def signup_for_competition(request, competition_slug):
    competition = get_object_or_404(Competition, slug=competition_slug)

    if request.user in competition.participants.all():
        messages.info(request, 'You are already signed up for this competition.')
    else:
        competition.participants.add(request.user)
        competition.save()
        messages.success(request, 'Successfully signed up for the competition!')

    return redirect(competition.get_absolute_url())
