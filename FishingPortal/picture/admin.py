from django.contrib import admin

from FishingPortal.picture.models import Picture


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    pass
