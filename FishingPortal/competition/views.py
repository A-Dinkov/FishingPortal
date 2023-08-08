
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as views
from FishingPortal.competition.forms import CompetitionCreationForm
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
        competition = form.save(commit=False)
        competition.business = self.request.user.owned_businesses.first()
        competition.save()
        return super().form_valid(form)
