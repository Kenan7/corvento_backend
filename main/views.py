from rest_framework.generics import (
    ListCreateAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from main.models import Event, Category
from main.serializers import EventsSerializer, CategorySerializer
from rest_framework import filters


class EventListCreateView(ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['author__first_name', 'title', 'desc', 'category__name']


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


class CategoryListCreateView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class CategoryDetailView(RetrieveAPIView):
    lookup_field = 'slug'
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryUpdateView(UpdateAPIView):
    lookup_field = 'slug'
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryDestroyView(DestroyAPIView):
    lookup_field = 'slug'
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
