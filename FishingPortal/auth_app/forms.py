from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AdminPasswordChangeForm, BaseUserCreationForm, \
    PasswordResetForm, SetPasswordForm, AuthenticationForm
from FishingPortal.auth_app.models import RegularUser, UserProfile


UserModel = get_user_model()


class RegularUserCreationForm(BaseUserCreationForm):
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={
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


class CustomLoginForm(AuthenticationForm):

    username = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter email'
        }),

    )

    password = forms.CharField(
        label='',
        strip=False,
        widget=forms.PasswordInput(attrs={
            "autocomplete": "current-password",
            'placeholder': 'Enter password',
        }),
    )


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
                attrs={'placeholder': 'Write something about yourself',
                       'rows': 5, 'cols': 40
                       }
            )
        }


class RegularUserChangeForm(UserChangeForm):

    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('email', 'password')


class UserProfileEditForm(ProfileCreationForm):
    class Meta(ProfileCreationForm.Meta):
        widgets = {
            'bio': forms.Textarea(
                attrs={'rows': 10, 'cols': 40}
            )
        }


class CustomAdminPasswordChangeForm(AdminPasswordChangeForm):

    class Meta:
        model = RegularUser
        fields = ('old password', 'new_password1', 'new_password2')


class DeleteUserForm(forms.ModelForm):
    model = UserModel, UserProfile

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
        model = UserModel
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
        model = UserModel
        fields = ('new_password1', 'new_password2')