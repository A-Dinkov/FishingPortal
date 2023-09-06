# Django imports
from django.urls import path

# Application imports
from FishingPortal.common.views import like_object
from FishingPortal.picture.views import (
    BusinessPhotoListView, UploadPictureView, PrivatePhotoView, PhotoDetailView,
    PhotoEditView, PhotoDeleteView, PhotoListView, OwnerPhotoView,
)

urlpatterns = [
    path('upload/', UploadPictureView.as_view(), name='upload_photo'),
    path('my-photos/', PrivatePhotoView.as_view(), name='show_my_photos'),
    path('owner-photos/', OwnerPhotoView.as_view(), name='owner_photos'),
    path('details/<str:slug>/', PhotoDetailView.as_view(), name='photo_details'),
    path('edit/<str:slug>/', PhotoEditView.as_view(), name='edit_photo'),
    path('delete/<str:slug>/', PhotoDeleteView.as_view(), name='delete_photo'),
    path('list-photos/', PhotoListView.as_view(), name='list_photos'),
    path('business/<int:business_pk>/list-photos', BusinessPhotoListView.as_view(), name='business_photo'),
    path('like/photo/<slug:object_slug>/', like_object, name='like_photo', kwargs={'model': 'photo'}),
]
