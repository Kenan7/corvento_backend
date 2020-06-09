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
from django.views.generic import TemplateView
from fcm_django.models import FCMDevice
from django.http import HttpResponse, Http404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.utils import timezone


def send_notification(request, **kwargs):
    try:
        devices = FCMDevice.objects.all()
        try:
            slug_from_url = kwargs.get("slug")
        except:
            HttpResponse("No slug provided")
        try:
            event_from_url = Event.objects.get(slug=slug_from_url)
            title = event_from_url.title
            body = event_from_url.desc
            devices.send_message(title=title, body=body)
        except:
            Http404("We could not find event this 'slug'")
        return HttpResponse(f"Success! Notification for this Event[{title} - {body}] has been sent!")
    except:
        return HttpResponse("Unexpected error. Please contact with us")


# class Testt(TemplateView):
#     template_name = 'test/index.html'


class Home(TemplateView):
    template_name = 'main/index.html'


class Policy(TemplateView):
    template_name = 'main/policy.html'


class Terms(TemplateView):
    template_name = 'main/terms.html'


class EventListView(ListAPIView):
    # queryset = Event.objects.all()
    #                                                                       Optimized from 33 queries to 3 query
    #                                                                       ~1800ms query --- > ~650ms
    queryset = Event.objects.get_nonfeatured()
    serializer_class = EventALLSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = [
        'title',
        'description',
        'community',
        'category__name'
    ]
    filterset_fields = ['featured', 'category__id']

    @method_decorator(cache_page(60*60*2))  # cache for 2 hours
    def dispatch(self, *args, **kwargs):
        return super(EventListView, self).dispatch(*args, **kwargs)

    # def filter_queryset(self, queryset):
    #     queryset = super(EventListView, self).filter_queryset(queryset)
    #     return queryset


class EventFeaturedListView(ListAPIView):
    queryset = Event.objects.get_featured()
    serializer_class = EventALLSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = [
        'title',
        'description',
        'community',
        'category__name'
    ]
    filterset_fields = ['featured']

    @method_decorator(cache_page(60*60))  # cache for one hour
    def dispatch(self, *args, **kwargs):
        return super(EventFeaturedListView, self).dispatch(*args, **kwargs)


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
