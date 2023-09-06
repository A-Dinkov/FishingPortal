# Django imports
import django_filters
from django import forms
from django.contrib.auth import get_user_model

# Application imports
from FishingPortal.adventure.models import Adventure
from FishingPortal.business.models import Business
from FishingPortal.competition.models import Competition
from FishingPortal.picture.models import Picture

UserModel = get_user_model()


class BasePictureFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    upload_date = django_filters.DateFilter(field_name='upload_date',
                                            lookup_expr='exact',
                                            widget=forms.DateInput(attrs={'class': 'datepicker'}))

    class Meta:
        model = Picture
        fields = ['title', 'upload_date']


class PictureFilter(BasePictureFilter):
    related_adventure = django_filters.ModelChoiceFilter(queryset=Adventure.objects.all())
    related_business = django_filters.ModelChoiceFilter(queryset=Business.objects.all())
    related_competition = django_filters.ModelMultipleChoiceFilter(queryset=Competition.objects.all(),
                                                                   widget=forms.CheckboxSelectMultiple)
    uploader = django_filters.ModelChoiceFilter(queryset=UserModel.objects.all())


class PictureFilterPrivate(BasePictureFilter):
    related_adventure = django_filters.ModelChoiceFilter(queryset=Adventure.objects.all())
    related_competition = django_filters.ModelMultipleChoiceFilter(queryset=Competition.objects.all(),
                                                                   widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.filters['related_adventure'].queryset = Adventure.objects.filter(adventurer=user)
        self.filters['related_competition'].queryset = Competition.objects.filter(participants=user)


class PictureFilterOwner(BasePictureFilter):
    related_business = django_filters.ModelChoiceFilter(queryset=Business.objects.all())
    related_competition = django_filters.ModelMultipleChoiceFilter(queryset=Competition.objects.all(),
                                                                   widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.filters['related_business'].queryset = Business.objects.filter(owner=user)
        self.filters['related_competition'].queryset = Competition.objects.filter(business__owner=user)


class BusinessPictureFilter(BasePictureFilter):
    def __init__(self, *args, **kwargs):
        business = kwargs.pop('business', None)
        super().__init__(*args, **kwargs)
        if business:
            self.filters['upload_date'].queryset = Picture.objects.filter(related_business=business)
