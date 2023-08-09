from django.urls import path

from .views import DeleteBusinessView, BusinessCreateView, BusinessDetailView, BusinessOwnerView, EditBusinessView

urlpatterns = [
    path('create/', BusinessCreateView.as_view(), name='create_business'),
    path('details/<str:slug>', BusinessDetailView.as_view(), name='business_details'),
    path('delete/<str:slug>', DeleteBusinessView.as_view(), name='delete_business'),
    path('private/', BusinessOwnerView.as_view(), name='private_page'),
    path('edit/<str:slug>', EditBusinessView.as_view(), name='edit_business')
]
