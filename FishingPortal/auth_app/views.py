from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as auth_views
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView


from FishingPortal.auth_app.forms import RegularUserCreationForm, ProfileCreationForm, \
    CustomPasswordResetForm, AppSetPasswordForm, UserProfileEditForm, CustomLoginForm
from FishingPortal.auth_app.mixins import AnonymousUserOnlyMixin
from FishingPortal.auth_app.models import RegularUser, UserProfile


class RegisterUser(AnonymousUserOnlyMixin, SuccessMessageMixin, auth_views.CreateView,):
    template_name = 'auth_app/register.html'
    success_url = reverse_lazy('home')
    success_message = 'Your registration is successful'
    form_class = RegularUserCreationForm

    def form_valid(self, form):
        # without explicitly mentioning the parent class name in super()-->Python3 and later
        response = super().form_valid(form)
        self.request.session['new_user_id'] = self.object.id

        # Authenticate the user using the user's email and password
        email, password = form.cleaned_data.get('email'), form.cleaned_data.get('password1')
        new_user = authenticate(email=email, password=password)

        # Log in the authenticated user
        if new_user is not None:
            login(self.request, new_user)

        return response


class UserProfileCreateView(LoginRequiredMixin, auth_views.CreateView):
    model = UserProfile
    form_class = ProfileCreationForm
    template_name = 'auth_app/create_profile.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Set the user field in the UserProfile to the currently registered user
        form.instance.user = self.request.user
        return super(UserProfileCreateView, self).form_valid(form)


class ShowProfile(LoginRequiredMixin, auth_views.DetailView):
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
            return render(request, 'auth_app/profile_not_exist.html')


class UpdateUserProfileView(LoginRequiredMixin, auth_views.UpdateView):
    model = UserProfile
    form_class = UserProfileEditForm
    template_name = 'auth_app/edit-profile.html'

    def get_success_url(self):
        # Provide the success URL with the pk of the created UserProfile
        return reverse_lazy('profile', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        # Set the user field in the UserProfile to the currently registered user
        form.instance.user = self.request.user
        return super().form_valid(form)


class CustomLoginView(LoginView):
    template_name = 'auth_app/login.html'
    form_class = CustomLoginForm


class CustomLogoutView(LogoutView):
    pass


class ShowUserList(LoginRequiredMixin, auth_views.ListView):
    model = RegularUser
    template_name = 'auth_app/user-list.html'


class DeleteUser(LoginRequiredMixin, auth_views.DeleteView):
    model = RegularUser
    template_name = 'auth_app/delete_user.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super(DeleteUser, self).form_valid(form)


class AppPasswordResetView(PasswordResetView):
    template_name = 'auth_app/password-reset.html'
    form_class = CustomPasswordResetForm


class AppPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'auth_app/password-reset-done.html'


class AppPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'auth_app/password-reset-confirm.html'
    form_class = AppSetPasswordForm


class AppPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'auth_app/password_reset_complete.html'
