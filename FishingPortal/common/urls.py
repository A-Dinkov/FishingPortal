from django.urls import path
from django.views import generic as auth_views
from FishingPortal.common.views import RegularUserHomeView, BusinessOwnerView

urlpatterns = [
    path('', auth_views.TemplateView.as_view(template_name='common/home.html'), name='home'),
    path('about/', auth_views.TemplateView.as_view(template_name='common/about.html'), name='about'),
    path('contact/', auth_views.TemplateView.as_view(template_name='common/contact.html'), name='contact'),
    path('private-regular/<int:pk>/', RegularUserHomeView.as_view(), name='private_regular'),
    path('private-owner/<int:pk>/', BusinessOwnerView.as_view(), name='private_owner'),
]
