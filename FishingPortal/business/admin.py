from django.contrib import admin

from FishingPortal.business.forms import BusinessCreationForm
from FishingPortal.business.models import Business


@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    form = BusinessCreationForm

    list_display = ('lake_name', 'city', 'phone_number')
    list_filter = ('lake_name', 'city', 'phone_number')

