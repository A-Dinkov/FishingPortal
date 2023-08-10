from django.contrib import admin

from FishingPortal.adventure.forms import AdventureCreationForm
from FishingPortal.adventure.models import Adventure


@admin.register(Adventure)
class Adventure(admin.ModelAdmin):
    form = AdventureCreationForm
    list_display = ('name', 'place', 'date')
    list_filter = ('name', 'place', 'date')
