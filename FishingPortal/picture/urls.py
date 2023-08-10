from django.urls import path

from FishingPortal.picture.views import UploadPictureView

urlpatterns = [
    path('upload/', UploadPictureView.as_view(), name='upload_photo')
]
