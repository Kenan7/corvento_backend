from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)

from app_user.models import AppUser
from app_user.serializers import (
    AppUserSerializers, CustomRegisterSerializer, AppUserDetailsSerializer
)
from dj_rest_auth.registration.views import RegisterView


class AppUserListAPIView(ListAPIView):
    queryset = AppUser.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = AppUserSerializers


class AppUserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = AppUser.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = AppUserDetailsSerializer
    lookup_field = 'uuid'


class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer
