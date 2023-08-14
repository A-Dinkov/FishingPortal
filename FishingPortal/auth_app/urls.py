# Django imports
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views import generic as views

# Project-specific imports
from .views import (
    AppPasswordResetCompleteView, AppPasswordResetConfirmView,
    AppPasswordResetDoneView, AppPasswordResetView, CustomLoginView,
    CustomLogoutView, DeleteUser, RegisterUser, ShowProfile,
    ShowUserList, UpdateUserProfileView, UserProfileCreateView
)


urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('user_list/', ShowUserList.as_view(), name='user_list'),
    path('create_profile/', UserProfileCreateView.as_view(), name='create_profile'),
    path('profile/<int:pk>/', ShowProfile.as_view(), name='profile'),
    path('profile_not_exist/', views.TemplateView.as_view(
        template_name='auth_app/profile-not-exist.html'),
         name='profile_not_exist'
         ),
    path('delete_user/<int:pk>', DeleteUser.as_view(), name='delete_user'),
    path('password_reset/', AppPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', AppPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', AppPasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password_reset_complete/', AppPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('edit-profile/<int:pk>/', UpdateUserProfileView.as_view(), name='edit_profile')

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)