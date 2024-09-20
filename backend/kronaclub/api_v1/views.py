# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status, viewsets

from eventsapp.models import (
    Event,
    Location,
    # Attendee,
    # ThemeOfEvent,
    # EventTheme
)
from eventsapp.serializers import (
    EventSerializer,
    LocationSerializer,
    # AttendeeSerializer,
    # ThemeOfEventSerializer,
    # EventThemeSerializer
)



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        # 'register': reverse('api:users:list', request=request, format=format),
        'token create': reverse('api:jwt-create', request=request, format=format),
        'token refresh': reverse('api:jwt-refresh', request=request, format=format),
        'token verify': reverse('api:jwt-verify', request=request, format=format),
        # 'password reset': reverse('api:users-reset-password', request=request, format=format),
        # 'password change': reverse('api:rest_password_change', request=request, format=format),
        'events': reverse('api:events-list', request=request, format=format),
        'locations': reverse('api:locations-list', request=request, format=format),
    })


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


# class UserViewSet(viewsets.ModelViewSet):
#     serializer_class = EventSerializer
#     queryset = Event.objects.all()

