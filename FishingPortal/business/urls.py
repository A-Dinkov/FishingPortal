from django.urls import path

from .views import BusinessCreateView, BusinessShowView, DeleteBusinessView

urlpatterns = [
    path('create/', BusinessCreateView.as_view(), name='create_business'),
    path('show/<int:pk>/', BusinessShowView.as_view(), name='show_business'),
    path('delete/<slug>/', DeleteBusinessView.as_view(), name='delete_business')
]
