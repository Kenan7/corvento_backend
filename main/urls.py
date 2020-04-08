from django.urls import path, include
from main import views
urlpatterns = [
    path(
        'home/',
        views.EventListCreateView.as_view(), name='events_list_create'
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
    ),

    # categories
    path(
        'category/',
        views.CategoryListCreateView.as_view(), name='category_list_create'
    ),
    path(
        'category/<slug:slug>/detail/',
        views.CategoryDetailView.as_view(), name='category_detail'
    ),
    path(
        'category/<slug:slug>/update/',
        views.CategoryUpdateView.as_view(), name='category_update'
    ),
    path(
        'category/<slug:slug>/delete/',
        views.CategoryDestroyView.as_view(), name='category_delete'
    ),
]
