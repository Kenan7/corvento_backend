from rest_framework import serializers
from app_user.models import AppUser, UserNotifications


class UserNotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNotifications
        fields = '__all__'


class AppUserSerializers(serializers.ModelSerializer):

    class Meta:
        model = AppUser
        fields = [
            'email',
            'firebase_id',
            'uuid',
            'image',
            'firebase_token',
            'created_at'
        ]


class AppUserDetailsSerializer(serializers.ModelSerializer):
    notifications = UserNotificationsSerializer()

    class Meta:
        model = AppUser
        fields = [
            'email',
            'uuid',
            'firebase_id',
            'image',
            'firebase_token',
            'notifications',
            'created_at'
        ]
        read_only_fields = ('email',)
