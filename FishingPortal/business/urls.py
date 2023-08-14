# Django imports
from django.urls import path

# Application imports
from .views import (
    DeleteBusinessView, BusinessCreateView, BusinessDetailView,
    EditBusinessView, LakesListDisplayView
)
from FishingPortal.common.views import like_object

urlpatterns = [
    path('create/', BusinessCreateView.as_view(), name='create_business'),
    path('details/<str:slug>', BusinessDetailView.as_view(), name='business_details'),
    path('delete/<str:slug>', DeleteBusinessView.as_view(), name='delete_business'),
    path('edit/<str:slug>', EditBusinessView.as_view(), name='edit_business'),
    path('lakes_list/', LakesListDisplayView.as_view(), name='list_lakes'),
    path('like/business/<slug:object_slug>/', like_object, name='like_business', kwargs={'model': 'business'}),

]
