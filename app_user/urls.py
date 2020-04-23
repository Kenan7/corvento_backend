from django.urls import path
from app_user import views


urlpatterns = [

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
        '<int:pk>/detail/',
        views.AppUserRetrieveAPIView.as_view(),
        name='app_user_detail'
    ),
    path(
        '<int:pk>/edit/',
        views.AppUserUpdateAPIView.as_view(),
        name='app_user_edit'
    ),

]
