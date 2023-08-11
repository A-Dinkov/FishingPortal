from django.core.paginator import Paginator
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


class ListAdventuresView(LoginRequiredMixin, views.ListView):
    model = Adventure
    template_name = 'adventure/list-adventures.html'
    context_object_name = 'user_adventures'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        adventure = Adventure.objects.all()

        paginator = Paginator(adventure, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        context['paginator'] = paginator
        return context
