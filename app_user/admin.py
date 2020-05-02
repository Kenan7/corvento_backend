from django.contrib import admin
from app_user.models import AppUser, ContactForm, UserNotifications
from app_user.forms import CustomAppUserChangeForm
# from app_user.forms import CustomModelForm


@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    # add_form = CustomAppUserCreationForm
    form = CustomAppUserChangeForm
    # form = CustomModelForm
    list_display = ("email",)
    search_fields = ("email",)
    ordering = ("created_at",)
    # exclude = ['groups', 'user_permissions']


admin.site.register(ContactForm)
admin.site.register(UserNotifications)
