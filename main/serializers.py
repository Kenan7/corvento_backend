from rest_framework import serializers
from main.models import Event, Category


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'name'
