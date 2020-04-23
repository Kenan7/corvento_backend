from django.contrib.auth.forms import UserCreationForm, UserChangeForm


# class CustomAppUserCreationForm(UserCreationForm):
#     class Meta:
#         model = AppUser
#         fields = ('email', 'first_name',
#                   'last_name', 'gender')


from django.forms import ModelForm
from .models import AppUser
from versatileimagefield.forms import VersatileImageFormField
from versatileimagefield.fields import SizedImageCenterpointClickDjangoAdminField


class CustomAppUserChangeForm(UserChangeForm):
    class Meta:
        model = AppUser
        fields = [
            'email',
            'image',
            'firebase_token',
            'notifications'
        ]


class CustomModelForm(VersatileImageFormField):
    image = SizedImageCenterpointClickDjangoAdminField(required=False)

    class Meta:
        model = AppUser
        fields = ('image',)
