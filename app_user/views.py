from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from app_user.models import AppUser, ContactForm
from app_user.serializers import (
    AppUserSerializers,
    AppUserDetailsSerializer,
    ContactFormSerializer,
    ContactFormALLSerializer
)


class AppUserListAPIView(ListAPIView):
    queryset = AppUser.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = AppUserSerializers


class AppUserCreateAPIView(CreateAPIView):
    serializer_class = AppUserSerializers


class AppUserRetrieveAPIView(RetrieveAPIView):
    queryset = AppUser.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = AppUserDetailsSerializer
    lookup_field = 'firebase_id'


class AppUserUpdateAPIView(UpdateAPIView):
    queryset = AppUser.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = AppUserDetailsSerializer
    lookup_field = 'firebase_id'


class ContactFormCreateAPIView(CreateAPIView):
    serializer_class = ContactFormSerializer


class ContactFormListAPIView(ListAPIView):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormALLSerializer
