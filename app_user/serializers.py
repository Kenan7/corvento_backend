from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from app_user.models import AppUser, UserNotifications


class AppUserSerializers(serializers.ModelSerializer):

    class Meta:
        model = AppUser
        fields = [
            'email', 'first_name', 'last_name', 'uuid', 'gender', 'image',
        ]


class CustomRegisterSerializer(RegisterSerializer):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('NON', 'Prefer Not to Say')
    ]

    username = None
    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(write_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    gender = serializers.CharField(required=True)
    image = serializers.ImageField(required=False)

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()

        return {
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'gender': self.validated_data.get('gender', ''),
            'image': self.validated_data.get('image', ''),
        }


class UserNotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNotifications
        fields = '__all__'


class AppUserDetailsSerializer(serializers.ModelSerializer):
    notifications = UserNotificationsSerializer()

    class Meta:
        model = AppUser
        fields = [
            'email', 'first_name', 'last_name', 'gender', 'uuid', 'image', 'notifications'
        ]
        read_only_fields = ('email',)
