from django.urls import path
from FishingPortal.competition.views import CompetitionCreateView, CompetitionDetailsView, CompetitionEditView, \
    CompetitionDeleteView, signup_for_competition, CompetitionsListDisplayView, ParticipantsListDisplayView, \
    sign_off_from_competition

urlpatterns = [
    path('create/', CompetitionCreateView.as_view(), name='create_competition'),
    path('details/<str:slug>/', CompetitionDetailsView.as_view(), name='competition_details'),
    path('edit/<str:slug>/', CompetitionEditView.as_view(), name='edit_competition'),
    path('delete/<str:slug>/', CompetitionDeleteView.as_view(), name='delete_competition'),
    path('<str:slug>/signup', signup_for_competition, name='signup_for_competition'),
    path('<str:slug>/signoff', sign_off_from_competition, name='sign_off_from_competition'),
    path('competition_list/', CompetitionsListDisplayView.as_view(), name='list_competitions'),
    path('<str:slug>/participants_list/', ParticipantsListDisplayView.as_view(), name='list_participants')
]
