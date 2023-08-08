from django.urls import path
from FishingPortal.competition.views import CompetitionCreateView

urlpatterns = [
    path('create/', CompetitionCreateView.as_view(), name='create_competition')
]