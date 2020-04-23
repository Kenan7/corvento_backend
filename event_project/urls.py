from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from app_user import views

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Event Project API')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/docs/', schema_view),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/events/', include('main.urls')),
    path('api/users/', include('app_user.urls')),
    path('api/categories/', include('main.url_category')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
