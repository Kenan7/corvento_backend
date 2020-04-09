from django.urls import path, include
from main import views
urlpatterns = [
    path(
        'list/',
        views.EventListView.as_view(), name='events_list'
    ),
    path(
        'create/',
        views.EventCreateView.as_view(), name='events_create'
    ),
    path(
        '<slug:slug>/detail/',
        views.EventDetailView.as_view(), name='event_detail'
    ),
    path(
        '<slug:slug>/update/',
        views.EventUpdateView.as_view(), name='event_update'
    ),
    path(
        '<slug:slug>/delete/',
        views.EventDestroyView.as_view(), name='event_delete'
    )
]
