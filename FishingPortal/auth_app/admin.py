from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from FishingPortal.auth_app.forms import RegularUserChangeForm, RegularUserCreationForm, CustomAdminPasswordChangeForm, \
    UserProfileEditForm
from FishingPortal.auth_app.models import RegularUser, UserProfile


@admin.register(RegularUser)
class CustomUserAdmin(UserAdmin):

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_regular_user",
                    "is_owner",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "consent"),
            },
        ),
    )
    form = RegularUserChangeForm
    add_form = RegularUserCreationForm
    change_password_form = CustomAdminPasswordChangeForm
    list_display = ("email", "is_staff")
    list_filter = ("is_staff", "is_superuser", "is_active", "is_owner", "groups")
    search_fields = ("email",)
    ordering = ("email",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    form = UserProfileEditForm

    list_display = ('first_name', 'last_name', 'city', 'age')
    search_fields = ('first_name', 'last_name', 'city', 'age')
    list_filter = ('first_name', 'last_name', 'city', 'age')
    ordering = ('first_name',)

