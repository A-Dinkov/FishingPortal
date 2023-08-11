from django.urls import path
from FishingPortal.adventure.views import CreateAdventureView, AdventureDetailView, EditAdventureView, \
    DeleteAdventureView, ListAdventuresView

urlpatterns = [
    path('create/', CreateAdventureView.as_view(), name='create_adventure'),
    path('details/<str:slug>', AdventureDetailView.as_view(), name='adventure_details'),
    path('edit/<str:slug>', EditAdventureView.as_view(), name='edit_adventure'),
    path('delete/<str:slug>', DeleteAdventureView.as_view(), name='delete_adventure'),
    path('list-adventures/', ListAdventuresView.as_view(), name='list_adventures'),
]