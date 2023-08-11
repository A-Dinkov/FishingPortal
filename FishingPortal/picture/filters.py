import django_filters
from django import forms
from django.contrib.auth import get_user_model
from .models import Picture
from ..adventure.models import Adventure
from ..business.models import Business
from ..competition.models import Competition

UserModel = get_user_model()


class PictureFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')  # Filter title with case-insensitive partial match
    upload_date = django_filters.DateFilter(field_name='upload_date', lookup_expr='exact')
    # Filter by exact upload date

    related_adventure = django_filters.ModelChoiceFilter(queryset=Adventure.objects.all())
    related_business = django_filters.ModelChoiceFilter(queryset=Business.objects.all())

    # For ManyToManyField relations, I am using ModelMultipleChoiceFilter
    related_competition = django_filters.ModelMultipleChoiceFilter(queryset=Competition.objects.all(),
                                                                   widget=forms.CheckboxSelectMultiple)

    # For filtering by the user who uploaded the picture
    uploader = django_filters.ModelChoiceFilter(
        queryset=UserModel.objects.all())

    class Meta:
        model = Picture
        fields = ['title', 'upload_date', 'related_adventure', 'related_business', 'related_competition', 'uploader']


class PictureFilterPrivate(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(PictureFilterPrivate, self).__init__(*args, **kwargs)

        if user:
            self.title = django_filters.CharFilter(lookup_expr='icontains')
            self.upload_date = django_filters.DateFilter(field_name='upload_date', lookup_expr='exact')
            self.filters['related_adventure'].queryset = Adventure.objects.filter(adventurer=user)
            self.filters['related_competition'].queryset = Competition.objects.filter(participants=user)

    class Meta:
        model = Picture
        fields = ['title', 'upload_date', 'related_adventure', 'related_competition']

