from django.contrib import admin

from FishingPortal.picture.forms import UploadPictureForm
from FishingPortal.picture.models import Picture


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    form = UploadPictureForm
    list_display = ('title', 'upload_date', 'image')
    list_filter = ('title', 'upload_date', 'related_business', 'related_competition', 'related_adventure')
