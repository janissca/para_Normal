from django.urls import include, path
from rest_framework import routers

from api_v1.views import (
    api_root,
    EventViewSet,
    LocationViewSet,
    AttendeeViewSet,
    ThemeOfEventViewSet,
    EventThemeViewSet,
    UsersViewSet,
    TypeOfUserViewSet,
)


app_name = 'api'

router = routers.DefaultRouter()
router.register('events', EventViewSet, basename='events')
router.register('locations', LocationViewSet, basename='locations')
router.register('attendees', AttendeeViewSet, basename='attendees')
router.register('types_of_events', ThemeOfEventViewSet, basename='types_of_events')
router.register('event_themes', EventThemeViewSet, basename='event_themes')
router.register('users', UsersViewSet, basename='users')
router.register('types_of_users', TypeOfUserViewSet, basename='types_of_users')


urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('', api_root),
]

urlpatterns += router.urls
