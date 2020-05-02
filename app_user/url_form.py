from django.urls import path
from app_user import views


urlpatterns = [

    path(
        'create/',
        views.ContactFormCreateAPIView.as_view(),
        name='contact_form_create'
    ),

    path(
        'list/',
        views.ContactFormListAPIView.as_view(),
        name='contact_form_list'
    ),
]
