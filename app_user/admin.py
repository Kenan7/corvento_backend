from django.contrib import admin
from app_user.models import AppUser
from app_user.forms import CustomAppUserChangeForm
# from app_user.forms import CustomModelForm


@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    # add_form = CustomAppUserCreationForm
    form = CustomAppUserChangeForm
    # form = CustomModelForm
    list_display = ("email", "first_name", "is_superuser")
    search_fields = ("first_name", "email")
    ordering = ("created_at",)
    exclude = ['groups', 'user_permissions']
