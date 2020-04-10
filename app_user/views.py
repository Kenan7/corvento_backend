from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.decorators import api_view, APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, AllowAny

from app_user.models import AppUser
from app_user.serializers import (
    AppUserSerializers, CustomRegisterSerializer, AppUserDetailsSerializer
)
from dj_rest_auth.registration.views import RegisterView, ConfirmEmailView


class AppUserListAPIView(ListAPIView):
    queryset = AppUser.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = AppUserSerializers


class AppUserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = AppUser.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = AppUserDetailsSerializer
    lookup_field = 'uuid'


class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer

    # def post(self, request, format=None):
    #     serializer = CustomRegisterSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class CustomVerifyEmailView(APIView, ConfirmEmailView):
#     permission_classes = (AllowAny,)
#     allowed_methods = ('POST', 'OPTIONS', 'HEAD')

#     def get_serializer(self, *args, **kwargs):
#         return VerifyEmailSerializer(*args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.kwargs['key'] = serializer.validated_data['key']
#         confirmation = self.get_object()
#         confirmation.confirm(self.request)
#         return Response({'detail': _('ok')}, status=status.HTTP_200_OK)

#     def get_object(self, queryset=None):
#         key = self.kwargs['key']
#         emailconfirmation = EmailConfirmationHMAC.from_key(key)
#         if not emailconfirmation:
#             if queryset is None:
#                 queryset = self.get_queryset()
#             try:
#                 emailconfirmation = queryset.get(key=key.lower())
#             except EmailConfirmation.DoesNotExist:
#                 raise EmailConfirmation.DoesNotExist
#         return emailconfirmation

#     def get_queryset(self):
#         qs = EmailConfirmation.objects.all_valid()
#         qs = qs.select_related("email_address__appuser")
#         return qs
