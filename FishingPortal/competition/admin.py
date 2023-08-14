# Django imports
from django.contrib import admin

# Application imports
from FishingPortal.competition.forms import CompetitionCreationForm
from FishingPortal.competition.models import Competition


@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    form = CompetitionCreationForm
    list_display = ('name', 'place', 'date')
    list_filter = ('name', 'place', 'date', 'business')

