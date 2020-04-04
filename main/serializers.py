from rest_framework import serializers
from main.models import Event


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
