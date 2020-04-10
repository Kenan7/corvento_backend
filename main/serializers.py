from rest_framework import serializers
from main.models import Event, Category
from app_user.serializers import AppUserDetailsSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ('slug',)


class EventCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class EventALLSerializer(serializers.ModelSerializer):
    author = AppUserDetailsSerializer()
    category = CategorySerializer()

    class Meta:
        model = Event
        fields = [
            'title', 'desc', 'image',
            'venue', 'slug', 'category', 'author'
        ]
