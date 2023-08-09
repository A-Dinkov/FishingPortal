from django.urls import path
from FishingPortal.competition.views import CompetitionCreateView, CompetitionDetailsView, CompetitionEditView, \
    CompetitionDeleteView, signup_for_competition

urlpatterns = [
    path('create/', CompetitionCreateView.as_view(), name='create_competition'),
    path('details/<str:slug>/', CompetitionDetailsView.as_view(), name='competition_details'),
    path('edit/<str:slug/>', CompetitionEditView.as_view(), name='edit_competition'),
    path('delete/<str:slug/>', CompetitionDeleteView.as_view(), name='delete_competition'),
    path('sign_up/<str:slug>/', signup_for_competition, name='signup_competition')
]
