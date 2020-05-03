from django.urls import path
from app_user import views


urlpatterns = [

    path(
        'send/',
        views.send_notifications
    ),
    path(
        'list/',
        views.AppUserListAPIView.as_view(),
        name='app_user_list'
    ),
    path(
        'create/',
        views.AppUserCreateAPIView.as_view(),
        name='app_user_create'
    ),
    path(
        '<slug:firebase_id>/detail/',
        views.AppUserRetrieveAPIView.as_view(),
        name='app_user_detail'
    ),
    path(
        '<slug:firebase_id>/edit/',
        views.AppUserUpdateAPIView.as_view(),
        name='app_user_edit'
    ),

]
