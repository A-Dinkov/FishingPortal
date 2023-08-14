# Django imports
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views import generic as gen_views

# Application imports
from FishingPortal.competition.forms import CompetitionEditForm, CompetitionCreationForm
from FishingPortal.competition.models import Competition


class CompetitionCreateView(LoginRequiredMixin, gen_views.CreateView):
    model = Competition
    form_class = CompetitionCreationForm
    template_name = 'competition/create.html'

    def get_success_url(self):
        user = self.request.user
        return reverse('private_owner', args=[user.pk])

    def get_form_kwargs(self):
        kwargs = super(CompetitionCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        competition = form.save()
        return super().form_valid(form)


class CompetitionDetailsView(LoginRequiredMixin, gen_views.DetailView):
    model = Competition
    template_name = 'competition/details.html'


class CompetitionEditView(LoginRequiredMixin, gen_views.UpdateView):
    model = Competition
    form_class = CompetitionEditForm
    template_name = 'competition/edit.html'

    def get_success_url(self):
        user = self.request.user
        return reverse('private_owner', args=[user.pk])


class CompetitionDeleteView(LoginRequiredMixin, gen_views.DeleteView):
    model = Competition
    template_name = 'competition/delete.html'
    context_object_name = 'competition'

    def get_success_url(self):
        user = self.request.user
        return reverse('private_owner', args=[user.pk])

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        return response

    def form_valid(self, form):
        messages.success(self.request, "The business was deleted successfully.")
        return super(CompetitionDeleteView, self).form_valid(form)


@login_required
def signup_for_competition(request, slug):
    competition = get_object_or_404(Competition, slug=slug)

    has_profile = hasattr(request.user, 'userprofile')
    if not has_profile:
        messages.error(request, 'You need to create a profile first before signing up for a competition.')
        return redirect('create_profile')

    if request.user in competition.participants.all():
        messages.info(request, 'You are already signed up for this competition.')
    else:
        competition.participants.add(request.user)
        competition.save()
        messages.success(request, 'Successfully signed up for the competition!')

    return redirect('list_competitions')


@login_required
def sign_off_from_competition(request, slug):
    competition = get_object_or_404(Competition, slug=slug)

    if request.user in competition.participants.all():
        competition.participants.remove(request.user)
        competition.save()
        messages.success(request, 'Successfully signed off from the competition!')
    else:
        messages.info(request, 'You are not signed up for this competition.')

    return redirect('list_competitions')


class CompetitionsListDisplayView(LoginRequiredMixin, gen_views.ListView):
    model = Competition
    template_name = 'competition/competition-list.html'
    context_object_name = 'competitions'
    paginate_by = 5


class ParticipantsListDisplayView(CompetitionDetailsView):
    template_name = 'competition/participants-list.html'
    context_object_name = 'competition'
    paginate_by = 5

    def get_queryset(self):
        return super().get_queryset().prefetch_related('participants__userprofile')

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        competition = self.get_object()
        participants = competition.participants.all()

        paginator = Paginator(participants, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        context['paginator'] = paginator
        return context





