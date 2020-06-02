from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from app_user import views
from main import views as main_views
# from rest_framework_swagger.views import get_swagger_view

# schema_view = get_swagger_view(title='Event Project API')


urlpatterns = [
    path('admin/postgres-metrics/', include('postgres_metrics.urls')),
    path('admin/', admin.site.urls),
    path('', main_views.Home.as_view(), name='home'),
    path('tinymce/', include('tinymce.urls')),
    # path('api/docs/', schema_view),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/events/', include('main.urls')),
    path('api/users/', include('app_user.urls')),
    path('api/categories/', include('main.url_category')),
    path('api/form/', include('app_user.url_form')),
    path('privacy-and-policy', main_views.Policy.as_view(), name='policy'),
    path('terms-and-conditions', main_views.Terms.as_view(), name='terms'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
