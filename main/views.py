from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (
    ListCreateAPIView,
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from main.models import Event, Category
from main.serializers import (
    EventCreateSerializer, CategorySerializer, EventALLSerializer
)
from rest_framework import filters


class EventListView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventALLSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = [
        'author__first_name', 'title', 'desc',
    ]
    filterset_fields = ['featured', 'category__id']


class EventFeaturedListView(ListAPIView):
    queryset = Event.objects.get_featured()
    serializer_class = EventALLSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = [
        'author__first_name', 'title',
        'desc', 'category__name'
    ]
    filterset_fields = ['featured']


class EventCreateView(CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventCreateSerializer


class EventDetailView(RetrieveAPIView):
    lookup_field = 'slug'
    serializer_class = EventALLSerializer
    queryset = Event.objects.all()


class EventUpdateView(UpdateAPIView):
    lookup_field = 'slug'
    serializer_class = EventCreateSerializer
    queryset = Event.objects.all()


class EventDestroyView(DestroyAPIView):
    lookup_field = 'slug'
    serializer_class = EventCreateSerializer
    queryset = Event.objects.all()


# couldn't implement
# class EventsByCategory(ListAPIView):
#     lookup_field = 'id'
#     queryset = Category.event_set
#     serializer_class = EventALLSerializer

#                                             #
#              Category Views                 #
#                                             #


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
