from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from app_user.models import AppUser
from app_user.serializers import (
    AppUserSerializers,  AppUserDetailsSerializer
)


class AppUserListAPIView(ListAPIView):
    queryset = AppUser.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = AppUserSerializers


class AppUserCreateAPIView(CreateAPIView):
    serializer_class = AppUserSerializers


class AppUserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = AppUser.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = AppUserDetailsSerializer
    lookup_field = 'uuid'
