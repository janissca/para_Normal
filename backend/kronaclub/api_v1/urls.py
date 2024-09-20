from django.urls import include, path
from rest_framework import routers

from api_v1.views import (
    api_root,
    EventViewSet,
    LocationViewSet,
    AttendeeViewSet,
    ThemeOfEventViewSet,
    EventThemeViewSet,
)


app_name = 'api'

router = routers.DefaultRouter()
router.register('events', EventViewSet, basename='events')
router.register('locations', LocationViewSet, basename='locations')
router.register('attendees', AttendeeViewSet, basename='attendees')
router.register('types_of_events', ThemeOfEventViewSet, basename='types_of_events')
router.register('event_themes', EventThemeViewSet, basename='event_themes')


urlpatterns = [
    path('', api_root),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    # path('login/', CustomLogin.as_view(), name='rest_login'),
    # path('', include('rest_auth.urls')),
    # path('registration/', include('rest_auth.registration.urls')),
    # path('rest-auth/', include('rest_auth.urls')),
    # path('rest-auth/registration/', include('rest_auth.registration.urls'))
    # path('oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]

urlpatterns += router.urls
