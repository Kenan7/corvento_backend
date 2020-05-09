from rest_framework import serializers
from app_user.models import (
    AppUser,
    ContactForm
)


class AppUserSerializers(serializers.ModelSerializer):

    class Meta:
        model = AppUser
        fields = [
            'id',
            'email',
            'firebase_id',
            'image',
            'firebase_token',
            'created_at'
        ]


class AppUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = [
            'id',
            'email',
            'firebase_id',
            'image',
            'firebase_token',
            'created_at'
        ]
        read_only_fields = ('email',)


class ContactFormALLSerializer(serializers.ModelSerializer):
    user_id = AppUserDetailsSerializer()

    class Meta:
        model = ContactForm
        fields = [
            'id',
            'subject',
            'message',
            'email',
        ]


class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = '__all__'
