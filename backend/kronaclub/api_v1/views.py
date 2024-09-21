# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status, viewsets
from rest_framework import filters
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend


from eventsapp.models import (
    Event,
    Location,
    Attendee,
    ThemeOfEvent,
    EventTheme
)
from eventsapp.serializers import (
    EventSerializer,
    EventDetailSerializer,
    LocationSerializer,
    AttendeeSerializer,
    ThemeOfEventSerializer,
    EventThemeSerializer
)
from users.models import (
    CustomUser,
    TypeOfUser,
)
from users.serializers import (
    CustomUserSerializer,
    TypeOfUserSerializer,
)
from api_v1.filters import (
    UserFilter
)


class IsOwnerOrAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True

        return obj.user == request.user


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'register': reverse('api:customuser-list', request=request, format=format),
        'token create': reverse('api:jwt-create', request=request, format=format),
        'token refresh': reverse('api:jwt-refresh', request=request, format=format),
        'token verify': reverse('api:jwt-verify', request=request, format=format),
        'password reset': reverse('api:customuser-reset-password', request=request, format=format),
        'password set': reverse('api:customuser-set-password', request=request, format=format),
        'reset password confirm': reverse('api:customuser-reset-password-confirm', request=request, format=format),

        'events': reverse('api:events-list', request=request, format=format),
        'locations': reverse('api:locations-list', request=request, format=format),
        'attendees': reverse('api:attendees-list', request=request, format=format),
        'types_of_events': reverse('api:types_of_events-list', request=request, format=format),
        'event_themes': reverse('api:event_themes-list', request=request, format=format),

        'users': reverse('api:users-list', request=request, format=format),
        'types_of_users': reverse('api:types_of_users-list', request=request, format=format),
    })


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = EventDetailSerializer(instance, context={'request': request})
        return Response(serializer.data)


class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


class AttendeeViewSet(viewsets.ModelViewSet):
    serializer_class = AttendeeSerializer
    queryset = Attendee.objects.all()


class ThemeOfEventViewSet(viewsets.ModelViewSet):
    serializer_class = ThemeOfEventSerializer
    queryset = ThemeOfEvent.objects.all()


class EventThemeViewSet(viewsets.ModelViewSet):
    serializer_class = EventThemeSerializer
    queryset = EventTheme.objects.all()


class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['first_name', 'last_name']
    filterset_class = UserFilter
    # filterset_fields = ['email', 'first_name', 'last_name', 'telegram_login', 'telegram_id', 'phone_number']
    # filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    # search_fields = ('email', 'first_name', 'last_name', 'telegram_login', 'telegram_id', 'phone_number')
    # ordering_fields = ('email', 'last_name', 'first_name', 'is_active')
    # ordering = ['-is_active', ]
    # http_method_names = ['get', 'put', 'patch', 'head', 'delete', 'options']


class TypeOfUserViewSet(viewsets.ModelViewSet):
    serializer_class = TypeOfUserSerializer
    queryset = TypeOfUser.objects.all()
