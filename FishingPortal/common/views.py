# Django imports
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, get_object_or_404, redirect
from django.views import generic as views

# Application imports
from FishingPortal.adventure.models import Adventure
from FishingPortal.business.models import Business, Like
from FishingPortal.picture.models import Picture

UserModel = get_user_model()


class RegularUserHomeView(LoginRequiredMixin, views.DetailView):
    model = UserModel
    template_name = 'common/private-regular.html'
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


def like_object(request, model, object_slug):
    # Get the model class based on the 'model' string
    model_mapping = {
        "business": {"class": Business, "redirect_view": "business_details"},
        "photo": {"class": Picture, "redirect_view": "photo_details"}
    }

    if model not in model_mapping:
        raise ValueError("Invalid model type")

    model_class = model_mapping[model]["class"]

    # Retrieve the object using the slug
    obj = get_object_or_404(model_class, slug=object_slug)
    content_type = ContentType.objects.get_for_model(obj)

    # Check if the user has already liked this object
    liked = Like.objects.filter(user=request.user, content_type=content_type, object_id=obj.id).exists()

    if liked:
        # If they have, unlike it by deleting the Like object
        Like.objects.filter(user=request.user, content_type=content_type, object_id=obj.id).delete()
    else:
        # If they haven't, like it by creating a new Like object
        Like.objects.create(user=request.user, content_object=obj)

    # Redirect to the appropriate view based on the model type
    return redirect(model_mapping[model]["redirect_view"], slug=object_slug)
