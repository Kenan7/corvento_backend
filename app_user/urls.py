from django.urls import path
from app_user import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),

    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path(
        'list/',
        views.AppUserListAPIView.as_view(),
        name='app_user_list'
    ),
    path(
        '<uuid:uuid>/',
        views.AppUserRetrieveUpdateDestroyAPIView.as_view(),
        name='app_user_rud'
    ),

]
