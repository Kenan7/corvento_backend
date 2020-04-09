# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from app_user.models import AppUser


# class CustomAppUserCreationForm(UserCreationForm):
#     class Meta:
#         model = AppUser
#         fields = ('email', 'first_name',
#                   'last_name', 'gender')


# class CustomAppUserChangeForm(UserChangeForm):
#     class Meta:
#         model = AppUser
#         fields = UserChangeForm.Meta.fields

from django.forms import ModelForm

from versatileimagefield.fields import SizedImageCenterpointClickDjangoAdminField
from versatileimagefield.forms import VersatileImageFormField

from .models import AppUser


class CustomModelForm(VersatileImageFormField):
    image = SizedImageCenterpointClickDjangoAdminField(required=False)

    class Meta:
        model = AppUser
        fields = ('image',)
