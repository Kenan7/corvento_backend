from django.urls import path, include
from main import views
urlpatterns = [
    # categories
    path(
        '',
        views.CategoryListCreateView.as_view(), name='category_list_create'
    ),
    path(
        '<slug:slug>/detail/',
        views.CategoryDetailView.as_view(), name='category_detail'
    ),
    path(
        '<slug:slug>/update/',
        views.CategoryUpdateView.as_view(), name='category_update'
    ),
    path(
        '<slug:slug>/delete/',
        views.CategoryDestroyView.as_view(), name='category_delete'
    ),
]
