from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.views import generic as views
from django.shortcuts import render, get_list_or_404

from FishingPortal.adventure.models import Adventure
from FishingPortal.business.models import Business

UserModel = get_user_model()


class RegularUserHomeView(LoginRequiredMixin, views.DetailView):
    model = UserModel
    template_name = 'common/private-regular.html'
    # context_object_name = 'user_object'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_adventures = Adventure.objects.filter(adventurer=self.object)
        user_competitions = self.object.competitions.all()
        paginator = Paginator(user_competitions, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        context['paginator'] = paginator

        context['user_adventures'] = user_adventures
        context['user_competitions'] = user_competitions

        return context


class BusinessOwnerView(LoginRequiredMixin, views.ListView):
    template_name = 'common/private-owner.html'
    model = Business
    paginate_by = 2

    def get_queryset(self):
        # This ensures that only the businesses owned by the user are fetched.
        return get_list_or_404(Business, owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get the list of businesses owned by the user.
        user_businesses = self.get_queryset()

        # Fetch related competitions for those businesses.
        # This creates a dictionary where the key is a business and the value is a list of its competitions.
        business_competitions = {business: business.competitions.all() for business in user_businesses}

        paginator = Paginator(user_businesses, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        context['paginator'] = paginator

        context['business_competitions'] = business_competitions
        return context
