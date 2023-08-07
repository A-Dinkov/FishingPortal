from django.urls import path

from .views import DeleteBusinessView, BusinessCreateView, BusinessDetailView, BusinessOwnerView

urlpatterns = [
    path('create/', BusinessCreateView.as_view(), name='create_business'),
    path('details/', BusinessDetailView.as_view(), name='business_details'),
    path('delete/<slug:slug>/', DeleteBusinessView.as_view(), name='delete_business'),
    path('private/', BusinessOwnerView.as_view(), name='private_page')
]
