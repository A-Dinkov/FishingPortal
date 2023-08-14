# Django imports
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as gen_views
from django.contrib.auth import views as auth_views

# Application imports
from FishingPortal.auth_app import forms as app_forms
from FishingPortal.auth_app.mixins import AnonymousUserOnlyMixin
from FishingPortal.auth_app.models import RegularUser, UserProfile


class RegisterUser(AnonymousUserOnlyMixin, SuccessMessageMixin, gen_views.CreateView,):
    template_name = 'auth_app/register.html'
    success_url = reverse_lazy('home')
    success_message = 'Your registration is successful'
    form_class = app_forms.RegularUserCreationForm

    def form_valid(self, form):
        response = super().form_valid(form)
        self.request.session['new_user_id'] = self.object.id

        # Authenticate the user using the user's email and password
        email, password = form.cleaned_data.get('email'), form.cleaned_data.get('password1')
        new_user = authenticate(email=email, password=password)

        # Log in the authenticated user
        if new_user is not None:
            login(self.request, new_user)

        return response


class UserProfileCreateView(LoginRequiredMixin, gen_views.CreateView):
    model = UserProfile
    form_class = app_forms.ProfileCreationForm
    template_name = 'auth_app/create-profile.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Set the user field in the UserProfile to the currently registered user
        form.instance.user = self.request.user
        return super(UserProfileCreateView, self).form_valid(form)


class ShowProfile(LoginRequiredMixin, gen_views.DetailView):
    model = UserProfile
    template_name = 'auth_app/profile.html'

    def get(self, request, *args, **kwargs):
        # Get the primary key from the url`s kwargs
        pk = kwargs.get('pk')

        try:
            # Try to fetch the UserProfile object
            user_profile = UserProfile.objects.get(pk=pk)
            context = {'user_profile': user_profile}
            return render(request, self.template_name, context)
        except UserProfile.DoesNotExist:
            # If the UserProfile does not exist, display a custom message
            return render(request, 'auth_app/profile-not-exist.html')


class UpdateUserProfileView(LoginRequiredMixin, gen_views.UpdateView):
    model = UserProfile
    form_class = app_forms.UserProfileEditForm
    template_name = 'auth_app/edit-profile.html'

    def get_success_url(self):
        # Provide the success URL with the pk of the created UserProfile
        return reverse_lazy('profile', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        # Set the user field in the UserProfile to the currently registered user
        form.instance.user = self.request.user
        return super().form_valid(form)


class CustomLoginView(auth_views.LoginView):
    template_name = 'auth_app/login.html'
    form_class = app_forms.CustomLoginForm


class CustomLogoutView(auth_views.LogoutView):
    pass


class ShowUserList(LoginRequiredMixin, gen_views.ListView):
    model = RegularUser
    template_name = 'auth_app/user-list.html'


class DeleteUser(LoginRequiredMixin, gen_views.DeleteView):
    model = RegularUser
    template_name = 'auth_app/delete-user.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, "The user was deleted successfully.")
        return super(DeleteUser, self).form_valid(form)


class AppPasswordResetView(auth_views.PasswordResetView):
    template_name = 'auth_app/password-reset.html'
    form_class = app_forms.CustomPasswordResetForm


class AppPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'auth_app/password-reset-done.html'


class AppPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'auth_app/password-reset-confirm.html'
    form_class = app_forms.AppSetPasswordForm


class AppPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'auth_app/password-reset-complete.html'
