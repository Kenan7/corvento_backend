from rest_framework.generics import (
    ListCreateAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from main.models import Event
from main.serializers import EventsSerializer


class EventListCreateView(ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventsSerializer


class EventDetailView(RetrieveAPIView):
    lookup_field = 'slug'
    serializer_class = EventsSerializer
    queryset = Event.objects.all()


class EventUpdateView(UpdateAPIView):
    lookup_field = 'slug'
    serializer_class = EventsSerializer
    queryset = Event.objects.all()


class EventDestroyView(DestroyAPIView):
    lookup_field = 'slug'
    serializer_class = EventsSerializer
    queryset = Event.objects.all()
