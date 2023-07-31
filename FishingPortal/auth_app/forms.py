from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AdminPasswordChangeForm, BaseUserCreationForm, \
    PasswordResetForm, SetPasswordForm
from FishingPortal.auth_app.models import RegularUser, UserProfile


class RegularUserCreationForm(BaseUserCreationForm):
    email = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter email'
        }),

    )

    password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Create password',
            'data-toggle': 'custom-helper-text',
        }),

    )

    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm password',
            'data-toggle': 'custom-helper-text',
        }),
    )

    consent = forms.BooleanField(
        required=True,
        label='',
        widget=forms.CheckboxInput(attrs={
            'label': None,
            'placeholder': None
        })
    )

    class Meta:
        model = RegularUser
        fields = ('email', 'password1', 'password2', 'consent')


class ProfileCreationForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'age', 'city', 'bio', 'image_profile']

        labels = {
            'first_name': '',
            'last_name': '',
            'age': '',
            'city': '',
            'bio': '',
        }

        widgets = {
            'first_name': forms.TextInput(
                attrs={'placeholder': 'Enter your First Name'}
            ),

            'last_name': forms.TextInput(
                attrs={'placeholder': 'Enter your Last Name'}
            ),

            'age': forms.NumberInput(
                attrs={'placeholder': 'Enter your age'}
            ),

            'city': forms.TextInput(
                attrs={'placeholder': 'Enter your city'}
            ),

            'bio': forms.Textarea(
                attrs={'placeholder': 'Write something about yourself'}
            )
        }


class RegularUserChangeForm(UserChangeForm):

    class Meta(UserCreationForm.Meta):
        model = RegularUser
        fields = ('email', 'password')


class UserProfileEditForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'age', 'city', 'bio', 'image_profile']

        labels = {
            'first_name': '',
            'last_name': '',
            'age': '',
            'city': '',
            'bio': '',
            'image_profile': ''
        }


class CustomAdminPasswordChangeForm(AdminPasswordChangeForm):

    class Meta:
        model = RegularUser
        fields = ('old password', 'new_password1', 'new_password2')


class DeleteUserForm(forms.ModelForm):
    model = RegularUser, UserProfile

    class Meta:

        fields = ('first_name', 'last_name', 'email', 'bio', 'profile_image')


class CustomPasswordResetForm(PasswordResetForm):

    email = forms.EmailField(
        label='',
        max_length=254,
        widget=forms.EmailInput(attrs={
            "autocomplete": "email",
            "placeholder": 'Enter email'
        }),
    )

    class Meta(PasswordResetForm):
        model = RegularUser
        fields = ('email', )


class AppSetPasswordForm(SetPasswordForm):

    new_password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            "autocomplete": "new-password",
            "placeholder": "Enter new password"
        }),
        strip=False,
    )
    new_password2 = forms.CharField(
        label='',
        strip=False,
        widget=forms.PasswordInput(attrs={
            "autocomplete": "new-password",
            "placeholder": "Enter new password"
        }),
    )

    class Meta(SetPasswordForm):
        model = RegularUser
        fields = ('new_password1', 'new_password2')