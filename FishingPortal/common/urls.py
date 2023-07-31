from django.urls import path
from django.views import generic as auth_views


urlpatterns = [
    path('', auth_views.TemplateView.as_view(template_name='common/home.html'), name='home'),
    path('about/', auth_views.TemplateView.as_view(template_name='common/about.html'), name='about'),
]
