from django.urls import path

from FishingPortal.picture.views import UploadPictureView, PrivatePhotoView, PhotoDetailView, PhotoEditView, \
    PhotoDeleteView, PhotoListView, BusinessPhotoListView

urlpatterns = [
    path('upload/', UploadPictureView.as_view(), name='upload_photo'),
    path('my-photos/', PrivatePhotoView.as_view(), name='show_my_photos'),
    path('details/<str:slug>/', PhotoDetailView.as_view(), name='photo_details'),
    path('edit/<str:slug>/', PhotoEditView.as_view(), name='edit_photo'),
    path('delete/<str:slug>/', PhotoDeleteView.as_view(), name='delete_photo'),
    path('list-photos/', PhotoListView.as_view(), name='list_photos'),
    path('business/<int:pk>/list-photos', BusinessPhotoListView.as_view(), name='business_photo')
]
